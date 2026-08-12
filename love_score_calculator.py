
def true_love_checker (input_word1, input_word2):
    lovers_name = input_word1 + input_word2
    target_list1 = ["t", "r", "u", "e"]
    target_list2 = ["l", "o", "v","e"]

   
# ///////////////////////////this code creates a list of zero's with a len of the respective target_list///////////////////////
    count_list1 = [0] * len(target_list1)
    count_list2 = [0] * len(target_list2)


#   //////////////////////////this check how many times the names appear in the both target_list//////////////////////
    for letter in lovers_name:
        if letter in target_list1:
            index1 = target_list1.index(letter)
            count_list1[index1] += 1

    for letter in lovers_name:
        if letter in target_list2:
            index2 = target_list2.index(letter)
            count_list2[index2] += 1

# ///this are the list of the number of times the lovers name appears in "true and love" based on their index values/////
    appearance_in_true = []
    appearance_in_false  = []


# //this uses the length of "true" and "false" as the range of the loop and a list of the number of times the letter in////
# //////lovers name appears in "true and love" based on their index values is appended to final_result in a tuple////

    for i in range(len(target_list1)):
         appearance_in_true .append((target_list1[i], count_list1[i]))

    for i in range(len(target_list2)):
        appearance_in_false.append((target_list2[i], count_list2[i]))

    final_output = str(sum(count_list1)) + str(sum(count_list2))

    print (appearance_in_true)
    print (appearance_in_false)

    print (count_list1)
    print (count_list2)
    print(final_output)

true_love_checker("Angela Yu", "Jack Bauer")


