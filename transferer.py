import os
import shutil
source = r'C:\Users\DELL\OneDrive\Desktop\Pro_102'
list_of_files = os.listdir(source)
for files in list_of_files:
    root,extension = os.path.splitext(files)
    if(extension == None):
        continue
    if extension in [ '.txt','.docx','.doc','.pdf']:
        path1 = source+'/'+files
        path2 = source + '/'+"Document_Files"
        path3 = source + '/'+"Document_Files"+'/'+files
        if (os.path.exists(path2)):
            print('Moving...')
            shutil.move(path1,path3)
        else:
            os.mkdir('Document_files')
            print('Moving..')
            shutil.move(path1,path3) 
    if extension in ['.jpg']:
        path4 = source+'/'+files
        path5 = source + '/'+"Image_Files"
        path6 = source + '/'+"Image_Files"+'/'+files           
        if(os.path.exists(path5)):
            print('Moving')
            shutil.move(path4,path6)
        else:
            os.mkdir('Image_Files')
            print('Moving')
            shutil.move(path4,path6)    
print('Do you want to reverse')
print('1 for yes or 2 for no')
choice = int(input('1 or 2: '))
if(choice == 1):
    path2n = source + '/'+"Document_Files"
    path5n = source + '/'+"Image_Files"
    list1 = os.listdir(path2n)
    list2 = os.listdir(path5n) 
    for e in list1:
        sou = path2n+'/'+ e
        shutil.move(sou,source) 
    for i in list2:
        sour = path5n+'/'+i
        shutil.move(sour,source)

       