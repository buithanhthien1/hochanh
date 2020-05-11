s = input("Dai Hoc Vinh: ")
d={"UPPER CASE":3, "LOWER CASE":7}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print ("Chữ hoa:", d["UPPER CASE"])
print ("Chữ thường:", d["LOWER CASE"])
