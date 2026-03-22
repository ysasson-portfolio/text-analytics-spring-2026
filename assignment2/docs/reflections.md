\#Reflection for Assignment 2



* How many of 20 did the model get right (by your judgment)?



Based on what I predicted, the model got 18/20 correct.



* Did the model fail on the “tricky” examples? Why?



The model did fail on 1 of the "tricky" examples. I believe that it failed because of the way that the review started. It started really poisitve with "The visuals were beautiful", and that weighed really heavy in terms of the tokenization and vectorization towards the positive review. the words following were not specifically negative which made it difficult to properly classify it as a negative review.



* Did the model handle out-of-domain examples? Why or why not?



The "out-of-domain" examples also were handled 4/5 times successfully. I think that the ones that succeeded used words that were very clearly either positive or negative and may have had words that increased emphasis (i.e. painfully, cinematic, etc.). The one that failed started out with the overall positive tone "The new phone is visually stunning" but then doesn't use words that a machine learning model knows means something negative. "fell apart" could mean something fell down or something negative. This is where machine learning models requires sophisticated training and robustness. 



* What does this tell you about your model’s generalization ability?



I still maintain that this model can be very easily generalized because it succeeded 80% of the time at classifying reviews that are out of context or domain and overall succeeded 90% of the time. I think that the more information that this model will train on, the more the model will learn to handle different meanings with the same word, positive and negative as it relates to context, and other difficult language nuances. 



* Would you trust this model in production based on this test?



Based on this test, I would really trust the model in production. 

