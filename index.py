from src.app import serve
from src.app import app  # this line enables the serverless functions discover the Flask App.

if __name__ == '__main__':
    serve()