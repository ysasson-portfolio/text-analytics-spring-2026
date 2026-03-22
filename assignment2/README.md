# Assignment 2: Text Classification
### By: Yarden Sasson
### Submitted on 3/22/26


## Overview
This assignment has us using Machine Learning Algorithms and Feature Engineering methods to classify texts. In this code specifically, we will be looking at set of 50,000 movie reviews that were collected from IMDB and associated with a Binary Classification of "Positive" or "Negative". The Tokenization and Vectorization methods used in this analysis were TF-IDF and Count Vectorizer. The four machine learning algorithms used were Naive Bayes, Logistic Regression, SVM, and Random Forest. Based the combination of Vectorization methods and machine learning algorithms, this code is attempting to classify the movie reviews into those either Positive or Negative classes. Once the best model has been established, I then applied to other reviews (including tricky wording and out of context reviews). 

## Dataset
- **Name:** IMDB Dataset of 50K Movie Reviews
- **Source:** https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews
- **Size:** 50000 rows and 2 columns
- **Classes:** Positive or Negative
- **Distribution:** This is a completely balanced distribution with 50% Positive reviews and 50% Negative Reviews

## Best Model Results
- **F1 Score:** 0.893231
- **Precision:** 0.899756
- **Recall:** 0.8868
- **Training and Prediction Time:** 0.8560 seconds

## Important Class/Labels with Justification


## Model Comparison Table

| Algorithm | Feature | Accuracy | Train+Predict (s) | Memory Usage | Interpretability|
|:---------:|:-------:|:--------:|:-----------------:|:------------:|:----------------:|
| Naive Bayes | CountVectorizer | 0.8562 | 0.2612 | 0.854894 | 1 | Most Interpretable |
| Logistic Regression | CountVectorizer | 0.8765 | 3.6591 | 0.876290 | 2 | Very Interpretable |
| SVM | CountVectorizer | 0.8673 | 18.0844 | 0.867472 | 5 | Least Interpretable |
| Random Forest | CountVectorizer | 0.8520 | 98.0443 | 0.853000 | 7 | Not as Interpretable but can give the most insights |





## Recommendation with Justification

## Files
- `notebooks/classification.ipynb` - Main analysis notebook
- `docs/AI_usage_log.md` - AI interaction documentation
- `docs/report.pdf` - Written Technical Memo
- `docs/reflection.md` - Lessons learned

## How to Run

# Install requirements
!pip install pandas numpy vaderSentiment textblob matplotlib seaborn bs4 contractions scikit-learn nltk rank_bm25 gensim sentence-transformers tf-keras

# Launch Jupyter
jupyter notebook notebooks/classification.ipynb
