"""Find, open, and read file to gather a specific text."""

from pathlib import Path

from rich.console import Console

import typer
# create a Typer object to support the command-line interface
cli = typer.Typer()

def confirms_valid_file(file: Path) -> bool:
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

def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # determine if the boolean value is True or False
    if answer is True:
    # if the input variable answer is True, then return "Yes"
        return "Yes"
    # if the input variable answer is False, then return "No"
    elif answer is False:
        return "No"

def word_search(text: str, word: str) -> bool:
    """Determine whether or no.. a word is found in the text in case-sensitive fashion."""
    # perform a case-sensitive search for the word in5 the provided text
    # text = file1.read()
    for line in text.split("\n"):
        words = line.split(" ")
        if word in words:
            return True
    return False

@cli.command()
def word(
    word: str = typer.Option(None),
    dir: Path = typer.Option(None),
    file: Path = typer.Option(None),
):
    """Process a file by searching for a specified word."""
    # create a console for rich text output
    console = Console()
    # add extra space after the command to run the program
    console.print()
    # create the full name of the file
    # file_fully_qualified = dir / file
    file_fully_qualified = Path(f"{dir}/{file}")
    # consult the expected output on the course web site for a description
    # of what type of output your program needs to produce when running in the terminal window
    # display a message to explain the file that will be input
    # confirm the file is valid and so the program should search through it for the word
    # --> read in the contents of the file
    # --> read in the contents of the file
    confirm_valid_file = confirms_valid_file(file_fully_qualified)
    # --> search for the word in the contents of the file by calling function
    # --> display a message about whether the word was or was not found
    # since the file was not valid and thus you cannot install it display a message
    if confirm_valid_file is True:
        file = open(file_fully_qualified, "r")
        file_string = file.read()
        # print(file_string)
        words = word_search(file_string, word)
        call_function = human_readable_boolean(words)
        console.print()
        console.print(f"😃 Searching through the file called {file_fully_qualified}!")
        console.print()
        console.print(f"Was the word '{word}' found in the file input/proactive.txt? {call_function}")
    else: 
        console.print()
        console.print(f"😃 Searching through the file called {file}!")
        console.print()
        console.print(f"🤷 {file} was not a valid file")
        console.print()

def confirm_valid_file():
    return None