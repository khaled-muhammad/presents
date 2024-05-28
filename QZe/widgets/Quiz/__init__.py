import os
from ...widgets.subTitle import subTitle
from ...combiner import combiner
import string
import re

class Quiz:
    quizName    = None
    L           = ""
    smallChars  = list(string.ascii_lowercase)

    def __init__(self, quizName=0):
        self.quizName = quizName

    def quiz(self, content):
        template = ""

        with open(os.path.dirname(os.path.realpath(__file__)) + '/quiz.html', 'r') as Template:
            template = Template.read()

        template = template.replace("{content}", content)

        return template
    
    def choice(self, question, choices, isBig=0, direction='ltr'):
        txtChoices = ""
        template = ""
        currentChoice = 0
        if isBig == 0:
            with open(os.path.dirname(os.path.realpath(__file__)) + '/choiceQuestion.html', 'r') as Template:
                template = Template.read()

            for choice in choices:
                txtChoices += f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{self.smallChars[currentChoice]}</span> </div></div> {choice}</div>"
                currentChoice += 1

            template = template.replace("{question}", question)
            template = template.replace("{choices}", txtChoices)
        elif isBig == 1:
            with open(os.path.dirname(os.path.realpath(__file__)) + '/bigChoiceQuestion.html', 'r') as Template:
                template = Template.read()

            template = template.replace("{question}", question)
            template = template\
                .replace("{O1}", f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{self.smallChars[0]}</span> </div></div> {choices[0]}</div>")\
                    .replace("{O2}", f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{self.smallChars[1]}</span> </div></div> {choices[1]}</div>")\
                        .replace("{O3}", f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{self.smallChars[2]}</span> </div></div> {choices[2]}</div>")\
                            .replace("{O4}", f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{self.smallChars[3]}</span> </div></div> {choices[3]}</div>")
        elif isBig == 2:
            with open(os.path.dirname(os.path.realpath(__file__)) + '/choiceQuestion.html', 'r') as Template:
                template = Template.read()

            for choice in choices:
                txtChoices += "<div>" + f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{self.smallChars[currentChoice]}</span> </div></div> {choice}</div>" + "</div>"
                currentChoice += 1

            template = template.replace("{question}", question)
            template = template.replace("{choices}", txtChoices)

        if direction == 'rtl':
            template = template.replace("{style}", "direction: rtl;text-align:right;font-family: 'Al Nile';")
            template = template.replace("{liClass}", "ar")
        else:
            template = template.replace("{style}", "")
            
        return template

    def reading(self, paragraphs, choiceQuestions, title='Read the following passage, then answer the questions :'):
        template = ""
        combinedParagraphs = ""
        renderedChoiceQuestions = ""

        with open(os.path.dirname(os.path.realpath(__file__)) + '/reading.html', 'r') as Template:
            template = Template.read()
        
        for p in paragraphs:
            result = re.search('\^\^(.*)\^\^', p)
            if result:
                p = p.replace(f'^^{result.group(1)}^^', f'<span style="font-weight:bold;text-decoration:underline;">{result.group(1)}</span>')
            
            combinedParagraphs += f"<div class='paragraph'>{p}</div>"

        for cQ in choiceQuestions:
            if 'isBig' in cQ.keys():
                renderedChoiceQuestions += self.choice(cQ['question'], cQ['choices'], cQ['isBig'])
            else:
                maxC = 0
                for c in cQ['choices']:#20
                    if len(c) > maxC:
                        maxC = len(c)
                
                renderedChoiceQuestions += self.choice(cQ['question'], cQ['choices'], 2 if maxC >= 25 else 1 if maxC>= 17 else 0)

        template = template.replace('{paragraphs}', combinedParagraphs)
        template = template.replace('{choices}', renderedChoiceQuestions)

        self.L += "<div>" + combiner(
            subTitle("B. Reading & Critical Thinking", 'blue'),
            f"<h3 class='quizTitle'><div class='roundedBox'>2</div> {title}</h3>",
            template
        ) + "</div>"

    def choicesQ(self, questions, title = "Choose the correct answer:"):
        currentQN = 1

        allQ = ""

        for q in questions:
            if 'isBig' in q.keys():
                allQ += self.choice(q['question'], q['choices'], q['isBig'])
            else:
                maxC = 0
                for c in q['choices']:#20
                    if len(c) > maxC:
                        maxC = len(c)
                
                allQ += self.choice(q['question'], q['choices'], 2 if maxC >= 25 else 1 if maxC>= 17 else 0)
            currentQN += 1

        self.L += combiner(
            f"<h3 class='quizTitle'><div class='roundedBox'>1</div> {title}</h3>",
            allQ
        )
    
    def translation(self, toAr, toEn, titles=['Translate into Arabic:', 'Translate into English:']):
        template = ""

        with open(os.path.dirname(os.path.realpath(__file__)) + '/translation.html', 'r') as Template:
            template = Template.read()

        template = template.replace("{toAraTitle}", titles[0])
        template = template.replace("{toEnTitle}", titles[1])
        #
        if toAr != None:
            template = template.replace("{toArabic}", toAr)
        #else:
        #    template = template.replace("{toArabic}", toAr)

        renderedChoiceQuestions = ""
        for cQ in toEn:
            if 'isBig' in cQ.keys():
                renderedChoiceQuestions += self.choice(cQ['question'], cQ['choices'], cQ['isBig'], direction='rtl')
            else:
                maxC = 0
                for c in cQ['choices']:#20
                    if len(c) > maxC:
                        maxC = len(c)
                
                renderedChoiceQuestions += self.choice(cQ['question'], cQ['choices'], 2 if maxC >= 25 else 1 if maxC>= 17 else 0, direction='rtl')

        template = template.replace("{toEnglish}", renderedChoiceQuestions)

        self.L += combiner(
            subTitle("C. Translation", 'blue'),
            template,
        )

    def writing(self, questions, title='Choose the correct answer:'):
        template = ""

        with open(os.path.dirname(os.path.realpath(__file__)) + '/writing.html', 'r') as Template:
            template = Template.read()

        renderedChoiceQuestions = ""
        for cQ in questions:
            if 'isBig' in cQ.keys():
                renderedChoiceQuestions += self.choice(cQ['question'], cQ['choices'], cQ['isBig'])
            else:
                maxC = 0
                for c in cQ['choices']:#20
                    if len(c) > maxC:
                        maxC = len(c)
                
                renderedChoiceQuestions += self.choice(cQ['question'], cQ['choices'], 2 if maxC >= 25 else 1 if maxC>= 17 else 0)

        template = template.replace("{toEnglish}", renderedChoiceQuestions)

        template = template.replace("{choices}", renderedChoiceQuestions)

        self.L += combiner(
            subTitle("D. Writing", 'blue'),
            f"<h3 class='quizTitle'>{title}</h3>",
            template,
        )

    def compiler(self):
        if self.quizName == 0:
            wantedTitleImage = 'file:///Volumes/louda/Developer/Python/QBooksCreator/widgets/unitTest.png'
        elif self.quizName == 1:
            wantedTitleImage = 'file:///Volumes/louda/Developer/Python/QBooksCreator/widgets/GExercise1.png'
        elif self.quizName == 2:
            wantedTitleImage = 'file:///Volumes/louda/Developer/Python/QBooksCreator/widgets/GExercise2.png'
        elif self.quizName == 3:
            wantedTitleImage = 'file:///Volumes/louda/Developer/Python/QBooksCreator/widgets/GExercise3.png'

        return combiner(
            f"<img src='{wantedTitleImage}' style='width:650px;display:block;margin:0 auto;' />",
            subTitle("A. Vocabulary and Structures", 'blue'),

            self.quiz(self.L),
        )




def advancedChoices(title, questions, guideTitle="Choose the correct answer:", currentQN = None):
    if currentQN == None:
        currentQN = 1
    else:
        currentQN = currentQN + 1

    smallChars  = list(string.ascii_lowercase)
    combinedQuestions = ""

    if title == 0:
        wantedTitleImage = 'file:///Volumes/louda/Developer/Python/QBooksCreator/widgets/EOnV.png'
    elif title == 1:
        wantedTitleImage = 'file:///Volumes/louda/Developer/Python/QBooksCreator/widgets/EOnS.png'
    elif title == 2:
        wantedTitleImage = 'file:///Volumes/louda/Developer/Python/QBooksCreator/widgets/AdvancedEOnV.png'
    elif title == 3:
        wantedTitleImage = 'file:///Volumes/louda/Developer/Python/QBooksCreator/widgets/AdvancedEOnS.png'


    def choice(question, choices, isBig=0):
        txtChoices = ""
        template = ""
        currentChoice = 0
        if isBig == 0:
            with open(os.path.dirname(os.path.realpath(__file__)) + '/choiceQuestion.html', 'r') as Template:
                template = Template.read()

            for choice in choices:
                txtChoices += f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #eb67a0;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[currentChoice]}</span> </div></div> {choice}</div>"
                currentChoice += 1

            template = template.replace("{question}", question)
            template = template.replace("{choices}", txtChoices)
        elif len(choices) > 4:
            with open(os.path.dirname(os.path.realpath(__file__)) + '/choiceQuestion.html', 'r') as Template:
                template = Template.read()

            for choice in choices:
                txtChoices += "<div>" + f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[currentChoice]}</span> </div></div> {choice}</div>" + "</div>"
                currentChoice += 1

            template = template.replace("{question}", question)
            template = template.replace("{choices}", txtChoices)
        elif isBig == 1:
            with open(os.path.dirname(os.path.realpath(__file__)) + '/bigChoiceQuestion.html', 'r') as Template:
                template = Template.read()

            template = template.replace("{question}", question)
            template = template\
                .replace("{O1}", f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[0]}</span> </div></div> {choices[0]}</div>")\
                    .replace("{O2}", f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[1]}</span> </div></div> {choices[1]}</div>")\
                        .replace("{O3}", f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[2]}</span> </div></div> {choices[2]}</div>")\
                            .replace("{O4}", f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[3]}</span> </div></div> {choices[3]}</div>")
        elif isBig == 2:
            with open(os.path.dirname(os.path.realpath(__file__)) + '/choiceQuestion.html', 'r') as Template:
                template = Template.read()

            for choice in choices:
                txtChoices += "<div>" + f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[currentChoice]}</span> </div></div> {choice}</div>" + "</div>"
                currentChoice += 1

            template = template.replace("{question}", question)
            template = template.replace("{choices}", txtChoices)


        return template

    for q in questions:
        try:
            if 'isBig' in q.keys():
                combinedQuestions += choice(q['question'], q['choices'], q['isBig'])
        except:
            print(q)
            exit()
        else:
            maxC = 0
            for c in q['choices']:#20
                if len(c) > maxC:
                    maxC = len(c)
            
            combinedQuestions += choice(q['question'], q['choices'], 2 if maxC >= 25 else 1 if maxC>= 17 else 0)
        currentQN += 1


    return combiner(
        #f"<img src='{wantedTitleImage}' style='width:650px;display:block;margin:0 auto;' />",
        f"<div class='quiz'> <h3 class='quizTitle'>{guideTitle}</h3> <ol class='Questions' start='{currentQN}'>{combinedQuestions}</ol></div>"
    )