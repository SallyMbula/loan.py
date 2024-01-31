def main():
  # prompt the user for their age
  age = int(input("please enter your age: "))
  # prompt the user for their annual income
  income = int(input("please enter your annual income: "))
  # check if the user is eligible for a loan
  if age >= 21 and income >= 21000:
    print("congratulations, you qualify for a loan")
  else:
    if age < 21:
      print("unfortunately, we're unable to offer you a loan at this time")


if __name__ == "__main__":
  main()
