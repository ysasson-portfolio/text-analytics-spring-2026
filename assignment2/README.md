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

Seeing that the audience of this analysis is a technical manager and entertainment executives, I think that the most important label that we need to look at our where the sentiment labels are marked "negative". When it comes to good reviews, I am sure they are important and tell the company where they have succeeded, but the negative reviews are where the companies can really look to make improvements for their viewers and/or audience. Negative reviews are a great opportunity to hear where the pain points are and improve the efforts of the company for any current or upcoming project. If companies do not improve on really important negative issues, they are at risk of losing millions or even billions of dollars in lost revenues after the customers decide they are not willing to come back. Examples of this could be whether the audience didn't like certain CGI efforts, the first installment of a series was not as pleasing, or whether they need to invest their money into different projects. This allows the entertainment studios to create action items to improve the products. Making changes from negative reviews will ensure greater success because they are not going to lose customers. Negative reviews are one of the biggest indicators of whether a product will succeed or fail.



## Model Comparison Table

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


## Custom Interference Summary

- **Correct Classifications:** 18/20

Key Findings
- When it comes to the text within the domain of this subject, the model performed very well. 
- With the trickier reviews, the word choice is very important.
- Words with multiple meanings can affect the prediction that the model makes.
- The way the words are tokenized and vectorized have an affect on the meaning of each word and can affect the way the model makes a prediction.
- When it comes to out of context reviews, the model performs very well. However, the way words are used again has a very important affect. 
- Emphasized words can throw off the entire prediction if there are not enough words of the opposite emotion to bring it back.
- Since machine learning does not handle slang well, it can affect the emotion behind a review.
- I would trust this model to be generalized in production. 
- Model is successful 90% of the time and is successful in out-of-domain reviews 80% of the time.

## Recommendation with Justification

Based on the data provided in the Model Comparison Idea above, I would recommend using the Logistic Regression model combined with the Tokenization and Vectorization from the TF-IDF process. For sentiment analysis and text classification in reviews, it is very important that we optimize the right performance metric. In this case, it is very important to max the F1 score because that is the statistic that shows the balance between Precision and Recall. If we optimize for Precision, we are only looking at the Positive Reviews to be Positive. Optimizing for recall would mean that accuracy would drop significantly and we would be looking at almost every review as misclassified. Looking at the F1 score, will allow us to look at all of the correct classifications while addressing any misclassifications that may occur in the dataset. This model also scores higher than any other model in every single metric except for Training and Predicting Speed. The accuracy for this model is very high as presented in this code and as the Custom Interference showed it can be generalized while still being a high performing model. 

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
