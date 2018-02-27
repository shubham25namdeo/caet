
def find_longest_word(wordlist):
    maxlen=len(wordlist[0])
    maxword=wordlist[0]
    for i in wordlist:
        if (len(i)>maxlen):
            maxword=i
            maxlen=len(i)

    return maxword

print(find_longest_word(["abc","efhregb","12sdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdfsdf","sfjbefhhbdghbeeg","efjewfgefhgefhefwefhbwefhwef"]))
