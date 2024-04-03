
# R users picking up Python

## But why?

> Think of Python and R as *complementary* and not competing tools

## Pizza vs Ravioli
- [2017 comparison](https://www.airitilibrary.com/Article/Detail/16838602-201707-201711160005-201711160005-355-371)

|  R |  Python |
| :-- | :-- |
| [![Introduction to Statistical Learning by Gareth et al.](https://images.squarespace-cdn.com/content/v1/5ff2adbe3fe4fe33db902812/1611294680091-25SIDM9AHA8ECIFFST23/Screen+Shot+2021-01-21+at+11.02.06+AM.png?format=150w 'R version')](https://www.statlearning.com/resources-second-edition) | 
 [![Python version](https://images.squarespace-cdn.com/content/v1/5ff2adbe3fe4fe33db902812/8b373fbe-d1b4-4351-b803-0d3cd5bba1b0/ISLP_cover.png?format=150w 'Python version')](https://www.statlearning.com/resources-python) |


## Recommended readings

- [Best practices for R and Python side by side](https://docs.google.com/presentation/d/1Tc6bMM7UWm92aahi-pleJUBNRh_fDl_D7jgNZbErbY4/)
- [Using Python in R with reticulate](https://cran.r-project.org/web/packages/reticulate/vignettes/python_primer.html)
- [Experiences on transitioning Python projects to R](https://towardsdatascience.com/the-starter-guide-for-transitioning-your-python-projects-to-r-8de4122b04ad)

 
## Packages available in both R and Python

| Package name | R | Python | Notes |
| :-- | :-- | :-- | :-- |
| Plotly | https://plotly.com/r/ | https://plotly.com/python/ | [side-by-side guide](https://datascientyst.com/pandas-vs-r-cheat-sheet/) |
| Polars[^1]: | https://rpolars.github.io/ | https://docs.pola.rs/ | [side-by-side guide](https://robertmitchellv.com/blog/2022-07-r-python-side-by-side/r-python-side-by-side.html), [Polars vs Pandas](https://blog.jetbrains.com/dataspell/2023/08/polars-vs-pandas-what-s-the-difference/) |
| Bayesian inference | [rstan](https://cran.r-project.org/web/packages/rstan/vignettes/rstan.html) |  [pystan](https://pystan.readthedocs.io/) | ... |
| janitor | janitor | Pyjanitor |

[^1]:[A simple benchmark Colab demo comparing Ploars with Pandas in Python](https://colab.research.google.com/drive/1N8Z7a1ULXpHV7qqZZ-lLmQ1cHjnkJ7XW)



## Comparable packages (not direct port) 

| Package name | R | Python | Notes |
| :-- | :-- | :-- | :-- |
| ... | bioconductor | biopython | ... |
| Violin plots, heatmaps  | ggplot2 | Seaborn | [seaborn and ggplot2](https://medium.com/@oneymavenessa/an-alliance-python-and-r-seaborn-and-ggplot2-233864b77bc4)|


[Return to Home](https://bccdc-dsi.github.io/Python-Git-workshop/)
