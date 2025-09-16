import re 
import os 

from typing import List, Dict

filepath1 = 'temp/cites.txt'
filepath2 = 'temp'

def CheckingTemp():
    if os.path.exists(filepath2) and os.path.isdir(filepath2):
        print("Found temp, no need to worry")
    else:
        os.makedirs("filepath2")
    
def ParseNotes(filepath: str) -> List[Dict]:
    """
    Временная нарезка найденного cites.txt в подходящий нам вид, что даст нам возможность 
    после передать массив с цитатами дальше на выгрузку в SQL
    """
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    pattern = r'\*\*>.*?\n\*\*>(.*?)•(.*?)\n((?:.*?\n)*?)(?=\n\*\*>|\n\s*\n|$)'
    cites = []
    matches = re.finditer(pattern, content, re.DOTALL)

    for match in matches:
        cite = {
            'Book_title': match[0],
            'Author_name': match[1],
            'Cite': match[2]
        }
        cites.append(cite)
    
    return cites
    
parsed = ParseNotes(filepath1)
for i, note in enumerate(parsed, 1):
    print(f"Запись #{i}")
    print(f"Книга #{note['Book_title']}")
    print(f"Автор #{note['Author_name']}")
    print(f"Запись #{note['Cite']}")
    print("-"*50)