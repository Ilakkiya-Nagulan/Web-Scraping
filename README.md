# Amazon Product Data Scraper

This repository contains a Python-based web scraper designed to extract and compile data from structured HTML pages simulating Amazon product listings. The scraper reads specific elements from HTML files, such as product names, prices, and reviews, and exports them into an organized Excel spreadsheet. This project aims to demonstrate and facilitate learning about web scraping, data parsing, and automation of data entry into spreadsheets.

## Project Features

1. **HTML Parsing**: Utilizes the BeautifulSoup library to navigate and parse HTML content.
2. **Data Extraction**: Capable of extracting key product details including names, prices, and reviews.
3. **Excel Integration**: Uses the pandas and openpyxl libraries to seamlessly export the scraped data into Excel format, allowing for easy data manipulation and reporting.

## Technical Requirements

This project requires the installation of several Python libraries to function properly. The necessary libraries include:

1. **beautifulsoup4**: For parsing HTML documents.
2. **lxml**: Acts as a parser for BeautifulSoup and provides tools for XML processing.
3. **pandas**: Facilitates data manipulation and analysis.
4. **openpyxl**: Enables reading from and writing to Excel files.

## Installation

You can install the required dependencies using the following commands:

```bash
pip install beautifulsoup4
pip install lxml
pip install pandas
pip install openpyxl
```

Alternatively, you can create a `requirements.txt` file and install all dependencies at once:

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

### Running the Application

1. Clone the repository:

```bash
git clone https://github.com/your-username/amazon-product-data-scraper.git
cd amazon-product-data-scraper
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

> Note: Make sure to create a `requirements.txt` file that includes all the required packages. You can generate this file using:

```bash
pip freeze > requirements.txt
```

3. Run the scraper script to extract data and export it to an Excel file:

```bash
python webscrape.py
```

## Steps to Implement

1. **Setup Development Environment**: Install Visual Studio Code, Python, and the required libraries (BeautifulSoup, pandas, openpyxl).
2. **Prepare HTML File**: Download and save the `Amazon.html` file in your project directory.
3. **Create and Code Script**: Write a Python script, `webscrape.py`, to parse the HTML and extract product details.
4. **Execute Script**: Run the script from Visual Studio Code’s terminal to perform the data extraction.
5. **Verify Output**: Check the `Products.xlsx` file to ensure it contains the correct columns and data extracted from the HTML.

## Execution of the Code

This Python script is designed to parse a locally saved HTML file of an Amazon product listing page and extract information about each product.

### Code Explanation

1. **Import necessary modules**: The script imports pandas for data manipulation, and BeautifulSoup for parsing HTML.
2. **Define `read_and_parse_html` function**: This function takes a file path as an argument, opens the file, reads its content, and parses the HTML using BeautifulSoup. It returns a BeautifulSoup object.
3. **Define `extract_product_info` function**: This function takes a BeautifulSoup object as an argument. It finds all `div` elements with a specific class (which represents individual product listings), and for each `div`, it finds the product name, price, and reviews. It stores this information in a dictionary and appends the dictionary to a list.
4. **Define `save_to_excel` function**: This function takes a list of product information dictionaries and an optional file path as arguments. It converts the list to a pandas DataFrame and saves the DataFrame to an Excel file.
5. **Define `main` function**: This function is the main entry point of the script. It calls the `read_and_parse_html` function to parse the HTML file, the `extract_product_info` function to extract the product information, and the `save_to_excel` function to save the information to an Excel file.
6. **Run the `main` function**: If the script is run as a standalone program (not imported as a module), the `main` function is called.

The script assumes that the structure of the HTML file matches the structure of an Amazon product listing page. If the structure is different, the script might not work correctly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
- [lxml](https://lxml.de/)

---
