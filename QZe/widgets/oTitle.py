import os

def oTitle(title):
    template = ""

    with open(os.path.dirname(os.path.realpath(__file__)) + '/oTitle.html', 'r') as Template:
        template = Template.read()

    template = template.replace("{0}", title[0])
    template = template.replace("{1}", title[1:])

    return template