def max_riqueza(accounts):
    maxima_riqueza = 0
    for cliente in accounts:
        riqueza_total = 0
        riqueza_total += sum(cliente)
        while riqueza_total > maxima_riqueza:
            maxima_riqueza = riqueza_total
    return maxima_riqueza



def main():
    accounts = [
    [1,2,3],
    [3,2,1],
    [5,5,5],
    [1,1,1]
]
    maxima_riqueza = max_riqueza(accounts)
    print(f"El clientes mas rico tiene {maxima_riqueza}$")
main()