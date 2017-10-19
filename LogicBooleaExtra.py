
##           Math   Calc  Hist   Eng   PubSp  Art  Legal  Cyber  Acct  Credit
b_record  = [False, True, True, True, False, False, False, True, False, 60]
a_record  = [False, True, True, False, True, False, True, True, False, 75]
c_record  = [True, False, True, True, True, False, False, False, False, 54]


#for x in a_record:
#    print(x)
    
Math = a_record[0]
Calc = a_record[1]
Hist = a_record[2]
Eng = a_record[3]
PubSp = a_record[4]
Art = a_record[5]
Legal = a_record[6]
Cyber = a_record[7]
Acct = a_record[8]
Credit = a_record[9]

##General Education completed?
if (Math or Calc) and Hist and (Eng or PubSp):
    GenEd = True
    print ("GenEd complete")
else:
    GenEd = False
    print ("GenEd non-complete")
    
##Major completed?
dlbMajor = False
if Art or Legal or Cyber or Acct:
    Major = True
    print ("Major complete")
    if Cyber and Legal:
        dlbMajor = True
else:
    Major = False
    print ("Major non-complete")

##Total credits completed?
dlbCredit = False
if Credit >= 60:
     reqCredit = True
     print ("Credit complete")
     if Credit >= 75:
         dlbCredit = True
else:
    reqCredit = False
    print ("Credits non complete")

##Ready to graduate???
if GenEd and Major and reqCredit:
    print ("Congratuations!  You have met all requirements to graduate.")
    if dlbMajor and dlbCredit:
        print("You will be recieving a double major degree in Cyber and Legal.")
else:
    print ("Unfortunately you have not met all requirements to graduate. Review list above.")





    
