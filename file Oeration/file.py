varName = "Kamor"

# open(varName+".txt", 'a')
# open(varName+".pdf", 'a')
# open(varName+".docx", 'a')
# open(varName+".jpg", 'a')
# open(varName+".png", 'a')
# open(varName+".exe", 'a')
# open(varName+".html", 'a')

# myHtml = open("Kamor.txt", "r")
# print(myHtml.read())

f = open(varName+".txt", "a")
f.write("Start Writing")
f.close()

# open and read the file after the appending:
f = open(varName+".txt", "r")
print(f.read())
