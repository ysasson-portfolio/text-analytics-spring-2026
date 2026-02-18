# Assignment 1: Sentiment Analysis- AI Usage Log



## Task 1: Transformer Model Running Optimization  

### Task I was Trying to Achieve:

In this task, I didn't realize that running the transformer would take so much time. I was trying to make the transformer model run more efficiently, so it can complete the model analysis more quickly. Another issue I was trying to solve was using a .apply method to apply the model to the entire column within the dataframe. 



### What prompt did you use?

I have a dataframe with a column cleaned reviews from an airline. I am trying to apply a transformer function to it but it is giving me issues. here is my code. # Convert to Hugging Face Dataset hf\_dataset = Dataset.from\_pandas(review\_df\['clean\_review']) # Use the map method as shown above for tokenization or inference # ... (map function code from above) ... processed\_dataset = review\_df.clean\_review.map(tokenizer, batched=True) # (Optional) convert back to pandas if needed processed\_df = processed\_dataset.to\_pandas() hf\_dataset = Dataset.from\_pandas(df)



### What did AI suggest?

AI suggested to create a function that batches the data from within the dataset and map them over a copy of the original dataframe.



### What did you modify?

I modified by still using a batching process, except that I utilized it in a for loop that would go through the different batches and store the outputs in a list that I could use to relate to the original dataframe. 



### Why did I modify it?

I followed up and asked if there was a way to run it without using a map function because it was still taking too long. 



### What did I learn?

I learned that sometimes models will take a while to run regardless of the efforts we make to speed it up. Although, batching is a good method to increase the efficiency while running the model. 



(Link to Chat Transcript)\[https://chatgpt.com/share/699573ba-0c80-8001-b965-2f5be6a16966]



## Task 2: Regex to Remove URL

### Task I was Trying to Achieve:

In this task, I was trying to remove the URLs from the text and I asked it how to remove the url (BA.com or UK.gov)



### What prompt did you use?

How do I clean HTML within text using regex code?



### What did AI suggest?

It suggested that I do the following code:

``` python

import re

text = "Visit: https://www.geeksforgeeks.org/ for more info."

pattern = r'https?://\\S+|www\\.\\S+'

result = re.sub(pattern, "\[URL REMOVED]", text)

print(result)

\# Output: Visit: \[URL REMOVED] for more info.

```



### What did you modify?

I modified the code to cut out any domain that is typically used with any text that is attached to it.



### Why did I modify it?

I modified the code because there were not any typical urls in any of the reviews using the typical "http://"



### What did I learn?

Here I learned that there are multiple ways to input URLs into a text and the I needed to consider other ways to implement the same idea. This made me go back to the datacamp course we did earlier and see how to include "or" arguments within my regex code.



