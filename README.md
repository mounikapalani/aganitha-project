# **PubMed Paper Fetcher**
A **command-line tool** to fetch research papers from **PubMed** and filter those affiliated with **pharmaceutical or biotech companies**. Results can be **saved as a CSV file** or displayed in the console.

---

## **🚀 Features**
✅ Fetches research papers from **PubMed API**.  
✅ Filters **non-academic authors** (biotech/pharma companies).  
✅ Outputs results in **CSV format** or **console**.  
✅ Supports **complex PubMed search queries**.  
✅ Provides **debugging mode** for troubleshooting.

---

## **📦 Installation**
### **1️⃣ Install Poetry (Dependency Manager)**
Before running the project, **install Poetry** if you haven't already:

```sh
curl -sSL https://install.python-poetry.org | python3 -
```
Then
```
git clone https://github.com/mounikapalani/aganitha-project.git
cd aganitha-project
poetry install
```
Fetch Research Papers 
```
poetry run get-papers-list "cancer treatment"
```
For Custome file name
```
poetry run get-papers-list "genomics" -f results.csv
```
By default this application fetch 10 count, For get more Papers
```
poetry run get-papers-list "genomics" -f results.csv --max-results 20
```