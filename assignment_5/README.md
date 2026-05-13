# Assignment 5: Language Models in Practice: Job Fit Analyzer (Option B)
### By: Yarden Sasson
### Submitted on 5/13/26


## Overview
This assignment has us applying language model concepts to a career problem. In this case, LLMs and RAG were used in order to compare resumes to job descriptions and then perform three different kinds of analysis using effective prompt engineering, LLM processes, evaluating the output, and communicating these results to an audience. The three kinds of analysis were a keyword analysis, skills gap analysis, and a fit summary narrative. This analysis was done within a Jupyter Notebook created in Colab and then applied to a streamlit application so people can conduct their own analysis in an easy to use way. 

## Link to Application
https://bsan6200-assignment5-ys.streamlit.app/

## Dataset
- Job Descriptions: Each job description has its own .txt file with a description that was copied and pasted from the Job Posting on LinkedIn.
- Resume: Copied into a .txt file from my own resume.
- Metadata: .csv file that was filled in with information based on the Job Postings. 

## Set Up and Instructions

1. Download all of the files from the GitHub and store it somewhere. 

2. Clone the Repository (This is set up in the Jupyter Notebook).

3. Create the .env file with the necessary API key information in the format 

OPENAI_API_KEY=your_openai_api_key_here
CHROMA_DB_DIR=./chroma_db

Purchase the API key for OpenAI by going on platform.openai.com

4. Make sure you have all of the files stored in the correct locations in the correct format including all job descriptions in the job_descriptions folder in .txt files, resume in the resume folder in a .txt file, metadata in the data folder in a csv file, streamlit application in the main folder, requirements.txt in the main folder, .gitignore in the main folder, .env stored locally only in the main folder, and the rag_pipeline notebook in the notebook folder. 

5. Make sure that all of the required libraries are installed on your local machine. (can be done on the notebook)

6. Change the directory of your command prompt where the main folder is stored.

7. Run the streamlit by using the command python -m streamlit run streamlit_app.py


## Models and Tools Used

- Coding Language: Python

- Libraries and Frameworks:
	- Streamlit: Use to build the interactive web application interface
	- OpenAI API: Used to generate the analysis reports using GPT-40-mini.
	- Sentence Transformers: Used to generate the semantic embeddings for the resume and job describe text chunks.

- Models Used:
	- all-MiniLM-L6-v2: Used to generate the text chunkings
	- GPT-40-mini: Used for the analysis reports. 

## Paid vs. Free

There were two models that were used throughout the process in the Jupyter Notebook. The first model was the `sentence-transformers/all-MiniLM-L6-v2` for the embedding process. This is a model that was used to create the embedding score which would later be used in the chunking strategy and then stored in the vectors. I used the free version for this because there was a lot of experimentation to determine the optimal amount of chunks with the right amount of over lap. 

The Second tool that was used was a connection to OpenAI using their API key. This was paid and I chose it because of the fact that it is a tried and true model and that we can the model many times for a low cost. Also, having a OpenAI account prior to this assignment for ChatGPT has made it easy to purchase the necessary credits for this assignment. The only difference is that we need to make sure that I needed to make sure that the API key was put in the .env file to make it run properly.

## Key Findings

| Job Title | Company | Analysis Type | Retrieval Relevance | Skill Identification Accuracy | Actionability | Faithfulness |
|---|---|---|---|---|---|---|
| Business Intelligence Analyst | Guitar Center | Skill Gap Analysis | Yes | Correct | 4 | Faithful |
| Business Intelligence Analyst | Guitar Center | Keyword Alignment Analysis | Yes | Incorrect | 5 | Faithful |
| Business Intelligence Analyst | Guitar Center | Fit Narrative Analysis | Yes | Incorrect | 3 | Faithful |
| Business Intelligence Analyst, Sports – Brand Consulting | Creative Artists Agency | Skill Gap Analysis | Yes | Correct | 5 | Faithful |
| Business Intelligence Analyst, Sports – Brand Consulting | Creative Artists Agency | Keyword Alignment Analysis | Yes | Incorrect | 4 | Hallucinated |
| Business Intelligence Analyst, Sports – Brand Consulting | Creative Artists Agency | Fit Narrative Analysis | Yes | Correct | 2 | Faithful |
| Business Intelligence Analyst | Los Angeles Tourism and Convention Board | Skill Gap Analysis | Yes | Incorrect | 5 | Hallucinated |
| Business Intelligence Analyst | Los Angeles Tourism and Convention Board | Keyword Alignment Analysis | Yes | Correct | 2 | Faithful |
| Business Intelligence Analyst | Los Angeles Tourism and Convention Board | Fit Narrative Analysis | Yes | Incorrect | 3 | Hallucinated |


When it comes to this project there were a few key insights that I discovered. The first one is that the more information we are able to provide to a model through the prompt the better the results would be. When the prompt for the Skills Gap Analysis was being written, the performance of the model improved each time we added new information to the prompt and a new structure. This will effectively guide the LLM to retrieve the right information from the two sets of documents and output it in a specific way. This was especially made more apparent when a few-shot approach was utilized in the skills gap analysis. The more vague the prompt is the more opportunity the LLM has to hallucinate and put stuff in the responses that is not in the source document or is not factual. This is exactly what happened with the Keyword Alignment Analysis. 

Another key finding that I found was that the way the documents are written influence the response that the LLM will output. The RAG system will retrieve the relevant text based on what it literally. The main problem with this is that it is more difficult to make connections based on subtle meanings or words that are semantically similar. This whole problem can be resolved by taking an example from the first key finding. The more specific we are when prompting, the better the model can be at identifying subtle meanings and words/phrases that are related to each other.

The third main finding is that the chunk size that we use to create the embedding is the one of the most important tools that we use when it comes to developing the context that a model can use. When the number is too large, it will produce less clusters; however it can produce a large amount of text with the opportunity for overlapping context or a wide range of topics that can be discussed. If the number is too small, there is significantly lower clusters, but it will be more specific when it comes to context. This limits what the conversations could be about when it comes to certain vectors. 


## File Descriptions
- `notebooks/rag_pipeline.ipynb` - Main analysis notebook
- `AI_usage_log.md` - AI interaction documentation
- `memo.md` - Written Technical Memo
- `streamlit_app.py` - The python file that streamlit will use to make the application. 
- `requirements.txt` - List of required libraries and versions of said libraries for the streamlit file to function properly
- `.gitignore` - tells GitHub what kind of files or folder to ignore/not track in the project.
- `data/resume/resume.txt`- The .txt file that the model will use for the resume
- `data/job_descriptions` - Folder that contains all of the individual job descriptions that will be used for comparison to the resume by the model. Each individual job description is saved as its own .txt file.
- `data/jd_metadata.csv` - This file stores the metadata for each job description in the job_description folder including job title, company, and more. 
- `evaluation/test results.md` - File that shares the results and key findings from the results of the models performance
- `.env (not included in GitHub)` - This file stores sensitive information including API keys. This file should be stored locally and then applied to the files by storing it in the same location or same folder. 
