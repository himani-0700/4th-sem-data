with open("words.txt", "r") as f:
    def three_con_doub_ltr(word):
        for l in range(len(word)-5):
            if word[l] == word[l+1] and word[l+2]==word[l+3] and word[l+4]==word[l+5]:
                return True
        return False
    for word in f:
        if three_con_doub_ltr(word):
            print(word)
          
