# Analysis Methods

The purpose of this investigation is to determine whether it is possible to **measure quality of a story in an unbiased and reproducible way.**

Rubric analysis is a well-known evaluation method for large bodies of text. It basically means that you define seperate categories/themes/topics to evaluate the text (the so-called rubric-axes) and score the text on each category. To guide the scoring process, quantitative scores are accompanied by arguments that state what awards a certain score (the so-called descriptors). If you are interested. If you are interested, you can find more about rubric scroing methods here:

* [https://vu.nl/en/employee/didactics/how-to-develop-a-rubric](https://vu.nl/en/employee/didactics/how-to-develop-a-rubric)
* [https://en.wikipedia.org/wiki/Rubric_(academic)](https://en.wikipedia.org/wiki/Rubric (academic))
* [https://smowl.net/en/blog/assessment-rubrics/](https://smowl.net/en/blog/assessment-rubrics/)

The scope of our analysis are serious Hermione/Viktor Harry Potter fanfictions (so-called vikmiones), meaning:

* The story is a Harry Potter Fanfiction.
* One of the main focus points in the story is the Hermione/Viktor relationship.
* Hermione/Viktor is one of the endgame pairings.
* The story contains meaningful narrative content (explicit scenes are not the main purpose of the text).

You can find the rubric that was used for this narrative scope [here](https://metabee12345.github.io/Vikmiones/Rubric/). The rubric has been tuned to the scope, but formulations and criteria have been specifically formulated in a way to only judge the quality of execution of the work; not to punish any creative choices on plot, characterizations, worldbuilding, etc. As such, the rubric is aiming to be *discrimination-free* within the scope.

Next, a suitable portion of vikmione has to be selected, and the rubric has to be applied to each of them. This is done with generative AI (we used ChatGPT, with GPT-5.3). It is no certainty that an AI reader is able to judge a story better then a human reader. AI evaluation was chosen for its consistency and reproducibility, rather than for superior interpretative ability. Finally, the results were interpreted using statistical analysis. Read below about the details on each of the different steps.

# Dataset selection

Vikmione stories were selected from [AO3](https://archiveofourown.org/), one of the largest sites to host fanfiction in the world. However, it also has a detailed tag-system on relationships, characters, and other story elements that allow us to easily and effectively sweep the site content, and a standarised PDF-export. The PDF-export is an important feature, as AI-readers are heavily influenced by the format and structure of the documents offered. By using a standarised PDF-export for each investigated story, this type of bias can be effectively eliminated from the story.

You can use the AO3 tag-system to search for vikmione stories [here](https://archiveofourown.org/tags/Hermione%20Granger*s*Viktor%20Krum/works). In this analysis, we did **not consider** vikmiones from another source then AO3 (because those document formats are different). We sampled the site at **date 9th of APril 2026**.

We used the following criteria to reduce the set of [all vikmiones on AO3](https://archiveofourown.org/tags/Hermione%20Granger*s*Viktor%20Krum/works) to a workable scope of 'serious' stories:

* Select *Harry Potter - J. K. Rowling* as the only fandom, and **exclude** cross-overs.
* Select *Language: English* This is the largest portion of available languages, and we wish to eliminate biases in the analysis due to different languages.
* Select *Wordcount: >=50k* The number of 50k words is fairly aribtrary, but the purpose of this filter is to distuingish one-shots and short-stories from longer ones.
* *Exclude other Hermione relationships*, for example:

    - Hermione Granger/Draco Malfoy
    - Hermione Granger/Ron Weasley
    - Hermione Granger/Harry Potter
    - Hermione Granger/Severus Snape
    - Hermione Granger/Charlie Weasley
    - Hermione Granger/Fred Weasley
    - Hermione Granger/George Weasley

On the **9th of April 2026**, the total collection of [Hermione/Viktor stories]https://archiveofourown.org/tags/Hermione%20Granger*s*Viktor%20Krum/works) was 1716 works. The above selection steps reduced this to 122 works. See the definition of the vikmione scope above. usually, when Hermione/Viktor is combined in a story with another Hermione-pairing, the Hermione/Viktor-pairing is not endgame. This is not a hard-enforced rule, but a very strong pattern. Hence, together with the wordcount-filter (longer fics with meaningful narrative content), crossover-filter (our scope is pure Harry Potter) and

* Manual read of tags & Summaries

# Evaluation Pipeline

To apply the rubric to the Vikmione stories, the following procedure was used:

* Choose a standard AI-tool and LLM for the evaluation (We used ChatGPT with GPT-5.3)
* Choose a standard document format for all stories, to counteract AI sensitivity to document format. For example: the AO3 PDF export.
* Switch off memory functions and cross-chat functions
* Open a fresh empty chat
* Load a **single** rubric axis into the first prompt; Terminate the model response immediately after the rubric axis has been acknowledged.
* Into the second prompt, load as many PDF documents as permitted by the models features (in our case the limit was 20).
* Add the following prompt text:

*Score all supplied PDFs against the above evaluation model. Briefly argue each score using the source material. Rely solely on the descriptors for calibration of the scoring scale. Do not compare between the stories at all. We want independent and non-relative scores. NB: use only the narrative body text. Do NOT use or infer information from: Tags, Author Notes, Summary, Chapter Titles, or other metadata of any kind. If such elements are present in the text, ignore them entirely.*

* Repeat the process for all stories under consideration, and for all 10 rubric axis. NB: **Use new chats every time, at least when switching rubric axis!**
* Scores for each axis were aggregated manually into a total score (see the [rubric]((https://metabee12345.github.io/Vikmiones/Rubric/)) for the exact rules).
* The first outcome of the LLM is final, do not supply any additional questions/context to steer the evaluation, as these biases the scoring between stories.

**Irregularities:**

* In the case of canon-consistency, AI/LLM evaluation tends to structurally underscore this axis, due to a lack of causal reasoning power. LLM’s tend to map how much a character’s actions match their canonical outcomes, but this is the wrong approach. The axis clearly states: how likely it is that the canonical version of the character makes the same decision given the new circumstances. Even though the axis text clearly states this, an LLM is not very capable of picking this up, Hence, A secondary prompt was used to correct for this effect. Final scores were accepted for this axes, only after manual verification of the model’s reasoning.

*NB: Do not take into account whether plot circumstances look like canon, or are extreme. What matters is, would the characters act the same as their canonical counterparts do, under those new (and possible more extreme) circumstances. Use causal reasoning. We are solely interested in the characters, do not weight the circumstances. Rescore all documents. Note that this is a less strict rule then what you previously applied.*

But note that this is no guarantee. One still must carefully read the justifications and scores and then determine whether this sounds reasonable. As such, Canon-Consistency is simple less reproducible with LLMs then the other axes.

* Theme Quality measures reader impression, which simple fluctuates a bit more then the other axes in its evaluation. But the pipeline can be used. There is simple more fluctuation, not a systematic bias, as is the case with canon Consistency.

# Statistical Analysis

Still have to develop this.
