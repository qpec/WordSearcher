import os
input_file_reference = open('p-value.txt')
input_file_content = input_file_reference.readlines()
jargon_words_matched = []

#parameter to adjust
jargon_words_database = ['null hypothesis', 'p-value', 'mean']

#start search protocol
program_initiated = False
print('to initiate your search, type: START')
while program_initiated == False:
    if input() == 'START':
        print('search iteration initiated')
        program_initiated = True
        break
    else:
        continue

#search protocol
while program_initiated == True:
    for line in input_file_content:
        for word in jargon_words_database:
            if word in line:
                if word not in jargon_words_matched:
                    jargon_words_matched.append(word)
                    print(word + ' found in source file!')
    break

print(list(jargon_words_matched))
        

