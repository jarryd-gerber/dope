import requests


class CodeshipService:
    """."""

    def __init__(self):
        """."""
        self.http = requests
        self.url = 'https://api.codeship.com/v2'
        self.headers = {'Content-Type': 'application/json'}

    def authenticate(self):
        """Authenticate with CodeShip API."""
        response = requests.post(
            url=f'{self.url}/auth',
            headers=self.headers,
            auth=('user', 'pass'),
        )
        import pdb; pdb.set_trace()

    def create_project(self):
        """."""
        pass


if __name__ == '__main__':
    service = CodeshipService()
    service.authenticate()

