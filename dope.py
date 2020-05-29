"""The ORIGINAL Dope CLI tool."""


import os
import importlib
import click
from templates import File
from templates import Directory
from exceptions import DopeProjectExists


@click.command()
@click.option(
    '--name',
    prompt='Project name',
    default='hello-world',
    help='A meaningful name for your project.'
)
@click.option(
    '--template',
    prompt='Poject definition template',
    default='default',
    help='The template defining your projects files and directories.'
)
def roll(name, template):
    """Dope - A CLI for hand rolling software projects.

    Args:
        name: Project name.
        template: Template file defined in templates directory.
    """
    click.echo(f'Dope is hand rolling {name} with the {template} template...')

    base_path = os.path.dirname(os.path.abspath(__file__))
    project_path = os.path.join(base_path, name)
    template_module = importlib.import_module(f'templates.{template}')

    if os.path.exists(project_path):
        raise DopeProjectExists(f'{name} already rolled!')

    os.mkdir(project_path)

    for node in template_module.template:
        if isinstance(node, Directory):
            click.echo(f'creating directory...{node.name}')
            dir_path = os.path.join(project_path, node.name)
            os.mkdir(dir_path)

        elif isinstance(node, File):
            if node.extension:
                click.echo(f'creating file...{node.name}.{node.extension}')
                file_path = os.path.join(project_path, f'{node.name}.{node.extension}')
            else:
                click.echo(f'creating file...{node.name}')
                file_path = os.path.join(project_path, f'{node.name}')

            open(file_path, 'w').close()

    click.echo(f'{name} successfully rolled. Your template is dank!')


if __name__ == '__main__':
    roll()
