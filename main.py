import os
from importxls import ClassData


def main():
    """
    The main function
    :return: void
    """
    filepath = os.getcwd()
    filepath = filepath+"/Mark_Sheet.xlsx"
    ClassMarks = ClassData(filepath)
    print("BEST PERFORMERS")
    MaximumMarksinSDLC(ClassMarks)
    MaximumMarksinPython(ClassMarks)
    MaximumMarksinMBSE(ClassMarks)
    # ClassMarks.printdata()
    # print(ClassMarks.listps())
    print("AVERAGE MARKS")
    averagemarksSDLC(ClassMarks)
    averagemarkspython(ClassMarks)
    averagemarksMBSE(ClassMarks)
    print("POOR PERFORMERS")
    MinimumMarksinMBSE(ClassMarks)
    MinimumMarksinPython(ClassMarks)
    MinimumMarksinSDLC(ClassMarks)
    # ExpectedMarks(ClassMarks)
    MeetingExpectationsinMBSE(ClassMarks)
    MeetingExpectationsinPython(ClassMarks)
    MeetingExpectationsinSDLC(ClassMarks)
    pass



def MaximumMarksinSDLC(ClassMarks):
    """
    it prints the name of the person who scored the maximum marks in SDLC module
    :param ClassMarks: object of ClassData
    :return: Void
    """
    PSnumbers = ClassMarks.listps()
    name = None
    maxmarks = 0
    for i in PSnumbers:
        currMarks = ClassMarks.getmarksbypsSDLC(i)
        if currMarks > maxmarks:
            maxmarks = currMarks
            name = ClassMarks.getname(i)
        else:
            pass
    print(name+" scored maximum marks in SDLC")


# def ExpectedMarks(ClassMarks):
#     """
#     it prints if the student is meeting the required expectations or not
#     :param ClassMarks: object of ClassData
#     :return: Void
#     """
#     PSnumbers = ClassMarks.listps()
#     sname=None
#     Expected=55
#     for exp in PSnumbers:
#         TheMarks = ClassMarks.getmarksbyps(exp)
#         if TheMarks >= Expected:
#             sname=ClassMarks.getname(exp)
#         else:
#             print(sname + "Student is not meeting the required expectations")
#
#     print(sname + "Student is meeting the required expectations")


def MaximumMarksinPython(ClassMarks):
    """
    it prints the name of the person who scored the maximum marks in SDLC module
    :param ClassMarks: object of ClassData
    :return: Void
    """
    PSnumbers = ClassMarks.listps()
    name = None
    maxmarks = 0
    for i in PSnumbers:
        currMarks = ClassMarks.getmarksbypspython(i)
        if currMarks > maxmarks:
            maxmarks = currMarks
            name = ClassMarks.getname(i)
        else:
            pass
    print(name+" scored maximum marks in python")


def MaximumMarksinMBSE(ClassMarks):
    """
    it prints the name of the person who scored the maximum marks in SDLC module
    :param ClassMarks: object of ClassData
    :return: Void
    """
    PSnumbers = ClassMarks.listps()
    name = None
    maxmarks = 0
    for i in PSnumbers:
        currMarks = ClassMarks.getmarksbypsMBSE(i)
        if currMarks > maxmarks:
            maxmarks = currMarks
            name = ClassMarks.getname(i)
        else:
            pass
    print(name+" scored maximum marks in MBSE")


def MinimumMarksinMBSE(ClassMarks):
    """
    it prints the name of the person who scored the maximum marks in SDLC module
    :param ClassMarks: object of ClassData
    :return: Void
    """
    PSnumbers = ClassMarks.listps()
    name = None
    minmarks = 100
    for i in PSnumbers:
        currMarks = ClassMarks.getmarksbypsMBSE(i)
        if currMarks < minmarks:
            minmarks = currMarks
            name = ClassMarks.getname(i)
        else:
            pass
    print(name+" scored minimum marks in MBSE")


def MinimumMarksinPython(ClassMarks):
    """
    it prints the name of the person who scored the maximum marks in SDLC module
    :param ClassMarks: object of ClassData
    :return: Void
    """
    PSnumbers = ClassMarks.listps()
    name = None
    minmarks = 100
    for i in PSnumbers:
        currMarks = ClassMarks.getmarksbypspython(i)
        if currMarks < minmarks:
            minmarks = currMarks
            name = ClassMarks.getname(i)
        else:
            pass
    print(name+" scored minimum marks in Python")


def MinimumMarksinSDLC(ClassMarks):
    """
    it prints the name of the person who scored the maximum marks in SDLC module
    :param ClassMarks: object of ClassData
    :return: Void
    """
    PSnumbers = ClassMarks.listps()
    name = None
    minmarks = 100
    for i in PSnumbers:
        currMarks = ClassMarks.getmarksbypsSDLC(i)
        if currMarks < minmarks:
            minmarks = currMarks
            name = ClassMarks.getname(i)
        else:
            pass
    print(name+" scored minimum marks in SDLC")


def averagemarksSDLC(ClassMarks):

    mylst = ClassMarks.getmarksSDLC()

    avgsdlc = sum(mylst)/len(mylst)
    print(avgsdlc,  " is the average marks of SLDC")


def averagemarkspython(ClassMarks):

    mylst = ClassMarks.getmarksPython()

    avgpython = sum(mylst)/len(mylst)
    print(avgpython , " is the average marks of python")


def averagemarksMBSE(ClassMarks):

    mylst = ClassMarks.getmarksMBSE()

    avgMBSE = sum(mylst)/len(mylst)
    print(avgMBSE , " is the average marks of MBSE")
    
    
def MeetingExpectationsinMBSE(ClassMarks):
    """
    it prints the name of the person meeting expectations or not in MBSE
    :param ClassMarks: object of ClassData
    :return: Void
    """
    PSnumbers = ClassMarks.listps()
    name = None
    for i in PSnumbers:
        currMarks = ClassMarks.getmarksbypsMBSE(i)
        if currMarks > 55:
            name = ClassMarks.getname(i)
            print(name+" is meeting expectations in MBSE")   
        else:
            print(name+" is not meeting expectations in MBSE")
            
            
def MeetingExpectationsinPython(ClassMarks):
    """
    it prints the name of the person meeting expectations or not in Python
    :param ClassMarks: object of ClassData
    :return: Void
    """
    PSnumbers = ClassMarks.listps()
    name = None
    for i in PSnumbers:
        currMarks = ClassMarks.getmarksbypspython(i)
        if currMarks > 55:
            name = ClassMarks.getname(i)
            print(name+" is meeting expectations in Python")
        else:
            print(name+" is meeting expectations in Python")
            
            
 def MeetingExpectationsinSDLC(ClassMarks):
    """
    it prints the name of the person meeting expectations or not in SDLC
    :param ClassMarks: object of ClassData
    :return: Void
    """
    PSnumbers = ClassMarks.listps()
    name = None
    for i in PSnumbers:
        currMarks = ClassMarks.getmarksbypsSDLC(i)
        if currMarks > 55:
            name = ClassMarks.getname(i)
            print(name+" is meeting expectations in SDLC")
        else:
            print(name+" is not meeting expectations in SDLC")

if __name__ == "__main__":
    main()
