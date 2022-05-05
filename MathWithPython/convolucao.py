def conv(InitS, GradPerc):
    ''' This function takes 2 lists and returns the convolution between them'''
    
    convList = [0,0,0] #Iniciates convList to avoid an index error in convolution loop, in the case of 4 elements 
    GraduatedStudents = []

    for j in range(len(InitS)+len(GradPerc)-1): #Adds the elements of convList

        if j < len(InitS): #Adds the elements of the new Students list, creating a reverse convList
            convList.insert(0,InitS[j])
        else: #When finishes the new Students list, adds Zero to connList to auxiliate in convolution
            convList.insert(0,0)
        A = 0

        for i in range (len(GradPerc)):
            A += convList[i] * GradPerc[i]
            ''' Multiplicates convlist e sum each element passing by percent of graduated students list'''
        GraduatedStudents.append(A)

    return GraduatedStudents

def printTable(GradList, year=2009):
    '''This function receives a list of graduated students and prints a table with the year and
       how many students graduated that year, starting a course in 2005 and finishing in 2009's
       beginning by default'''
    
    print("\t Year \t Graduated")
    
    for i in GradList:
        print("\t",year,"\t",i)
        year +=1
        

#Number of studentes starting a new course in the university
InitialNumberStudents = [400,600,500,300,100,500,200,300,600]
#Percent of students who finishes a course in [4, 5, 6, 7] years
GraduatedPercPerYear = [0.5,0.3,0.1,0.05]

GradStudents = conv(InitialNumberStudents,GraduatedPercPerYear)
printTable (GradStudents)

