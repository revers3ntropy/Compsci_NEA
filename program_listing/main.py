"""
                                         Joseph Coppin
                                  Computer Science GSCE Coursework

This file gets run to run the program. it first checks if you want to run the program normally
or text-based, and hen runs it dependant on the answer.
This file gets run to run the program. I have decided that I will try to separate any
functions larger than 15 lines or 5 if statements as a general rule, and that this file will
contain as little as possible as it cannot be moved into the program listing.

I have decided that I will try to separately any functions larger than 15 lines or 5 if
statements as a general rule, and that this file will contain as little as possible as it
cannot be moved into the program listing.

I will be using a file to store global data in each program. I found that it is the best way to
give access to the current entered details to all menu options, and also allow data such as
airplane information to be stored easily. I will be referring to the global data file as 'g'
in most files.

Global Functions:
    main
    get_program_type

Imports:                                                                                         """
import pygame as py

import program_listing.text.global_data as text_g
import program_listing.text.init as text_init
import program_listing.text.tick as text_tick

import program_listing.full.global_data as full_g
import program_listing.full.init as full_init
import program_listing.full.tick as full_tick


def main(program_type: str):
    """
    initialises and then runs the main loop for the selected program

    args:
        program_type - which program is to be run, text-based or the full
    """
    py.display.set_caption("Joseph Coppin's NEA")

    if program_type == 'text':

        text_init.init()

        while text_g.go:
            text_tick.tick()

    elif program_type == 'full':

        full_init.init()

        while full_g.go:
            full_tick.tick()

    else:
        raise Exception(f"Program type is {program_type}, which is not valid")

    py.quit()


# ================================================================================================
#  get_program_type -- controls selecting the program type, and then the whole Program.
#
#  INPUT:  none
#
#  RETURNS:  program_type: str - which type of program should be run, full or text
# ================================================================================================
def get_program_type():
    print(
        "\n\nWelcome to Joseph Coppin's Computer Science Component 3 non-examined assessment "
        "project! "
        "\nWould you like to run the full program, or just the text-based one? \n"
    )

    program_type = False
    while not program_type:

        print("Please enter 'full' for the full program, and 'text' for the text-based one. \n")
        answer = input()
        if answer not in ('full', 'text'):
            print("\n Sorry, that is not a valid response. Please enter either 'full' or 'text'. \n")
        else:
            program_type = answer

    return program_type


if __name__ == '__main__':
    main(get_program_type())
