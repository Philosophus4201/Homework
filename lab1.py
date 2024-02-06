class Pupa:
    salary_count = 0
    def take_salary(self, salary):
        self.salary_count += salary
    def do_work(self, s1, s2):
        # при s1 > s2,s2 дополняется 0 до длины s1
        print( [s1[i]+s2[i] for i in range(min(len(s1),len(s2)))] + max(s1,s2)[min(len(s1),len(s2)):] )

class Lupa:
    salary_count = 0
    def take_salary(self, salary):
        self.salary_count += salary
    def do_work(self, s1, s2):
        # при s1 > s2,s2 дополняется 0 до длины s1
        print( [s1[i]-s2[i] for i in range(min(len(s1),len(s2)))] + (s1[len(s2):] if len(s1)>len(s2) else [-1*j for j in s2[len(s1):]]))
class Accountant:
    def give_salary(self, worker, salary):
        worker.take_salary(salary)
