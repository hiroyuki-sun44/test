from flask import Flask

application = Flask(__name__)

def main():
    application.run('127.0.0.1',8000)

if __name__ == '__main__':
    application.run('127.0.0.1',8000,debug=True)
