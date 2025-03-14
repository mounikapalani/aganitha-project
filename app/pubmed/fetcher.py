import requests
import xml.etree.ElementTree as ET
from typing import List, Dict, Optional

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

COMPANY_KEYWORDS = ["pharma", "biotech", "therapeutics", "biosciences", "genomics"]

def search_pubmed(query: str, max_results: int = 10) -> List[str]:
    params = {"db": "pubmed", "term": query, "retmax": max_results, "retmode": "xml"}
    response = requests.get(PUBMED_SEARCH_URL, params=params)
    response.raise_for_status()
    
    root = ET.fromstring(response.text)
    return [id_elem.text for id_elem in root.findall(".//Id")]

def fetch_paper_details(pubmed_id: str) -> Optional[Dict[str, str]]:
    params = {"db": "pubmed", "id": pubmed_id, "retmode": "xml"}
    response = requests.get(PUBMED_FETCH_URL, params=params)
    response.raise_for_status()

    root = ET.fromstring(response.text)
    article = root.find(".//PubmedArticle")
    if not article:
        return None

    title = article.findtext(".//ArticleTitle", "N/A")
    pub_date = article.findtext(".//PubDate/Year", "N/A")
    corresponding_author = "N/A"
    non_academic_authors, company_affiliations = [], []

    for author in article.findall(".//Author"):
        affiliation = author.findtext(".//Affiliation", "").lower()

        if any(keyword in affiliation for keyword in COMPANY_KEYWORDS):
            author_name = author.findtext(".//LastName", "Unknown") + " " + author.findtext(".//ForeName", "")
            non_academic_authors.append(author_name)
            company_affiliations.append(affiliation)

        if "@" in affiliation:
            corresponding_author = affiliation

    return {
        "PubmedID": pubmed_id,
        "Title": title,
        "Publication Date": pub_date,
        "Non-academic Author(s)": "; ".join(non_academic_authors) or "N/A",
        "Company Affiliation(s)": "; ".join(company_affiliations) or "N/A",
        "Corresponding Author Email": corresponding_author
    }
