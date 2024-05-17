from flask import Flask, render_template
from json import load
from random import choice

app = Flask(__name__)
app.debug = True

@app.route('/')
def main():
    q = 'what is 2+2'
    a = 0
    s = 'placeholder source'
    
    with open('questions.json') as f:
        d = choice(load(f))
        q = d['question'].strip()
        a = str(d['answer'])
        s = d['source'].strip()
    
    return render_template("main.html", q=q, a=a, s=s)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)