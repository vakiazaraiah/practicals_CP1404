"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


def main():
    score = taking_score()
    check_score(score)


def check_score(score):
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


def taking_score():
    score = float(input("Enter score: "))
    return score
main()