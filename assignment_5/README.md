# Assignment 5: Language Models in Practice: Job Fit Analyzer (Option B)
### By: Yarden Sasson
### Submitted on 5/13/26


## Overview
This assignment has us applying language model concepts to a career problem. In this case, LLMs and RAG were used in order to compare resumes to job descriptions and then perform three different kinds of analysis using effective prompt engineering, LLM processes, evaluating the output, and communicating these results to an audience. The three kinds of analysis were a keyword analysis, skills gap analysis, and a fit summary narrative. This analysis was done within a Jupyter Notebook created in Colab and then applied to a streamlit application so people can conduct their own analysis in an easy to use way. 

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

##Key Findings

| Algorithm | Feature | Accuracy | Train+Predict (s) | F1 | Memory Usage | Interpretability |
|:---------:|:-------:|:--------:|:-----------------:|:--:|:------------:|:----------------:|
| Naive Bayes | CountVectorizer | 0.8562 | 0.2612 | 0.854894 | 1 | Most Interpretable |
| Logistic Regression | CountVectorizer | 0.8765 | 3.6591 | 0.876290 | 2 | Very Interpretable |
| SVM | CountVectorizer | 0.8673 | 18.0844 | 0.867472 | 5 | Least Interpretable |
| Random Forest | CountVectorizer | 0.8520 | 98.0443 | 0.853000 | 7 | Not as Interpretable but can give the most insights |
| Naive Bayes | TF-IDF | 0.8620 | 0.2526 | 0.859813 | 3 | Most Interpretable |
| Logistic Regression | TF-IDF | 0.8940 | 0.8560 | 0.893231 | 4 | Very Interpretable |
| SVM | TF-IDF | 0.8862 | 0.9517 | 0.885743 | 6 | Least Interpretable |
| Random Forest | TF-IDF | 0.8526 | 93.3095 | 0.854807 | 8 | Not as Interpretable but can give the most insights |


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
