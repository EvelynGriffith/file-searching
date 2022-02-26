# File Searching

## Evelyn Griffith

## Program Output

### What is the output from running the following commands?

TODO: Use a fenced code block to provide the output for this command.

- `poetry run search --word ethical --dir input --file file.txt`

TODO: Use a fenced code block to provide the output for this command.

- `poetry run search --word ethical --dir input --file proactive.txt`

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### A function that confirms that a file containing data is valid

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

#### A function that produces a human readable response for a boolean value

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

#### A function that performs a case-sensitive search for a word in a file

TODO: Use a fenced code block to provide the requested source code
TODO: Write at least one paragraph to explain the request source code

### What is the purpose of the `pyproject.toml` file?

The purpose of the pyproject.toml file is to create a virtual environment for the code to live in. It will set the linting tools in order so that they can best be used as well as allowing for the user to have information on the package settings. This file is very useful because it also allows for the dependencies that the file needs to live on through the environment that it creates. However, I think that the most important part of this file is that it allows the dependencies to connect together and work together so that they can be the most productive in the given environment.

### What is the purpose of the `poetry.lock` file?

This file is a lot like the pyproject.toml file because it still involves the dependencies that are used for the created poetry environment. However, this file is different becuase it actually makes it so that your dependencies dont update when working on a project. The way that this was explained to me was that if there is a large company working on a project over an extended period f time, there will be alot of things that will update in the outside world (meaning outside of your environment). Now you need to imagine that everyone working on the file would no longer have the same versions of technology. This would be very bad because now all of a sudden the tech won't do certain things and the project is no longer uniform. This is what the lock file makes sure will never happen. It keeps the project locked in an environment where things that dont need to be changed will not be succeptible to change.

### What are three different ways in which you can run the `search` program?

```poetry run search --word conundrum --dir input --file proactive.txt```
This is one way in which you can run the program. This command operates through the CLI function by accessing the poetry shell and running a program called search. It will then run the program using the attribute called word with the word being "conundrum". That means that the program is going to parse through the file called proactive.txt and try to find the word conundrum. If it can't find the word then it would report that the word is not in the file.

```poetry run search --word ethical --dir input --file proactive.txt ```
This is the next way to run the program. This is very similar to the other way of running the program except it changes the attribute so that instead of looking for the word "conundrum" the program will look for the word "ethical".

TODO: Describe the third way for running the program, giving a command and a paragraph

- TODO: provide a command

### What was the greatest challenge that you faced when completing this assignment?

I think my greatest challenge was getting the program to actually decide if the word was in the file. Basically, the problem was that my code was looking at the words correctly, but it wasnt really determining whether or not the word was equal to the thing that the function was trying to find.

### Based on your experiences with this project, what is one way in which you want to improve?

TODO: Provide a one-paragraph response that answers this question in your own words.
