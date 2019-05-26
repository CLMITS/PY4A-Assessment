class Foraverage :
    passing = 70
    def __init__(self, full_name,s1,sc1,s2,sc2,s3,sc3,s4,sc4,s5,sc5):
        self.full_name = full_name
        self.s1 = s1
        self.sc1 = sc1
        self.s2 = s2
        self.sc2 = sc2
        self.s3 = s3
        self.sc3 = sc3
        self.s4 = s4
        self.sc4 = sc4
        self.s5 = s5
        self.sc5 = sc5
    def total_avg(self):
        self.tsum = self.sc1 + self.sc2 + self.sc3 + self.sc4 + self.sc5
        self.tavg = (self.tsum/500)*100
        if self.tavg<self.passing :
            print("\nYou've Failed")
        else :
            print("\nYou've Passed")
        return self.tavg
    def set_pass(cls, amount):
        cls.passing = amount    
    
p1 = int(input("\n\nPlease input your passing average score: "))
Foraverage.set_pass(Foraverage,p1)
n1 = input("\nWhat is your Full Name? : ")

v1 = int(input("What is your average in English? : "))
v2 = int(input("What is your average in Math? : "))
v3 = int(input("What is your average in Filipino? : "))
v4 = int(input("What is your average in Science? : "))
v5 = int(input("What is your average in History? : "))

subj_1 = Foraverage(n1,"English",v1,"Mathematics",v2,"Filipino",v3,"Science",v4,"History",v5)

print("\n"+subj_1.full_name)
print("",subj_1.s1,"\t",subj_1.sc1)
print("",subj_1.s2,"\t",subj_1.sc2)
print("",subj_1.s3,"\t",subj_1.sc3)
print("",subj_1.s4,"\t",subj_1.sc4)
print("",subj_1.s5,"\t",subj_1.sc5)
print("The average score you've got is:",Foraverage.total_avg(subj_1))
