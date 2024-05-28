import os

#from header import header
#from footer import footer

class Header:
    def __init__(self, template_path='header.html', content={}) -> None:
        with open(template_path, 'r') as Template:
            self.template = Template.read()

        for placeholder, val in content.items():
            self.template = self.template.replace(f"{{{placeholder}}}", val)
    
        self.template = self.template.replace("{content}", "")

    @staticmethod
    def fromJson(data):
        return Header(
            template_path=data.get("template_path", "header.html"),
            content= data['content'],
        )

class Footer:
    def __init__(self, template_path='footer.html', content={}) -> None:
        with open(template_path, 'r') as Template:
            self.template = Template.read()
        
        for placeholder, val in content.items():
            self.template = self.template.replace(f"{{{placeholder}}}", val)
        
        self.template = self.template.replace("{content}", "")
        
    
    @staticmethod
    def fromJson(data):
        return Footer(
            template_path=data.get("template_path", "footer.html"),
            content=data['content']
        )

def page(unitName, pageNumber, content, header=None, footer=None):
    template = ""

    with open(os.path.dirname(os.path.realpath(__file__)) + '/page.html', 'r') as Template:
        template = Template.read()

    if header == None:
        template = template.replace('{header}', '')
    else:
        template = template.replace('{header}', header.template)

    if footer == None:
        template = template.replace('{footer}', '')
    else:
        template = template.replace('{footer}', footer.template)

    template = template.replace('{body}', content)

    return template