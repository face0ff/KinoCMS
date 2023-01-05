from waitress import serve

from KinoCMS.wsgi import application

if __name__ == '__main__':
    serve(application, port='8000', threads=50)