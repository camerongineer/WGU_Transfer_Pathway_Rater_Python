# budget == 5 == cheap / difficulty == 5 == easy / speed == 5 == fast to complete
import json
from typing import Dict

reviewer_rating = {
    "Saylor Academy": {"budget": 5, "difficulty": 1, "speed": 3},
    "Sophia Learning": {"budget": 5, "difficulty": 5, "speed": 5},
    "StraighterLine": {"budget": 3, "difficulty": 4, "speed": 3},
    "Study.com": {"budget": 2, "difficulty": 3, "speed": 2}}


def get_parameter_importance(parameter: str) -> int:
    importance_map = {"slightly": 1, "moderately": 3, "extremely": 5}
    prompt_map = {
        "budget": "How important to you is it that the courses are cheap? ",
        "difficulty": "How important to you is it that the courses are easy? ",
        "speed": "How important to you is it that the courses can me completed quickly? "}
    print(f"{prompt_map[parameter]}(OPTIONS = slightly, moderately, extremely): ", end="")
    importance = input()
    while importance not in importance_map:
        print("That was not a valid choice, "
              "please choose from the following options. (OPTIONS = slightly, moderately, extremely): ", end="")
        importance = input()
    print()
    return importance_map[importance]


def select_transfer_school() -> str:
    print()
    school_map = {"1": "Saylor Academy", "2": "Sophia Learning", "3": "StraighterLine", "4": "Study.com"}
    for i in range(1, 5):
        print(f"{i}: {school_map[str(i)]}")
    print("Please select the school for which you would like your personalized rating. "
          "(OPTIONS = 1, 2, 3, 4): ", end="")
    choice = input()
    if choice not in school_map:
        print("This is not a valid choice.\n")
        return "invalid"
    else:
        return school_map[choice]


def tabulate_rating(budget_importance: int, difficulty_importance: int, speed_importance: int, school: str) -> float:
    max_point_total = (budget_importance * 5) + (difficulty_importance * 5) + (speed_importance * 5)
    school_ratings = reviewer_rating[school]
    budget_score = school_ratings["budget"] * budget_importance
    difficulty_score = school_ratings["difficulty"] * difficulty_importance
    speed_score = school_ratings["speed"] * speed_importance
    actual_tabulated_score = 5 / (max_point_total / (budget_score + difficulty_score + speed_score))
    rounded_score = round(actual_tabulated_score * 4) / 4  # rounds score to nearest .25
    return rounded_score


def print_hoots(rating: float, school_name: str):
    import time
    print()
    rating_expand = int(rating * 8)
    if 0 < rating_expand % 8 < 3:
        rating_expand += 1
    wgu_owl = [[" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", "(", "Q", "v", "Q", ")", " "],
               [" ", "(", " ", "w", "g", "u", " ", ")"],
               [" ", " ", " ", "\"", " ", "\"", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " "]]
    for i in range(8):
        for j in range(rating_expand):
            print(wgu_owl[i][j % 8], end="")
            if wgu_owl[i][j % 8] != " ":
                time.sleep(.02)
        print()
    print(f"{school_name} has received a rating of {rating} hoots\n\n\n")


def set_all_importance_parameters() -> Dict[str, int]:
    importance_parameters = {
        "budget": get_parameter_importance("budget"),
        "difficulty": get_parameter_importance("difficulty"),
        "speed": get_parameter_importance("speed")}
    save_importance_parameters(importance_parameters)
    return importance_parameters


def load_saved_importance_parameters() -> Dict[str, int]:
    try:
        with open("save_file.json", "r") as save_file:
            save_file_data = json.load(save_file)
            importance_parameters = {
                "budget": int(save_file_data["budget"]),
                "difficulty": int(save_file_data["difficulty"]),
                "speed": int(save_file_data["speed"]),
            }
            valid_values = [1, 3, 5]
            if (importance_parameters["budget"] not in valid_values
                    or importance_parameters["difficulty"] not in valid_values
                    or importance_parameters["speed"] not in valid_values):
                raise IOError
            reversed_importance_map = {1: "slightly", 3: "moderately", 5: "extremely"}
            print(f"It is {reversed_importance_map[importance_parameters['budget']]} "
                  "important to you that courses are cheap to take\n"
                  f"It is {reversed_importance_map[importance_parameters['difficulty']]}"
                  " important to you that courses are easy to complete\n"
                  f"It is {reversed_importance_map[importance_parameters['speed']]} "
                  "important to you that courses are fast to complete\n")
            print("\n\nWould you like to change these parameters of importance for this review? (OPTIONS = y, n): ", end="")
            answer = input()
            while answer not in ["y", "n", "yes", "no"]:
                print("That is not a valid choice, please answer 'y' for yes or 'n' for no")
                answer = input()
            if answer in ["yes", "y"]:
                return set_all_importance_parameters()
            else:
                return importance_parameters
    except IOError:
        return set_all_importance_parameters()


def save_importance_parameters(importance_parameters: Dict[str, int]):
    with open("save_file.json", "w") as save_file:
        json.dump(importance_parameters, save_file)


def main():
    print("\n\n\n")
    importance_parameters = load_saved_importance_parameters()
    school_name = select_transfer_school()
    while school_name == "invalid":
        school_name = select_transfer_school()
    print_hoots(tabulate_rating(importance_parameters["budget"],
                                importance_parameters["difficulty"],
                                importance_parameters["speed"],
                                school_name), school_name)


main()
