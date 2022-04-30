def conv(InitS, GradPerc):
    convList = [0,0,0]
    GraduatedStudents = []

    for j in range(len(InitS)+len(GradPerc)-1):

        if j < len(InitS):
            convList.insert(0,InitS[j])
        else:
            convList.insert(0,0)
        A = 0

        for i in range (len(GradPerc)):
            A += convList[i] * GradPerc[i]

        GraduatedStudents.append(A)

    return GraduatedStudents

def printTable(GradList, year=2009):
    print("\t Year \t Graduated")
    
    for i in GradList:
        print("\t",year,"\t",i)
        year +=1
        


InitialNumberStudents = [400,600,500,300,100,500,200,300,600]
GraduatedPercPerYear = [0.5,0.3,0.1,0.05]

GradStudents = conv(InitialNumberStudents,GraduatedPercPerYear)
printTable (GradStudents)

