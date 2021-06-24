class Subject(object):
    def __init__(self,sub_name,TH_max_marks = None,PR_max_marks = None):
        self.subject_name    = sub_name
        self.TH_max_marks    = TH_max_marks
        self.PR_max_marks    = PR_max_marks


# Sem 1
sem1_sub_details = {
    704111 : Subject("Engineering Physics",100,25),
    704112 : Subject("Engineering Chemistry",100,25),
    704113 : Subject("Engineering Mathematics-I",100,25),
    704114 : Subject("Applied Mechanics",100,25),
    704115 : Subject("Basic Electrical Engineering",100,25),
    704116 : Subject("Basic Mechanical Engineering",100,25),
    704117 : Subject("Communication Skills",25,25),
    704118 : Subject("Workshop Practice",None,25)
}

# Sem 2
sem2_sub_details = {
    704121 : Subject("Engineering Physics",100,25),
    704122 : Subject("Engineering Chemistry",100,25),
    704123 : Subject("Engineering Mathematics-II",100,25),
    704124 : Subject("Engineering Graphics",100,25),
    704125 : Subject("Basic Civil Engineering",100,25),
    704126 : Subject("Computer Programming",None,25),
    704127 : Subject("Basic Electronics",50,25),
    704128 : Subject("Professional Communication",25,25),
    704129 : Subject("Audit Course-Workshop for Skill",None,1)
}

# Sem 3
sem3_sub_details = {
    7047211 : Subject("Engineering Mathematics-III",125,None),
    7047212 : Subject("Electronics Circuit Analysis and Design-I",100,75),
    7047213 : Subject("Network Theory & Analysis",100,25),
    7047214 : Subject("Digital Techniques",100,75),
    7047215 : Subject("Analog Communication",100,75),
    7047216 : Subject("Electronic Software Lab-I",None,50),
}

# Sem 4
sem4_sub_details = {
    7047221 : Subject("Electronics Circuit Analysis and Design-II",100,75),
    7047222 : Subject("Data Structure",100,75),
    7047223 : Subject("Control Systems",100,25),
    7047224 : Subject("Linear Integrated Circuits",100,75),
    7047225 : Subject("Signals and Systems",125),
    7047226 : Subject("Electronic Software Lab-II",None,50),
    "ENG2016": Subject("Environmental Studies",70,None)
}

# Sem 5
sem5_sub_details = {
    7047311 : Subject("Electro Magnetic Engg.& Radiating System",100,25),
    7047312 : Subject("Principles of Digital Communication",100,75),
    7047313 : Subject("Digital Signal Processing",100,50),
    7047314 : Subject("Microcontroller-I",100,75),
    7047315 : Subject("Software Engineering & Project Management System",100,None),
    7047316 : Subject("Electronics Software Lab-III",None,50),
    70401 : Subject("NPTEL Course",50,None)
}

# Sem 6
sem6_sub_details = {
    7047321 : Subject("Radar & Microwave Engineering",100,25),
    7047322 : Subject("Microcontroller-II(PIC)",100,75),
    7047323 : Subject("Electronics Applications & System Design",100,75),
    7047324 : Subject("Optical Communication",100,50),
    7047325 : Subject("Mobile Communication",125,25),
    7047326 : Subject("Mini Hardware Project",None,25),
}