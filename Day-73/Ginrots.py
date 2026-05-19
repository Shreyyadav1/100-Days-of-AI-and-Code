# Step 1: Read input string
s = input()

# Step 2: Custom sorting
# Priority:
# lowercase -> uppercase -> odd digits -> even digits

result = sorted(

    s,

    key=lambda x: (

        # Digits come after letters
        x.isdigit(),

        # Even digits come after odd digits
        x.isdigit() and int(x) % 2 == 0,

        # Uppercase comes after lowercase
        x.isupper(),

        # Finally sort naturally
        x
    )
)

# Step 3: Print final string
print("".join(result))