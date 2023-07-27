# Data Extraction Automation

## Table of Contents
- [Introduction](#introduction)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Introduction
This project provides a handy toolkit for extracting and transforming data from various online sources. It leverages the powerful pandas library to facilitate easy extraction of tables from websites and CSV files and extract tables from PDFs.

## Description
Often, when dealing with data analysis or machine learning tasks, we encounter data in various formats spread across different sources. This project aims to streamline the process of extracting and transforming data from the most common sources like websites, CSV files, and PDFs, making it easier for data scientists and analysts to access relevant data effortlessly.

## Installation
To use this toolkit, you'll need Python and the pandas library installed on your system. If you don't have pandas installed, you can do so via pip:

```bash
pip install pandas
```

The project also requires the 'camelot' library for PDF data extraction. You can install it using:

```bash
pip install camelot-py[cv]
```

## Usage
The toolkit provides three main functionalities:

1. Extracting tables from websites using pandas:
```python
import pandas as pd

# Example: Extracting tables from a website
website = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
print(len(website))  # 23 tables
print(website[1])  # first table
```

2. Extracting CSV files from websites using pandas:
```python
# Example: Extracting a CSV file from a website and renaming columns
import pandas as pd

df_premier23 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')
df_premier23.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'}, inplace=True)
print(df_premier23)
```

3. Extracting tables from PDFs using Camelot:
```python
import camelot

# Example: Extracting tables from a PDF and exporting to CSV
tables = camelot.read_pdf('foo.pdf', pages='1')
print(tables)
tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')
```

## Examples
In the 'examples' folder, you will find more detailed examples demonstrating how to use the toolkit for various data extraction scenarios.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as per the terms of the license.
