lista_filmova=[{"naziv":"The Godfather","br_pozitivnih":1000,"br_negativnih":10},
          {"naziv": "The pianist", "br_pozitivnih":500,"br_negativnih":30},
          {"naziv":"Beautiful Mind","br_pozitivnih":600, "br_negativnih": 45}]
max_film={}
max_value=0
for film in lista_filmova:
    if film["br_pozitivnih"]>max_value:
        max_value=film["br_pozitivnih"]
        max_film=film
print(max_film)
print("----------------------------------")
term="The"
for film in lista_filmova:
    if film["naziv"].startswith("The"):
        print(film)

