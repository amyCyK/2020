
def main():
    print('''
Enter one of the following:
       1 to print the contents of input data file")
       2 to print all valid input data")
       3 to print all students overall mark")
       4 to print all students whose mark less than 40")
       5 to plot distribution of grade
       Q to end
       ''')    
    Instruction=int(input("Enter 1 to 5"))
    if Instruction == 1:
        item1()
    elif Instruction == 2:
        item2()
    elif Instruction == 3:
        item3()
    elif Instruction == 4:
        item4()
    elif Instruction == 5:
        item5()
    elif Instruction == "Q":
        exit()

def item1():
    print('''
50123456_lam tai man_85.5_80.0_80.0_90.0
50223456_li tai man_61.0_90.5_60.0_55.5
50323456_wong tai man_90.0_30.0_50.0_79.5
50423456_ng tai man_62.75_70.0_65.5_48.5
50523456_lau tai man_58.0_62.4_86.55_70.0
50623456_chui tai man_31.0_64.5_46.0_29.5
50723456_lim tai man_86.45_60.0_88.5_89.5
50823456_pok tai man_53.0_35.50_75.5_49.5
50923456_kim tai man_58.25_80.0_36.0_56.5
50023456_tsang tai man_35.5_20.0_55.5_79.0
50713456_lee tai man_26.45_30.0_35.5_30.5
50813456_po tai man_23.0_35.50_25.5_29.5
50913456_yim tai man_18.25_40.0_36.0_26.5
50013456_tse tai man_5.5_20.0_5.5_9.0''')
    main()


#main routine
main()





