
# WebScraper

A simple and efficient Python-based web scraper that uses Selenium to automate the extraction of table data from websites. The scraped data is saved as a CSV file and can be optionally imported into a MySQL database.

## 🚀 Features

- Automates table data extraction using Selenium
- Supports dynamic table selection via dropdown menus
- Saves scraped data as CSV
- Imports data into MySQL for further analysis (optional)
- Customizable and easy to extend

## 🧠 Use Case

Useful for:
- Automating data collection from dynamic websites
- Converting scraped HTML tables into structured datasets
- Populating relational databases with real-time data

## 📂 Project Structure
```
webscraper/
├── main.py          # Main scraper script using Selenium
├── requirements.txt # List of dependencies
└── README.md        # Project documentation
```


## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/bhargavsai-lingampalli/webscraper.git
cd webscraper
```

### 2. Install Dependencies

Ensure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
```

### 3. Configure WebDriver

Make sure to install the correct WebDriver (e.g., [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)) and place it in your system PATH.

### 4. Run the Script

```bash
python main.py
```

Make sure to edit `main.py` if you want to change the URL, table structure, dropdown logic, or database credentials.

## 🛠 Technologies Used

- Python
- Selenium
- Pandas
- MySQL Connector (optional)

## 📝 License

This project is licensed under the MIT License.

## 🙌 Author

Developed by [Bhargav Sai Lingampalli](https://github.com/bhargavsai-lingampalli)

> Feel free to fork, contribute or report any issues!
