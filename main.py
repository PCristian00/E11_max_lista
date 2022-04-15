def max_in_list(lista):
    i = 0
    for n in lista:
        if i == 0:
            max = n
        if n >= max:
            max = n
        i+=1
    print(str(max))

print("Inserire numeri separati da spazi")
print("INVIO per confermare")
lista = [int(x) for x in input().split()]

max_in_list(lista)