"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD" and "qld": "Queensland", "NSW" and "nsw": "New South Wales", "NT" and "nt": "Northern Territory", "WA" and "wa": "Western Australia",
               "ACT" and "act": "Australian Capital Territory", "VIC" and "vic": "Victoria", "TAS" and "tas": "Tasmania"}
# print(STATE_NAMES)

state = input("Enter short state: ")
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ")
