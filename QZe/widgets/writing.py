import os

class Essay:
    def __init__(self, subject, title='Write an essay of about 180 words on:'):
        self.subject = subject
        self.title = title
        self.template = ""
        self.eL = ""

    def _read_template(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + '/essay.html', 'r') as Template:
            self.template = Template.read()

    def _generate_empty_lines(self):
        for _ in range(20):
            self.eL += "<hr class='dotsLine' />"

    def generate_essay(self):
        self._read_template()
        self._generate_empty_lines()

        essay_template = self.template.replace("{title}", self.title)
        essay_template = essay_template.replace("{essaySubject}", self.subject)
        essay_template = essay_template.replace("{emptyLines}", self.eL)

        return "<div class='quiz'>" + essay_template + "</div>"

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data.get("title", ""), json_data.get("kind", "Write an essay of about 180 words on:"))


class OpenEndedQuestion:
    def __init__(self, question='Write an essay of about 180 words on:'):
        self.question = question
        self.template = ""
        self.eL = ""

    def _read_template(self):
        with open(os.path.dirname(os.path.realpath(__file__)) + '/open_ended.html', 'r') as Template:#open_ended_question.html
            self.template = Template.read()

    def _generate_empty_lines(self):
        for _ in range(2):
            self.eL += "<hr class='dotsLine' />"

    def generate_essay(self):
        self._read_template()
        self._generate_empty_lines()

        essay_template = self.template.replace("{question}", self.question)
        essay_template = essay_template.replace("{liClass}", "ar")
        essay_template = essay_template.replace("{style}", "")
        essay_template = essay_template.replace("{emptyLines}", self.eL)

        return "<div class='quiz'>" + essay_template + "</div>"

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data.get("title", ""), json_data.get("kind", "Write an essay of about 180 words on:"))