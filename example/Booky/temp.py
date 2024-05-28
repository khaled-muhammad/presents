import os
from sys import argv

unit_name = argv[1]

l = [
        "Vocab1",
        "VocabStudy15C",
        "VocabStudy1",
        "MiniTest1",
        "Structure1",
        "Vocab2",
        "VocabStudy25C",
        "VocabStudy2",
        "MiniTest2",
        "Structure2",
        "novel",
        "LanguageHints",
        "AEOnV",
        "AEOnS",
        "test"
    ]

# for n in l:
#     with open('scheme/'+n+'.json', 'w') as f:
#         f.write("[]")

# for n in os.listdir('../Gem/saves/'):
#     os.mkdir('saves/'+n)

for i in l:
    os.system(f"code '{os.path.join('saves/', unit_name, i+'.json')}'")