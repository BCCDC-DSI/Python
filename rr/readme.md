
# Reproducibility

## Version control
- [Git](../git)

## Platforms
- Kaggle
- Digital Ocean
- Google Colab
- Jupyter.org
- ...


## Recommended practices
- [markdown](https://www.markdownguide.org/basic-syntax/)

## Example workflows
<details>
<summary>R</summary>

  ```
  # Makefile (target: required_files)
  
  manuscript.pdf: manuscript.Rmd simulated_data.csv 
  
  Rscript -e 'rmarkdown::render("manuscript.Rmd")' 
  
  simulated_data.csv: simulate.R
  
  Rscript -e 'source("simulate.R")' 
  ```
Source: [MDPI 2020](https://mdpi-res.com/psych/psych-03-00053/article_deploy/psych-03-00053.pdf)

</details>


## References
- Davos: A Python package ‘‘smuggler’’ for constructing lightweight reproducible notebooks, Paxton C. Fitzpatrick, Jeremy R. Manning [2024 article](https://doi.org/10.1016/j.softx.2023.101614)
