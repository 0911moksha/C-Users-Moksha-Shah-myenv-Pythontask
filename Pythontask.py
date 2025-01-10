import csv
#to load the csv file
def load_csv():
    try:
        with open('question and answers details.csv',mode ="r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            score = 0
            for row in csv_reader:
                question_text = row[1]
                optionA = row[2]
                optionB = row[3]
                optionC = row[4]
                optionD = row[5]
                print(f"{question_text}")
                print(f"(A){optionA}")
                print(f"(B){optionB}")
                print(f"(C){optionC}")
                print(f"(D){optionD}")
                input_answer = input("Enter options[A/B/C/D]").upper()
                for option in question_text:
                    if option in ['A','B','C','D']:
                        return True
                answer = row[6]
                print(f"Correct answer is:")
                if not option == answer:
                    print(answer)
                if input_answer == answer:
                        score+=1
                        print("The answer is correct")
                else:
                    print("Invalid")
                print(f"Your score is {score}")            
                    
    except FileNotFoundError:
        print(f"File {file} not found") 
load_csv()
