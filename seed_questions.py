from app import create_app, db
from app.models import Question

app = create_app()

questions = [
    ("What is the capital of Pakistan?", "Karachi", "Lahore", "Islamabad", "Peshawar", "C"),
    ("Which language is mainly used for web page structure?", "Python", "HTML", "SQL", "Java", "B"),
    ("Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", "C"),
    ("How many days are there in a week?", "5", "6", "7", "8", "C"),
    ("Which is the largest ocean?", "Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean", "C"),
    ("What is the boiling point of water at sea level?", "50°C", "75°C", "100°C", "150°C", "C"),
    ("Which language is used for styling web pages?", "HTML", "CSS", "Python", "SQL", "B"),
    ("What does CPU stand for?", "Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Computer Processing Utility", "A"),
    ("Which device is used to input text into a computer?", "Monitor", "Keyboard", "Speaker", "Printer", "B"),
    ("Which planet is closest to the Sun?", "Earth", "Mars", "Mercury", "Venus", "C"),
    ("How many continents are there?", "5", "6", "7", "8", "C"),
    ("Which animal is known as the King of the Jungle?", "Tiger", "Lion", "Elephant", "Bear", "B"),
    ("What is 10 + 15?", "20", "25", "30", "35", "B"),
    ("Which one is a programming language?", "HTML", "CSS", "Python", "HTTP", "C"),
    ("What does RAM stand for?", "Random Access Memory", "Read Access Memory", "Run Access Module", "Random Application Memory", "A"),
    ("Which country is famous for the Eiffel Tower?", "Italy", "France", "Germany", "Spain", "B"),
    ("How many hours are there in a day?", "12", "18", "24", "36", "C"),
    ("Which is the largest planet in our Solar System?", "Earth", "Mars", "Jupiter", "Saturn", "C"),
    ("What is the opposite of hot?", "Warm", "Cold", "Dry", "Soft", "B"),
    ("Which color is made by mixing red and blue?", "Green", "Orange", "Purple", "Yellow", "C"),
    ("What does SQL mainly work with?", "Images", "Databases", "Videos", "Games", "B"),
    ("Which company developed Windows?", "Apple", "Microsoft", "Google", "Amazon", "B"),
    ("Which language is commonly used for data analysis?", "Python", "HTML", "CSS", "XML", "A"),
    ("What is 5 × 6?", "20", "25", "30", "35", "C"),
    ("Which organ pumps blood through the human body?", "Brain", "Heart", "Lung", "Kidney", "B"),
    ("How many months are there in a year?", "10", "11", "12", "13", "C"),
    ("Which is the fastest land animal?", "Lion", "Horse", "Cheetah", "Tiger", "C"),
    ("What does URL stand for?", "Uniform Resource Locator", "Universal Read Link", "User Resource Link", "Uniform Read Locator", "A"),
    ("Which one is an operating system?", "Python", "Linux", "HTML", "SQL", "B"),
    ("Which planet do humans live on?", "Mars", "Venus", "Earth", "Jupiter", "C"),
    ("What is 100 ÷ 10?", "5", "10", "15", "20", "B"),
    ("Which instrument is used to measure temperature?", "Barometer", "Thermometer", "Speedometer", "Compass", "B"),
    ("Which gas do humans need for breathing?", "Carbon Dioxide", "Oxygen", "Nitrogen", "Hydrogen", "B"),
    ("Which is the smallest prime number?", "0", "1", "2", "3", "C"),
    ("What does AI stand for?", "Automated Internet", "Artificial Intelligence", "Advanced Internet", "Automatic Information", "B"),
    ("Which protocol is commonly used for secure websites?", "HTTP", "FTP", "HTTPS", "SMTP", "C"),
    ("How many sides does a triangle have?", "2", "3", "4", "5", "B"),
    ("Which database is commonly used with Flask for small projects?", "SQLite", "Photoshop", "Excel", "PowerPoint", "A"),
    ("What is the file extension for a Python file?", ".html", ".css", ".py", ".js", "C"),
    ("Which technology is used to create dynamic HTML pages with Flask?", "Jinja2", "NumPy", "Pandas", "Matplotlib", "A")
]

with app.app_context():

    for item in questions:

        new_question = Question(
            question=item[0],
            option_a=item[1],
            option_b=item[2],
            option_c=item[3],
            option_d=item[4],
            correct_answer=item[5]
        )

        db.session.add(new_question)

    db.session.commit()

    print("40 questions added successfully!")