import os

questions = [
    {
        "question": "What is the capital of Australia?",
        "options": ["A. Canberra", "B. Sydney", "C. Melbourne", "D. Perth"],
        "correct": "A",
        "feedback": "Correct, Canberra is the capital city of Australia!",
        "facts": {
            "A": "Canberra was chosen as a compromise between Sydney and Melbourne.",
            "B": "Sydney is Australia's largest city and known for its Opera House.",
            "C": "Melbourne is famous for its cultural diversity and coffee.",
            "D": "Perth is one of the most isolated major cities in the world."
        }
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Saturn", "B. Neptune", "C. Jupiter", "D. Earth"],
        "correct": "C",
        "feedback": "Correct, Jupiter is the largest planet in the solar system!",
        "facts": {
            "A": "Saturn is famous for its stunning ring system, which is made of ice and rock particles.",
            "B": "Neptune is the farthest planet from the Sun and has winds that can reach up to 1,500 miles per hour!",
            "C": "Jupiter is so massive that it could fit 1,300 Earths inside it!",
            "D": "Earth is the only planet known to support life and is the densest planet in the solar system."
        }
    },
    {
        "question": "Who wrote the play Romeo and Juliet?",
        "options": [
            "A. Charles Dickens",
            "B. Roald Dahl",
            "C. William Shakespeare",
            "D. George Orwell"
        ],
        "correct": "C",
        "feedback": "Correct, William Shakespeare wrote Romeo and Juliet!",
        "facts": {
            "A": "Charles Dickens wrote classics like 'Oliver Twist' and 'Great Expectations.'",
            "B": "Roald Dahl is best known for his children's books like 'Matilda' and 'Charlie and the Chocolate Factory.'",
            "C": "William Shakespeare is often called the 'Bard of Avon' and wrote 39 plays, including 'Macbeth' and 'Hamlet.'",
            "D": "George Orwell wrote '1984' and 'Animal Farm,' which critique totalitarianism and political corruption."
        }
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Au", "B. Ag", "C. Go", "D. Gl"],
        "correct": "A",
        "feedback": "Correct, Au is the chemical symbol for gold!",
        "facts": {
            "A": "Gold's symbol 'Au' comes from the Latin word 'aurum,' meaning 'shining dawn.'",
            "B": "Ag is the symbol for silver, derived from the Latin word 'argentum.'",
            "C": "There is no element with the symbol 'Go.'",
            "D": "Gl is not a valid chemical symbol, but 'Gl' could refer to 'Gluon,' a particle in physics!"
        }
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["A. 5", "B. 4", "C. 8", "D. 7"],
        "correct": "D",
        "feedback": "Correct, there are 7 continents!",
        "facts": {
            "A": "There are only 5 continents if you combine Europe and Asia into one continent called 'Eurasia.'",
            "B": "There are no recognized continents with only 4. However, some believe there used to be more continents before plate tectonics changed the planet.",
            "C": "There are 7 continents, but some believe there are 8 if you count Zealandia, a submerged continent near New Zealand.",
            "D": "The 7 continents are: Africa, Antarctica, Asia, Europe, North America, Australia, and South America."
        }
    },
    {
        "question": "Which language has the most native speakers in the world?",
        "options": ["A. English", "B. Spanish", "C. Mandarin Chinese", "D. Hindi"],
        "correct": "C",
        "feedback": "Correct, Mandarin Chinese has the most native speakers!",
        "facts": {
            "A": "English is widely spoken as a second language, making it the most spoken language in the world overall.",
            "B": "Spanish is spoken by over 460 million people and is the official language in 20 countries.",
            "C": "Mandarin Chinese has over 900 million native speakers, primarily in China and Taiwan.",
            "D": "Hindi is the main language spoken in India, with over 340 million native speakers."
        }
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["A. Leonardo da Vinci", "B. Vincent Van Gogh", "C. Claude Monet", "D. Edvard Munch"],
        "correct": "A",
        "feedback": "Correct, Leonardo da Vinci painted the Mona Lisa!",
        "facts": {
            "A": "Leonardo da Vinci painted the Mona Lisa between 1503 and 1506, and it now hangs in the Louvre Museum in Paris.",
            "B": "Vincent Van Gogh is famous for his bold, expressive brushstrokes, especially in 'Starry Night.'",
            "C": "Claude Monet was a founder of the French Impressionist movement, best known for his 'Water Lilies' series.",
            "D": "Edvard Munch painted 'The Scream,' one of the most iconic expressions of anxiety in art history."
        }
    },
    {
        "question": "What is the square root of 64?",
        "options": ["A. 16", "B. 8", "C. 4", "D. 12"],
        "correct": "B",
        "feedback": "Correct, the square root of 64 is 8!",
        "facts": {
            "A": "16 is the square of 4, but it's not the square root of 64.",
            "B": "8 is the square root of 64, meaning 8 * 8 = 64.",
            "C": "4 is the square root of 16, not 64.",
            "D": "12 is close but is the square root of 144, not 64."
        }
    },
    {
        "question": "Which year did the Titanic sink?",
        "options": ["A. 1914", "B. 1911", "C. 1912", "D. 1890"],
        "correct": "C",
        "feedback": "Correct, the Titanic sank in 1912!",
        "facts": {
            "A": "1914: Even though the Titanic did not sink in this year, a famous handgun called the '1911' was introduced during this time.",
            "B": "1911: The Titanic had not yet set sail, but the RMS Olympic was still in service in this year!",
            "C": "1912: The Titanic tragically sank after hitting an iceberg on its maiden voyage.",
            "D": "1890: The Titanic was not even built yet, but the world was still reeling from the industrial revolution's advancements."
        }
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["A. Diamond", "B. Steel", "C. Tungsten", "D. Gold"],
        "correct": "A",
        "feedback": "Correct, the hardest natural substance on Earth is diamond!",
        "facts": {
            "A": "Diamonds are formed under extreme pressure deep within the Earth's mantle and are the hardest natural material known.",
            "B": "Steel is a strong alloy made of iron and carbon, but it's not harder than diamond.",
            "C": "Tungsten is one of the hardest metals and is known for its high melting point.",
            "D": "Gold is a soft metal and is often alloyed with other metals for use in jewelry and coins."
        }
    }
]

score = 0

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def ask_question(q):
    clear()
    print(f"{q['question']}\n")
    for option in q["options"]:
        print(option)
    answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
    if answer in q["facts"]:
        print(f"\nFun Fact: {q['facts'][answer]}")
    return answer
    
for idx, question in enumerate(questions, 1):
    user_answer = ask_question(question)
    if user_answer == question["correct"]:
        print(f"\n{question['feedback']}")
        score += 1
    else:
        print(f"\nNot correct. The correct answer was {question['correct']}.")
        print(f"Fun Fact: {question['facts'][question['correct']]}")
        
    input("\nPress Enter to continue...")

clear()
print(f"Game Over! Your final score is {score} out of {len(questions)}.\n")

if score == len(questions):
    print("Excellent work! You're a trivia master!")
elif score >= len(questions) // 2:
    print("Good job! Keep practicing to improve.")
else:
    print("Better luck next time!")