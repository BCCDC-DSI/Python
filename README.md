[View as GitPages](https://bccdc-dsi.github.io/Python-Git-workshop/) | [View on GitHub](https://github.com/BCCDC-DSI/Python-Git-workshop/edit/main/colab/readme.md)

# 2024-APR-05: Interactive workshop on Git & Python for Reproducible Research

## Setup
 
### April 4th - prep session

- We will assist attendees with installing Anaconda3 and getting accounts for ```Streamlit``` and GitHub. 

### April 5th - main session

Please create an account for each of the following platforms depending on your personal goals:

| Accounts to obtain | Goals |
| :-- | :-- |
| Colab[^1] | ... if you would like to save your work done during the workshop |
| Colab, GitHub, Streamlit | ... if you would like to get the most out of the workshop |
| [Google](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=ARZ0qKJlj6VIf3H8gET1BA2BD8q98Mm4xnSs68VLWCmFiPkNzPaJJzqZc710ymyW9iZ8fWezEDxlLg&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1207831730%3A1711210547935397&theme=mn&ddm=0), [GitHub](https://github.com/), [Streamlit](https://streamlit.io), [Kaggle](https://www.kaggle.com/) | ... if you would like to try out everything that was mentioned during the workshop |

[^1]:Colab + Kaggle ***offer free Graphical Processing Units*** for deep learning

## Quick how-to

- **Windows users**, visit [Citrix PHSA login page](https://remoteapps.healthbc.org/logon/LogonPoint/tmindex.html) to download Anaconda3 (needed for creation of virtual environments) 
- **Mac users**, use terminal and simply copy-paste to install Git:
  ```
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  brew install git
  ```


## Python from beginning

| Complexity |   |
| :-- | :-- |
| Python 101 | - [Colab notebooks on select topics to help you get started](colab/) <-- ***Offers free GPU*** <br>- [https://ubc.syzygy.ca/](https://ubc.syzygy.ca/) <br>- [https://sfu.syzygy.ca/](https://sfu.syzygy.ca/) <br>- [Jupyter.org](https://jupyter.org/try-jupyter/lab/) |
| Python 102 | - [Installing on your personal device with admin rights](https://intro-stat-learning.github.io/ISLP/installation.html) <br>- [Creating virtual environments inhouse](python/seasoned) <br>- [Guidelines](https://docs.google.com/presentation/d/1Tc6bMM7UWm92aahi-pleJUBNRh_fDl_D7jgNZbErbY4/) <br>- [IDE tools](rr/tools) |
| Python 201 | - [Demo on writing classes](https://colab.research.google.com/github/hmok/Tutorials/blob/master/beginnersPythonCheatSheet.ipynb#scrollTo=Class_inhertitance) <br>- [Demo on Copying objects](https://colab.research.google.com/drive/17pKv9A7dLAiG2DDcY1nsnXflWBk3XTRK)|  
| Python users picking up R | - [2019 blog](https://medium.com/@nawazahmad20/r-for-python-programmers-part-1-ca4eab668b8c) <br> |


    

For software-production projects, please ***consult with your manager before electing to develop your products in Python***.  

## R users complementing work with Python
- [Resources](r_users/)
 
## Reproducible Research (RR)

- [Resources](rr)
- [Repeatable development environments with IDE](rr/tools)

## Open textbooks 
- [R for Data Science](https://r4ds.had.co.nz/index.html) ([Python](https://byuidatascience.github.io/python4ds/index.html) version) 
- [Python for SAS Users](https://www.pythonforsasusers.com/)
- [Introduction to Statistical Learning](https://www.statlearning.com/resources-second-edition)
   - [Python / R versions of this textbook](https://github.com/intro-stat-learning/ISLP_labs/tree/stable)
     <details>      
      <summary>Setting up the virtual environment for ISLP</summary>
      
        To install the current version of the requirements run:
      
        ```
        $ pip install -r https://raw.githubusercontent.com/intro-stat-learning/ISLP_labs/v2.1.3/requirements.txt
        $ jupyter lab Ch02-statlearning-lab.ipynb   # an example to launch the notebook for Chapter 2 
        ```
  
     </details>

### Domain specific
- [Python for biologists](https://www.pythonforbiologists.org/)

   
## Acknowledgements

Many thanks to *Data & Analytics Services* and the curriculum consultants:
- Abdulaa Babili
- Chris Fjell 
- Citlali Marquez
- Dahn Jeong
- Fran Thistlethwaite
- Jamal Taghavimehr
- John Palmer
- Michael Kuo
- Mike Irvine
- Nirupama Tamvada
- Rebeca Falcao


