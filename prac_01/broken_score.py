"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score > 100:
    print("invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("passable")
elif score >= 0:
    print("bad")
else:
    print("invalid score")
