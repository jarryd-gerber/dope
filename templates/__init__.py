"""A module for the Dope template components."""


class Directory:
    """An object describing a system directory."""
    def __init__(self, name, children=None, root=None):
        """Instantiate a Directory object.

        Args:
            name: Name of the directory.
            children: A list of File or Directory objects.
            root: The parent directory of self.
        """
        self.name = name
        self.children = children
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
