from bs4 import BeautifulSoup

def fullWidth(child):
    return f"<div display=block; width=100%;>{child}</div>"

def aligner(*children):
    areas = ""
    mergedChildren = ""

    for child in children:
        areas += child[0]
        mergedChildren += child[1]
    
    return f"<div style='width:100%; position:relative;'>{areas}{mergedChildren}</div>"
    #return f"<div style='width:100%; position:relative; background-color: red;'>{areas}<div style='width:100%; position:relative; background-color: green;'>{mergedChildren}</div></div>"

def alignContainer(align, child):
    alignment = []

    if align == 0:
        alignment.append(0)
        alignment.append(0)
    elif align == 1:
        alignment.append(53)
        alignment.append(50)
    elif align == 2:
        alignment.append(104.7)
        alignment.append(100)


    return [
        f"<div style='visibility: hidden;width:0!important;z-index: -1;display:inline-block;'>{child}</div>",
        f"<div style='position:absolute;left:{alignment[0]}%;transform:translateX(-{alignment[1]}%);bottom:0;'>{child}</div>"
    ]

def alignText(align, child):
    if align == 0:
        align = "left"
    elif align == 1:
        align = "center"
    elif align == 2:
        align = "right"

    soup = BeautifulSoup(child, "html.parser")
    for tag in soup.find_all():
        #print(dir(tag))
        if 'style' in tag.attrs:
            tag.attrs['style'] += f"text-align: {align};"
        else:
            tag.attrs['style'] = f"text-align: {align};"
    
    #print(dir(soup))
    return soup.renderContents().decode("UTF-8")