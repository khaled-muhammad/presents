import os
import re

from ..combiner import combiner
from ..widgets.mcq import mcq
from ..widgets.subTitle import subTitle

class Paragraph:
    def __init__(self, text):
        self.text = text

    def format_text(self):
        result = re.search('\^\^(.*)\^\^', self.text)
        if result:
            self.text = self.text.replace(f'^^{result.group(1)}^^', f'<span style="font-weight:bold;text-decoration:underline;">{result.group(1)}</span>')
        return f"<div class='paragraph'>{self.text}</div>"

class MCQ:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def toJson(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "correct_answer": self.answer,
        }

    def calculate_choice_width(self):
        max_choice_width = max(len(choice) for choice in self.choices)
        return 2 if max_choice_width >= 25 else 1 if max_choice_width >= 17 else 0

    def render_mcq(self):
        choice_width = self.calculate_choice_width()
        return mcq(self.question, self.choices, choice_width)

def OpenEnded(question, direction='ltr'):
    with open(os.path.dirname(os.path.realpath(__file__)) + '/open_ended.html', 'r') as Template:
        template = Template.read()

    template = template.replace('{question}', question)

    if direction == 'rtl':
        template = template.replace("{style}", "direction: rtl;text-align:right;font-family: 'Al Nile';")
        template = template.replace("{liClass}", "ar")
    else:
        template = template.replace("{style}", "")
    
    return template

class Comprehension:
    def __init__(self, paragraphs, mcqs, openEnded=[], title='Read the following passage, then answer the questions:'):
        self.paragraphs = [Paragraph(p) for p in paragraphs]
        self.mcqs = [MCQ(cQ['question'], cQ['choices'], cQ['correct_answer']) for cQ in mcqs]
        self.title = title
        self.openEnded = openEnded

    def render(self):
        combined_paragraphs = ''.join(p.format_text() for p in self.paragraphs)
        rendered_mcqs = ''.join(mcq.render_mcq() for mcq in self.mcqs)
        rendered_open_ended_questions = ''.join(OpenEnded(q['question']) for q in self.openEnded)

        with open(os.path.dirname(os.path.realpath(__file__)) + '/comprehension.html', 'r') as template_file:
            template = template_file.read()

        template = template.replace('{paragraphs}', combined_paragraphs)
        template = template.replace('{mcqs}', rendered_mcqs)
        if len(self.openEnded) == 0:
            template = template.replace('{open_ended}', '')
            template = template.replace('<h3 class=\'quizTitle\'>Answer the following questions:</h3>', '')
        else:
            template = template.replace('{open_ended}', rendered_open_ended_questions)

        return "<div class='quiz'>" + combiner(
            subTitle("B. Reading & Critical Thinking", 'blue'),
            f"<h3 class='quizTitle'><div class='roundedBox'>2</div> {self.title}</h3>",
            template
        ) + "</div>"

    @classmethod
    def from_json(cls, json_data):
        data = json_data.get('data', {})
        return cls(
            paragraphs=data.get('passage', []),
            mcqs=data.get('mcq', []),
            openEnded=data.get('open_ended', []),
            title='Read the following passage, then answer the questions:'
        )