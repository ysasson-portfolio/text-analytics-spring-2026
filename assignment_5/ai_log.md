# AI Usage Log – Assignment 5 Option B: Job Fit Analyzer

## Overview
This document summarizes how AI assistance was used throughout the development of the Assignment 5 Job Fit Analyzer project. The project involved building a Retrieval-Augmented Generation (RAG) system that compares resumes against job descriptions using multiple analysis methods and a Streamlit application interface.

The log documents the actual use of AI during development, including code generation, debugging, refactoring, deployment assistance, environment configuration, and documentation support.

---

# Entry 1 – Debugging Metadata and DataFrame Errors

## AI use category
Debugging and error diagnosis

## What task were you trying to do?
I was trying to connect metadata from a CSV file to selected job descriptions inside my Streamlit application. The application was failing with a KeyError related to the filename column.

## What prompt did you use?
I shared the full traceback error message showing:

```python
KeyError: 'filename'
```

and provided screenshots of the metadata structure and Streamlit code.

## What did AI suggest?
AI suggested that the metadata file likely did not contain a lowercase column named `filename`. It recommended creating a more flexible metadata parsing function that could handle multiple column naming formats such as:
- filename
- File Name
- file_name
- Job Title
- title

AI generated an updated `get_job_info()` function that normalized column names before matching.

## What did you modify?
I updated the metadata extraction logic to normalize column names and support multiple naming conventions. I also updated the logic to strip `.txt` extensions before comparing filenames.

## Why did you modify it?
The original code assumed exact column names and failed when the uploaded metadata file used different capitalization and formatting.

## What did you learn?
I learned that relying on exact column names can make applications fragile. Normalizing column names and handling multiple naming conventions creates more reliable applications. I also learned that it is important to keep the column names consistent with what I am naming my variables. Even if the column name does not appear in a normal way, this will prevent the misnaming of variables within the function and other code. 

## Any AI errors found?
No major errors were found in this suggestion. However, I still needed to adapt the logic to match the exact structure of my metadata file.

---

# Entry 2 – Refactoring RAG Functions for Direct Resume vs Job Description Comparison

## AI use category
Code refactoring and architecture design

## What task were you trying to do?
I wanted to refactor my original RAG analysis functions so they compared a single selected resume against a single selected job description instead of retrieving random chunks through vector search during every analysis.

## What prompt did you use?
I shared the full implementations of:
- `skill_gap_analysis_few_shot()`
- `skill_gap_analysis_zero_shot()`
- `ask_rag()`

and asked how to refactor them to directly compare one resume against one job description.

## What did AI suggest?
AI suggested restructuring the functions so they accepted:

```python
job_description
resume_text
job_title
company
```

instead of:

```python
question, k=5
```

AI also suggested separating retrieval from analysis by:
- using ChromaDB only for finding top matching jobs
- using direct comparisons for the actual analyses

## What did you modify?
I rewrote all analysis functions to directly take:
- resume text
- job description text
- job title
- company

I removed vector retrieval logic from the final analysis functions.

## Why did you modify it?
The previous structure mixed retrieval and analysis together, which made debugging harder and caused inconsistent comparisons between jobs.

## What did you learn?
I learned that RAG systems are cleaner when retrieval and analysis are separated into different stages. I also learned that the vector storing is different based on the number of documents are being used by the model. 

## Any AI errors found?
AI initially generated duplicate analysis execution logic in one notebook loop, which later caused repeated outputs. I corrected this manually.

---

# Entry 3 – Designing a Streamlit Application

## AI use category
Application development and UI integration

## What task were you trying to do?
I needed to convert my notebook-based RAG system into a working Streamlit web application.

## What prompt did you use?
I uploaded:
- my notebook
- a completed example Streamlit application
- my partially completed `streamlit_app.py`

and asked how to populate the application with my notebook logic.

## What did AI suggest?
AI generated a complete Streamlit application that:
- loaded resumes and job descriptions
- created vector stores with ChromaDB
- performed the three analyses
- supported top-3 job retrieval
- displayed results in the UI
- supported environment variable loading

## What did you modify?
I updated:
- metadata handling
- path loading
- deployment logic
- error handling
- Streamlit secrets integration

## Why did you modify it?
The generated code needed adjustments for my repository structure and Streamlit Cloud deployment.

## What did you learn?
I learned how to structure Streamlit applications using cached resources, reusable helper functions, and modular analysis pipelines. I also learned that using an .env application on streamlit is very different than running it locally on your device. This means that I had to change the structure for some of the code to make sure that it used the secrets function. Storing a variable in secrets allows us to pull sensitive information such as the API key without the public having access to it. 

## Any AI errors found?
The generated Streamlit file contained:
- indentation errors
- duplicate logic in some loops
- path assumptions that failed on Streamlit Cloud

These issues had to be corrected manually.

---

# Entry 4 – Debugging Python Indentation and Syntax Errors

## AI use category
Debugging and syntax correction

## What task were you trying to do?
I was trying to run the Streamlit application locally, but Python repeatedly produced indentation errors.

## What prompt did you use?
I shared screenshots of:
- terminal errors
- VS Code line numbers
- the affected sections of the Streamlit file

## What did AI suggest?
AI identified:
- hidden indentation issues
- misplaced leading spaces
- possible missing triple quotes
- malformed multiline prompts

AI pointed out a hidden leading space before:

```python
if client is None:
```

## What did you modify?
I removed hidden leading spaces and reformatted the error checking section.

## Why did you modify it?
Python requires strict indentation consistency, and even one extra space can invalidate the file.

## What did you learn?
I learned that multiline prompts and indentation issues are common causes of Python syntax failures when it comes to streamlit. This indentation error was also caused by when I copied and pasted the necessary code from the notebook into VSCode for the python file. I learned that it in .py files the indentation is more sensitive and that I need to copy and paste something that I have my cursor in the right position. Even one space off can cause an issue. 

## Any AI errors found?
The generated file itself originally contained the indentation issue that caused the error.

---

# Entry 5 – Configuring Environment Variables and API Keys

## AI use category
Environment configuration and deployment security

## What task were you trying to do?
I needed to securely store and load API keys for local development and Streamlit deployment.

## What prompt did you use?
I asked:
- how to create a `.env` file
- how to use `.gitignore`
- how to deploy secrets to Streamlit Cloud
- whether `.env` files should be uploaded to GitHub

## What did AI suggest?
AI suggested:
- creating a `.env` file locally
- adding `.env` to `.gitignore`
- using Streamlit Secrets for deployment
- using:

```python
st.secrets.get()
```

for deployed apps

## What did you modify?
I:
- created local `.env` files
- updated `.gitignore`
- configured Streamlit Secrets
- updated the `load_llm()` function to support both local and deployed environments

## Why did you modify it?
API keys should never be exposed publicly in GitHub repositories.

## What did you learn?
I learned that .env files are strictly for local storage and we can apply the information to the secrets function in streamlit when I need to have information restricted to the public. 

## Any AI errors found?
No major issues. However, I initially misunderstood how Streamlit Cloud handles secrets.

---

# Entry 6 – Resolving API Key Authentication Errors

## AI use category
Debugging API configuration

## What task were you trying to do?
I was trying to initialize the OpenAI client in Colab and Streamlit.

## What prompt did you use?
I shared screenshots showing:

```python
AuthenticationError: Incorrect API key provided
```

and uploaded my `.env` formatting.

## What did AI suggest?
AI identified several possible causes:
- malformed `.env` formatting
- hidden line breaks in the API key
- cached environment variables
- revoked keys
- missing `override=True` in `load_dotenv()`

## What did you modify?
I regenerated API keys and corrected `.env` formatting. Following this I reloaded the variables locally with the correct information causing more security and simplicity when I tested the variable locally.

## Why did you modify it?
The OpenAI client could not authenticate because the key formatting and loading process were inconsistent.

## What did you learn?
I learned how environment variables persist inside Colab sessions and how `.env` formatting errors can break authentication. I also learned that GitHub and OpenAI can flag when an API key has leaked and shut it down in order to prevent any issues with the fraudulent use of the API key.

## Any AI errors found?
Some troubleshooting steps assumed the API key itself was invalid when the problem was actually formatting and caching.

---
# Entry 7 – Creating a Requirements File and Managing Dependencies

## AI use category
Dependency management

## What task were you trying to do?
I needed to create a valid `requirements.txt` file for Streamlit deployment.

## What prompt did you use?
I asked:
- whether Torch was required
- how to reduce deployment size
- which package versions to use

## What did AI suggest?
AI generated:
- full dependency lists
- pinned version numbers
- lighter versions without Torch
- protobuf/chromadb compatibility fixes

## What did you modify?
I removed unnecessary dependencies such as:
- torch
- sentence-transformers

from deployment requirements because the deployed app no longer generated embeddings locally.

## Why did you modify it?
The large dependencies caused Streamlit deployment delays and version conflicts.

## What did you learn?
I learned how dependencies affect deployment size and how package compatibility issues can break cloud deployments.

## Any AI errors found?
Some early recommendations included unnecessary packages that were no longer used in the final application.

---

# Entry 8 – Fixing Streamlit Cloud Path Issues

## AI use category
Deployment debugging

## What task were you trying to do?
The deployed Streamlit app could not find resumes and job descriptions even though the files existed in GitHub.

## What prompt did you use?
I asked why the application could not locate documents despite the files existing in the repository.

## What did AI suggest?
AI suggested replacing relative paths with:

```python
Path(__file__).parent
```

and restructuring the file loading logic to use script-relative paths.

## What did you modify?
I updated:
- resume loading
- job description loading
- metadata loading

so they used absolute script-relative paths.

## Why did you modify it?
Streamlit Cloud runs applications from different working directories than local notebooks.

## What did you learn?
I learned that deployment environments often require more robust file path handling and it is important to create different ways that are hardcoded for the python file to use.

## Any AI errors found?
No major issues were found.

---

# Entry 9 – Notebook and GitHub Rendering Issues

## AI use category
Notebook troubleshooting

## What task were you trying to do?
GitHub could not properly render my notebook after uploading it.

## What prompt did you use?
I shared screenshots showing notebook rendering failures and metadata errors.

## What did AI suggest?
AI suggested:
- removing corrupted widget metadata
- clearing notebook outputs
- using notebook conversion tools

## What did you modify?
I cleaned notebook metadata and removed corrupted widget states.

## Why did you modify it?
GitHub could not render the notebook because Colab-specific widget metadata was incompatible.

## What did you learn?
I learned that notebook metadata can break GitHub rendering even when the notebook itself runs correctly.

## Any AI errors found?
I found that it was only one part of the outputs that was preventing the preview whenever it was showing. Anytime the embedding process was being run, it loaded these green bars and it was preventing the output. It was only one output that needed to be cleared and not the entire notebook like the AI suggested. 

---

# Entry 10 – Creating the AI Usage Log

## AI use category
Documentation and academic reporting

## What task were you trying to do?
I needed to create a complete AI usage log documenting how AI was used throughout the development of the Assignment 5 project.

## What prompt did you use?
I asked AI to:
- review the full conversation
- identify all project-related exchanges
- organize them into professional academic log entries
- format the final output as a Markdown document for GitHub

## What did AI suggest?
AI generated a structured AI usage log using:
- categorized entries
- professional formatting
- detailed summaries of prompts, modifications, lessons learned, and debugging issues

## What did you modify?
I reviewed the generated entries and verified that they accurately reflected the actual development process.

## Why did you modify it?
The log needed to honestly represent the development workflow and distinguish between AI-generated suggestions and my own implementation decisions.

## What did you learn?
I learned the importance of documenting AI-assisted development workflows transparently and accurately.

## Any AI errors found?
The AI-generated log required review to ensure the entries remained truthful, specific, and aligned with the actual project history.

