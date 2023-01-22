# Bulletproof Testing in Python
This is a workshop on testing and mocking in Python. 


## Set Up
To do this workshop, you will need to have installed Python, git, pip, and Coverage on your machine.

### Python
To check if you already have Python, run 
```
python --version
```
or
```
python3 --version
```
in the command line.

If you do not have Python on your machine, download it from [the official website](https://python.org/downloads/).

### Git
To check if you already have git, run 
```
git version
```
in the command line.

If you do not have git on your machine, install it following [the official guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).


### Pip
To check if you already have pip, run 
```
pip --version
```
or
```
pip3 --version
```
in the command line.

If you do not have pip on your machine,  install it following [the official guide](https://pip.pypa.io/en/stable/installation/).



### Coverage
To check if you already have Coverage, run 
```
coverage --version 
```
in the command line.

If you do not have Coverage on your machine, install it by entering
```
pip install coverage
```
or
```
pip3 install coverage
```
in the command line.


## Getting Started
First, clone this repo

```
git clone [REPO]
cd [REPO]
```


Try running the application with `python3 main.py Ford`. Does it work?






## Extra

Run tests with `python3 -m unittest tests/*Test.py`


Check test coverage with:

`coverage run main.py Ford`

`coverage report -m`