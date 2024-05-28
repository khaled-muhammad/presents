from qze_presentation import ContactInfo, Presentation
import json

with open('sec3 u12 voc short quiz.json', 'r') as f:
    questions_data = json.load(f)

output_path = "sec3 u12 voc short quiz.pptx"

prst = Presentation()
prst.addIntro(
    brand_name='Bri8minz',
    title='Senior 3 Unit 4',
    background_image='xxx.jpg',
)
prst.addTitleSlide('Vocab')
for i, q in enumerate(questions_data):
    prst.addMCQ(q, i+1)
prst.addEndSlide(
    contactInfo=ContactInfo(
        phone_number= '01559025553',
        teacher_picture= 'teacher_picture.jpg',
    )
)

prst.save(output_path)