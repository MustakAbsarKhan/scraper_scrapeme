---

# 🛒 Scrapeme Web Scraper

### ⚡ Production-Ready Python Scraper (Sync + Async) with Pagination, Concurrency & Data Export

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python">
  <img src="https://img.shields.io/badge/Requests-Sync%20HTTP-green">
  <img src="https://img.shields.io/badge/Aiohttp-Async%20HTTP-blueviolet">
  <img src="https://img.shields.io/badge/BeautifulSoup-Parsing-orange">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-purple">
  <img src="https://img.shields.io/badge/Status-Production--Ready-success">
</p>

---

## 🚀 Overview

A **robust, scalable web scraping project** built with Python that extracts product data from a real-world eCommerce demo site.

This repository demonstrates **two approaches**:

* 🧵 **Synchronous Scraping (requests)** — simple, readable, beginner-friendly
* ⚡ **Asynchronous Scraping (aiohttp + asyncio)** — fast, concurrent, production-grade <br>

✔ Handles **pagination automatically** <br>
✔ Extracts **complete product metadata** <br>
✔ Implements **polite scraping practices** <br>
✔ Exports clean data into **CSV format** <br>

---

## 🎯 Features

✨ What makes this project stand out:

### Core Features

* 🔄 **Automatic Pagination Detection**
* 🌐 **Session-Based Requests**
* 🧠 **Fault-Tolerant Data Extraction**
* 📦 **Structured Data Storage**
* 📊 **CSV Export via pandas**

### Advanced Features

* ⚡ **Async Scraping (Concurrency with asyncio)**
* 🚀 **Parallel Page Fetching (Massive Speed Boost)**
* ⏱️ **Polite Scraping (Delays & Headers)**
* 🔗 Extracts:

  * Product Title
  * Price
  * Image URL
  * Product URL

---

## 🧠 Architecture Overview

### 🧵 Synchronous Flow

```text
Initialize Session → Fetch Page → Parse → Repeat → Save CSV
```

### ⚡ Asynchronous Flow

```text
Fetch First Page → Detect Total Pages
        ↓
Create Async Tasks (All Pages)
        ↓
Execute Concurrent Requests (asyncio.gather)
        ↓
Parse HTML → Store Data → Export CSV
```

---

## ⚡ Sync vs Async Comparison

| Feature     | Sync (requests) 🧵 | Async (aiohttp) ⚡    |
| ----------- | ------------------ | -------------------- |
| Execution   | Sequential         | Concurrent           |
| Speed       | Slower             | Much Faster 🚀       |
| Complexity  | Easy               | Intermediate         |
| Scalability | Limited            | High                 |
| Use Case    | Small projects     | Large-scale scraping |

---

## 🛠️ Tech Stack

| Category      | Tools Used          |
| ------------- | ------------------- |
| Language      | Python 🐍           |
| Sync HTTP     | requests            |
| Async HTTP    | aiohttp + asyncio   |
| Parsing       | BeautifulSoup (bs4) |
| Parser Engine | lxml                |
| Data Handling | pandas              |

---

## 📂 Project Structure

```
scrapeme-scraper/
│
├── scraper.py              # Sync version (requests)
├── scraper_async.py        # Async version (aiohttp)
├── products_info.csv       # Output (sync)
├── products_info_async.csv # Output (async)
└── README.md               # Documentation
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
pip install requests aiohttp beautifulsoup4 lxml pandas
```

---

## ▶️ Usage

### 🧵 Run Sync Version

```bash
python scraper.py
```

---

### ⚡ Run Async Version

```bash
python scraper_async.py
```

---

## 📊 Sample Output

### 🖥️ Console (Async Example)

```
Fetched: page 1
Fetched: page 2
Fetched: page 3
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
* ✔ Uses safe parsing patterns
* ✔ Async version handles **partial failures gracefully**

---

## ⚠️ Ethical Scraping

This project follows best practices:

* ⏳ Uses **delays / controlled concurrency**
* 🤝 Avoids aggressive request patterns
* 📜 Built for **educational purposes**

> Always respect `robots.txt` and website terms.

---

## 🔮 Future Enhancements

* 🔁 Retry logic + exponential backoff
* 🌍 Proxy / IP rotation
* 📦 Export to JSON / Database
* 🧾 Logging system (production-grade)
* ⚙️ CLI tool support
* ☁️ Deploy as API / microservice

---

## 👨‍💻 Author

**Mohammad Mustak Absar Khan**

🔗 GitHub:
[https://github.com/MustakAbsarKhan](https://github.com/MustakAbsarKhan)

---

## ⭐ Support & Contribution

If you found this useful:

⭐ Star the repository
🍴 Fork it
🚀 Build your own version

---
