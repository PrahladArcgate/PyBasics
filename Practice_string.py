from audioop import reverse


name =input("Enter your name : ")
reverse =name[-1 :: -1]
print(f"reverse of your name is {reverse}")