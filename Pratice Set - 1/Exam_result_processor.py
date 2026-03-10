m1 , m2, m3 , m4, m5 = map(int , input("Enter marks: ").split())

#check fail condition 
if m1 < 35 or m2 < 35 or m3 < 35 or m4 < 35 or m5 < 35:
    print("FAIL")
else:
    avg = (m1 + m2 + m3 + m4 + m5) / 5

    if avg >= 75:
        print("DISTINCTION")
    else:
        print("PASS")