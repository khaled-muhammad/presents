import os
from ..combiner import combiner
from ..widgets.generTitle import generTitle
import string
from langdetect import detect

smallChars  = list(string.ascii_lowercase)
arabic_letters = [
    'ا', 'ب', 'ج', 'د', 'ه', 'و', 'ز', 'ح', 'ط', 'ي', 'س', 'ش', 'ص', 'ض', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي'
]
optionsForm = """<div class='choiceQuestion'>
    {renderedQuestion}

    <div class='options'>
        {options}
    </div>
</div>"""

choiceQuestionT = """<div class='choiceQuestion'>
    <li class="engNumbering" style="{qStyle}"><h3 style="font-family: 'Kailasa';font-weight: 200;font-size: 14pt;display: inline-block;">{question}</h3></li>

    <div class='options'>
        {choices}
    </div>
</div>"""

def arabicNumsToIndianNums(number):
    # Convert Arabic numerals to Indian numerals
    arabic_numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    indian_numerals = ['٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩']

    # Convert each digit in the number
    indian_number_str = ''.join(indian_numerals[arabic_numerals.index(digit)] for digit in str(number))

    return indian_number_str

def translation(toAra, toEn, titles=['Translate into Arabic:', 'Translate into English:'], emptyLines=4):
    template = ""

    with open(os.path.dirname(os.path.realpath(__file__)) + '/translations.html', 'r') as Template:
        template = Template.read()
    
    renderedArabicTranslations = ""
    renderedEnglishTranslations = ""

    for tQ in range(0, len(toAra)):
        renderedArabicTranslations += f"<h4><span>{tQ+1}. </span>{toAra[tQ]}</h4>" + '<br />'

        for eLine in range(emptyLines):
            renderedArabicTranslations += f"<hr class='dotsLine' />"

    for tQ in range(0, len(toEn)):
        renderedEnglishTranslations += f"<h4 style=\"direction: rtl; font-family: 'Almarai';\">{arabicNumsToIndianNums(tQ+1)}. {toEn[tQ]}</h4>" + '<br />'

        for eLine in range(emptyLines):
            renderedEnglishTranslations += f"<hr class='dotsLine' />"

    template = template.replace("{toAraTitle}", titles[0])
    template = template.replace("{toEnTitle}", titles[1])
    template = template.replace("{toArabic}", renderedArabicTranslations)
    template = template.replace("{toEnglish}", renderedEnglishTranslations)


    return template

def choice(question, choices, isBig=0, isQArabic=False, isChoicesArabic=False):
    txtChoices = ""
    template = ""
    currentChoice = 0
    qAdditonalStyles = ''
    choicesAdditonalStyles = ''

    if isQArabic == True:
        qAdditonalStyles = 'direction: rtl; text-align: right;'
    if isChoicesArabic == True:
        choicesAdditonalStyles += 'direction: rtl; text-align: right;'
        smallChars = ['أ', 'ب', 'ج', 'د']

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
        template = f"{choiceQuestionT}"

        for choice in choices:
            if isChoicesArabic == False:
                txtChoices += f"<div style=\"position: relative;width: 100%;{choicesAdditonalStyles}\">" + f"<div class='choice' style=\"position: relative;width: 100%;\"><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[currentChoice]}</span> </div></div> {choice}</div>" + "</div>"
            else:
                txtChoices += f"<div style=\"position: relative;width: 100%;{choicesAdditonalStyles}\">" + f"<div class='choice' style=\"position: relative;width: 100%;\">{choice} <div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block; margin-left:5px;'><div class='choiceN' style='right: 1px !important;'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[currentChoice]}</span> </div></div> </div>" + "</div>"
            currentChoice += 1

        template = template.replace("{qStyle}", qAdditonalStyles)
        template = template.replace("{question}", question)
        template = template.replace("{choices}", txtChoices)
        if isQArabic == True:
            template = template.replace("engNumbering", "")
            template = template.replace("</li>", f"<span style='color: #D0232B;font-weight: bold;font-family: \"Kharabeesh\";font-size: larger;'> .{str(currentQN).replace('1', '١').replace('2', '٢').replace('3', '٣').replace('4', '٤').replace('5', '٥').replace('6', '٦').replace('7', '٧').replace('8', '٨').replace('9', '٩')}</span> </li>")

    return template


def choicesTranslation(toAr, toEn, titles=['Choose the correct Arabic translation:', 'Choose the correct English translation:']):
    renderedToAr = ""
    renderedToEn = ""

    for tQ in range(0, len(toAr)):
        renderedToAr += optionsForm\
            .replace(
                "{renderedQuestion}",
                f"<h4 style='margin: 0 25px;'><span>{tQ+1}. </span>{toAr[tQ]['from']}</h4>" + '<br />')\
                    .replace(
                        "{options}",
                        "".join(
                            f"<div style=\"position: relative;width: 100%;direction: rtl; text-align: right;\">" + f"<div class='choice' style=\"position: relative;width: 100%;\"><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block; margin-left:5px;'><div class='choiceN' style='right: 1px !important;'> <span style='display: table-cell;vertical-align: middle;'>{arabic_letters[i]}</span> </div></div> {o}</div>" + "</div>" for i, o in enumerate(toAr[tQ]['to'])
                            ))

    for tQ in range(0, len(toEn)):
        renderedToEn += optionsForm\
            .replace(
                "{renderedQuestion}",
                f"<h4 style=\"direction: rtl; font-family: 'Almarai'; margin: 25px 0;\">{arabicNumsToIndianNums(tQ+1)}. {toEn[tQ]['from']}</h4>" + '<br />')\
                    .replace(
                        "{options}",
                        "".join(
                            f"<div style='display:block;'><div class='choice'><div class='choiceNC' style='width: 16px;height: 16px;border-radius:100%;border: 1px solid #D0232B;display:inline-block;'><div class='choiceN'> <span style='display: table-cell;vertical-align: middle;'>{smallChars[i]}</span> </div></div> {o}</div></div>" for i, o in enumerate(toEn[tQ]['to'])
                            ))


    return combiner(
        "<div class='quiz'>",
        generTitle(titles[0]),
        renderedToAr,
        generTitle(titles[1]),
        renderedToEn,
        "</div>",
    )

def sepData(data):
    # Initialize dictionaries for each language
    english_data = []
    arabic_data  = []

    # Iterate through the original data and categorize based on detected language
    for item in data:
        try:
            detected_language = detect(item["from"])
        except:
            print(data)
            print(item["from"])
            print("ERRRROR")
            exit()
        if detected_language == 'en':
            english_data.append(item)
        elif detected_language == 'ar':
            arabic_data.append(item)
    
    return english_data, arabic_data