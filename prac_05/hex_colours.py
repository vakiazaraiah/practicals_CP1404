"""
Gets the input from user and show off color codes.
"""

COLORS = {"AliceBlue": "#fof8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
               "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "##76eec6",
               "aquamarine4": "#458b74"}

# gets input from user and prints out the color code.

color_name = input("Please enter the name of the color// ")
while color_name != "":
    if color_name in COLORS.keys():

        color_code = COLORS[color_name]
        print(color_code)
    else:
        print("Error no color")
    color_name = input("Please enter the name of the color// ")
