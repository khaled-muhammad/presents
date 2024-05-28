import os

def arabicMiniTitle(title):
    template = ""

    with open(os.path.dirname(os.path.realpath(__file__)) + '/arabicMiniTitle.html', 'r') as Template:
        template = Template.read()

    template = template.replace("{text}", title)

    return template