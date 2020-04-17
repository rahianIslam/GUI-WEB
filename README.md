# ENGG 519.07 Digital Engineering II: FINAL EXAM
## Question 1: Command Line Interface
The goal is to implement a Python program that allows converting Covid-19 statistics downloaded in CSV format from https://covid19stats.alberta.ca/ to a custom SQLite database as used in Assignemt 6.

Create a Python program that:
1. Provides a command line interface using `argparse` with:
   - Two mandatory arguments: csv_filename, sqlite_filename.
   - An optional argument `-d`, `--drop` to specify how many rows to drop, starting from most recent (date).
2. Loads data from the csv file with filename provided. CSV format is according to covid19stats.alberta.ca containing every case and corresponding date. An example is available `q1-cli/covid19dataexport.csv`. Use this file for your tests.
3. Converts information to have the number of cases per date.
4. Saves the converted information to an SQLite database containing one table `alberta` with two columns: `date`, and `daily_cases`. The expected output is available `q1-cli/measurements.db`. Your output should match this database.
5. Notifies the user in case there was an error, e.g. csv file not found. You may assume that the csv format is always correct.

Hint: Once values are in a Pandas DataFrame `df`, these can be saved to a table in an sqlite database using:
```python
from sqlalchemy import create_engine
db_uri = 'sqlite:///measurements.db'
engine = create_engine(db_uri, echo=False)
df.to_sql(name='alberta', con=engine, if_exists='replace') 
engine.dispose()
```
   
Your code is to be added to `q1-cli/convert_covid_csv2sqlite.py`. Steps 2. - 5. are to be implemented in the function `convert_csv2sqlite`. Make sure you include your name on the first line. This file contains skeleton code to get you started (see `#TODO:`).

Test your file by running `python convert_covid_csv2sqlite.py -d 1 covid19dataexport.csv measurements2.db`. The output should match `q1-cli/measurements.db`.

## Question 2: Graphical User Interface
The goal is to implement a Python program with a graphical user interface that allows measuring the number of words and sentences in a text. You have already implemented the relevant functions in assignment1 text-statistics. This code can be re-used.

Create a Python program that:
1. Provides a graphical user interface using `tkinter` with:
   - Two tk.Text fields, one for pasting text to be analyzed, the other to display the results.
   - One ttk.Button to start the analysis.
   - Uses the grid geometry manager to place widgets.
2. Uses two functions to calculate (1) number of words and (2) number of sentences. A sentence is terminated by a period, question, or exclamation mark.

Your code is to be added to `q2-gui/tkinter_word_count.py`. Make sure you include your name on the first line. You are free to choose implementation details and layout. Please consider that pasted text in general contains multipe paragraphs (lines). The input tk.Text widget should allow review of pasted text and its size should be adequate for this task.

Test your program by pasting text from `q2-gui/feynman.txt`. There are 1071 words and 53 sentences.

## Question 3: Web progamming
The goal is to implement a Python web server application returning a desired number of elements of the Fibonacci sequence. 

Create a Python program that:
1. Uses Flask and Jinja2 templates:
    - To provide a dynamic route on localhost port 5000.
    - To pass the desired number of elements of the Fibonacci sequence to display.
    - To create dynamic HTML containing the number of elements, as well as a list of these Fibonacci elements.
2. When visiting http://localhost:5000/fibonacci/5 the rendered HTML page would state that 5 Fibonacci elements were requested and include the first 5 Fibonacci numbers 1, 1, 2, 3, 5 either in a HTML list or table.
3. The Python code includes all imports and code to start the server in a single file.
4. The view function calls another function to generate the list of Fibonacci numbers.
5. The dynamic HTML is generated using Jinja2 templates.
6. There is no need to style this website, no CSS needed.

Add your Python code to `q3-web/flask_fibonacci.py` and the HTML template to `q3-web/templates/fibonacci.html`. Make sure you include your name on the first line.
