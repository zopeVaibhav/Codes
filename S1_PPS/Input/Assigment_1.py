days  = float (input("Enter No of Days Present: "))
wages = float (input("Enter wages per Day: ")) 
basic = wages*days;
HRA   = basic*0.1
DA    = basic*0.05
PF    = basic*0.12
netsalary = basic + HRA + DA - PF;
print("Net Salary",netsalary)
print("HRA",HRA)
print("DA",DA)
print("PF",PF)