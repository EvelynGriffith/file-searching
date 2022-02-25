"""Find, open, and read file to gather a specific text."""

from pathlib import Path
from pickletools import string1

from rich.console import Console

import typer
# create a Typer object to support the command-line interface
cli = typer.Typer()

def confirm_valid_file(file: Path) -> bool:
    """Confirm that the provided file is a valid path."""
    # determine if the file is not None and if it is a file
    path_to_file = 'input/proactive.txt'
    path = Path(path_to_file)
    path.is_file()
    # return a value to indicate if the file is valid
    # by checking that the is_file() function returns True
    if file is not None:
        if file.is_file():
            return True
    # This function should return True when the file is
    # not None and it is also a valid file. Otherwise, this
    # function should return False to indicate it is not value.
    return False


def human_readable_boolean(answer: bool) -> str:
    """Produce a human-readable Yes or No for a boolean value of True or False."""
    # determine if the boolean value is True or False
    if answer is True:
    # if the input variable answer is True, then return "Yes"
        return "Yes"
    # if the input variable answer is False, then return "No"
    else:
        return "no"

def word_search(text: str, word: str) -> bool:
    """Determine whether or no.. a word is found in the text in case-sensitive fashion."""
    # perform a case-sensitive search for the word in the provided text

    # text = file1.read()
    if word in text:
        return True
    else:
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
    file_fully_qualified = dir / file
    # consult the expected output on the course web site for a description
    # of what type of output your program needs to produce when running in the terminal window
    # display a message to explain the file that will be input
    # confirm the file is valid and so the program should search through it for the word
    # --> read in the contents of the file
    # --> read in the contents of the file
    confirmed_file = confirm_valid_file(file)
    # --> search for the word in the contents of the file by calling function
    file_string = open(file_fully_qualified, "r")
    # file_string = file_fully_qualified.read()
    words = word_search(file_string, word)
    call_function = human_readable_boolean(words)
    # --> display a message about whether the word was or was not found
    # since the file was not valid and thus you cannot install it display a message
    console.print()
    console.print(f"😃 Searching through the file called {file_string}!")
    console.print()
    console.print(f"Was the word '{word}' found in the file input/proactive.txt? {call_function}")
    console.print()
    console.print(f"😃 Searching through the file called input/notfound.txt!")
    console.print()
    console.print(f"🤷 input/notfound.txt was not a valid file")
    console.print()
