"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think it will create a list with some random words
some_words = [
    "what",
    "does",
    "this",
    "line",
    "do",
    "?",
]  # it created a list with the words 'what' 'does' ' this' 'line' 'do' and '?'

# I think it will iterate over the elements in the list printing each one out one by one
for word in some_words:  # it printed out each individual elment from the list
    print(word)

# I think it will do the same as the function above
for x in some_words:  # it printed out each individual element again
    print(x)

# I think it will print the whole list at once
print(some_words)  # it printed out the list on one line

# I think it will compare whether the length of the list is bigger than 3 and if true will return a string saying it contains more than 3 words
if (
    len(some_words) > 3
):  # checked whether the length of the list is greater than 3 and printed the phrase "some_words contains more than 3 words"
    print("some_words contains more than 3 words")

# platform.uname() acesses the underlying platforms data such as hardware, os and interpreter version
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


# runs the function usefulFunction
usefulFunction()
