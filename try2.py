class ModelAnswerHtmlGenerator:
    def __init__(self):
        self.sections = []

    def add_section(self, title, content):
        self.sections.append((title, content))

    def add_multiple_choice(self, questions):
        answers_html = "".join([
            f"""
            <div class="answer-item">
                <div class="question-number">{num}.</div>
                <div class="correct-answer">{answer}</div>
            </div>
            """ for num, answer in questions.items()
        ])
        self.add_section("1) Choose the correct answer:", f"""
        <div class="answers-grid">
            {answers_html}
        </div>
        """)

    def add_comprehension(self, questions, open_ended):
        answers_html = "".join([
            f"""
            <div class="answer-item">
                <div class="question-number">{num}.</div>
                <div class="correct-answer">{answer}</div>
            </div>
            """ for num, answer in questions.items()
        ])
        open_ended_html = "".join([
            f"""
            <div class="open-ended-item">
                <div class="question-text">{question}</div>
                <div class="open-correct-answer">{answer}</div>
            </div>
            """ for question, answer in open_ended.items()
        ])
        self.add_section("2) Comprehension:", f"""
        <div class="answers-grid">
            {answers_html}
        </div>
        <div class="open-ended-answers">
            {open_ended_html}
        </div>
        """)

    def add_translation(self, translations):
        translation_html = "".join([
            f"""
            <div class="open-ended-item">
                <div class="open-correct-answer" style="direction: {direction}; text-align: {align};">{text}</div>
            </div>
            """ for text, direction, align in translations
        ])
        self.add_section("3) Translation:", f"""
        <div class="open-ended-answers">
            {translation_html}
        </div>
        """)

    def add_novel(self, contents):
        novel_html = "".join([
            f"""
            <div class="open-ended-item">
                <div class="open-correct-answer">{content}</div>
            </div>
            """ for content in contents
        ])
        self.add_section("4) Novel:", novel_html)


    def render(self):
        sections_html = "".join([
            f"""
            <div class="quiz">
                <h3 class='quizTitle'>{title}</h3>
            </div>
            <div class="margin">
                <div class="md-question">
                    {content}
                </div>
            </div>
            """ for title, content in self.sections
        ])
        return f"""
        <div class="md-title">Model Answer</div>
        {sections_html}
        """

# Data
multiple_choice_data = {
    1: "Khaled",
    2: "Paris",
    3: "Mars",
    4: "Harper Lee",
    5: "Pacific Ocean",
    6: "Oxygen",
    7: "1912",
    8: "Leonardo da Vinci",
    9: "2",
    10: "Diamond",
    11: "Australia"
}

comprehension_data = {
    1: "b) To maintain the health of our planet and future generations",
    2: "b) Solar, wind, and hydropower",
    3: "a) It"
}

open_ended_data = {
    "Why should societies adopt green technologies?": "Societies should adopt green technologies because they offer sustainable alternatives to fossil fuels, reducing carbon footprints and pollution. This helps mitigate climate change and promotes a more sustainable future.",
    "How do education and awareness help environmental conservation?": "Education and awareness help by informing people about the environment's importance and the threats it faces. Informed individuals are more likely to take protective actions, and community involvement empowers contributions to local conservation efforts."
}

translations_data = [
    ("١- تكمن أهمية الجمعيات الخيرية في مساعدة الفقراء و المحتاجين. فتقوم الجمعيات الخيرية بعمل ممتاز لأنها تعمل في كل أنحاء العالم.", "rtl", "right"),
    ("Education and awareness help by informing people about the environment's importance and the threats it faces. Informed individuals are more likely to take protective actions, and community involvement empowers contributions to local conservation efforts.", "ltr", "left")
]

novel_data = "Education and awareness help by informing people about the environment's importance and the threats it faces. Informed individuals are more likely to take protective actions, and community involvement empowers contributions to local conservation efforts."

# Create quiz and add sections
quiz = ModelAnswerHtmlGenerator()
quiz.add_multiple_choice(multiple_choice_data)
quiz.add_comprehension(comprehension_data, open_ended_data)
quiz.add_translation(translations_data)
quiz.add_novel(novel_data)

# Render HTML
html_output = quiz.render()

import pyperclip
pyperclip.copy(html_output)