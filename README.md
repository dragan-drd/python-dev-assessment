# Python Developer Assessment

## Overview
Assessment of basic programming skills using the python language
Covering:
    - Data structures and algorithms
    - Object oriented programming
    - Debugging
    - Error handling
    - API requests
    - Code style and formatting


## Task list

### 1. Setup & Foundational Review

#### 1.1 Environment Setup
- Setting up the coding environment, such as installing the python interpreter, VS Code, git
- Creating a [hello.py](hello.py) test file to verify if everything is set up correctly

#### 1.2 Version Control Basics
- Basic command and navigation using git, such as branching, committing changes and pushing to a remote repository

#### 1.3 Code Style & Linting
- Installing `black` and `flak8` and running the scripts on [bad_style.py](bad_style.py) example

### 2. Core Programming Concepts & Problem Solving

#### 2.1 Basic Data Structures & algorithms
- Solving various challenges in the [dsa_challenges.py](dsa_challenges.py) file

#### 2.2 Object-Oriented Programming (OOP) Fundamentals
- Practicing OOP fundamentals and concepts in the [book_store.py](book_store.py) file

#### 2.3 Error Handling & Debugging
- Debugging intentionaly faulty code in [debug_errors.py](debug_errors.py) , practicing using the IDE debugger and fixing the code so it can handle errors and fail gracefully

### 3 Integration

#### 3.1 Basic API Interaction
- Practicing sending requests to an external API using the `requests` library, parsing the JSON response into a more usefull data type and handling any network errors and missing data 
- Code can be found in [api_client.py](api_client.py)

#### 3.2 Submission
- Merging all the branches back into main
- Handling any merge conflincts
- Writing this README

***

### Prerequisites
- python interpreter 3.11 or greater
- IDE or code editor of your choice
- git
- `black` - `pip install black`
- `flake8` - `pip install flake8`
- `requests` library - `pip install requests`

#### Running the code
- Simply run the python interpreter from a terminal on any of the files
```
python <example.py>
```

***

### Reflections

Even though python was the first programming language i learned, i havent used it in many years, it was challenging remembering all of the syntax and the built in functionallity of the language, as i am more used to lower level languages like C.
Because of that my code may take on a more manual and explicit approach rather than using functionality built into the language (i have to say it can be a lot more convenient).

This challenge was a nice refresher on OOP and data structures, and i learned quite a lot about using git in the command line (i used the Github Desktop GUI previously) and about code styling and linting which i must admit is probably the area i have to improve on the most.