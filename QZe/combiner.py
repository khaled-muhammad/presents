def combiner(*widgets):
    widgets = list(widgets)
    returnedData = ""

    for widget in widgets:
        returnedData += widget + "\n"

    return returnedData