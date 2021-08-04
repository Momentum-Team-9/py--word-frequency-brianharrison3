lines = "hello world Chas,e  Coding is hard"
punctuation = ['.' , ',' , ':', "'" , '"']
for occurance in punctuation:
    lines = lines.replace(occurance,"")
print(lines)
