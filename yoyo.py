
#YoYo Notes
#Author : Dan and Yinka
#Purpose : Exercise
#Description : Simple terminal note taking application


# --------------- Terminal Interface ---------------------------


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


#-------------------- Functions ----------------------------------



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
            print(sub_menu_interface)
        case "E":
            print("About Application")
        case "R":
            print("Now Exiting YoYo Notes..\n\n\n\n")
        case other:
            print("Unrecognised Input")
            return take_menu_input()
        
        


print(main_menu_interface)

take_menu_input()

#-------------------- Functions ----------------------------------