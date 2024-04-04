
# Demo notebooks

|  | Activity | Summary notes |
| :-- | :-- | :-- |
| 0 | [myfirstpy_colab](https://colab.research.google.com/drive/1zCnCLvfYvJk9-UoHYwG2wrz2cneBwaD0) | - [Colab "How-to" Slides](https://docs.google.com/presentation/d/1mTPV4Wqup52IBjfxC3nbBIzovJB-01w1g-l-kQH_Zrc/) | 
| 1 | [Workshop_demo1](https://colab.research.google.com/drive/1imlBKcMkvBnz61H6lFv8cnwvv066zd76) | Highlighting ```polars```, ```seaborn```, ```plotly``` |
| 2 | [Workshop_demo2](https://colab.research.google.com/drive/1BZjUHZugpOIoT3WNCYiRKReROyIHCnu-) | Interactive maps with ```folium```+```bianca```  |
| 3 | Data [I/O (input/output)](https://colab.research.google.com/drive/1THB6N2GOHPA7bxIMeKx50zTp1enKZkkl) <br> | - Examples in ```.json```, ```.xlsx```, ```.data```, ```.csv```, ```.pkl``` <br>  |
| 4 | - [Basics of text processing](https://colab.research.google.com/drive/1wVz-94bDw_teotHaeKXqguPIN75fD7Mo) <br> - [Excel workbook](https://colab.research.google.com/drive/15ErdtG6BFvIvIaydXFr2fLyLJwqoLfQJ?usp=sharing)  <br> - [Downloading files from a website](https://colab.research.google.com/drive/1H5uD5gsuIR_z7qXkY5GUkrFyyT_sOEYG) <br> - [SQLite](https://colab.research.google.com/drive/1WciD3M0D_34yyoSO0DKMa7EpFHcaCUwh) <br> - [Benchmarking demo](https://colab.research.google.com/drive/1N8Z7a1ULXpHV7qqZZ-lLmQ1cHjnkJ7XW) <br> - [```polars``` cheatsheet](https://colab.research.google.com/drive/1ChG5jSXlSH2DUDUwCrRcIbArzzfipF-9) <br> - [plotly](https://colab.research.google.com/drive/1_wnigtXDxg4BSerhWOLC6xi8v76F8UUY) for interactive data visualization | |

### Mounting to Google Drive

```
import os

from google.colab import drive
drive.mount('/content/drive')

my_work_dir = '/content/drive/MyDrive/my_work_dir/'
my_work_dir

try:
  os.mkdir( my_work_dir )
except Exception as e:
  print( e ) 
```

### Suggestions on future Colab notebooks?

- [ ] _______ Add your suggestions here _______

## Data
- [Mapping UBC](https://www.tomasbeuzen.com/python-for-geospatial-analysis/chapters/chapter2_spatial-viz-and-modelling.html)
- [https://j.mp/iriscsv](https://j.mp/iriscsv)
- [Stats Government of New Zealand](https://www.stats.govt.nz/)
- [More here](../data/)

## Kaggle demos
- [```Seaborn``` data visualization](https://www.kaggle.com/learn/data-visualization)
- [```biopython](https://www.kaggle.com/code/samira1992/bioinformatics-project-4-msa)
- [Web-scraping](https://www.kaggle.com/code/jonbown/web-scraping-box-office-data-with-python) 

