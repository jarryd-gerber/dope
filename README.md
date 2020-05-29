# Dope CLI
A CLI for hand rolling software projects using dank templates.

## How to install:
```
git clone git@github.com:jarryd-gerber/dope
cd dope
docker build . --no-cache
```

## Example usages:

**command:**
```
docker-compose run dope --help
```

**output:**
```
Usage: dope.py [OPTIONS]

  Create the actual structure of the project dirs and files.

  Args:     name: Project name.     template: Template file defined in
  templates directory.

Options:
  --name TEXT      A meaningful name for your project.
  --template TEXT  The structure of your projects files and directories.
  --help           Show this message and exit.
```
**command:**
```
docker-compose run dope --name demo-project --template default
```

**output:**
```
Dope is hand rolling demo-project with the default template...
creating file...Dockefile
creating file...requirements.txt
creating directory...service
demo-project successfully rolled. Your template is dank!
```
