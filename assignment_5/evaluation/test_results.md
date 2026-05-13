# Test Results

When creating the model that will eventually be used for multiple forms of analysis we had to conduct a few different experiments to make sure that we are implementing the best strategies when creating these models. These experiments included the chunking strategy, prompt testing, prompt iterations, and the final analysis. 

## Chunking Strategy 

When conducting the chunking strategies, we decided to test whether or not to do fixed sized chunking and sentence based chunking. Fixed size chunking is when we chunk based on a certain number of characters with a certain amount of overlap. This was a good method but sometimes the chunk would split up a word causing the chunk to end on a non-existent word. This can create a false sense of context and missed items that are related to the question at hand. The second item splits the text into chunks based on the number of characters while allowing the model to finish the sentence in case the word or sentence gets cut off. This performed better because it allowed for the full context to be considered in every single effort of retrieval by the model. Sentence based chunking allowed the model to produce results that are easier to understand and are more complete. This is why sentence based chunking was applied to the model after verifying it with a similarity search test.  

## Prompt Testing

When designing the model, it is very important to make sure the prompt is written in a well enough way to produce the optimal results. The first method is zero-shot prompting which means that we did not provide the model with examples. Zero-shot resulted in responses that were considered pretty good but were generally vague or covered a wide variety of different topics because of the fact that there was a lack of specificity in the prompt. Utilizing few-shot prompting, where we provide examples within the prompt, returned answers that were very specific related to the case and were easily interpretable. Also the examples made it easier for the model to make connections with the information that were less obvious than the zero shot prompting. This is why it was decided to the few-shot prompting method in the model.

## Prompt Iterations

The first iteration I started with was a base line prompt that asked for a skill gap analysis based on the descriptions. This baseline resulted a good response with relevant segments from the document. However, the detail was not as prominent within the response. This also missed out information that we help us identify the relevant documents it used. The first iteration after the baseline was changed by adding more details within the prompt and also providing a change that can provide the user with ways to decrease the skill gap. This improved the model because it provided all of this information in one location. The third iteration was adding more details in a very structured way that was understood by the model while having as much information as possible to guide the model in a specific way. It also added the report output aspect took the information from the relevant documents while doing its best to follow the constraints. This is why I kept adding details to the models and made sure to be strict while giving the model room to be creative (for more subtle phrases). 

## Final Evaluation Table

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

The model in this case is not perfect. The Skill Gap Analysis performed the best because it was the most detailed while being able to draw connections between certain tasks and the job descriptions (even if the texts were not using identical words). The fit narrative analysis is the second best because it was able to perform creatively while still finding the relevant pieces of text and then including it as evidence. The keyword alignment analysis still performed well, but was the worst one out of the three. This is because the keyword alignment is strictly dependent on finding the same word. However, it is still performing well.

## Failure Analysis

There were certain times where the model failed the first time where I consider the model to fail is where it does not consider tasks that are related to each other on the resume or the job description. An example of this, was when the LA Tourism Board for the Business Intelligence Analyst has Data Cleaning as a different task than Data Analysis. Where this fails is that this Data Cleaning is a part of Data Analysis. I think that this is the kind of thing that fails because the Keyword Alignment Analysis takes things too literally and does not consider the relationships between these different tasks. 

Another task that this kind of fails is when the model said that I did not have experience in project management when I specifically list 4 or 5 different projects that I have led or organized. This is because certain words were not explicitly used to specify that I have done the task. I think that in the Keyword Alignment Analysis along with the Skills Gap Analysis to give it more creativity because this is where the source of failure could be. 