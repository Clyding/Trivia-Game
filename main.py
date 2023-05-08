from project1 import Questions

def main():
    player1_score = 0
    player2_score = 0

    asked_qstns = []
    player1 = input("Please enter the name of player1: ")
    player2 = input("Please enter the name of player2: ")
    for question in range(len(question_list)):
        while len(asked_qstns) < 20:
            current_question = question_list[question]
            if current_question in asked_qstns:
                continue

            print(current_question.getquestion())
            answer = [current_question.getanswer1(), current_question.getanswer2(), current_question.getanswer3(), current_question.getanswer4()]

            for j in range(len(answer)):
                print(f"{j + 1}. {answer[j]}")
            player1_choice = int(input("Enter your choice " + str(player1) + " "))
            if player1_choice == current_question.getSolution():
                player1_score += 1
                
            print(current_question.getquestion())
            for j in range(len(answer)):
                print(f"{j + 1}. {answer[j]}")
            player2_choice = int(input("Enter your choice " + str(player2) + " "))
            if player2_choice == current_question.getSolution():
                player2_score += 1
            asked_qstns.append(current_question)
            break
            

    if player1_score > player2_score:
        print(str(player1) + " earned a total score of " + str(player1_score) + " out of 20")
        print(str(player2) + " earned a total score of " + str(player2_score) + " out of 20")
        print("Congratulation to " + player1 + " the winner")
    elif player2_score > player1_score:
        print(str(player1) + " earned a total score of " + str(player1_score) + " out of 20")
        print(str(player2) + " earned a total score of " + str(player2_score) + " out of 20")
        print("Congratulation to " + player2 + " the winner")
    else:
        print("Tie Game")

    print("Thank you for playing the trivia game!")


question_list = [
    Questions("1) Which team won the NBA championship in 2021?", "Los Angeles Lakers", "Miami Heat", "Golden State Warriors", "Brooklyn Nets", 1),
    Questions("2) What is the highest grossing movie of all time?", "Avatar", "Titanic", "Avengers: Endgame", "Star Wars: The Force Awakens", 3),
    Questions("3) What is the most popular programming language in 2021?", "Java", "Python", "C++", "JavaScript", 2),
    Questions("4) Who is the all-time leading scorer in the NBA?", "Kareem Abdul-Jabbar", "LeBron James", "Michael Jordan", "Kobe Bryant", 1),
    Questions("5) What is the name of the highest peak in North America?", "Denali", "Mount Everest", "K2", "Mount Kilimanjaro", 1),
    Questions("6) Which artist has won the most Grammy Awards?", "Beyonce", "Taylor Swift", "Michael Jackson", "Quincy Jones", 4),
    Questions("7) What is the capital city of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", 3),
    Questions("8) What is the name of the fictional city where Batman operates?", "Gotham City", "Metropolis", "Central City", "Star City", 1),
    Questions("9) What is the chemical symbol for gold?", "Au", "Ag", "Cu", "Fe", 1),
    Questions("10) What is the name of the first man to walk on the moon?", "Neil Armstrong", "Buzz Aldrin", "Michael Collins", "Yuri Gagarin", 1),
    Questions("11) What is the highest mountain in the world?", "Mount Kilimanjaro", "Mount Everest", "Mount Denali", "Mount Aconcagua", 2),
    Questions("12) Which programming language was created by Guido van Rossum?", "Java", "Python", "C++", "JavaScript", 2),
    Questions("13) Which NFL team has won the most Super Bowl championships?", "Pittsburgh Steelers", "New England Patriots", "Dallas Cowboys", "San Francisco 49ers", 1),
    Questions("14) What is the name of the actor who plays Iron Man in the Marvel Cinematic Universe?", "Chris Evans", "Robert Downey Jr.", "Chris Hemsworth", "Tom Holland", 2),
    Questions("15) Which country won the 2018 FIFA World Cup?", "Brazil", "Spain", "France", "Germany", 3),
    Questions("16) Which planet in our solar system is known as the 'Red Planet'?", "Venus", "Jupiter", "Mars", "Neptune", 3),
    Questions("17) What is the most visited country in the world?", "France", "United States", "China", "Spain", 1),
    Questions("18) Which team has the most NBA titles? ", "Chicago Bulls", "Miami Heat", "Detroit Pistons", "Los Angeles Lakers", 4),
    Questions("19) Who was the previous all time NBA leading scorer before Lebron? ", "Magic Johnson", "Michael Jordan", "Bill Rusell", "Hakeem Olajuwon", 1),
    Questions("20) What is the atomic number of Molybdenum", 26, 42, 63, 36, 2)]

if __name__ == "__main__":
    main()