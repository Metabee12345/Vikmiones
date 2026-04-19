# Discussion

The full list of rubric scores can be found [here](https://metabee12345.github.io/Vikmiones/Results/). The purpose of the rubric development and application, is to determine whether it is possible to **measure quality of a story in an unbiased and reproducible way.**

# Statistics

Here, we discuss the outcomes and meaning of different statistical tools. The calculation procedure is explained [here](https://metabee12345.github.io/Vikmiones/Methods/).

## Cronbach's alpha

As such, [Cronbach's alpha](https://en.wikipedia.org/wiki/Cronbach%27s_alpha) was calculated for the rubric results, yielding α = 0.78±0.01

Now, α=0 means the different tests (rubric axes) are completely unrelated, while α=1 means that the different tests (rubric axes) measure the exact same thing.
As such, the interpretation of α = 0.78±0.01 requires some nuance. As this value is fairly high, the different rubric axes are clearly related by some underlying principle. However, as α is also significantly lower then 1, the different rubric axes also clearly measure distinct properties in a story. This result is exactly what we are hoping for. We do not want the different rubric axes to have nothing to do with each other. Why else would we combine them into the same rubric? But we also do not want them to measure the exact same thing. Ehy else would we need different axes? We want the axes to all measure different aspects of the same underlying property. α = 0.78±0.01 clearly demonstrates that this is the case.

However, Cronbach's alpha cannot tell us anything about what this underlying property is. We hope that it is intrinsic story quality. But that cannot be extracted using Cronbach's alpha. Only that the rubric clearly contains some underlying property.

## Spearman correlation

The Spearman correlation of the rubric (for all 30 [stories](https://metabee12345.github.io/Vikmiones/Results/)) for two different rubric evaluations, was found to be ρ=0.92

This proves that ranking, based on the rubric score is extremely stable. Again, it does not prove that the rubric indeed measures story quality, but we do know for sure that the rurbic measures different aspects of some underlying property of stories (α = 0.78±0.01), and that ranking stories based on this underlying property is extremely stable (ρ=0.92).

## Mean Relative Deviation (MRD)

The Mean relative Deviation was calculated to be MRD = 5.7 with rubric scores ranging from 0 till 100. The interpretation of this number requires some context. For the 30 [stories](https://metabee12345.github.io/Vikmiones/Results/) investigated, scores range from MIN=34.1 to MAX=87.9 with μ=65.1 and σ=13.3

Note that these properties are reasonably close to a uniform distribution (with these MIN and MAX, these would be μ=61 and σ=15.5). As such, we conclude that the rubric scores do not cluster for different stories, but have a good spread. A spread that is meaningful, as σ is about 2.3x larger then the MRD.

As such, the fluctiuations in rubric score (MRD) are significantly smaller then the spread in rubric scores (σ). Hence, we conclude that the absolute rubric score provides a meaningful distinction for stories.

## Conclusion

We conclude that the rubric developed for Vikmione stories measures different aspects of a clear underlying property from those stories (α = 0.78±0.01). The absolute rubric score assigned to the stories is a meaningful number (MRD = 5.7; σ=13.3) to reflect that underlying property, and ranking based on this underlying property is stable (ρ=0.92). But it remains to be seen whether this underlying property is indeed what we call 'intrinsic story quality'.

# Correlation study

The correlation between Popularity and Total rubric score was investigated, wehere Popularity is defined as Correction*Hits/Time. Correction is a factor between 0 and 1, with only a substantial deviation from 1 in the first several months after publication, to correct for the effects of a launch spike. Further detials are explained in our [Methds](https://metabee12345.github.io/Vikmiones/Mwethods/). See the figure below for the correlation plot.

<p style="text-align: center;">
  <img
    src="https://raw.githubusercontent.com/Metabee12345/Vikmiones/main/Script/Correlation.png"
    alt="Correlation between rubric score and popularity"
    style="max-width: 100%; height: auto; border: 1px solid #ddd; padding: 4px;"
  ><br>
  <em>
    Figure: Correlation between rubric score and popularity (lifecycle*hits/time).
  </em>
</p>

