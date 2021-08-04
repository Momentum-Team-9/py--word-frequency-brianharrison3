#open file
with open("one-today.txt") as one_today:
#replace /n
    lines = one_today.read().replace('\n', ' ')
#lowercase
    lines = lines.lower()
#replace punctution
    punctuation = ['.' , ',' , ':', "'" , '"']
    for occurance in punctuation:
        lines = lines.replace(occurance,"")
#replace stop words
    STOP_WORDS = [
    '—', ' an ', ' and ', ' are ', ' as ', ' at ', ' be ', ' by ', ' for ', ' from ', ' has ', ' he ',
    ' i ', ' in ', ' is ', ' it ', ' its ', ' of ', ' on ', ' that ', ' the ', ' to ', ' were ',
    ' will ' , ' with ' , ' a ' ]
    for word in STOP_WORDS:
        lines = lines.replace(word," ")
#string into list
    def Convert(text):
        list_poem = list(text.split(" "))   
        return list_poem 
    lines = Convert(lines)

   



#wordcount
    wordcount = {};
#get rid of empty spaces
    empty = [" ", '', '']
    for word in lines:
        if word in empty:
            lines.remove(word)
#print words
    for single_word in lines: 
        wordcount[single_word] = wordcount.get(single_word, 0) + 1
        
        print(wordcount[single_word], single_word)
    #print(sorted(wordcount.items(), key=lambda seq: seq[0]))
        


