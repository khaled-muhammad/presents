import aspose.slides as slides
import aspose.pydrawing as draw
from mod import modIt
from models import Dialogue, Comprehension
import string

smallChars     = list(string.ascii_lowercase)
arabic_letters = [
    'ا', 'ب', 'جـ', 'د', 'ه', 'و', 'ز', 'ح', 'ط', 'ي', 'س', 'ش', 'ص', 'ض', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'ه', 'و', 'ي'
]

class ContactInfo:
    def __init__(self, phone_number:str, teacher_picture=None) -> None:
        self.phone_number = phone_number
        self.teacher_picture = teacher_picture


def make_names_equal_length(name1, name2):
    len1 = len(name1)
    len2 = len(name2)

    if len1 < len2:
        name1 += " " * (len2 - len1)
    elif len2 < len1:
        name2 += " " * (len1 - len2)

    return name1, name2


class Presentation():
    slides_count = -1
    def __init__(self, template='template.pptx') -> None:
        self.template = template
        self.pres     = slides.Presentation(template)
    
        for layout in self.pres.layout_slides:
            if layout.name == 'intro':
                self.intro_layout = layout
            elif layout.name == 'mcq':
                self.mcq_layout = layout
            elif layout.name == 'next_objective_title':
                self.next_objective_title_layout = layout
            elif layout.name == 'quiz_next_objective':
                self.quiz_next_objective_layout = layout
            elif layout.name == 'dialogue':
                self.dialogue_layout = layout
            elif layout.name == 'open_ended':
                self.open_ended_layout = layout
            elif layout.name == 'to_ar':
                self.to_ar_layout = layout
            elif layout.name == 'to_en':
                self.to_en_layout = layout
            elif layout.name == 'end_slide':
                self.end_slide_layout = layout
            
    def addIntro(self, brand_name:str, title:str, background_image):
        slide = self.pres.slides.insert_empty_slide(self.slides_count+1, self.intro_layout)

        for i, shp in enumerate(slide.shapes):
            if shp.placeholder != None:
                if shp.name == 'brand_name':
                    shp.text_frame.text = brand_name
                elif shp.name == 'title':
                    shp.text_frame.text = title

        # Sets conditions for background image
        slide.background.type = slides.BackgroundType.OWN_BACKGROUND
        slide.background.fill_format.fill_type = slides.FillType.PICTURE
        slide.background.fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.STRETCH

        # Loads the image
        img = draw.Bitmap(background_image)

        # Adds image to presentation's images collection
        imgx = self.pres.images.add_image(img)

        slide.background.fill_format.picture_fill_format.picture.image = imgx


        self.slides_count += 1

    def addTitleSlide(self, title):
        slide = self.pres.slides.insert_empty_slide(self.slides_count+1, self.next_objective_title_layout)
        for i, shp in enumerate(slide.shapes):
            if shp.placeholder != None:
                shp.text_frame.text = title
        
        self.slides_count += 1

    def addQuizQuestionTitle(self, title):
        slide = self.pres.slides.insert_empty_slide(self.slides_count+1, self.quiz_next_objective_layout)
        for i, shp in enumerate(slide.shapes):
            if shp.placeholder != None:
                if shp.name == 'title':
                    shp.text_frame.text = title
        
        self.slides_count += 1

    def addMCQ(self, question:dict, question_number:int):
        # Add a new slide using the last layout slide
        slide = self.pres.slides.insert_empty_slide(self.slides_count+1, self.mcq_layout)
        # Gets the main sequence of the slide.
        sequence = slide.timeline.main_sequence
        for i, shp in enumerate(slide.shapes):
            if shp.placeholder != None:
                if shp.name == 'question_number':
                    shp.text_frame.text = str(question_number)
                    continue
                elif shp.name == 'question':
                    shp.text_frame.text = question['question']
                    continue
                else:
                    #print(shp.name)
                    # Changes the text in each placeholder
                    shp.text_frame.text = question['choices'][i-1]
                    if 'correct_answer' in question.keys():
                        if question['choices'][i-1] == question['correct_answer']:
                            # Adds Fade animation effect to shape
                            effect = sequence.add_effect(shp, slides.animation.EffectType.BRUSH_ON_UNDERLINE, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.ON_CLICK)
                            effect2 = sequence.add_effect(shp, slides.animation.EffectType.BRUSH_ON_COLOR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.WITH_PREVIOUS)

        self.slides_count += 1

    def addOpenEnded(self, question:dict, question_number:int):
        slide = self.pres.slides.insert_empty_slide(self.slides_count+1, self.open_ended_layout)

        for i, shp in enumerate(slide.shapes):
            if shp.placeholder != None:
                if shp.name == 'question':
                    shp.text_frame.text = question['question']
                elif shp.name == 'answer':
                    shp.text_frame.text = question['correct_answer']
                elif shp.name == 'question_number':
                    shp.text_frame.text = str(question_number)

        self.slides_count += 1

    def addToArTranslation(self, question:dict, question_number:int):
        slide = self.pres.slides.insert_empty_slide(self.slides_count+1, self.to_ar_layout)

        for i, shp in enumerate(slide.shapes):
            if shp.placeholder != None:
                if shp.name == 'question':
                    shp.text_frame.text = question['from']
                elif shp.name == 'options':
                    tf = shp.text_frame

                    for i, option in enumerate(question['to']):
                            para2 = slides.Paragraph()
                            para2.text = f"{arabic_letters[i]}) {option}"
                            tf.paragraphs.add(para2)

                            if option == question['correct_answer']:
                                slide.timeline.main_sequence.add_effect(para2, slides.animation.EffectType.BRUSH_ON_UNDERLINE, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.ON_CLICK)
                                slide.timeline.main_sequence.add_effect(para2, slides.animation.EffectType.BRUSH_ON_COLOR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.WITH_PREVIOUS)

                elif shp.name == 'question_number':
                    shp.text_frame.text = str(question_number)

        self.slides_count += 1

    def addToEnTranslation(self, question:dict, question_number:int):
        slide = self.pres.slides.insert_empty_slide(self.slides_count+1, self.to_en_layout)

        for i, shp in enumerate(slide.shapes):
            if shp.placeholder != None:
                if shp.name == 'question':
                    shp.text_frame.text = question['from']
                elif shp.name == 'options':
                    tf = shp.text_frame

                    for i, option in enumerate(question['to']):
                            para2 = slides.Paragraph()
                            para2.text = f"{smallChars[i]}) {option}"
                            tf.paragraphs.add(para2)

                            if option == question['correct_answer']:
                                slide.timeline.main_sequence.add_effect(para2, slides.animation.EffectType.BRUSH_ON_UNDERLINE, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.ON_CLICK)
                                slide.timeline.main_sequence.add_effect(para2, slides.animation.EffectType.BRUSH_ON_COLOR, slides.animation.EffectSubtype.NONE, slides.animation.EffectTriggerType.WITH_PREVIOUS)

                elif shp.name == 'question_number':
                    shp.text_frame.text = str(question_number)

        self.slides_count += 1

    def addDialogue(self, dialogue:Dialogue):
        slide = self.pres.slides.insert_empty_slide(self.slides_count+1, self.dialogue_layout)
        collected_dialogue = ""
        speaker1 = dialogue.speakers[0]
        speaker2 = dialogue.speakers[1]
        print("Speaker 1:", speaker1)
        print("Speaker 2:", speaker2)
        speaker1_in_pres, speaker2_in_pres = make_names_equal_length(speaker1, speaker2)
        for utterance in dialogue.conversation.utterances:
            if utterance.speaker == speaker1:
                collected_dialogue += speaker1_in_pres + ": " + utterance.utterance + '\n'
            else:
                collected_dialogue += speaker2_in_pres + ": " + utterance.utterance + '\n'
        
        for i, shp in enumerate(slide.shapes):
            if shp.placeholder != None:
                shp.text_frame.text = collected_dialogue

        self.slides_count += 1

    def addComprehension(self, comprehension:Comprehension):
        for paragraph in comprehension.paragraphs:
            slide = self.pres.slides.insert_empty_slide(self.slides_count+1, self.dialogue_layout)
            self.slides_count += 1

            for i, shp in enumerate(slide.shapes):
                if shp.placeholder != None:
                    shp.text_frame.text = paragraph.text
        
        if len(comprehension.mcqs) != 0:
            self.addQuizQuestionTitle("Choose the correct answer")
            for i, mcq in enumerate(comprehension.mcqs):
                self.addMCQ(mcq.toJson(), i+1)

        if len(comprehension.openEnded) != 0:
            self.addQuizQuestionTitle("Answer the following questions")

            for i, question in enumerate(comprehension.openEnded):
                self.addOpenEnded(question, i+1)

    def addEndSlide(self, contactInfo:ContactInfo):
        slide = self.pres.slides.insert_empty_slide(self.slides_count+1, self.end_slide_layout)

        for i, shp in enumerate(slide.shapes):
            if shp.placeholder != None:
                if shp.name == 'phone_number':
                    shp.text_frame.text = contactInfo.phone_number
                elif shp.name == 'teacher_pic' and contactInfo.teacher_picture != None:
                    shp.fill_format.fill_type = slides.FillType.PICTURE
                    with open(contactInfo.teacher_picture, "rb") as in_file:
                        shp.fill_format.picture_fill_format.picture.image = self.pres.images.add_image(in_file)
                        shp.fill_format.picture_fill_format.picture_fill_mode = slides.PictureFillMode.STRETCH
                #shp.text_frame.text

        self.slides_count += 1

    def save(self, path):
        self.pres.save(path, slides.export.SaveFormat.PPTX)
        modIt(path)