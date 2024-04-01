# lists with objects

from Question_Manager import Question_Manager

questions = [
    "How big is the Dunwoody campus?\n(a) 5 acres\n(b) 10 acres\n(c) 15 acres\n(d) 20 acres\n\n",
    "What year was Dunwoody founded?\n(a) 1902\n(b) 1914\n(c) 1936\n(d) 1974\n\n",
    "Dunwoody merged with Northwestern Electronics Institute (NEI) in which year?\n(a) 2003\n(b) 2010\n(c) 2015\n(d) 2020\n\n",
    "What is the name of the highschool that Dunwoody sponsored in 2007?\n(a) Dunwoody High school\n(b) Dunwoody Academy\n(c) Dunwoody High School of Technology\n(d) Dunwoody Educational Institute\n\n",
    "Which country has Dunwoody had overseas programs in?\n(a) Jamaica\n(b) Libya\n(c) Indonesia\n(d) All of the above\n\n",
    "During what year was an agreement signed between the University of Minnesota and Dunwoody?\n(a) 1918\n(b) 1932\n(c) 1920\n(d) 1954\n\n",
    "The Ford Foundation gave Dunwoody a grant in what year?\n(a) 1940\n(b) 1920\n(c) 1972\n(d) 1953\n\n",
    "Who is the current president of Dunwoody?\n(a) Scott Stallman\n(b) Rich Wagner\n(c) William Dunwoody\n(d) Milton Towner\n\n",
    "What year did the first Dunwoody buildings open?\n(a) 1914\n(b) 1915\n(c) 1916\n(d) 1917\n\n",
    "When was the agreement between Dunwoody and the U of M terminated?\n(a) 1940\n(b) 1982\n(c) 2000\n(d) 2010\n\n"
]

answers = [
    Question_Manager(questions[0], "c"),
    Question_Manager(questions[1], "b"),
    Question_Manager(questions[2], "a"),
    Question_Manager(questions[3], "b"),
    Question_Manager(questions[4], "d"),
    Question_Manager(questions[5], "c"),
    Question_Manager(questions[6], "d"),
    Question_Manager(questions[7], "b"),
    Question_Manager(questions[8], "d"),
    Question_Manager(questions[9], "c")
]

print(Question_Manager.run_test(answers))