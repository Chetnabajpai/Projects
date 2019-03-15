def send(x):
    if (x==1):
        print("""
    ____________
    |          |
    |          |
    |    o     |
    |          |
    '----------'
    """)
    elif(x==2):
        print("""
    ____________
    |          |
    | o        |
    |          |
    |       o  |
    '----------'
    """)
    elif(x==3):
        print("""
    ____________
    |          |
    |  o       |
    |     o    |
    |        o |
    '----------'
    """)
    elif(x==4):
        print("""
    ____________
    |          |
    |  o   o   |
    |          |
    |  o   o   |
    '----------'
    """)
    elif(x==5):
        print("""
    ____________
    |          |
    | o     o  |
    |    o     |
    | o     o  |
    '----------'
    """)
    elif(x==6):
        print("""
    ____________
    |          |
    | o  o  o  |
    |          |
    | o  o  o  |
    '----------'
    """)

if __name__=='__main__':
    import random
    print(" Hi! So you're in a mood to roll today? We got your back!")
    exit=False
    enter=(input(("Press Enter to Roll (or) Type 'Exit' to Close.\n\n")).lower())
    count=0

    if (enter=="exit"):
        exit=True

    while(enter=="" or not exit):
        dice_number=random.randint(1,6)
        count = count + 1
        print(f"{count}>You got a {dice_number}")
        send(dice_number)
        enter=(input("Press Enter to Roll Again! \n").lower())

        if (enter=="exit"):
            exit=True

        else:
            print("\n")
            continue
