"""A module for the Dope template components."""


class Directory:
    """An object describing a system directory."""
    def __init__(self, name, subdirs=None, root=None):
        """Instantiate a Directory object.

        Args:
            name: Name of the directory.
            subdirs: A list of sub directories.
            root: The parent directory of self.
        """
        self.name = name
        self.subdirs = subdirs
        self.root = root


class File:
    """An object describing a system file."""
    def __init__(self, name, extension=None, contents=None, root=None):
        """Instantiate a File object.

        Args:
            name: Name of the file.
            extension: The file type extension eg. txt.
            contents: The contents of the file.
            root: The parent directory of self.
        """
        self.name = name
        self.extension = extension
        self.contents = contents
        self.root = root
