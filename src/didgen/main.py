import click

import didgen.__init__ as init
from didgen.generator import generator


@click.group()
def cli():
    """W3C Decentralized Identifier Generator"""
    pass


@cli.command
def version():
    """Print the application version information"""
    click.echo(init.__version__)


@cli.command
def generate():
    """Generate the W3C Decentralized Identifier"""
    generator()


if __name__ == "__main__":
    cli()
