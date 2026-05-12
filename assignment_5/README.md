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






## Models and Tools Used

## Paid vs. Free

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


## Files
- `notebooks/rag.ipynb` - Main analysis notebook
- `AI_usage_log.md` - AI interaction documentation
- `memo.md` - Written Technical Memo
- `streamlit_app.py` - The python file that streamlit will use to make the application. 
- `requirements.txt` - List of required libraries and versions of said libraries for the streamlit file to function properly
- `.gitignore` - tells GitHub what kind of files or folder to ignore/not track in the project.
- `data/resume/resume.txt`- The .txt file that the model will use for the resume
- `data/job_descriptions` - Folder that contains all of the individual job descriptions that will be used for comparision to the resume by the model. Each individual job description is saved as its own .txt file.
- `evaluation/test results.md` - File that shares the results and key findings from the results of the models performance.


## How to Run

# Install requirements
!pip install pandas numpy vaderSentiment textblob matplotlib seaborn bs4 contractions scikit-learn nltk rank_bm25 gensim sentence-transformers tf-keras

# Launch Jupyter
jupyter notebook notebooks/classification.ipynb
