filename = 'output.txt'

file = open('output.txt','w')
user_input = input("Enter data to write in the file:")
file.write(user_input+'\n')

file = open('output.txt','a')
appending = input("Enter additional data to append:")
file.write(appending+'\n')
print('Data successfully appended.')
print('Final content of the',filename+':')

file = open('output.txt','r')
reading_file=file.read()
print(reading_file)
file.close()
