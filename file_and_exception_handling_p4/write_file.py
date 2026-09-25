#Writes over existin data.
with open("data.txt","w") as file:
    file.write("How are you")

#Appends the data written in text file.
with open("data.txt","a") as file:
    file.write("\nGreat to hear")