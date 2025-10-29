answers = {
		0 : "A",
		1 : "B",
		2 : "B",
		3 : "A", 
		4 : "C",
		5 : "A",
		6 : "B", 
		7 : "C",
		8 : "A",  
		9 : "A",
	}

questions = ["Who parted the Red Sea?", "Which king had a whole choir defeat armies?", "God told Jonah to go to…?", "Which disciple walked on water briefly?", "Jesus fed 5,000 with…", "Who denied Jesus 3 times?", "The Lord is my Shepherd… is Psalm…", "I can do all things through Christ…", "Where is “Faith without works is dead”?", "What did Jesus say on the Cross?"]

options = ["A Moses B Elijah C Aquaman D Noah", "A David B Jehoshaphat C Nebuchadnezzar D Beyoncé", "A Nigeria B Nineveh C Starbucks D Jerusalem", "A Peter B Judas C James D Paul", "A Pizza + Coke B Water + Salt C 5 loaves + 2 fish D 12 loaves + 12 fish", "A Peter B John C Simon the Zealot D That soldier with bad breath", "A 1 B 23 C 119 D 91", "A Proverbs 31:10 B Genesis 1:1 C Philippians 4:13 D Ezekiel 37:10", "A James B Hebrews C Matthew D Revelation", "A 'It is finished' B 'BRB' C 'Give me Fanta' D 'Take me to your leader'"]



def get_question(choice):
	question = questions[choice]
	return question

def get_option(choice):
	option = options[choice]
	return option

def compare_answer(count,choice,answer):
	if answers[choice] == answer.upper():
		return "Correct!"
	else:
		return"Sorry, maybe next time!"
def increase_score(count,choice,answer):
	if answers[choice] == answer.upper():
		count += 1
	return count

def final_score(count):
	return count