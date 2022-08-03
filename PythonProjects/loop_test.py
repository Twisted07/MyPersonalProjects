while True:
    try:
        data = float(input("\nHow much is in your account?\n"))
        break
    except ValueError:
        data = print("\nInvalid input. Input digits only.\n")
print(f"Your account balance is {data}")