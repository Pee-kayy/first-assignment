#in these tasks, i was able to use my knowledge of inbuilt functions such as(input(), min(), max(), float())
#  then methods such as  (.max .min .sort .append .remove) and data structures(list and set)


#1 and 3 cause it takes inputs and also adds element to the end of the list 
user_inputs = []
# NUM_INPUTS = 6
print("\n--- Step 1: Collecting Initial 5 Inputs (No Loop) ---")

user_inputs.append(input("Enter input #1 of 5 (try entering a duplicate!): "))
user_inputs.append(input("Enter input #2 of 5 (try entering a duplicate!): "))
user_inputs.append(input("Enter input #3 of 5 (try entering a duplicate!): "))
user_inputs.append(input("Enter input #4 of 5 (try entering a duplicate!): "))
user_inputs.append(input("Enter input #5 of 5 (try entering a duplicate!): "))

print(f"\nInitial List: {user_inputs}")

print("\n Step 2: Removing Duplicates")

# Convert the list to a 'set cause a set is a function that automatically removes duplicates, 
# then convert it back to a list to maintain order.
unique_inputs = list(set(user_inputs))

# step 4 Update the main list reference
user_inputs = unique_inputs

print(f"List after removing duplicates: {user_inputs}")

print("\n--- Step 4: Removing an Element ---")
element_to_remove = input("enter an elemnt to be removed ")
user_inputs.remove(element_to_remove)
print(f"this is your new list after removal {user_inputs}\n")

# sttep 5 print maximum and minimum numbers
maximum = max(user_inputs)
minimum = min(user_inputs)
print(f"based on the current available numbers the manximun number is {maximum} and the minimum number is {minimum} \n")

#step 6 
print("this is step 6 it sorts the list")
user_inputs.sort()
print(f"this is the sorted list {user_inputs}")

