try:
    file = open('Sampl.txt','r+')
    reading = file.read()
    print(reading)
    file.close()
except FileNotFoundError:
    print("This file",'Sample.txt',"does not exist.")


