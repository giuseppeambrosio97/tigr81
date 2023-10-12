import typer
from tigr81.commands.scaffold import scaffold

app = typer.Typer()

app.add_typer(scaffold.app(), name="scaffold")
