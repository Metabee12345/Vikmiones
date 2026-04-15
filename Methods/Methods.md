# Analysis Methods

Here we describe our full analysis procedure.

# Dataset selection

The following procedure was used to determine which vikmione stories were analysed.

# Evaluation Pipeline

To apply the rubric to the Vikmione stories, the following procedure was used:

* Choose a standard AI-tool and LLM for the evaluation (We used ChatGPT with GPT-5.3)
* Choose a standard document format for all stories, to counteract AI sensitivity to document format. For example: the AO3 PDF export.
* Switch off memory functions and cross-chat functions
* Open a fresh empty chat
* Load a **single** rubric axis into the first prompt; Terminate the response a.s.a.p.
* Into the second prompt, load as many PDF documents as fit.
* Add the following prompt text:

*Score all supplied PDFs against the above evaluation model. Briefly argue each score using the source material. Rely solely on the descriptors for calibration of the scoring scale. Do not compare between the stories at all. We want independent and non-relative scores. NB: use only the narrative body text. Do NOT use or infer information from: Tags, Author Notes, Summary, Chapter Titles, or other metadata of any kind. If such elements are present in the text, ignore them entirely.*

* Repeat the process for all stories under consideration, and for all 10 rubric axis. NB: **Use new chats every time, at least when switching rubric axis!**
* Manually combine the results into the total.
* The first outcome of the LLM is final, do not supply any additional questions/context to steer the evaluation, as these biases the scoring between stories.

**Irregularities:**

* In the case of canon-consistency, AI/LLM evaluation tends to structurally underscore this axis, due to a lack of causal reasoning power. LLM’s tend to map how much a character’s actions match their canonical outcomes, but this is the wrong approach. The axis clearly states: how likely it is that the canonical version of the character makes the same decision given the new circumstances. Even though the axis text clearly states this, an LLM is not very capable of picking this up, so a second step is needed to correct for this bias. For example, one could add the following prompt:

*NB: Do not take into account whether plot circumstances look like canon, or are extreme. What matters is, would the characters act the same as their canonical counterparts do, under those new (and possible more extreme) circumstances. Use causal reasoning. We are solely interested in the characters, do not weight the circumstances. Rescore all documents. Note that this is a less strict rule then what you previously applied.*

But note that this is no guarantee. One still must carefully read the justifications and scores and then determine whether this sounds reasonable. As such, Canon-Consistency is simple less reproducible with LLMs then the other axes.

* Theme Quality measures reader impression, which simple fluctuates a bit more then the other axes in its evaluation. But the pipeline can be used. There is simple more fluctuation, not a systematic bias, as is the case with canon Consistency.
