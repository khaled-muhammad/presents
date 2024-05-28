import os
import re
import string

smallChars  = list(string.ascii_lowercase)

def mcq(question, choices, isBig=0, direction='ltr'):
    txtChoices = ""
    template = ""
    currentChoice = 0
    if isBig == 0:
        with open(os.path.dirname(os.path.realpath(__file__)) + '/choiceQuestion.html', 'r') as Template:
            template = Template.read()

        for choice in choices:
            txtChoices += f"<div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[currentChoice]}</span> </div></div> {choice}</div>"
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

    if direction == 'rtl':
        template = template.replace("{style}", "direction: rtl;text-align:right;font-family: 'Al Nile';")
        template = template.replace("{liClass}", "ar")
    else:
        template = template.replace("{style}", "")
        
    return template