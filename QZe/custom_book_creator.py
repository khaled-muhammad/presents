from widgets.comprehension import Comprehension
from widgets.dialogue import Dialogue
from widgets.generTitle import generTitle
from widgets.text import text
from widgets.translation import choicesTranslation, sepData
from widgets.wrappers import alignContainer, alignText, aligner, fullWidth
from widgets.boxedText import boxedText
from widgets.arabicMiniTitle import arabicMiniTitle
from widgets.oTitle import oTitle
from widgets.subTitle import subTitle
from combiner import combiner
from widgets.title import Title
from section.page import page, Header, Footer
from weasyprint import HTML, CSS
import utils
from colorama import Fore
from widgets.Quiz import *
from identifier import BookScheme
from sys import argv
from langdetect import detect

from widgets.writing import Essay

# Loading main CSS
mainCss = CSS(filename="style.css")
# Loading Font Awesome CSS
fontAwesome = CSS(filename='all.min.css')

# Dictionary to keep track of the count of questions
questionsCount = {}

try:
    book_scheme_path = argv[1]
except:
    print("Pass the Book Scheme and rerun the script.")
    exit()

bookScheme = BookScheme.from_json_file(book_scheme_path)
marginalia = bookScheme.get_marginalia()

print(bookScheme)

for unit_name in sorted((name for name in os.listdir(os.path.join(bookScheme.path, 'saves/')) if not name.startswith('.')), key=utils.extract_first_number):
    print(unit_name)

    # Arranging the unit data files based on priority
    unitDataPathes = os.listdir(os.path.join(bookScheme.path, 'saves/', unit_name))
    unitDataPathesArranged = []

    # Checking if a preferred file exists and adding it to the arranged list
    for i in bookScheme.get_files_priority():
        if i in [j.split('.')[0] for j in unitDataPathes]:
            unitDataPathesArranged.append(i+'.json')
    
    data = []

    # Looping through the arranged data files
    for basename in unitDataPathesArranged:
        splitted_file_name = basename.split('.')

        file_name      = splitted_file_name[0]
        file_extension = splitted_file_name[1]

        if (bookScheme.is_excluded(file_name)):
            continue

        # Determining the kind of data based on filename
        kind = bookScheme.get_extended_file_name(file_name)
        if kind == None:
            if file_name == 'test':
                kind = 'Test'
        
        f_data = utils.read(os.path.join(bookScheme.path, 'saves/', unit_name, basename))
        print("   Proccessing:", file_name, '...')

        if isinstance(f_data, list) and len(f_data) != 0 and 'type' not in f_data[0].keys():
            for i in range(len(f_data)):
                if unit_name in questionsCount.keys():
                    questionsCount[unit_name] += 1
                else:
                    questionsCount[unit_name] = 0
                q = f_data[i]
                #q['question'] = '.'.join(q['question'].split('.')[1:])
                f_data[i] = q

            # Creating structured data
            guideTitle = "Choose the TWO correct answers out of the FIVE options given:" if len(f_data[0]['choices']) == 5 else "Choose the correct answer:"
            sT = subTitle(kind, 'blue') if kind != None else ''
            data.append({
                'kind': kind,
                #'data': subTitle(kind, 'blue') + advancedChoices(0, f_data, guideTitle=guideTitle) if kind.lower() == 'vocabulary' or kind.lower() == 'structure' else subTitle(kind, 'blue') + advancedChoices(0, f_data, guideTitle=guideTitle),
                'data': sT + advancedChoices(0, f_data, guideTitle=guideTitle),
            })
        elif isinstance(f_data, list) and len(f_data) != 0 and 'type' in f_data[0].keys():
            print("Analyzing test, please wait ...")
            test_titles = bookScheme.get_test_titles()
            test_data = ""
            test_data += subTitle(title=kind, color='blue')

            for question in f_data:
                qType = question['type']
                inBQType = test_titles[qType]

                print("   Rendering:", qType, '...')
                if qType in ['5choices', 'choices']:
                    content = question['data']
                    test_data += advancedChoices(0, content, guideTitle=inBQType)
                elif qType == 'dialogue':
                    dialgoue = Dialogue.fromJson(question)
                    test_data += generTitle(inBQType)
                    test_data += dialgoue.html()
                elif qType == 'comprehension':
                    comprehension = Comprehension.from_json(question)
                    test_data += comprehension.render()
                elif qType == 'translation':
                    translation = choicesTranslation(*sepData(question['data']))
                    test_data += translation
                elif qType == 'writing':
                    writing = Essay.from_json(question)
                    test_data += writing.generate_essay()

            data.append({
                'kind': kind,
                'data': test_data,
            })
        elif len(f_data) == 0:
            print("Empty file!")
            continue
        elif isinstance(f_data, dict) and 'type' in f_data.keys():
            fType = f_data['type']
            print(fType)
            if fType == 'translation':
                collectedD = choicesTranslation(*sepData(f_data['data']))
                sT = subTitle(fType, 'blue')
                data.append({
                    'kind': kind,
                    'data': sT + collectedD,
                })

    print("Creating pdf ...")
    # Creating PDF using WeasyPrint


    if marginalia != None and unit_name in marginalia.keys():
        pdf2 = HTML(
            string=page(
                unit_name,
                0,
                combiner(
                    # *data
                    *[i['data'] for i in data],
                ),
                header= Header.fromJson(marginalia[unit_name]['header']),
                footer= Footer.fromJson(marginalia[unit_name]['footer'])
            )
        )
    else:
        pdf2 = HTML(
            string=page(
                unit_name,
                0,
                combiner(
                    # *data
                    *[i['data'] for i in data],
                )
            )
        )

    # Writing the PDF
    pdf2.write_pdf(os.path.join(bookScheme.path, 'output/', f'{unit_name}.pdf'), stylesheets=[mainCss, fontAwesome])
    print("PDF was compiled successfully :)")