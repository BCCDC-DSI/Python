

# Creating and working in a virtual environment

Creation of virtual environments allows us to build a stable, reproducible, and portable environment. This strategy is applicable when you code in Python, R, etc.  


Users may create multiple virtual environments (VE) as project needs evolve. For instance, you may have created a VE that used R 4.1.1 last year, and wish to create a new one as you transition to R 4.3.1.

The three general steps of building a VE are:
1. Create
2. Activate
3. Build, i.e. build the environment by installing (opensource) software packages



Below, we provide abbreviated steps to get you started in building your own VE with Python 3.12; more detailed instructions can be found in [this Primer](https://realpython.com/python-virtual-environments-a-primer/). 

Note that we will use a command-line software called [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) that can be used in Windows, macOS, and other systems.




## Creating a virtual environment on your PC 




1. ```Program``` > ```Anaconda Powershell```

2. Change your current directory to your personal drive (U:\). Do so by typing below in PowerShell:
   ```
   U:
   ```

2. Create virtual environment (VE) named ```py3.12``` by typing a command like below in PowerShell:

   ```
   conda create --name py3.12 python=3.12   
   ```

3. Activate this VE with a command like this:

   ```
   conda activate py3.12
   ```   


## Building your new virtual environment 


1. When your new VE is activated, you will notice the its name appearing at the front like this:

   ```
   py3.12 U:\> 
   ```  

2. To install interactive Python, enter:

   ```
   pip install ipython
   ```  

3. To install other Python packages, enter:

   ```
   pip install plotly polars scikit-learn scikit-survival streamlit
   ```



## Creating a kernel for use of your new VE in Jupyter Notebook  

1. Install ipykernel 

   ```
   pip install ipykernel
   ```

2. To Create Jupyter kernel for use in Jupyter notebook:
  
   ```
   ipython kernel install --user --name=py3.12-ker
   ```
  
   where ```py3.12-ker``` is the name of the kernel that you may select from the menu once you launched Jupyter notebook (top-right corner)



[Return to Home](https://bccdc-dsi.github.io/Python-Git-workshop/)
