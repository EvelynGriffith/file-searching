# File Searching

## Evelyn Griffith

## Program Output

### What is the output from running the following commands?

```😃 Searching through the file called input/proactive.txt!

Was the word 'ethical' found in the file input/proactive.txt? Yes
```

- `poetry run search --word ethical --dir input --file file.txt`

```😃 Searching through the file called input/proactive.txt!

Was the word 'conundrum' found in the file input/proactive.txt? No
```

- `poetry run search --word ethical --dir input --file proactive.txt`

## Source Code and Configuration Files

### Describe in detail how your provided source code works

#### A function that confirms that a file containing data is valid

```def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    # return a value to indicate if the file is valid
    # by checking that the is_file() function returns True
    if file is not None:
        if file.is_file():
            return True
        else:
            return False
    # This function should return True when the file is
    # not None and it is also a valid file. Otherwise, this
    # function should return False to indicate it is not value.
```

This code is going to take the Path called file (while using the import called `from pathlib import Path`) and it's essentially going to open the find the file within its directory by using `file` in the if statement. Using the variable file, because it is linked to Pathlib, will allow the file to be found. Then it will say `if the file is not none:` this means, if there is a file there then continue into the if statement. The if statement will then use `is_file()` to determine if the file is in fact there and a file, and if it is a file then the program will return True if it is not a file or the file doesn't exist the program will return False as is stated through the else statement.

#### A function that produces a human readable response for a boolean value

```def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # determine if the boolean value is True or False
    if answer == True:
    # if the input variable answer is True, then return "Yes"
        return "Yes"
    # if the input variable answer is False, then return "No"
    elif answer == False:
        return "No"
```

What this function does is really quite simple. Because we need to use a boolean output in the function called word_search (which is our most important function in terms of actually gathering the information from the file), we need to have a function that will turn that boolean answer, meaning an answer that is true or false, into an answer that will be something that a human can understand. In this case that is "yes" or "no". The way that the function does this is by taking a variable called `answer`, which is defined in the name of the function as a boolean, using conditional logic to say "if the answer does not equal true, meaning that if the word was found in the file, the human_readible_boolean function should return the string "yes", otherwise it should return the string "no".

#### A function that performs a case-sensitive search for a word in a file

```def word_search(text: str, word: str) -> bool:
    """Determine whether or no.. a word is found in the text in case-sensitive fashion."""
    # perform a case-sensitive search for the word in5 the provided text
    # text = file1.read()
    for line in text.split("\n"):
        words = line.split(" ")
        if word in words:
            return True
    return False
```

This function is going to go into a file, as given by the command entered into the program, and it will read the file, split up the lines and determine if the entered word is in the file. The function will then return true if the word is in the file and be passed into the human_readible_boolean function to give us an answer that we will be able to interpret.

### What is the purpose of the `pyproject.toml` file?

The purpose of the pyproject.toml file is to create a virtual environment for the code to live in. It will set the linting tools in order so that they can best be used as well as allowing for the user to have information on the package settings. This file is very useful because it also allows for the dependencies that the file needs to live on through the environment that it creates. However, I think that the most important part of this file is that it allows the dependencies to connect together and work together so that they can be the most productive in the given environment.

### What is the purpose of the `poetry.lock` file?

This file is a lot like the pyproject.toml file because it still involves the dependencies that are used for the created poetry environment. However, this file is different becuase it actually makes it so that your dependencies dont update when working on a project. The way that this was explained to me was that if there is a large company working on a project over an extended period f time, there will be alot of things that will update in the outside world (meaning outside of your environment). Now you need to imagine that everyone working on the file would no longer have the same versions of technology. This would be very bad because now all of a sudden the tech won't do certain things and the project is no longer uniform. This is what the lock file makes sure will never happen. It keeps the project locked in an environment where things that dont need to be changed will not be succeptible to change.

### What are three different ways in which you can run the `search` program?

```poetry run search --word conundrum --dir input --file proactive.txt```
This is one way in which you can run the program. This command operates through the CLI function by accessing the poetry shell and running a program called search. It will then run the program using the attribute called word with the word being "conundrum". That means that the program is going to parse through the file called proactive.txt and try to find the word conundrum. If it can't find the word then it would report that the word is not in the file.

```poetry run search --word ethical --dir input --file proactive.txt```
This is the next way to run the program. This is very similar to the other way of running the program except it changes the attribute so that instead of looking for the word "conundrum" the program will look for the word "ethical".

```poetry run search --word proactive --dir input --file notfound.txt```
This is the final way to run the program which will allow for us to test whether or not an answer will be reported if the file itself doesnt exist.

### What was the greatest challenge that you faced when completing this assignment?

I think my greatest challenge was getting the program to actually decide if the word was in the file. Basically, the problem was that my code was looking at the words correctly, but it wasnt really determining whether or not the word was equal to the thing that the function was trying to find.

### Based on your experiences with this project, what is one way in which you want to improve?

I want to improve my knowledge of commands that I can use in the python language and I also want to be better about figuring out how to code well in labs. Right now I dont think I have a very comprehensive knowledge of what coding commands I can do and I would like to change that.
