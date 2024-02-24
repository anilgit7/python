with open("story.txt","r") as f:
    story=f.read()

t_start="<"
t_end=">"
start=-1
words=set()

for i, char in enumerate(story):
    if char== t_start:
        start=i
    
    if char==t_end and start!=-1:
        word= story[start:i+1] #slicing
        words.add(word)
        start=-1

answers={}
for word in words:
    answer= input("enter a word for"+word)
    answers[word]=answer

for word in words:
    story=story.replace(word,answers[word])

print(story)