import os

def boxedText(title):
    template = ""

    with open(os.path.dirname(os.path.realpath(__file__)) + '/boxedText.html', 'r') as Template:
        template = Template.read()

    template = template.replace("{text}", title)

    return template