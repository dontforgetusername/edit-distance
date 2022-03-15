# Viết chương trình bằng ngôn ngữ Python, sử dụng regular expression, để trích xuất danh sách các email, địa chỉ website, số điện thoại từ văn bản.
# Input: file văn bản, định dạng .txt
# Output: list các tuple có dạng (vị trí bắt đầu, độ dài, email/website/số điện thoại)


import re

def readFile(filename):
    f = open(filename, "r")
    x = f.read()
    return x

#ham tim mail
def getMailAddress(text):
    listTuples = []
    splitAt = 0
    temp = text
    while temp:
        x = re.search(r"\w+@[\w\.]+\w", temp)
        #neu co thi them vao list
        if x:
            start = x.span()[0] + splitAt
            length = x.span()[1] - x.span()[0]
            mail = x.group()
            mailTuple = (start, length, mail)
            listTuples.append(mailTuple)
            splitAt = x.span()[1]
            temp = temp[splitAt:]
        else:
            return listTuples

#ham tim web
def getWebAddress(text):
    listTuples = []
    splitAt = 0
    temp = text
    while temp:
        x = re.search(r"\w+\.[\w\.]*\w+", temp)
        if x:
            start = x.span()[0] + splitAt
            length = x.span()[1] - x.span()[0]
            web = x.group()
            webTuple = (start, length, web)
            listTuples.append(webTuple)
            splitAt = x.span()[1]
            temp = temp[splitAt:]
        else:
            return listTuples

#ham tim sdt
def getPhoneNumber(text):
    listTuples = []
    splitAt = 0
    temp = text
    while temp:
        x = re.search("\d{10}", temp)
        if x:
            start = x.span()[0] + splitAt
            length = x.span()[1] - x.span()[0]
            phone = x.group()
            phoneTuple = (start, length, phone)
            listTuples.append(phoneTuple)
            splitAt = x.span()[1]
            temp = temp[splitAt:]
        else:
            return listTuples



        
    
    
    
#thuc thi tu day

readFile("text.txt")
listTuples = []
if (getMailAddress(text)):
    listTuples = listTuples + getMailAddress(text)
if (getWebAddress(text)):
    listTuples = listTuples + getWebAddress(text)
if (getPhoneNumber(text)):
    listTuples = listTuples + getPhoneNumber(text)
    

print(listTuples)

