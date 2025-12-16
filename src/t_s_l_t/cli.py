"""Console script for t_s_l_t."""

import typer
from rich.console import Console

from t_s_l_t import utils

app = typer.Typer()
console = Console()


@app.command()
def main():
    """Console script for t_s_l_t."""
    console.print("Replace this message by putting your code into "
               "t_s_l_t.cli.main")
    console.print("See Typer documentation at https://typer.tiangolo.com/")
    utils.do_something_useful()


if __name__ == "__main__":
    app()
