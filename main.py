from mod import modIt
from models import Comprehension, Dialogue
from qze_presentation import ContactInfo, Presentation


from sample_data import questions_data

output_path = "Future Forms Sec 3 revision.pptx"

prst = Presentation()

prst.addIntro(
    brand_name='Bri8minz',
    title='Staying Healthy',
    background_image='healthy_habits_at_home.jpg',
)

prst.addTitleSlide('Future Forms Sec 3 revision')

for i, q in enumerate(questions_data):
    prst.addMCQ(q, i+1)

prst.addTitleSlide('Test on\nUnit 1')

prst.addQuizQuestionTitle("Complete the following Dialogue")

prst.addDialogue(
    dialogue=Dialogue.fromJson(
        data={
            "type": "dialogue",
            "about": "Tamer and Ali are talking about the release of Extraction 2 movie.",
            "conversation": [
                {
                    "speaker": "Tamer",
                    "utterance": ".................................................................. ?"
                },
                {
                    "speaker": "Ali",
                    "utterance": "Yes, I have! I loved the first one. When is Extraction 2 coming out?"
                },
                {
                    "speaker": "Tamer",
                    "utterance": "It's set to be released next month. I heard they've got some amazing action sequences planned."
                },
                {
                    "speaker": "Ali",
                    "utterance": ".................................................................... ?"
                },
                {
                    "speaker": "Tamer",
                    "utterance": "Absolutely! Chris is back as Tyler Rake. I can't wait to see how the story unfolds."
                },
                {
                    "speaker": "Ali",
                    "utterance": "Me too! Do you think it'll be as intense as the first one?"
                },
                {
                    "speaker": "Tamer",
                    "utterance": "..................................................................... ."
                },
                {
                    "speaker": "Ali",
                    "utterance": "Awesome! Let's plan to watch it together when it's out."
                },
                {
                    "speaker": "Tamer",
                    "utterance": "......................................................... !"
                }
            ]
        }
    )
)

prst.addQuizQuestionTitle(
    "Read the following passage, then Answer the questions")

prst.addComprehension(
    comprehension=Comprehension.from_json(
        json_data={
            "type": "comprehension",
            "data": {
                "passage": ["Electric cars are becoming increasingly popular as a sustainable alternative to traditional gasoline vehicles. These vehicles use electric motors powered by rechargeable batteries, producing zero tailpipe emissions. The environmental benefits, coupled with advancements in battery technology, have contributed to the growing adoption of electric cars worldwide.", "In addition to reducing air pollution, electric cars also play a significant role in decreasing our dependence on fossil fuels. With the global focus on combating climate change, the automotive industry is witnessing a shift towards cleaner and more energy-efficient transportation solutions. Governments and businesses alike are investing in the development of electric vehicle infrastructure, further promoting the widespread use of electric cars."],
                "mcq": [
                    {
                        "question": "What powers electric cars?",
                        "choices": ["Gasoline", "Solar energy", "Electric motors", "Hydrogen fuel cells"],
                        "answer": "Electric motors"
                    },
                    {
                        "question": "What is a key environmental benefit of electric cars mentioned in the passage?",
                        "choices": ["Reduced noise pollution", "Zero tailpipe emissions", "Increased air pollution", "High fuel consumption"],
                        "answer": "Zero tailpipe emissions"
                    }
                ],
                "open_ended": [
                    {
                        "question": "Explain one factor contributing to the growing popularity of electric cars.",
                        "answer": "The advancements in battery technology have made electric cars more practical and increased their overall range, making them a more viable option for consumers."
                    },
                    {
                        "question": "What challenges do you think electric cars might face in the future?",
                        "answer": "Potential challenges for electric cars may include the need for further infrastructure development, such as charging stations, and addressing concerns about the environmental impact of battery production and disposal."
                    }
                ]
            }
        }

    )
)

prst.addQuizQuestionTitle(
    "Choose the correct translation")

prst.addToArTranslation(
    question={
            "from": "how to run?",
            "to": [
                "كيف تجري؟",
                "كيف تلعب",
                "كيف تنام",
                "كيف تقفز؟"
            ],
            "correct_answer": "كيف تجري؟"
        },
    question_number=1
)

prst.addToEnTranslation(
    question={
            "from": "ما اسمك؟",
            "to": [
                "How old are you?",
                "What about your mom?",
                "What's your name?",
                "How to count from 1 to 10?"
            ],
            "correct_answer": "What's your name?",
    },
    question_number=2
)

prst.addEndSlide(
    contactInfo=ContactInfo(
        phone_number= '01559025553',
        teacher_picture= 'teacher_picture.jpg',
    )
)

prst.save(output_path)
