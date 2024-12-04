AYESHA_AGE = 16
ZARA_AGE = 25
NOOR_AGE = 48

def main():
    """
    Prompts the user for their age and checks if they are eligible to vote in 
    Ayesha, zara, or Noor based on their respective voting ages.
    """

    user_age = int(input("How old are you? "))

    if user_age >= AYESHA_AGE:
        print(f"You can vote in Ayesha where the voting age is {AYESHA_AGE}.")
    else:
        print(f"You cannot vote in Ayesha where the voting age is {AYESHA_AGE}.")
    
    if user_age >= ZARA_AGE:
        print(f"You can vote in Zara where the voting age is {ZARA_AGE}.")
    else:
        print(f"You cannot vote in Zara where the voting age is {ZARA_AGE}.")
    
    if user_age >= NOOR_AGE:
        print(f"You can vote in Noor where the voting age is {NOOR_AGE}.")
    else:
        print(f"You cannot vote in Noor where the voting age is {NOOR_AGE}.")
if __name__ == '__main__':
    main()