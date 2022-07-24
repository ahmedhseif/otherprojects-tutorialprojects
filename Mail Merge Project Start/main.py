# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("C:/Users/ahmed/PycharmProjects/Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") \
        as name_file:
    names = name_file.readlines()

with open("C:/Users/ahmed/PycharmProjects/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") \
        as starting_letter:
    full_letter = starting_letter.read()


for name in names:
    name = name.strip()
    with open(f"C:/Users/ahmed/PycharmProjects/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt",
              "w") as sample:
        test_sample = sample.write(full_letter.replace("[name]", f"{name}"))

