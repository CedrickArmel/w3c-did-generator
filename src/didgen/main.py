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
@click.option(
    "-n",
    "--number",
    "number",
    type=int,
    required=False,
    default=1,
    help="Number of key to generate. Defaults to 1",
)
def generate(number):
    """Generate the W3C Decentralized Identifier"""
    generator(number)


if __name__ == "__main__":
    cli()
