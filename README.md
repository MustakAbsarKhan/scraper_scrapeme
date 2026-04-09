---

# 🛒 Scrapeme Web Scraper

### ⚡ Production-Ready Python Scraper with Pagination, Data Export & Clean Architecture

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/Requests-HTTP-green">
  <img src="https://img.shields.io/badge/BeautifulSoup-Parsing-orange">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-purple">
  <img src="https://img.shields.io/badge/Status-Completed-success">
</p>

---

## 🚀 Overview

A **robust, scalable web scraper** built with Python that extracts product data from a real-world eCommerce demo site.

✔ Handles **pagination automatically**
✔ Extracts **complete product metadata**
✔ Implements **polite scraping practices**
✔ Exports clean data into **CSV format**

> 💡 Designed as a **portfolio-grade project** demonstrating real-world scraping skills.

---

## 🎯 Features

✨ What makes this project stand out:

* 🔄 **Automatic Pagination Detection**
* 🌐 **Session-Based Requests (Faster & Efficient)**
* 🧠 **Fault-Tolerant Data Extraction**
* ⏱️ **Random Delays (Anti-blocking)**
* 📦 **Structured Data Storage**
* 📊 **CSV Export via pandas**
* 🔗 Extracts:

  * Product Title
  * Price
  * Image URL
  * Product URL

---

## 🧠 How It Works

```text
Initialize Session → Fetch First Page → Detect Total Pages
        ↓
Loop Through Pages → Extract Product Data
        ↓
Apply Delay → Store Data → Convert to DataFrame
        ↓
Export to CSV
```

---

## 🛠️ Tech Stack

| Category      | Tools Used          |
| ------------- | ------------------- |
| Language      | Python 🐍           |
| HTTP Client   | requests            |
| Parsing       | BeautifulSoup (bs4) |
| Parser Engine | lxml                |
| Data Handling | pandas              |

---

## 📂 Project Structure

```
scrapeme-scraper/
│
├── scraper.py            # Core scraping logic
├── products_info.csv     # Generated dataset
└── README.md             # Documentation
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/scrapeme-scraper.git
cd scrapeme-scraper
```

### 2. Install Dependencies

```bash
pip install requests beautifulsoup4 lxml pandas
```

---

## ▶️ Usage

```bash
python scraper.py
```

---

## 📊 Sample Output

### 🖥️ Console

```
Response Status Code: 200
Max page number: 48

Scraping page 1...
Title: Bulbasaur, Price: £63

...

Total products scraped: 755
CSV saved successfully!
```

---

### 📄 CSV Output

| Title     | Price | Image URL | Product URL |
| --------- | ----- | --------- | ----------- |
| Bulbasaur | £63   | ...       | ...         |
| Ivysaur   | £87   | ...       | ...         |

✔ Encoding: `utf-8-sig` (Excel-ready)

---

## 🛡️ Error Handling & Reliability

* ✔ Handles **network failures**
* ✔ Prevents crashes from **missing HTML elements**
* ✔ Uses `try-except` for safe execution
* ✔ Continues scraping even if a page fails

---

## ⚠️ Ethical Scraping

This project follows best practices:

* ⏳ Uses **random delays (0.5–2s)**
* 🤝 Avoids aggressive request patterns
* 📜 Built for **educational purposes**

> Always respect `robots.txt` and website terms.

---

## 🔮 Future Enhancements

* 🚀 Async scraping (aiohttp / concurrency)
* 🔁 Retry & exponential backoff
* 🌍 Proxy / IP rotation
* 📦 Export to JSON / Database
* 🧾 Logging system (production-grade)
* ⚙️ CLI tool support
* ☁️ Deploy as API / microservice

---

## 👨‍💻 Author

**Mohammad Mustak Absar Khan**

🔗 GitHub: [https://github.com/MustakAbsarKhan](https://github.com/MustakAbsarKhan)

---

## ⭐ Support & Contribution

If you found this useful:

⭐ Star the repository
🍴 Fork it
🚀 Build your own version

---