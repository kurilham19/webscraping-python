# Objective

**Scrapping website using BeautifulSoap library. Retrieve name and price from website, then convert it into csv file.**

# Installation

## Installation using conda environment

1. **Python Conda Environment**

   - Install Anaconda or Miniconda: [Download Anaconda](https://www.anaconda.com/products/individual)

   - Create a conda environment:
     ```shell
     conda create --name <environment_name>
     ```

2. **Activating the Conda Environment**

   - Activate the conda environment:
     - On Windows:
       ```shell
       conda activate <environment_name>
       ```
     - On Unix or Linux:
       ```shell
       source activate <environment_name>
       ```

3. **Once the environment is activated, you're ready to use the project!**

## Installation using virtualenv

1. **Python Virtual Environment**

   - Install Python if not already installed: [Download Python](https://www.python.org/downloads/)

   - Create a virtual environment:

     ```shell
     python -m venv <environment_name>
     ```

   - Activate the virtual environment:
     - On Windows:
       ```shell
       <environment_name>\Scripts\activate
       ```
     - On Unix or Linux:
       ```shell
       source <environment_name>/bin/activate
       ```

2. **Project Dependencies**

   - Install the project dependencies:

     ```shell
     pip install -r requirements.txt
     ```

   - The `requirements.txt` file contains a list of project dependencies.

   - Once the installation is complete, you're ready to use the project!

## How to run the module

You can run the application in development by run the following command:

```shell
python main.py
```

## Result

The main.py will create .csv file to /assets/csv which the name you can define in

```python
# Convert list to csv
file_name = "ProductList3.csv"
```
