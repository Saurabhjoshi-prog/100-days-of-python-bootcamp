class QuizBrain:
    def __init__(self,questions_list):
        self.question=0
        self.score=0
        self.questions_list=questions_list
    def still_has_questions(self):
        return self.question+1<=len(self.questions_list)
    def next_question(self):
        a=self.questions_list[self.question]
        self.question+=1
        b=input(f"Q.{self.question}:{a.text}True/False")
        self.check_answer(b,a.answer)
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1

            print("Correct")
        else:
            print("Wrong")
        print(f"the right answer was{correct_answer}")
        print(f"your current score is {self.score}/{self.question}")
        print("\n")




