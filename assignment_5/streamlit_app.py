"""
Assignment 5 -- Option B: Job Fit Analyzer
BSAN 6200 | Spring 2026

Run with:
    python -m streamlit run streamlit_app.py

Setup:
    pip install streamlit openai chromadb pandas python-dotenv pypdf

Create a .env file with:
    OPENAI_API_KEY=your_key_here
"""

import os
import pandas as pd
import streamlit as st
import chromadb
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(
    page_title="Job Fit Analyzer",
    page_icon="🎯",
    layout="wide"
)

MODEL_ID = "gpt-4o-mini"


# ══════════════════════════════════════════
# Helper functions
# ══════════════════════════════════════════

def load_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def load_pdf_file(filepath):
    from pypdf import PdfReader
    reader = PdfReader(filepath)
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def load_file(filepath):
    if filepath.endswith(".pdf"):
        return load_pdf_file(filepath)
    return load_text_file(filepath)


def load_all_jds(jd_dir="data/job_descriptions"):
    docs = []

    if not os.path.exists(jd_dir):
        return docs

    for filename in sorted(os.listdir(jd_dir)):
        filepath = os.path.join(jd_dir, filename)

        if filename.endswith((".txt", ".pdf")):
            text = load_file(filepath)

            if text.strip():
                docs.append({
                    "text": text,
                    "source": filename
                })

    return docs


def load_resume(resume_dir="data/resume"):
    if not os.path.exists(resume_dir):
        return ""

    for filename in os.listdir(resume_dir):
        if filename.endswith((".txt", ".pdf")):
            return load_file(os.path.join(resume_dir, filename))

    return ""


def chunk_text_by_sentences(text, chunk_size=400, overlap_words=20):
    import re

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) > chunk_size and current_chunk:
            chunks.append(current_chunk.strip())

            words = current_chunk.split()
            overlap_text = " ".join(words[-overlap_words:]) if len(words) > overlap_words else current_chunk

            current_chunk = overlap_text + " " + sentence
        else:
            current_chunk += " " + sentence

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return [chunk for chunk in chunks if len(chunk) > 20]


def chunk_documents(documents):
    chunks = []

    for doc in documents:
        doc_chunks = chunk_text_by_sentences(
            doc["text"],
            chunk_size=400,
            overlap_words=20
        )

        for chunk in doc_chunks:
            chunks.append({
                "text": chunk,
                "source": doc["source"]
            })

    return chunks


@st.cache_data
def load_metadata():
    possible_paths = [
        "data/jd_metadata.csv",
        "data/jd_metadata.xlsx"
    ]

    for path in possible_paths:
        if os.path.exists(path):
            if path.endswith(".csv"):
                return pd.read_csv(path)
            if path.endswith(".xlsx"):
                return pd.read_excel(path)

    return pd.DataFrame()


@st.cache_resource
def load_vectorstore():
    jd_docs = load_all_jds()

    if not jd_docs:
        return None, []

    chunks = chunk_documents(jd_docs)

    client = chromadb.Client()

    try:
        client.delete_collection("job_fit")
    except Exception:
        pass

    collection = client.create_collection(
        name="job_fit",
        metadata={"hnsw:space": "cosine"}
    )

    collection.add(
        documents=[c["text"] for c in chunks],
        metadatas=[{"source": c["source"]} for c in chunks],
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    return collection, jd_docs


@st.cache_resource
def load_llm():
    api_key = os.environ.get("OPENAI_API_KEY", "")

    if not api_key:
        return None

    return OpenAI(api_key=api_key)


# ══════════════════════════════════════════
# Analysis functions
# ══════════════════════════════════════════

def skill_gap_analysis_few_shot(
    client,
    job_description,
    resume_text,
    job_title="Selected Job",
    company="Unknown Company"
):

    context = f"""
Resume:
{resume_text}

Job Title:
{job_title}

Company:
{company}

Job Description:
{job_description}
"""

    prompt = f"""
Task: Explain what is similar and what is missing from this resume that is relevant for each job description and create a report from these results. Please include evidence for each similarity or gap and how to address each gap. Also include the job that they are comparing in the report.
Constraints: Use only the resume and job descriptions that are available and do not assume any information that is not clearly stated. If things are related (i.e. Tableau and Power BI), it can be indicated as similar. Make sure that missing content does not exist in the resume.

Example 1:

Resume:
- Proficient in Excel, Python, Tableau, R
- Created reports and shared them in shareholder presentations
- Discovered insights through multiple forms of analysis including modeling.

#Job Description: Requires profieciency in excel, machine learning, Power BI, tableau, formulating stories through data)

Output: 
Match: Excel, Tableau, Discovered insights through analysis
Gap: Python, R
How to fix the gap: Dedicate time weekly to watch instructional videos on the programming languages or sign up for a educational service such as datacamp.
Relevance: Based on the current state of the resume, you have a strong foundation, but not enough experience to get hired and succeed in this position. 

Example 2:

Resume:
- Created PowerBI and Tableau dashboards to gain insights from the company datasets.
- Worked to create new strategies based on financial models.
- Python, R, SPSS experience prefered

#Job Description: Requires profieciency in excel,  Power BI, tableau, formulating stories through data)

Output: 
Match: Tableau, Discovered insights through analysis
Gap: financial modeling, Excel, PowerBI
How to fix the gap: Dedicate time weekly to watch instructional videos on the programming languages or sign up for a educational service such as datacamp.
Relevance: Based on the current state of the resume you do not enough experience or skills to get hired and succeed in this position. 

Context:
{context}

Question:
Compare this resume against the selected job description.

Answer:
"""

    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "system",
                "content": "You find the skill gaps of a person by comparing the job descriptions to resumes using only the documents that are provided"
            }
        ],
        temperature=0.1
    )

    answer = response.choices[0].message.content

    return {
        "analysis_type": "skill_gap_few_shot",
        "job_title": job_title,
        "company": company,
        "answer": answer,
        "context": context,
        "prompt": prompt
    }


def keyword_alignment_analysis(
    client,
    job_description,
    resume_text,
    job_title="Selected Job",
    company="Unknown Company"
):

    context = f"""
Resume:
{resume_text}

Job Title:
{job_title}

Company:
{company}

Job Description:
{job_description}
"""

    prompt = f"""
Task: Based on the resume, job descriptions, and keyword taken in the question to create keyword alignment analysis that compares the keywords in the job description to the resume.
Constraints: Use only the resume, job descriptions, and keywords that are available and do not assume any information that is not clearly stated.
Output: The output should include they keyword, Whether it includes any of the following direct match, semantic match, or missing, and the evidence from the job description and resume. Also show the keyword alignment percentage for each word along with the general. The next piece of the output should be a conclusion for each key word. The final output should be a report with the general conclusions. 

Context:
{context}

Question:
Compare this resume against the selected job description.

Answer:
"""

    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "system",
                "content": "You find the relevant positions by comparing keywords in the job description to the resume"
            }
        ],
        temperature=0.2
    )

    answer = response.choices[0].message.content

    return {
        "analysis_type": "keyword_alignment",
        "job_title": job_title,
        "company": company,
        "answer": answer,
        "context": context,
        "prompt": prompt
    }


def fit_summary_analysis(
    client,
    job_description,
    resume_text,
    job_title="Selected Job",
    company="Unknown Company"
):

    context = f"""
Resume:
{resume_text}

Job Title:
{job_title}

Company:
{company}

Job Description:
{job_description}
"""

    prompt = f"""

Task: Based on the resume and job descriptions, write a 3-4 sentence narrative assessement that expresses the person's fit for the role by citing specific evidence from both the resume and the job descriptions and include it in the narrative.
Give a fitness score and include it in the narrative along with the strengths and weaknesses within the alignment. 
Restrictions: Please make sure that the information stated in the narrative is specifically included in the either the job descriptions or the resume. Do not state anything that is not there. 

Context:
{context}

Question:
Compare this resume against the selected job description.

Answer:
"""

    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": prompt
            },
            {
                "role": "system",
                "content": "You evaluate if a candidate's fit for the role based on the job descriptions and the resume of the candidate."
            }
        ],
        temperature=0.1
    )

    answer = response.choices[0].message.content

    return {
        "analysis_type": "fit_summary",
        "job_title": job_title,
        "company": company,
        "answer": answer,
        "context": context,
        "prompt": prompt
    }


ANALYSIS_TYPES = {
    "Skill Gap Report": skill_gap_analysis_few_shot,
    "Keyword Alignment": keyword_alignment_analysis,
    "Fit Summary": fit_summary_analysis,
}


def run_analysis(
    client,
    analysis_function,
    job_description,
    resume_text,
    job_title,
    company
):
    return analysis_function(
        client=client,
        job_description=job_description,
        resume_text=resume_text,
        job_title=job_title,
        company=company
    )


# ══════════════════════════════════════════
# Optional: top matching jobs using vector search
# ══════════════════════════════════════════

def get_top_matching_jobs(collection, resume_text, jd_docs, top_n=3):
    if collection is None:
        return []

    results = collection.query(
        query_texts=[resume_text],
        n_results=min(top_n, len(jd_docs))
    )

    matched_sources = []

    for metadata in results["metadatas"][0]:
        matched_sources.append(metadata["source"])

    top_jobs = []

    for source in matched_sources:
        for doc in jd_docs:
            if doc["source"] == source and doc not in top_jobs:
                top_jobs.append(doc)
                break

    return top_jobs[:top_n]


def get_job_info(metadata, selected_filename, selected_label):
    job_title = selected_label.replace(".txt", "")
    company = "Unknown Company"

    if metadata.empty:
        return job_title, company

    metadata = metadata.copy()
    metadata.columns = metadata.columns.str.strip()

    filename_col = None
    title_col = None
    company_col = None

    for col in metadata.columns:
        if col.lower() in ["filename", "file name", "file_name"]:
            filename_col = col
        elif col.lower() in ["title", "job title", "job_title"]:
            title_col = col
        elif col.lower() == "company":
            company_col = col

    if filename_col is None:
        return job_title, company

    selected_row = metadata[
        metadata[filename_col].astype(str).str.strip().str.replace(".txt", "", regex=False)
        ==
        selected_filename.strip().replace(".txt", "")
    ]

    if not selected_row.empty:
        row = selected_row.iloc[0]

        if title_col:
            job_title = row[title_col]

        if company_col:
            company = row[company_col]

    return job_title, company
# ══════════════════════════════════════════
# Load resources
# ══════════════════════════════════════════

collection, jd_docs = load_vectorstore()
metadata = load_metadata()
client = load_llm()
resume_text = load_resume()


# ══════════════════════════════════════════
# UI
# ══════════════════════════════════════════

st.title("🎯 Job Fit Analyzer")
st.caption("Compare your resume against job descriptions using your Assignment 5 analysis methods.")

# ── Error checks ──

if client is None:
    st.error("OPENAI_API_KEY not found. Add it to your .env file.")
    st.stop()

if collection is None:
    st.error("No job descriptions found in data/job_descriptions/. Add your job description files there.")
    st.stop()

if not resume_text:
    st.error("No resume found in data/resume/. Add your resume file there.")
    st.stop()


# ── Sidebar ──

with st.sidebar:
    st.header("About")
    st.write("This application uses Large Language Models and Retrival Augmented Generation to conduct different kinds of analysis that are based on the resume and job descriptions that were uploaded into the data.")
    st.write('''
    1. Skill Gap Analysis:
    Reads over the resume and the job description and identifies where you have:
    - Matching Experience and Skills
    - Gaps in Skills and Experience
    - Ways to Close the Missing Gaps
    
    2. Keyword Alignment Analysis:
    Takes Keywords from the Job Description and compares it to the resume.
    
    3. Fit Summary Analysis:
    Takes the Resume and the Job Description and then generates a 3-4 sentence summary describing whether a person would be good for this role.''')
    st.header("Instructions:")
    st.write('''
    1. Select the Job Description, from the drop down, that you would like to compare to the resume that is already uploaded.
    2. Select the kind of analysis you would like to conduct by using the buttons. 
    3. Click Run Analysis

    Optional: 
    - If you would like to run all 3 analysis click the button on the bottom that will do it on all 3.
    - If you would like to run all 3 analysis on the top 3 Job Descriptions click the button on the bottom that will do it on all 3.
    '''
    )
    st.write(f"**JDs loaded:** {len(jd_docs)}")
    st.write("**Resume loaded:** Yes")
    st.write(f"**Model:** {MODEL_ID}")
    st.divider()
    
    st.caption("BSAN 6200 | Assignment 5 | Option B")


# ── JD selector ──

col_select, col_analysis = st.columns([1, 1])

with col_select:
    st.subheader("1. Select a Job Description")

    if not metadata.empty and {"company", "title", "filename"}.issubset(metadata.columns):
        jd_options = {
            f"{row['company']} -- {row['title']}": row["filename"]
            for _, row in metadata.iterrows()
        }
    else:
        jd_options = {
            doc["source"]: doc["source"]
            for doc in jd_docs
        }

    selected_label = st.selectbox(
        "Choose a JD:",
        list(jd_options.keys())
    )

    selected_filename = jd_options[selected_label]

    job_title, company = get_job_info(
        metadata,
        selected_filename,
        selected_label
    )

    jd_text = ""

    for doc in jd_docs:
        if doc["source"] == selected_filename:
            jd_text = doc["text"]
            break

    st.write("**Selected job title:**", job_title)
    st.write("**Company:**", company)

    with st.expander("Preview job description"):
        st.text(jd_text[:1500] + ("..." if len(jd_text) > 1500 else ""))

    with st.expander("Preview resume"):
        st.text(resume_text[:1500] + ("..." if len(resume_text) > 1500 else ""))


with col_analysis:
    st.subheader("2. Choose Analysis Type")

    analysis_type = st.radio(
        "Select analysis:",
        list(ANALYSIS_TYPES.keys())
    )


# ── Run single analysis ──

st.divider()

if st.button("🔍 Run Analysis", type="primary", use_container_width=True):
    with st.spinner(f"Running {analysis_type}..."):
        try:
            analysis_function = ANALYSIS_TYPES[analysis_type]

            result = run_analysis(
                client=client,
                analysis_function=analysis_function,
                job_description=jd_text,
                resume_text=resume_text,
                job_title=job_title,
                company=company
            )

            st.subheader(f"Results: {analysis_type}")
            st.write("**Job Title:**", result["job_title"])
            st.write("**Company:**", result["company"])
            st.markdown(result["answer"])

            with st.expander("View prompt"):
                st.text(result["prompt"])

        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")


# ── Run all 3 analyses on selected JD ──

st.divider()

if st.button("📊 Run All 3 Analyses on Selected JD", use_container_width=True):
    for name, analysis_function in ANALYSIS_TYPES.items():
        with st.spinner(f"Running {name}..."):
            try:
                result = run_analysis(
                    client=client,
                    analysis_function=analysis_function,
                    job_description=jd_text,
                    resume_text=resume_text,
                    job_title=job_title,
                    company=company
                )

                st.subheader(name)
                st.write("**Job Title:**", result["job_title"])
                st.write("**Company:**", result["company"])
                st.markdown(result["answer"])

                with st.expander(f"View prompt for {name}"):
                    st.text(result["prompt"])

                st.divider()

            except Exception as e:
                st.error(f"{name} failed: {str(e)}")


# ── Run all 3 analyses on top 3 matching jobs ──

st.divider()

if st.button("🏆 Run All 3 Analyses on Top 3 Matching Jobs", use_container_width=True):
    top_jobs = get_top_matching_jobs(
        collection=collection,
        resume_text=resume_text,
        jd_docs=jd_docs,
        top_n=3
    )

    if not top_jobs:
        st.error("Could not identify top matching jobs.")
    else:
        all_results = []

        for job in top_jobs:
            top_jd_text = job["text"]
            top_filename = job["source"]

            top_label = top_filename
            top_job_title, top_company = get_job_info(
                metadata,
                top_filename,
                top_label
            )

            st.header(f"{top_company} -- {top_job_title}")

            for name, analysis_function in ANALYSIS_TYPES.items():
                with st.spinner(f"Running {name} for {top_job_title}..."):
                    try:
                        result = run_analysis(
                            client=client,
                            analysis_function=analysis_function,
                            job_description=top_jd_text,
                            resume_text=resume_text,
                            job_title=top_job_title,
                            company=top_company
                        )

                        all_results.append(result)

                        st.subheader(name)
                        st.markdown(result["answer"])

                        with st.expander(f"View prompt for {top_company} -- {top_job_title} -- {name}"):
                            st.text(result["prompt"])

                        st.divider()

                    except Exception as e:
                        st.error(f"{name} failed for {top_job_title}: {str(e)}")

        st.success(f"Completed {len(all_results)} total analyses.")