def compute_triplets(integer_list):
    no_of_triplets = 0
    print(f"The Triplets are : ",end="")
    for i in range(len(integer_list)):
        for j in range(i+1,len(integer_list)):
            for k in range(j+1,len(integer_list)):
                if integer_list[i]+integer_list[j]+integer_list[k]==0:
                    print(f"({integer_list[i]},{integer_list[j]},{integer_list[k]}), ",end="")
                    no_of_triplets +=1
    return no_of_triplets


number_of_integers = int(input("Enter the number of integers required : "))
integer_list = []
print(f"Enter the {number_of_integers} required integers: ")
for i in range(number_of_integers):
    value_entered = int(input())
    integer_list.append(value_entered)



triplets = compute_triplets(integer_list)
if(triplets > 0):
    print(f"\n The total number of triplets are : {triplets}")
else:
    print("\nThere were no triplets found")
