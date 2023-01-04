print("Program zadaje nepoznatu riječ."
      "\nIgrač pogađa zadanu riječ utipkavanjem pojedinačnih"
      "\nmalih slova hrvatske abecede."
      "\n\nIgra se moze ponoviti najviše 4 puta"
      "\njer program ima toliko nepoznatih riječi."
      "\nBroj pokušaja jednak je broju slova u riječi puta 2.")

lista = ['papar', 'laptop', 'škola', 'pas', 'sat']  ##naša lista


def randomiremove(lista2):  ##funkcija koja uzima jednu random stvar iz naše liste, te istu stvar remove-a
    from random import choice
    nepoznata_rijec = choice(lista2)
    lista2.remove(nepoznata_rijec)
    nepoznata_rijec = nepoznata_rijec.replace('lj', '*').replace('nj', '?').replace('dž', '=')
    return nepoznata_rijec


def s2(x, y):  ##dio teksta koji se ponavlja svakim početkom nove igre
    return f"\n\n--------------------{x}.IGRA--------------------" \
           f"\n\nDopušta se najviše {y} pokušaja pogađanja slova" \
           "\n,te sva slova su mala slova hrvatske abecede"


def provjera(slovo, rijec,
             prazna_rijec):  ##provjerava postoji li naše uneseno slovo u našoj riječi te vraća praznu riječ
    i = 0
    while len(rijec) > i:
        if slovo is rijec[i]:
            prazna_rijec[i] = slovo
        i += 1
    prazna_rijec = ''.join(prazna_rijec)
    return prazna_rijec.replace('*', 'lj').replace('?', 'nj').replace('=', 'dž')


def main(x, brojigre):
    prazna_rijec = ["_" for _ in range(len(x))]
    pokusaj = 1
    broj_pokusaja = (len(x)) * 2
    print(s2(brojigre, broj_pokusaja))
    while pokusaj <= broj_pokusaja:
        unos = str(input("Unesi malo slovo: "))
        if unos == 'lj':
            unos = '*'
        if unos == 'nj':
            unos = '?'
        if unos == 'dž':
            unos = '='
        while unos not in 'abcćčdđefghijklmnoprsštuvzž*?=':
            unos = str(input("Neispravan unos,probajte ponovno: "))
        else:
            print(provjera(unos, x, prazna_rijec))
            if unos not in x:
                pokusaj += 1
            if provjera(unos, x, prazna_rijec) == x.replace('*', 'lj').replace('?', 'nj').replace('=', 'dž'):
                print("\nČestitam riječ uspiješno pogođena!")
                break
    else:
        x = x.replace('*', 'lj').replace('?', 'nj').replace('=', 'dž')
        print(f"Riječ je bila \"{x}\". Više sreće drugi put :(")


igra = 1
while len(lista) > 0:
    randomvarijabla = input("\nPRITISNI ENTER ZA NOVU IGRU")
    main(randomiremove(lista), igra)
    igra += 1

print("\nPotrosili ste sve riječi,za novu igru stisnite ctrl+alt+del.")
