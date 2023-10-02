import typer
from tigr81.commands import scaffold

app = typer.Typer()

app.add_typer(scaffold.app(), name="scaffold")
