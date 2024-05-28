import os
directory = os.path.dirname(os.path.realpath(__file__))
def localPather(filename):
    return directory + "/" + filename

class text:
    keywords        = None
    paragraphs      = []
    mode            = None
    title           = None
    reciever        = None
    sender          = None
    introducingText = None
    endingText      = None
    senderName      = None
    nextNumber      = 0
    cleaners        = [
        "{introducingText}",
        "{endingText}",
        "{senderName}",
        "({number})",
        "{text}"
    ]

    def __init__(self, keywords, title=None, reciever=None, sender=None, introducingText=None, endingText=None, senderName=None):
        self.keywords        = None
        self.paragraphs      = []
        self.mode            = None
        self.title           = None
        self.reciever        = None
        self.sender          = None
        self.introducingText = None
        self.endingText      = None
        self.senderName      = None
        self.nextNumber      = 0
        if title != None:
            self.mode = "essay"
            self.title = title
        elif title == None:
            self.mode = "email"
            self.introducingText = introducingText
            self.endingText = endingText
            self.senderName = senderName
            if "@" not in reciever:
                self.reciever = reciever + "@example.com"
            else:
                self.reciever = reciever

            if "@" not in sender:
                self.sender = sender + "@example.com"
            else:
                self.sender = sender
        
        self.keywords   = keywords

    def keyWordsBox(self, keywords, title="Check Vocabulary"):
        template = open(localPather("templates/key_words_box.html"), 'r').read()
        content = ""
        
        for keyword in keywords:
            content += f"<li>{keyword['meaning']}</li><hr style='display: block; height: 1px;border: 0; border-top: 1px dotted blue;' />"
        
        template = template.replace("{title}", title)
        template = template.replace("{content}", content)
        
        return template

    def paragraph(self, p):
        template = open(localPather("templates/paragraph.html"), 'r').read()

        template = template.replace("{content}", p)

        self.paragraphs.append(template)

    def paragraphKeyword(self):
        template = open(localPather("templates/paragraph_keyword.html"), 'r').read()

        template = template.replace("{text}", self.keywords[self.nextNumber]['word'])
        template = template.replace("{number}", str(self.nextNumber+1))
        self.nextNumber += 1

        return template

    def info(self):
        if self.mode == "essay":
            return f"<h1 class='textTitle'>{self.title}</h1>"
        elif self.mode == "email":
            template = open(localPather("templates/mail_info.html"), 'r').read()
            
            template = template.replace("{toMail}", self.reciever)
            template = template.replace("{fromMail}", self.sender)
            return template


    def render(self):
        template = open(localPather("templates/text.html"), 'r').read()
        paragraphs = ""

        for paragraph in self.paragraphs:
            paragraphs += paragraph

        template = template.replace("{info}", self.info())
        template = template.replace("{content}", paragraphs)
        template = template.replace("{keyWordsBox}", self.keyWordsBox(self.keywords))
        if self.mode == "email":
            template = template.replace("{introducingText}", self.introducingText)
            template = template.replace("{endingText}", self.endingText)
            template = template.replace("{senderName}", self.senderName)

        for cleaner in self.cleaners:
            template = template.replace(cleaner, "")

        return template