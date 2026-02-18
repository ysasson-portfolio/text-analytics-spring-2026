# Assignment 1: Sentiment Analysis


## Project Overview
This assignment compares three pretrained sentiment analysis models (VADER, TextBlob, and distilbert-base-uncased-emotion) 
on Airline Reviews [BA_AirlineReviews]. The goal is to understand strengths and weaknesses of each approach.

## Dataset
- **Name:** [Dataset name]
- **Source:** [https://www.kaggle.com/datasets/chaudharyanshul/airline-reviews]
- **Size:** [3700 rows]
- **Domain:** [Airline reviews / Customer Service reviews]

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
