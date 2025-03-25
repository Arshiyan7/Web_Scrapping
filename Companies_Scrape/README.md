# US Largest US Companies by Revenue 💰

## Project Overview

This project aims to scrape the "List of largest companies in the United States by revenue" from Wikipedia. The goal is to extract the data, clean it, and present it in a usable format (e.g., CSV, JSON).
# NOTE: Comments have been added using AI to enhance code readability.  
# The logic and implementation are entirely written by the user.  

## 🎯 Objective

*   Scrape data from the Wikipedia page.
*   Clean and transform the data.
*   Save the data to a CSV file.
*   Present the data in a human-readable format.

## ⚙️ Technologies Used

*   **Python:** The primary programming language.
*   **requests:** For making HTTP requests to fetch the Wikipedia page.
*   **Beautiful Soup 4 (bs4):** For parsing the HTML content.
*   **pandas:** For data manipulation and creating a DataFrame, also saving the data in a csv file

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
    python main.py  # Or the appropriate name of your script
    ```

4.  **Output:**

    The scraped data will be saved in the `/data` directory as `largest_us_companies.csv`.

