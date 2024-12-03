file_open = open("ipo-lr5-text.txt")#открывает файл
f = file_open.read()#читает файл
w = f.split()#разделяет сроку на подстроки
kolvo = len(w)#колво подстрок
print(kolvo)