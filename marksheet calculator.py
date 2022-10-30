# Designed By Syed Fasih Uddin

print(f"        UIT GPA CALCULATOR")
print(f"     Designed By Syed Fasih Uddin \n ")

SubGPs = []
SubCredits = []

class Subject():
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit
        # print("Name Assigned:", self.name)

    def quick_grade(self, grade):
        try:
            grade = grade.lower()

            if grade == 'a+':
                gp = 4.0
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            elif grade == 'a':
                gp = 4.0
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            elif grade == 'a-':
                gp = 3.7
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            elif grade == 'b+':
                gp = 3.4
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            elif grade == 'b':
                gp = 3.0
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            elif grade == 'b-':
                gp = 2.7
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            elif grade == 'c+':
                gp = 2.4
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            elif grade == 'c':
                gp = 2.0
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            elif grade == 'c-':
                gp = 1.7
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            elif grade == 'd+':
                gp = 1.4
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            elif grade == 'd':
                gp = 1.0
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"{self.name} GP = {gp}")
            else:
                gp = 0
                SubGPs.append(gp)
                SubCredits.append(self.credit)
                print(f"F Grade in {self.name} \n You can't Give Up!, Try Again")

        except:
            print('INVALID GRADE:only String Accepted')

# Final GPA Calculator that takes all subjects GPs and Credit hours
# Forumla = Sum of all ( credit hour * total of GP ) / total of credit hours

def CGPA():
    Nom = []
    TotalCredits = 0
    Nominator = 0
    for EachCredit in SubCredits:
        TotalCredits -= - EachCredit

    zipper = list(zip(SubGPs, SubCredits))
    for EachSub in zipper:
        multiplier = EachSub[0] * EachSub[1]
        Nom.append(multiplier)
    for Nomin in Nom:
        Nominator -= - Nomin

    GPA = (Nominator) / TotalCredits

    print(f"\n\n\n")
    print(f"        UIT CGPA CALCULATOR")
    print(f"     Designed By Syed Fasih Uddin \n ")

    print(f"Nominator = {Nominator}    Total Credit Hours = {TotalCredits}")
    print(f'     Your Cumulative GPA: {GPA:3.4f}')
    print(f"\n             You can do even better!")

    input("Press Enter To Continue")


####################################   How To Use   #########################################
'''
Format : Variable = Subject( " Subject Name " , Credit Hours )

If 
Full Student Portal is not Updated Use Divided Calculator
Format: Variable.dividedcalc( Quiz 1, Quiz 2,Quiz 3,Quiz 4,Quiz 5,Assign 1,Assign 2,Mid Term,Max Marks Till Now )

ELSE    USE Quick Calculator (Default Max Marks is set to 40 )
Format : Variable.quickcalc(Total Obtained Marks)

Finding Grade Point of Subject
Format: Variable.calc_GP()

When All Subjects GPs are calculated, Use GPA() Function to Calculate Semester GPA till now


Step 1 : Define Subject 
Step 2 : Enter Grade of Subject
Step 3 : Run GPA() Function

'''
######################### ENTER PILOT CODE BELOW ##################################
IST =  Subject("Islamic Studies", 2)
IST.quick_grade('a-')

