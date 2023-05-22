

# File = open(file = "File.txt",mode="r",encoding='utf-8')
# note = File.readlines()
# print(note)
# File.close()
x = 0
with open(file = 'File.txt',mode = 'a+',encoding='utf-8') as File:
    File.write(f'\ntest{x}')
    File.flush()
    File.seek(0,0)
    content = File.read()
    print(content)


