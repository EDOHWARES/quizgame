import requests
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {
        "text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home "
                "to eat.",
        "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.",
     "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can kill a small dog.", "answer": "True"},
    {"text": "Is Mount Everest the tallest mountain on Earth?", "answer": 'True'},
    {"text": "Is the Great Wall of China visible from space?", "answer": 'False'},
    {"text": "Do ostriches bury their heads in the sand when frightened?", "answer": 'False'},
    {"text": "Is the human body composed of approximately 60% water?", "answer": 'True'},
    {"text": "Is the Mona Lisa painting located in the Louvre Museum?", "answer": 'True'},
    {"text": "Are there 24 hours in a day?", "answer": 'True'},
    {"text": "Is the Pacific Ocean the largest ocean on Earth?", "answer": 'True'},
    {"text": "Are there more than 100 billion galaxies in the observable universe?", "answer": 'True'},
    {"text": "Is the Statue of Liberty located in New York Harbor?", "answer": 'True'},
    {"text": "Is the Amazon River the longest river in the world?", "answer": 'False'},
    {"text": "Is the moon larger than the planet Pluto?", "answer": 'False'},
    {"text": "Are there 52 weeks in a year?", "answer": 'True'}
]

