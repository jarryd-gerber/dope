"""The ORIGINAL Dope CLI tool."""


import os
import importlib
import click
from templates import File
from templates import Directory


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
    help='The structure of your projects files and directories.'
)
def roll(name, template):
    """Create the actual structure of the project dirs and files.

    Args:
        name: Project name.
        template: Template file defined in templates directory.
    """
    click.echo(f'Dope is hand rolling {name} with the {template} template...')

    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        project_path = os.path.join(base_path, name)
        template_module = importlib.import_module(f'templates.{template}')

        if not os.path.exists(project_path):
            os.mkdir(project_path)

        for node in template_module.template:
            if isinstance(node, Directory):
                click.echo(f'creating directory...{node.name}')

                dir_path = os.path.join(project_path, node.name)
                os.mkdir(dir_path)
            elif isinstance(node, File):
                click.echo(f'creating file...{node.name}.{node.extension}')

                if node.extension:
                    file_path = os.path.join(project_path, f'{node.name}.{node.extension}')
                else:
                    file_path = os.path.join(project_path, f'{node.name}')

                open(file_path, 'w').close()

        click.echo(f'{name} successfully rolled. Your template is dank!')
    except Exception as exc:
        click.echo('Something went wrong! Your template got stank!')
        raise exc


if __name__ == '__main__':
    roll()