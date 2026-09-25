#Character Frequency with Time complexity o(n) where we find every frequency of character present in the text.
text=input("Enter a text: ")
freq={}
for ch in text:
    freq[ch]=freq.get(ch,0)+1
print(freq)