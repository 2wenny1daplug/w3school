file = open("myfile.txt","w" )
L = ["This is Ashley \n","This is Isaiah \n", "This is Phoebe \n"]
file.write("Hi")
file.writelines(L)
file.close()

file = open("myfile.txt", "r+")
print("Output of the Read function is ")
print(file.read())
print()
file.seek(0)
