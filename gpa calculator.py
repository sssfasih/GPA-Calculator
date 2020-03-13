# Designed By Syed Fasih Uddin

print(f"            GPA CALCULATOR")
print(f"     Designed By Syed Fasih Uddin \n ")

class Subject():
    def __init__(self, name, credit):
        self.name = name
        self.credit = credit
        # print("Name Assigned:", self.name)

        # Calculation of GP During Semester when Full Student portal is not Updated (Created for later use)

    def dividedcalc(self, q1, q2, q3, q4, q5, a1, a2, md, maxmarks):
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.a1 = a1
        self.a2 = a2
        self.md = md
        self.maxmarks = maxmarks
        self.perc = ((q1 + q2 + q3 + q4 + q5 + a1 + a2 + md) / maxmarks) * 100
        print(f"Percentage in {self.name} = {self.perc}%")

        # When Full Student Portal is updated ; by Default Max Marks = 40

    def quickcalc(self, obtained):
        self.obtained = obtained
        self.perc = (obtained / 40) * 100
        print(f"Percentage in {self.name} = {self.perc}%")

        # CALCULATING Grade Point Per Subject According to Prospectus

    def GP(self):
        if self.perc > 100:
            raise ("Abay Alien % 100 se ziada kese agyi")
        elif self.perc == 100:
            raise ("100% Masha Allah top karoge")
        elif self.perc < 100 and self.perc >= 94:
            gp = 4.0
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        elif self.perc < 94 and self.perc >= 85:
            gp = 4.0
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        elif self.perc < 85 and self.perc >= 80:
            gp = 3.7
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        elif self.perc < 80 and self.perc >= 75:
            gp = 3.4
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        elif self.perc < 75 and self.perc >= 70:
            gp = 3.0
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        elif self.perc < 70 and self.perc >= 67:
            gp = 2.7
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        elif self.perc < 67 and self.perc >= 64:
            gp = 2.4
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        elif self.perc < 64 and self.perc >= 60:
            gp = 2.0
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        elif self.perc < 60 and self.perc >= 57:
            gp = 1.7
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        elif self.perc < 57 and self.perc >= 54:
            gp = 1.4
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        elif self.perc < 54 and self.perc >= 50:
            gp = 1.0
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"{self.name} GP = {gp}")
        else:
            gp = 0
            SubGPs.append(gp)
            SubCredits.append(self.credit)
            print(f"F Grade in {self.name} \n You can't Give Up!, Try Again")


SubGPs = []
SubCredits = []


# Final GPA Calculator that takes all subjects GPs and Credit hours
# Forumla = Sum of all ( credit hour * total of GP ) / total of credit hours

def GPA():
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
    print(f"            GPA CALCULATOR")
    print(f"     Designed By Syed Fasih Uddin \n ")

    print(f"Nominator = {Nominator}    Total Credit Hours = {TotalCredits}")
    print(f'     Your Semester GPA: {GPA:3.4f}')
    print(f"\n             You can do even better!")

    input("Press Enter To Continue")


####################################   How To Use   ########################################################
'''
Format : Variable = Subject( " Subject Name " , Credit Hours )

If 
Full Student Portal is not Updated Use Divided Calculator
Format: Variable.dividedcalc( Quiz 1, Quiz 2,Quiz 3,Quiz 4,Quiz 5,Assign 1,Assign 2,Mid Term,Max Marks Till Now )
 
ELSE    USE Quick Calculator (Default Max Marks is set to 40 )
Format : Variable.quickcalc(Total Obtained Marks)

Finding Grade Point of Subject
Format: Variable.GP()

When All Subjects GPs are calculated, Use GPA() Function to Calculate Semester GPA till now


Step 1 : Define Subject 
Step 2 : Calculate Each Subject
Step 3 : Calculate GP of EacH Subject
Step 4 : Calculate Final GPA

'''
########################################################################################################

ICT = Subject("ICT", 3)
ICT.quickcalc(32.5)
# ICT.dividedcalc(1.5, 1.5, 1, 1, 1.5, 4.5, 4.5, 17,40)
ICT.GP()

PF = Subject("Programming Fundamentals", 3)
PF.quickcalc(30.25)
PF.GP()

GPA()
