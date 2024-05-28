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
                <div class="open-correct-answer">{i+1}. {content}</div>
            </div>
            """ for i, content in enumerate(contents)
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