# from pprint import pprint
import json

points = 0



# with open('quiz.json') as json_file:
#     questions = json.loads(json_file.read().encode('UTF-8'))
#     print(questions)
    # pprint(questions)


# import json

# points = 0

def show_question(question):
    global points

    print()
    print(question, ["pytanie"])
    print("a:", question["a"])
    print("b:", question["b"])
    print("c:", question["c"])
    print("d:", question["d"])
    print()
#
    # questions = json.load(json_file)

    # for i in range(0, len(questions)):
    #     print(questions[i]["pytanie"])
    #     show_question(questions[i])
    answer = input("Ktorą odpowiedź wybierasz? ")

    if answer == question["prawidłowa odpowiedź"]:
        points += 1
        print("To prawidłowa odpowiedź, brawo! Masz już", points, "punktów.")
    else:
        print("Niestety to zła odpowiedź, prawidłowa odpowiedź to " + question["prawidłowa odpowiedź"] + ".")


with open("quiz.json", encoding="utf-8") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
#     print(questions[i]["pytanie"])
        show_question(questions[i])


    # show_question(questions[i])

    print()
    print("To koniec gry, zdobyta liczba punktów to " + str(points) + ".")