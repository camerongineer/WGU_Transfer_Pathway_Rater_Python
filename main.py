def print_hoots(rating: int):
    wgu_owl = [[" ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " "],
               [" ", "(", "Q", "v", "Q", ")", " "],
               ["(", " ", "w", "g", "u", " ", ")"],
               [" ", " ", "\"", " ", "\"", " ", " "],
               [" ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " "]]
    for i in range(7):
        for j in range(rating):
            print(wgu_owl[i][j], end="")
        print()


def select_transfer_school() -> str:
    school_map = {"1": "Saylor Academy", "2": "Sophia Learning", "3": "StraighterLine", "4": "Study.com"}
    for i in range(1, 5):
        print(f"{i}: {school_map[i]}")
    print("Please select the school that needs to be rated. (OPTIONS = 1, 2, 3, 4)", end="")
    choice = input()
    if choice not in school_map:
        print("This is not a valid choice.")
        return "invalid"
    else:
        return school_map[choice]


def get_budget_importance() -> int:
    importance_map = {"slightly": 1, "moderately": 3, "extremely": 5}
    print("How important to you is it that the courses are cheap? "
          "(OPTIONS = slightly, moderately, extremely): ", end="")
    importance = input()
    while importance not in importance_map:
        print("That was not a valid choice, "
              "please choose from the following options. (OPTIONS = slightly, moderately, extremely): ", end="")
        importance = input()
    return importance_map[importance]


def get_difficulty_importance():
    pass


def get_speed_importance():
    pass


def main():
    importance_parameters = {
        "budget": get_budget_importance(),
        "difficulty": get_difficulty_importance(),
        "speed": get_speed_importance()}
    school_name = select_transfer_school()
    while school_name == "invalid":
        school_name = select_transfer_school()
    