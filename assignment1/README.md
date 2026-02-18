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
1. distilbert-base-uncased-emotion performed better with 77% accuracy
2. VADER was very good at making a quick classification with a 59%
3. distilbert-base-uncased-emotion performed very well, but was by far the slowest model
4. TextBlob provided the least amount of insight and also required more cleaning.
5. The outputs for each of these models focus on different elements, but can be used to come to a standardized output.

## How to Run

# Install requirements
!pip install pandas numpy vaderSentiment textblob matplotlib seaborn bs4 contractions transformers torch huggingface_hub[hf_xet] hf_xet datasets

# Launch Jupyter
jupyter notebook notebooks/sentiment_analysis.ipynb

#Change the destinations of the files within the pd.read_csv functions

# Adjust Sample File
When the sample file is produced make sure to create a column called 'real_y' in the new sample file and put "Positive", "Negative", or "Neutral". Then load it back in and continue running it. It should already be in the code.

## Result Visualization
Can be found in Section 6 of the code

``` python

#Comparing Accuracy of the Models Based on the Performance from the Sample Dataset
print("VADER Accuracy:", accuracy_score(analyzed_sample_df['real_y'], analyzed_sample_df["vader_prediction"]))
print("TextBlob Accuracy:", accuracy_score(analyzed_sample_df['real_y'], analyzed_sample_df["textblob_prediction"]))
print("Transformer Accuracy:", accuracy_score(analyzed_sample_df['real_y'], analyzed_sample_df["Transformer_Prediction_Specified"]))

#Shows other performance metrics that the models have based on the sample data set
print("VADER Report:", classification_report(analyzed_sample_df['real_y'], analyzed_sample_df["vader_prediction"]))
print("TextBlob Report:", classification_report(analyzed_sample_df['real_y'], analyzed_sample_df["textblob_prediction"]))
print("Transformer Report:", classification_report(analyzed_sample_df['real_y'], analyzed_sample_df["Transformer_Prediction_Specified"]))

model_comparison = {
    'Criterion': ['Speed (seconds)', 'Accuracy (100 Sample)', 'Handles Emphasis', 'Handles Negation', 'Recall (Negative)', 'Recall (Neutral)', 'Recall (Positive)'],
    'VADER': [elapsed_time_vader, accuracy_score(analyzed_sample_df['real_y'], analyzed_sample_df["vader_prediction"]), 'Excellent', 'Good', 0.36 , 0.50, 0.95],
    'Textblob': [elapsed_time_textblob, accuracy_score(analyzed_sample_df['real_y'], analyzed_sample_df["textblob_prediction"]), 'Good', 'Good', 0.34, 0.00, 0.64],
    'Transformer': [elapsed_time_transformer, accuracy_score(analyzed_sample_df['real_y'], analyzed_sample_df["Transformer_Prediction_Specified"]), 'Better', 'Excellent',.79, 0.00,0.82],
    'Winner': ['VADER', 'Transformer', 'VADER', 'Transformer', 'Transformer', 'VADER', 'VADER'],
    'Justification': ['Almost 73 times faster than Transformer', '19% better','Able to take Punctuation and Capitalization into account', 'Able to use words to build the context','Highest recall value', 'Highest recall value', 'Highest recall value']
}

model_compare_df = pd.DataFrame(model_comparison)
print(model_compare_df)
```


## Files
- `notebooks/sentiment_analysis.ipynb` - Main analysis notebook
- `data/processed/airline_review_sample.csv` - My version of the sample spreadsheet
- `docs/AI_usage_log.md` - AI interaction documentation
- `docs/reflection.md` - Lessons learned
- `figures/text_length_distribution_hist.png` - Text Length Distribution Histogram

