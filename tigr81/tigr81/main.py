import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    FAST API project scaffolder
    """


@app.command()
def create_project_fast_api():
    """
    Scaffold a FAST API project
    """
    typer.echo("Loading portal gun")
