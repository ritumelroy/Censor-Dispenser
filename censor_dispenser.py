""" 
Completed by Ritu Melroy, January 2020
Cesnsors the list of words from the given emails. The word length is kept but each word is replaced by "X".
Censor One: Censors a phrase out. 
Censor Two: Censors a list of words out. 
Censor Three: Censors any occurance of a word from the “negative words” list after any “negative” word has occurred twice, as well as censoring everything from the list from the previous step as well and use it to censor email_three. 
Censor Four: Censors not only all of the words from the negative_words and proprietary_terms lists, but also censor any words in email_four that come before AND after a term from those two lists.
Project prompt and input emails provided by Codecademy (this is a challenge project not a step-by-step one).
"""


email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def censor_one(email, phrase):
    x = email.replace(phrase, "XXXXX")
    return x


def censor_two(email, list_of_words):
    new_list = [word.title() for word in list_of_words]
    final = list_of_words + new_list

    new_email = []
    list_email = email.split("\n")

    for para in list_email:
        para_words = para.split() 
        #print(para_words)
        #print()
        #new_para = []
        for bad_word in final:
            for i in range(0, len(para_words)):
                if para_words[i] == bad_word:
                    new_word =""
                    for char in bad_word:
                        new_word+="X"
                    para_words.remove(bad_word)
                    para_words.insert(i, new_word)
        para = " ".join(para_words)
        new_email.append(para)

    final_email = "\n".join(new_email)
    
    for word in final:
        if " " in word :
            if word in final_email:
                new_word =""
                for char in word:
                    new_word+="X"
                final_email = final_email.replace(word, new_word)
    return final_email


def censor_three(email, proprietary_terms, negative_words):
    n_email = censor_two(email, proprietary_terms)
    
    list_email = n_email.split("\n")
    list_all_words =[]
    for para in list_email:
        para_words = para.split() 
        list_all_words += para_words
    
    cnt =0
    
    index =0
    for i in range(0, len(list_all_words)):
        if list_all_words[i] in negative_words:
            cnt+=1
            
            if cnt>2:
                index = i
                
                break
    rest_list = list_all_words[i:]
    list_all_words = list_all_words[:i]
    
    rest_str = " ".join(rest_list)
    x = censor_two(rest_str, negative_words)

    rest_list = x.split()
    list_all_words.extend(rest_list)
    return " ".join(list_all_words)

def censor_four(email, proprietary_terms, negative_words):
    n_email = censor_three(email, proprietary_terms, negative_words)
    
    list_all_words = n_email.split()
    all_ind = []
    for i in range(0, len(list_all_words)):
        if "XX" in list_all_words[i]:
            all_ind+= [i]

    for idx in all_ind:
        #before
        before_word = list_all_words[idx-1]

        n_word = ""
        for i in before_word:
            n_word += "X"
        del list_all_words[idx-1]
        list_all_words.insert(idx-1, n_word)

        #after
        after_word = list_all_words[idx+1]
        n2_word = ""
        for i in after_word:
            n2_word += "X"
        del list_all_words[idx+1]
        list_all_words.insert(idx+1, n2_word)
    return " ".join(list_all_words)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable" ]

print()
x = censor_four(email_four, proprietary_terms, negative_words) #or change to test other three emails.
print(x)