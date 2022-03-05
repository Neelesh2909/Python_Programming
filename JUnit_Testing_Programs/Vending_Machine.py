notes = [1000,500,100,50,10,5,2,1]

def calculate_notes(amount,notes):
    total_notes = 0
    remaining_amount = 0
    if(amount ==0):
        return False
    else:
        for note_index in range(len(notes)):
            if amount >= notes[note_index]:
                # no_of_notes = amount//notes[note_index]
                # remaining_amount = amount%notes[note_index]
                no_of_notes,remaining_amount = divmod(amount,notes[note_index])
                amount = remaining_amount
                total_notes += no_of_notes
                print(f"There are {no_of_notes} Rs{notes[note_index]} notes")
            else:
                continue
        return total_notes


amount = int(input("Enter the amount here : "))
total_notes = calculate_notes(amount,notes)
print("Minimum number of notes needed to given as change:",total_notes)

