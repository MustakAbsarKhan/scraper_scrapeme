# 🛒 Scrapeme Web Scraper

A simple yet powerful Python web scraper that extracts product **titles** and **prices** from the Scrapeme website across all pages.

---

## 📌 Project Overview

This project demonstrates how to:

- Send HTTP requests using `requests`
- Parse HTML using `BeautifulSoup`
- Handle pagination automatically
- Extract structured product data
- Store scraped data into a CSV file using `pandas`
- Implement error handling and polite scraping (delays)

---

## 🚀 Features

- ✅ Scrapes **all pages automatically**
- ✅ Extracts **product title and price**
- ✅ Handles **missing elements safely**
- ✅ Uses **session + headers** to mimic real browser
- ✅ Includes **random delays** to avoid blocking
- ✅ Exports data to **CSV file**

---

## 🛠️ Technologies Used

- **Python 3**
- **requests**
- **BeautifulSoup (bs4)**
- **pandas**
- **lxml**

---

## 📂 Project Structure

```

scrapeme-scraper/
│── scraper.py
│── products_info.csv
│── README.md

````

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/scrapeme-scraper.git
cd scrapeme-scraper
````

Install dependencies:

```bash
pip install requests beautifulsoup4 lxml pandas
```

---

## ▶️ How to Run

```bash
python scraper.py
```

---

## 📊 Output

After running the script, a CSV file will be generated:

```
products_info.csv
```

### Example Output:

| Title     | Price |
| --------- | ----- |
| Bulbasaur | £63   |
| Ivysaur   | £87   |

---

## ⚠️ Notes

* This project is for **educational purposes only**
* Always respect a website’s **robots.txt** and terms of service
* Avoid sending too many requests in a short time

---

## 👨‍💻 Author

**Mohammad Mustak Absar Khan**

---

## ⭐ Support

⭐ If you found this helpful, consider giving it a ⭐ on GitHub!

If you like this project:

⭐ Star this repository

🍴 Fork it

🧠 Use it as inspiration

---
