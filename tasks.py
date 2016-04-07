from celery import Celery

app = Celery('hello', broker='redis://localhost/0')

@app.task
def hello():
    return 'hello world'

@app.task
def add(x,y):
    return x+y
