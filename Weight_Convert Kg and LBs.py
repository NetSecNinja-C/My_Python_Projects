Weight = float(input("Weight: "))
K_L = input("Kg or Lbs : ")

if K_L == str("Kg"):
    X = Weight * float(2.20462)
    print("Weight in Lbs : " + str(X))

elif K_L == str("Lbs"):
    Y = Weight / float(2.20462)
    print("Weight in Kg : " + str(Y))

print("Thank You")
