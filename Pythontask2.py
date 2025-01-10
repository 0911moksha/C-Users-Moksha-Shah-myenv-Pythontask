import csv
def load_csv():
    data =[]
    try:
        with open('Name and score.csv',mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File not found") 
        return data
    #to write the data in csv file
def write_csv(filename,data):
    with open(filename,mode = 'w',newline = '') as file:
        writer = csv.writer(file)
        writer.writerows(data)      
write_csv(filename='Name and score.csv',data=[['Name','Score'],['Moksha','6']])
        