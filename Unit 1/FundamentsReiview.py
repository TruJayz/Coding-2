 # Jalen Townsend

 def discount():
    itemPrice = input("please enter the iteam price")
    if itemPrice >= 50 or itemPrice <=75:
        discount = .15
        sum = itemPrice - sum
        print("this is your final total" + str(total))
    elif itemPrice > 75:
        discount = .25
        sum = itemPrice - sum
        print(sum)
        print("this is your final total" + str(total))
    else:
        print("sorry, you do not get a discount.")

    discount()
