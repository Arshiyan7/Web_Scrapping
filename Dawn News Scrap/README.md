# 📰 Dawn News Scraper 🌐

## Project Overview

This project scrapes headlines and links from the Dawn newspaper website (www.dawn.com).  The goal is to extract current news headlines and their corresponding URLs and save them into a CSV file.

## 🎯 Objective

*   Fetch the HTML content of the Dawn website.
*   Parse the HTML to extract all `<h2>` tags containing headlines and links.
*   Clean the data, ensuring proper URL formatting.
*   Save the extracted headlines and links into a CSV file named `dawn_headlines.csv`.

## ⚙️ Technologies Used

*   **Python:** The core programming language.
*   **requests:** For retrieving the HTML content of the website.
*   **Beautiful Soup 4 (bs4):** For parsing the HTML and navigating the DOM.
*   **pandas:** For creating DataFrames (though not explicitly used in the provided code, pandas is imported).
*   **csv:** For writing the extracted data to a CSV file.

## 🚀 Setup and Usage

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install dependencies:**

    ```bash
    pip install requests beautifulsoup4 pandas
    ```

3.  **Run the script:**

    ```bash
    python DAWN_News_Scrapping.ipynb  # Make sure you have jupyter installed
    ```
    or run this inside jupyter notebook

4.  **Output:**

    The scraped headlines and links will be saved in the same directory as the script, in a CSV file named `dawn_headlines.csv`. The script will print a confirmation message to the console: `"CSV Saved Successfully as dawn_headlines.csv"`.

## 📁 File Structure

*   `DAWN_News_Scrapping.ipynb`: Jupyter Notebook containing the Python code for scraping and saving the data.
*   `dawn_headlines.csv`: (Output) CSV file containing the scraped headlines and links.

## 📝 Notes

*   The script currently targets the main page of dawn.com.  Modifications may be needed to scrape specific sections or archives.
*   Website structures can change, potentially breaking the scraper. Regular maintenance and updates may be required to ensure the script continues to function correctly.
*   Be mindful of the website's terms of service and robots.txt when scraping. Avoid excessive requests to prevent overloading the server.