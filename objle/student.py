class Student(object):
    def __init__(self,name,score,age):
        self.name=name
        self.score=score
        self.__age=age

    def print_score(self):
        print('%s:%s'%(self.name,self.score))

    def get_grade(self):
        if self.score>90:
            return 'A'
        elif self.score<60:
            return 'C'
        else:
            return 'B'



    def get_age(self):
        return self.__age


