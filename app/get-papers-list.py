import click
from .pubmed.fetcher import search_pubmed, fetch_paper_details
from typing import Optional

@click.command()
@click.argument("query", type=str)
@click.option("-f", "--file", type=str, help="Output CSV file name.")
@click.option("--max-results", type=int, default=10, help="Number of results to fetch (default: 10).")
def main(query: str, file: Optional[str], max_results: int):
    try:
        pubmed_ids = search_pubmed(query, max_results)
        if not pubmed_ids:
            click.echo("No results found.")
            return


        results = [fetch_paper_details(pubmed_id) for pubmed_id in pubmed_ids]
        results = [r for r in results if r]  # Remove None values

        if not results:
            click.echo("No relevant papers found with non-academic affiliations.")
            return
        print(results)

    except requests.RequestException as e:
        click.echo(f"Error fetching data from PubMed: {e}", err=True)

if __name__ == "__main__":
    main()
