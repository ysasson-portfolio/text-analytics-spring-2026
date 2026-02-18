# Assignment 1: Sentiment Analysis


## Project Overview
This assignment compares three pretrained sentiment analysis models (VADER, TextBlob, and distilbert-base-uncased-emotion) 
on Airline Reviews [BA_AirlineReviews]. The goal is to understand strengths and weaknesses of each approach. The project starts with the cleaning the full reviews and pre-processing. Once the text was cleaned and pre-processed, the text was tokenized and vectorized for all 3 models with their own specific processes and conducted analysis on each set of results. The analysis conducted included confusion matrices, accuracy scores, descriptive statistics, and reasoning based on personal knowledge. All of the answers to the questions that Professor Vo asked us to answer is commented throughout the code.

## Dataset Description
- **Name:** BA_AirlineReviews
- **Source:** https://www.kaggle.com/datasets/chaudharyanshul/airline-reviews
- **Size:** 3700 rows
- **Domain:** Airline reviews / Customer Service reviews
- **Main Column for Text:** ReviewBody
- **Original Data Source:** Extracted by web scraping
- **Contains:** Customer Feedback for British Airways that includes element and service ratings for their flight, flight path, date, name, the review header, the full review, and more.


## Key Findings
1. VADER performed better on [X] with [Y]% accuracy
2. TextBlob struggled with [specific cases]
3. [Your key insight #3]

## Files
- `notebooks/sentiment_analysis.ipynb` - Main analysis notebook
- `docs/AI_usage_log.md` - AI interaction documentation
- `docs/reflection.md` - Lessons learned

## How to Run

# Install requirements
!pip install pandas numpy vaderSentiment textblob matplotlib seaborn bs4 contractions transformers torch huggingface_hub[hf_xet] hf_xet datasets

# Launch Jupyter
jupyter notebook notebooks/sentiment_analysis.ipynb

#Change the destinations of the files within the pd.read_csv functions

# Adjust Sample File
When the sample file is produced make sure to create a column called 'real_y' in the new sample file and put "Positive", "Negative", or "Neutral"
