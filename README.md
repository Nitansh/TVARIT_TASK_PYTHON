STEPS to run code on local
==========================
1. install git ( https://git-scm.com/book/en/v2/Getting-Started-Installing-Git )
2. git clone https://github.com/Nitansh/TVARIT_TASK_PYTHON.git
3. install python ( https://docs.python.org/3/using/windows.html )
4. install pip ( https://pip.pypa.io/en/stable/installation/ )
5. install virtualenv ( https://docs.python.org/3/library/venv.html )
6. Create a virtual environment
`python3 -m venv env`
7. Activate virtual environment
`source env/bin/activate`
8. install dependencies
`pip install -r requirements.txt`

Happy coding !!!


RUNNING CODE
=============
    >>> python app.py 1 2 3
    6

    >>> python app.py 1 13 2
    3

    >>> python app.py 2 1 14
    3

    >>> python app.py 1 2
    Exactly 3 numbers are required

    >>> python app.py 1 2 a
    All inputs must be numeric

RUN UNIT TEST
=============
    >>> python -m unittest