import csv
#to load the csv file
def load_csv():
    try:
        with open('question and answers details.csv',mode ="r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
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
                option = input("Enter options[A/B/C/D]").upper()
                for option in question_text:
                    if option in ['A','B','C','D']:
                        return True
                answer = row[6]
                print("Correct answer")
                if not option == answer:
                    print(answer)    
                     
                    #correct_answer = input("Enter answer[A/B/C/D]")
                    #if correctc_answer in ['A','B','C','D']:
                        #print("Correct answer")
                    #else:
                        #print("Incorrect answer")
                        #question_text+=1                   
                    
    except FileNotFoundError:
        print(f"File {file} not found") 
load_csv()
