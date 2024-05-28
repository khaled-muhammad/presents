
from QZe.widgets.comprehension import Comprehension
from QZe.widgets.translation import choicesTranslation, sepData
from QZe.widgets.Quiz import *
from QZe.section.page import page
from QZe.combiner import combiner
from QZe.widgets.oTitle import oTitle
from QZe.widgets.writing import OpenEndedQuestion
from QZe.widgets.generTitle import generTitle

from weasyprint import HTML, CSS

model_answer_data = open('model-answer.html', 'r').read() #''


# Loading main CSS
mainCss = CSS(filename="QZe/assets/css/style.css")
# Loading Font Awesome CSS
fontAwesome = CSS(filename='QZe/assets/css/all.min.css')

mcqs = [
    {
        "question": "What is ur name?",
        "choices": [
            "Aasem",
            "Sarah",
            "Muhammad",
            "Khaled"
        ],
        "correct_answer": "Khaled"
    },
    {
        "question": "What is the capital of France?",
        "choices": [
            "Berlin",
            "Madrid",
            "Paris",
            "Rome"
        ],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": [
            "Earth",
            "Mars",
            "Jupiter",
            "Saturn"
        ],
        "correct_answer": "Mars"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "choices": [
            "Harper Lee",
            "J.K. Rowling",
            "Ernest Hemingway",
            "Mark Twain"
        ],
        "correct_answer": "Harper Lee"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": [
            "Atlantic Ocean",
            "Indian Ocean",
            "Arctic Ocean",
            "Pacific Ocean"
        ],
        "correct_answer": "Pacific Ocean"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": [
            "Oxygen",
            "Gold",
            "Osmium",
            "Silver"
        ],
        "correct_answer": "Oxygen"
    },
    {
        "question": "In what year did the Titanic sink?",
        "choices": [
            "1905",
            "1912",
            "1918",
            "1923"
        ],
        "correct_answer": "1912"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "choices": [
            "Vincent van Gogh",
            "Pablo Picasso",
            "Leonardo da Vinci",
            "Claude Monet"
        ],
        "correct_answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the smallest prime number?",
        "choices": [
            "1",
            "2",
            "3",
            "5"
        ],
        "correct_answer": "2"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "choices": [
            "Gold",
            "Iron",
            "Diamond",
            "Platinum"
        ],
        "correct_answer": "Diamond"
    },
    {
        "question": "Which country is home to the kangaroo?",
        "choices": [
            "India",
            "Australia",
            "South Africa",
            "Brazil"
        ],
        "correct_answer": "Australia"
    }
]

mpdfText = page(
        "TRY",
        0,
        combiner(
            *[
                #oTitle('Quiz FR Night 1'),
                subTitle("MCQ Seq", 'color'),
                advancedChoices(0, mcqs, guideTitle="Choose the correct answer from the following: "),
                generTitle("Novel Questions: "),
                OpenEndedQuestion('What is ur name?').generate_essay(),
            ]
        )
    )

pdf2 = HTML(
    string=mpdfText
)
modelAnswerCss = CSS(filename="QZe/assets/css/model_answer.css")
model_answer_pdf = HTML(
    string=page(
        "Model Answer",
        0,
        model_answer_data
    )
)
model_answer_pdf.write_pdf('demo-model-answer.pdf', stylesheets=[mainCss, modelAnswerCss, fontAwesome])

# Writing the PDF
#pdf2.write_pdf('try.pdf', stylesheets=[mainCss, fontAwesome])