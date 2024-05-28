import os

lPath = os.path.dirname(os.path.realpath(__file__))

class Utterance:
    template = open(os.path.join(lPath, 'utterance.html'), 'r').read()

    def __init__(self, speaker:str, utterance:str,) -> None:
        self.speaker    = speaker
        self.utterance  = utterance
    
    def html(self):
        return self.template.replace('{speaker}', self.speaker).replace('{utterance}', self.utterance)

    @staticmethod
    def fromJson(data):
        return Utterance(data['speaker'], data['utterance'])

class Conversation:
    def __init__(self, utterances:list[Utterance]) -> None:
        self.utterances = utterances
    
    def html(self):
        return ''.join([u.html() for u in self.utterances])

    @staticmethod
    def fromJson(data):
        utterances = [Utterance.fromJson(utterance_data) for utterance_data in data]
        return Conversation(utterances)

class Dialogue:
    template = open(os.path.join(lPath, 'dialogue.html'), 'r').read()

    def __init__(self, about:str, conversation:Conversation) -> None:
        self.about          = about
        self.conversation   = conversation
    
    def html(self) -> str:
        return self.template.replace('{about}', self.about).replace('{utterances}', self.conversation.html())

    @staticmethod
    def fromJson(data):
        about = data['about']
        conversation = Conversation.fromJson(data['conversation'])
        return Dialogue(about, conversation)