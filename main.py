import pandas as pd
import requests
import os
from tqdm import tqdm
from handle import GetDescription, GetSamples


source = input('What is the file name (with extension): ')
delim = input('What is the delimiter: ')
file_name = input('What will be the output file name? ')
samples_amount = int(input('How many samples do you want to get? '))

os.system('cls' if os.name == 'nt' else 'clear')

print('Creating a dict to save the datas...')
result = {}
print('Result was created successfully!')


try:
    print('Reading the data file...')
    if delim == 'tab':
        data = pd.read_csv(f'./data/{source}', sep="\t")
    else:
        data = pd.read_csv(f'./data/{source}', sep=f"{delim}")
    print(f'{source} was read successfully...')
    words = [x for x in data.index]
    print(f'there is {len(words)} words in the {source}')
    del data
except:
    print('Error to read file')

print('\n')
try:
    print('starting to search translations...')
    for word in tqdm(words):
        print(f'Getting description and samples about: "{word}"')
        print(f'Getting description to "{word}"...')
        desc = GetDescription(word)
        res = requests.get(
            f'https://pt.bab.la/dicionario/ingles-portugues/{word}')
        print(f'Getting samples to "{word}"...')
        examples = GetSamples(res, samples_amount)
        print(f'Save "{word}" on dict')
        result[word] = [desc, examples]
        print(f'"{word}" was saved successfully!')

    del res, desc, examples, words, word
except:
    print('Error to create dictionary')


try:
    print(f'Creating {file_name} file...')
    f = open(f"./file/{file_name}.txt", "w+", encoding="utf-8")
    for key, value in tqdm(result.items()):
        print(f'Creating line to "{key}"')

        line = f"{key};"
        line += value[0]
        line += ";"
        for x in value[1]:
            line += " ".join(x)
            line += "/"

        print(f'"{key}" line was created successfully!')
        print(f'adding "{key}" line on {file_name}')
        f.write(line + '\n')
        print(f'"{key}" line was added successfully!')
    print(f'Closing {file_name}')
    f.close()
    print('Done!')
except:
    print('Error to create a txt file')
