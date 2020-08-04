# -*- coding: UTF-8 -*-
import math
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    print("Getting ready to start in 9")
    print("Getting ready to start in 8")
    print("Getting ready to start in 7")
    print("Getting ready to start in 6")
    print("Getting ready to start in 5")
    print("Getting ready to start in 4")
    print("Getting ready to start in 3")
    print("Getting ready to start in 2")
    print("Getting ready to start in 1")
    print("Let's go!")

    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"] ** 2 + triangle["height"] ** 2
    print("area = " + str((triangle["base"] * triangle["height"]) / 2))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5 ** 2 + 6 ** 2
    print(another_hyp)

    yet_another_hyp = 40 ** 2 + 30 ** 2
    print(yet_another_hyp)


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    for i in range(start, stop - 1, -1):
        countdown_msg = message + " " + str(i)
        print(countdown_msg)
    print(completion_message)
    


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """ Calculate hypotenuse of triangle """
    hypotenuse = math.sqrt(base ** 2 + height ** 2)
    return hypotenuse


def calculate_area(base, height):
    """ Calculate area of triangle """
    area = (base * height) / 2
    return area
    


def calculate_perimeter(base, height):
    """ Calculate perimeter of triangle """
    hypotenuse = calculate_hypotenuse(base, height)
    perimeter = base + height + hypotenuse
    return perimeter


def calculate_aspect(base, height):
    """ Calculate aspect of triangle """
    if height > base:
        return "tall"
    elif height < base:
        return "wide"
    else:
        return "equal"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    )

    facts = pattern.format(**facts_dictionary)
    if facts_dictionary["aspect"] == "tall":
        return facts + tall.format(**facts_dictionary)
    elif facts_dictionary["aspect"] == "wide":
        return facts + wide.format(**facts_dictionary)
    else:
        return facts + equal.format(**facts_dictionary)


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    dictionary_of_triange_facts = get_triangle_facts(base, height, units="mm")
    diagram = tell_me_about_this_right_triangle(dictionary_of_triange_facts)
    if return_diagram and return_dictionary:
        return {"diagram": diagram, "dictionary": dictionary_of_triange_facts}
    elif return_diagram:
        return diagram
    elif return_dictionary:
        return dictionary_of_triange_facts
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    import requests

    lengths = [up for up in range(3, 21, 2)] + [down for down in range(20, 3, -2)]
    return list_of_words_with_lengths(lengths)

def get_a_word_of_length_n(length):
    import requests

    baseURL = (
        "https://api.wordnik.com/v4/words.json/randomWords?"
        "api_key=a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5"
        "&minLength={length}"
        "&maxLength={length}"
        "&limit=1".format(length=length)
    )

    r = requests.get(baseURL)
    try:
        length = int(length)
    except ValueError:
        return None

    if 3 <= length <= 20: 
        if r.status_code is 200:
            message = r.json()[0]["word"]
            return message
     

def list_of_words_with_lengths(list_of_lengths):
    import requests
    pyramid_list = []
    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength={length}"
    for i in range(0, len(list_of_lengths)):
        length = list_of_lengths[i]
        r = requests.get(url.format(length=length))
        pyramid_list.append(r.text)
    return pyramid_list 


if __name__ == "__main__":
    do_bunch_of_bad_things()
    wordy_pyramid("a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
