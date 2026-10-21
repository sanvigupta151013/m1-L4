amount = int(input("Enter the amount to withdraw: "))
note3 = 0
note2 = 0
note1 = amount // 500
print("Number of 500 rupee notes:", note1)

if amount % 500 != 0:
    amount = amount % 500
    note2 = amount // 200
    print("Number of 200 rupee notes:", note2)

if amount % 200 != 0:
    amount = amount % 200
    note3 = amount // 100
    print("Number of 100 rupee notes:", note3)

sum = (note1 + note2 + note3)
print("Total number of notes:", sum)
