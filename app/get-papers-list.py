import click
from typing import Optional

@click.command()
@click.argument("query", type=str)
@click.option("-f", "--file", type=str, help="Output CSV file name.")
@click.option("--max-results", type=int, default=10, help="Number of results to fetch (default: 10).")
def main(query: str, file: Optional[str], max_results: int):
    print(query)

if __name__ == "__main__":
    main()
