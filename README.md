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
git clone https://github.com/beedel/bulletproof-testing.git
cd bulletproof-testing
```

Try running the application by entering `python3 main.py Ford` in the command line. Does it work?
You should see 
```angular2html
Ford Fiesta
Ford Mustang
Ford Focus
```
printed on the command line.

## Get to Know the Code
Have a look at the `src` directory. You will see three files - `CarApiClient.py`, `CarRepository.py`, and `CarResolver.py`.
All of the files have a comment explaining their purpose. Try to understand what their code does to ensure you can write test cases for it.

Can you think of any happy/failure test cases for these files? What are the possible flows of the application? Do any of the classes ever throw an exception?

If you want to, you can also have a look at the `main.py` file. It sets up the database and runs the application.

## Running the Tests
Run a test with `python3 -m unittest tests/<Filename>.py`

When you are done writing all of the tests, you can run all of them with `python3 -m unittest tests/*Test.py`.

## Get to Testing
Let's write some tests for this application.


### CarApiClientTest.py
Start with the `CarApiClientTest.py` file in the `tests/` folder. The comment above the class name includes guidance on what is already there and what is missing. Can you finish writing the test code for this class?

### CarResolverTest.py
Now look at the `CarResolverTest.py` file in the `tests/` folder. The comment above the class name includes guidance on what is already there and what is missing. Can you finish writing the test code for this class?

### Whoops!
You wrote all these test cases and thought you had it all. Think again!

In the `CarResolverTest.py` file you mocked out the database. This is good, because it makes your tests faster and ensures that you can control the values it returns.

But what if somebody changed the code for `CarRepository.py` and broke it?

Imagine an intern comes in, sees the line 
```
cursor.execute("SELECT * FROM cars WHERE brand=?", (manufacturer,))
```
and decides to follow proper naming conventions and change `brand` to `manufacturer`. After all, consistency is key!

Try changing it and running the application again. Does it break?

Now run the `CarResolverTest.py` file. All good?

We need to fix this. 

### CarResolverSmokeTest.py
Look at the `CarResolverSmokeTest.py` file in the `tests/` folder. The comment above the class name includes guidance on what is already there and what is missing. Can you finish writing the test code for this class?


## Extra

Check test coverage with:

`coverage run main.py Ford`

`coverage report -m`