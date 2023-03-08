# YoYo Notes
# Author : Dan and Yinka
# Purpose : Exercise
# Description : Simple terminal note taking application


# --------------- Terminal Interface ---------------------------
import sys


main_menu_interface = """
YOYO NOTES TERMINAL APPLICATION


-----------------------------
(Q) New Notes 

(W) View Notes

(E) About

(R) Exit 
-------------------------------


Yinka & Dan Labs (c) 2023
"""

save_or_delete_interface = """
(S) save --------- (D) delete
"""

sub_menu_interface = """
(R) return
"""


# --------------- Terminal Interface ---------------------------


# -------------------- Functions ----------------------------------


def save_or_delete_note_menu(note):
    user_option = input("> ")
    user_option.lower()

    match user_option:
        case "s":
            print("Input Note Name")
            name_of_note = input("> ")
            print(save_note(note=note, file_name=name_of_note))
        case "d":
            print(main_menu_interface)
            return take_menu_input()
        case other:
            print("Unrecognised Input , Please try again")
            save_or_delete_note_menu(note)


def save_note(note, file_name):
    write_note = note

    with open(file_name, 'w') as yoyo:
        yoyo.writelines(write_note)
        print(f"{file_name} Has Been Saved To Current Directory!\n\n\n")

        print(main_menu_interface)
        take_menu_input()


def take_new_notes():
    print("-\n\n\n")
    note = input("")
    print(save_or_delete_interface)
    save_or_delete_note_menu(note=note)


def take_menu_input():
    user_input = input("> ")
    user_input.lower()

    match user_input:
        case "Q":
            print("New Notes Started")
            take_new_notes()
        case "W":
            print("View Notes")
            view_notes()
        case "E" :
            print("About Application")
            about_application()
        case "R":
            print("Now Exiting YoYo Notes..\n\n\n\n")
            exit_application()
        case other:
            print("Unrecognised Input")
            return take_menu_input()


def view_notes():
    file_name = str(input("Enter a file name: ")).lower()
    # with open(file_name, 'r') as note:
    #     print(note.readlines())


    note = open(file_name, "r")
    print(note.readlines())
    note.close()
    print(main_menu_interface)
    take_menu_input()


def about_application():
    app_history = str(print(
        "\nA user friendly application built to enable seamless documentation by users.\n"
        "You can now take notes of important events in your life, or journal your feelings without having to worry about a loss of information.\n"
        "Easy. Reliable. Private\n"
    ))
    return app_history


def exit_application():
    print("Application exited")
    sys.exit()



print(main_menu_interface)
take_menu_input()

# -------------------- Functions ----------------------------------
