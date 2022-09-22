codigo_postal1 = "...._ __... ..... ..___"
codigo_postal2 = ".____ ___.. ___.. _____"
codigo_postal3 = "_.... ..___ ...__ _...."
codigo_postal4 = "..... __... .____ .____"
codigo_postal5 = "___.. ...._ ____. ____."
new_codigos_postales = ""
d1 = {
".____" : "1",
"..___" : "2",
"...__" : "3",
"...._" : "4",  
"....." : "5",
"_...." : "6",
"__..." : "7",
"___.." : "8",
"____." : "9",
"_____" : "0"
}

for x in d1:
    if x in codigo_postal1:
        codigo_postal1 = codigo_postal1.replace(x, d1[x])   
    if x in codigo_postal2:
        codigo_postal2 = codigo_postal2.replace(x, d1[x])     
    if x in codigo_postal3:
        codigo_postal3 = codigo_postal3.replace(x, d1[x]) 
    if x in codigo_postal4:
        codigo_postal4 = codigo_postal4.replace(x, d1[x])   
    if x in codigo_postal5:
        codigo_postal5 = codigo_postal5.replace(x, d1[x])  

print(codigo_postal1)
print(codigo_postal2)
print(codigo_postal3)
print(codigo_postal4)
print(codigo_postal5)      