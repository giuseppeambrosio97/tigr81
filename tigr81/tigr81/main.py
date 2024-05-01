import typer
from tigr81.commands.scaffold import scaffold
from tigr81.commands.monorepo import monorepo
from tigr81 import PYPY_URL, REPO_LOCATION, __version__ 

app = typer.Typer()

    
@app.command()
def version():
    """Check out version information"""
    typer.echo(f"v{__version__}")
    typer.echo("\nCheck out for new versions:")
    typer.echo(f"- {PYPY_URL}")
    typer.echo(f"- {REPO_LOCATION}")
    

app.command()(scaffold.scaffold)
app.add_typer(monorepo.app, name="monorepo")
