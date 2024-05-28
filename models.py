class Utterance:
    def __init__(self, speaker:str, utterance:str,) -> None:
        self.speaker    = speaker
        self.utterance  = utterance

    @staticmethod
    def fromJson(data):
        return Utterance(data['speaker'], data['utterance'])

class Conversation:
    def __init__(self, utterances:list[Utterance]) -> None:
        self.utterances = utterances

    @staticmethod
    def fromJson(data):
        utterances = [Utterance.fromJson(utterance_data) for utterance_data in data]
        return Conversation(utterances)

class Dialogue:
    def __init__(self, about:str, conversation:Conversation) -> None:
        self.about          = about
        self.conversation   = conversation

        speakers = []

        for u in self.conversation.utterances:
            speakers.append(u.speaker)
        
        self.speakers = tuple(speakers)

    @staticmethod
    def fromJson(data):
        about = data['about']
        conversation = Conversation.fromJson(data['conversation'])
        return Dialogue(about, conversation)

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

class Paragraph:
    def __init__(self, text):
        self.text = text
    
    #result = re.search('\^\^(.*)\^\^', self.text)
    #if result:
    #    self.text = self.text.replace(f'^^{result.group(1)}^^',

class Comprehension:
    def __init__(self, paragraphs, mcqs, openEnded=[], title='Read the following passage, then answer the questions:'):
        self.paragraphs = [Paragraph(p) for p in paragraphs]
        self.mcqs = [MCQ(cQ['question'], cQ['choices'], cQ['answer']) for cQ in mcqs]
        self.title = title
        self.openEnded = openEnded

    @classmethod
    def from_json(cls, json_data):
        data = json_data.get('data', {})
        return cls(
            paragraphs=data.get('passage', []),
            mcqs=data.get('mcq', []),
            openEnded=data.get('open_ended', []),
            title='Read the following passage, then answer the questions:'
        )