import os
ab=[]
path=os.path.join('C:','\\Users',os.getlogin(),'Appdata','Local','Packages','Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy','LocalState','Assets')
path78= "cd C:/ & cd Users & cd "+ os.getlogin()+" & cd Desktop & mkdir assets"
print (path78)
os.system(path78)
path2=os.path.join('C:','\\Users',os.getlogin(),'Desktop','assets')
os.system("xcopy "+ path +" " + path2)
path3="xcopy "+ path + path2
print(path3)
ent=os.scandir(path)
for entry in ent:
    ab.append(entry.name)
print(len(ab))

for i in range (0,len(ab)):
    #path6="cd C:/ & cd Users & cd "+ os.getlogin()+" & cd Appdata & cd Local & cd Packages & cd Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy & cd LocalState & cd Assets"
    path5= "cd C:/ & cd Users & cd "+ os.getlogin()+" & cd Desktop & cd assets"
    path9="j"+str(i)+"j.jpg"
    path7=path5+" & "+" ren "+ab[i]+" "+path9
    print(path9)
    os.system(path7)

