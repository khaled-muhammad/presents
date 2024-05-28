import pyperclip
import json

from QZe.widgets.comprehension import Comprehension
from QZe.widgets.translation import choicesTranslation, sepData
from QZe.widgets.Quiz import *
from QZe.section.page import page, Header, Footer
from QZe.combiner import combiner
from QZe.widgets.writing import OpenEndedQuestion
from QZe.widgets.generTitle import generTitle
from QZe.model_answer import ModelAnswerHtmlGenerator

from weasyprint import HTML, CSS
from qze_presentation import Presentation

prst      = Presentation()
pdf_data  = []
test_data = ''
model_answer = ModelAnswerHtmlGenerator()

translation_data = {
    'to_ar': [],
    'to_en': [],
}
# elif qType == 'dialogue':
#     dialgoue = Dialogue.fromJson(question)
#     test_data += generTitle(inBQType)
#     test_data += dialgoue.html()

# elif qType == 'writing':
#     writing = Essay.from_json(question)
#     test_data += writing.generate_essay()


current_q = 0

prst_title = input("Enter title for the presentation: ")

needIntro = True if input("Want to add an Intro slide? ") == "yes" else False

if needIntro:
    brand_name = input("Enter your branding name: ")
    prst_bg    = input("Enter the path or url for intro background image: ")
    if prst_bg == '':
        prst_bg = 'assets/default_bg.png'
    
    prst.addIntro(brand_name=brand_name, title=prst_title, background_image=prst_bg)
    test_data += subTitle(title=prst_title, color='blue')

def addQuestion():
    global current_q, test_data
    current_q += 1

    print("Choose question type: ")
    print("1- MCQ")
    print("2- Open-ended")
    print("3- English to Arabic translation")
    print("4- Arabic to English translation")
    print("5- Dialogue")
    print("6- Comprehension")
    print("7- Mix")

    selected_question_type = int(input("Select: "))

    if selected_question_type == 7:
        print("Adding sub group ...")
        addQuestion()
    elif selected_question_type == 1:
        input("Waiting for copying the MCQ json data ...")
        clipboard_data = pyperclip.paste()
        parsed_mcq_data = json.loads(clipboard_data)

        test_data += advancedChoices(0, parsed_mcq_data, guideTitle=question_name)
        mcq_correct_answers = {i+1: v['correct_answer'] for i, v in enumerate(parsed_mcq_data)}
        model_answer.add_multiple_choice(mcq_correct_answers)
        for q in parsed_mcq_data:
            prst.addMCQ(
                question=q,
                question_number=current_q
            )
    elif selected_question_type == 6:
        input("Waiting for copying the Comprehension json data ...")
        clipboard_data = pyperclip.paste()
        parsed_comprehension_data = json.loads(clipboard_data)
        comprehension = Comprehension.from_json(parsed_comprehension_data)
        test_data += comprehension.render()
        comprehension_data = {i+1: v['correct_answer'] for i, v in enumerate(parsed_comprehension_data['data']['mcq'])}
        open_ended_data = {v['question'] : v['correct_answer'] for v in parsed_comprehension_data['data']['open_ended']}
        model_answer.add_comprehension(comprehension_data, open_ended_data)
        prst.addComprehension(comprehension=comprehension)
    elif selected_question_type == 2:
        test_data += generTitle(question_name)
        data = []
        while True:
            question = input("Enter open-ended question (stop to end): ")
            if question == 'stop':
                break
            else:
                answer = input("Enter question answer: ")
                data.append({
                    'question': question,
                    'correct_answer': answer
                })
                test_data += OpenEndedQuestion(question=question).generate_essay()
        
        model_answer.add_novel([i['correct_answer'] for i in data])
        for q in data:
            prst.addOpenEnded(question=q, question_number=current_q)
    elif selected_question_type == 3:
        input("Waiting for copying the MCQ json data ...")
        clipboard_data = pyperclip.paste()
        parsed_mcq_data = json.loads(clipboard_data)
        translation_data["to_ar"].append(parsed_mcq_data)
        prst.addToArTranslation(
            question=parsed_mcq_data,
            question_number=current_q
        )
    elif selected_question_type == 4:
        input("Waiting for copying the MCQ json data ...")
        clipboard_data = pyperclip.paste()
        parsed_mcq_data = json.loads(clipboard_data)
        translation_data["to_en"].append(parsed_mcq_data)
        prst.addToEnTranslation(
            question=parsed_mcq_data,
            question_number=current_q
        )

while True:
    question_name = input("Enter Question Name (Enter to skip and stop to end): ")
    if question_name == 'stop' and question_name == 'end':
        break
    elif question_name != '':
        prst.addQuizQuestionTitle(question_name)

    addQuestion()

translation = choicesTranslation(toAr=translation_data["to_ar"], toEn=translation_data["to_en"])
model_answer.add_translation([
    *[(i['correct_answer'], 'rtl', 'right') for i in translation_data['to_ar']],
    *[(i['correct_answer'], 'ltr', 'left') for i in translation_data['to_en']],
])

test_data += translation
pdf_data.append({
    'kind': 'test',
    'data': test_data,
})

# Loading main CSS
mainCss = CSS(filename="QZe/assets/css/style.css")
modelAnswerCss = CSS(filename="QZe/assets/css/model_answer.css")
# Loading Font Awesome CSS
fontAwesome = CSS(filename='QZe/assets/css/all.min.css')

pdf2 = HTML(
    string=page(
        prst_title,
        0,
        combiner(
            *[d['data'] for d in pdf_data],
        )
    )
)

model_answer_pdf = HTML(
    string=page(
        prst_title,
        0,
        model_answer.render()
    )
)

# Writing the PDF
pdf2.write_pdf(f'{prst_title}.pdf', stylesheets=[mainCss, fontAwesome])
model_answer_pdf.write_pdf(f'{prst_title}-model-answer.pdf', stylesheets=[mainCss, modelAnswerCss, fontAwesome])

prst.save(f'{prst_title}.pptx')