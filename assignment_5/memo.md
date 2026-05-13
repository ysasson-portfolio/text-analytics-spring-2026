# Technical Memo

**TO:** Technical Manager
**FROM:** Yarden Sasson
**RE:** Job Fit Analyzer Application

**Summary:**

I have built an application that helps users determine their fitness and compatibility for the job based on their resume and the job descriptions of the resumes that they are interested in. This was done by building a Large Language Model that utilized a Retrieval Augmented Generation (RAG) system to pull the necessary information from the documents that are provided (resume, job descriptions, and the metadata for the job descriptions) and feed them to the mode. Each document that is applied to the model in the initial stages helps provide more context and data for the model to recall and use later to help make the determinations abut fitness. 

The three analyses that were used in this application to determine the fitness and compatibility of a candidate for the job were a skill gap analysis, keyword alignment analysis, and the fit summary narrative. The model conducts the skill gap analysis by reading the job description and the resume and finds the similarities and differences between the description and the resume by retrieving the relevant skills from the job description and comparing it to the resume. Once it finds the similarities and the skill gaps, the RAG system can retrieve the necessary evidence from both the job description and the resume. Then, the LLM can come up with ways to close the skill gap based on the retrieved excerpts. The Keyword analysis identifies the necessary keywords from the job description and then tries to see how relevant those keywords are to the person's resume. This identifies how relevant the important skills are and then identifies whether the person has something that matches the keyword on the resume. The final form of analysis takes the resume and job description and writes a 3-4 sentence narrative about whether or not the person is good for the job based on their resume. It will also retrieve the evidence to include in the narrative using the RAG system. 

**How the Prompts were built and why?**

When building the model we made conducted quite a few experiments when it came to the size of the chunks that were used for the embeddings for the model along with the prompts that the LLM will use along with the RAG system to generate the responses.

The job descriptions that were uploaded into the system varied in length which affected the overall number of clusters that were produced by the system. I did not want to put too large of a chunk size because it would go into the next description and change the context. I also wanted to make sure there was enough overlap to make sure that the descriptions could have a proper amount of context between the chunks. When looking at the way we chunk, I found it better to chunk by word instead of the fixed number of characters because it would not end the chunk in the middle of a word. This allows context to be maintained and easily interpretable by the model. 

Creating the prompt that the LLM would use to conduct the analysis had to be crafted very carefully. Experiments were conducted throughout the prompt engineering process including the length of the prompt, specificity of the prompt, whether or not it included examples, and how the prompt was broken down. The best prompt used specific sections within the prompt (i.e. Task and Restrictions) while also including an example. The more detail that was included the better the model performed. Also, having a few-shot approach (showing multiple examples within the prompt so that it can produce a very specific output) produced better results that were more detailed and relevant to the analysis that were trying to executed using the LLM. 

**Results**



**Key Limitation**

A limitation this project has is that sometimes texts have subtle meanings that the model or the RAG method will be deemed as irrelevant. The way that this model works is that it takes the exact meaning of the words in the context that is defined by the embeddings and the text being passed into the LLM. For example if a job is asking for experience with data visualization software, it may not always process that Tableau qualifies for that requirement. The wording of the job description and the resume is very important to make sure that the model picks up all of the relevant pieces of text even if it is not explicitly stated. 

Another limitation is that it takes the text too literally. When it comes to saying the amount of experience is necessary to do the job, it takes that as a major consideration. Most of the time requirements such as the amount of time they have been in the industry can be exaggerated by the people who are posting the job descriptions. Because of this the model can provide a more skewed judgement about whether the individual is qualified for the job. 
