import typer
from tigr81.commands.scaffold import scaffold
from tigr81.commands.monorepo import monorepo

app = typer.Typer()


app.command()(scaffold.scaffold)
app.add_typer(monorepo.app, name="monorepo")
