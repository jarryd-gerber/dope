"""A module for the Dope default template."""


from templates import File
from templates import Directory


template = (
    File(name='Dockefile'),
    File(name='requirements', extension='txt'),
    Directory(name='service')
)
