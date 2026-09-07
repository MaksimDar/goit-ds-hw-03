# GoIT DS HW-03: MongoDB CRUD & Web Scraping

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?logo=mongodb&logoColor=white)
![PyMongo](https://img.shields.io/badge/PyMongo-database%20driver-013220)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-web%20scraping-yellowgreen)
![Poetry](https://img.shields.io/badge/Poetry-dependency%20management-60A5FA?logo=poetry&logoColor=white)

## Description

A two-part homework project covering NoSQL database operations and web scraping. The first task implements full CRUD functionality for a MongoDB collection using PyMongo. The second task scrapes quotes and author biographies from a public site, exports the results to JSON, and imports them into MongoDB Atlas.

## Tech Stack

- **Python 3.10**
- **PyMongo** — MongoDB driver and CRUD operations
- **MongoDB Atlas** — cloud NoSQL database
- **Requests** & **BeautifulSoup4** (with the `lxml` parser) — web scraping
- **JSON** — intermediate data storage
- **Poetry** — dependency and environment management

## Functionality

**Task 1 — MongoDB CRUD (`main.py`)**
- `create_one_cat()` / `create_many_cats()` — insert one or several documents into the `cats` collection, with input type validation.
- `show_all_cats()` / `show_cat_info(name)` — read all records, or look up a single cat by name.
- `update_cat_age(name, age)` / `add_feature(name, feature)` — update an existing document's age or append a new characteristic.
- `delete_cat(name)` / `delete_all_cats()` — remove a single record or clear the collection.

**Task 2 — Web Scraping & Import (`task_2.py`)**
- Scrapes all quotes, tags, and authors from [quotes.toscrape.com](http://quotes.toscrape.com), including each author's biography page.
- Saves the results as `qoutes.json` and `authors.json`.
- Imports both JSON files into separate MongoDB collections (`quotes`, `authors`).

## Installation & Usage

```bash
git clone https://github.com/MaksimDar/goit-ds-hw-03.git
cd goit-ds-hw-03

poetry install
poetry run python3 main.py       # Task 1: MongoDB CRUD
poetry run python3 task_2.py     # Task 2: scraping + MongoDB import
```

> **Note:** database connection strings should be supplied via environment variables (e.g. a local `.env` file excluded from version control) rather than hardcoded in source files, in line with standard security practice for credential management.

## Links

- Repository: [github.com/MaksimDar/goit-ds-hw-03](https://github.com/MaksimDar/goit-ds-hw-03)
- Data source: [quotes.toscrape.com](http://quotes.toscrape.com)

## Author

**Maksym Dovhusha**
