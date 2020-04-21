# Author: Rahian Islam
from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def index():
    return ('Welcome to the Fibonacci Library')


@app.route('/fibonacci')
def fib():
    return ('Please enter the number of elements you want to see')


@app.route('/fibonacci/<num>')
def fibonacci(num): 
    num = int(num)
    if num<0: 
        print("Incorrect input") 
  
    else:
        a = 0
        b = 1
        c = 1
        fibo=[b]
        while b < 70 and c<num:
            a, b = b, a+b
            fibo.append(b)
            c += 1 
        
        return render_template('fibonacci.html', num_elements = num, fib_num = fibo) 

if __name__ == '__main__':
    app.debug = True
    app.run()