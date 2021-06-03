import views


def gen_comp_cycles(_n):
    # Compund i times within _n period of time
    res = []
    for i in range(1, _n-1):
        if _n%i == 0:
            res.append({'freq': _n/i, 'iter': i})
    return res


def simple_interest(cap, apr):
    # INTERES SIMPLE
    apr /= 100
    periods = [
        {'period': 'Year ', 'interest': apr },
        {'period': 'Month', 'interest': apr/12 },
        {'period': 'Daily', 'interest': apr/365 },
        {'period': 'Hour ', 'interest': (apr/365)/24 }
    ]
    views.header("Interes Simple")
    for item in periods:
        income = round(cap * item["interest"], 4)
        interest = round(item["interest"] * 100, 4)
        print(f'{item["period"]}: ${income} ({interest}%)')


def compound(apr, cap, gas):
    apr /= 100
    mpr = apr/12
    dpr = apr/365
    # INTERES COMPUESTO AL MES
    comp_month = gen_comp_cycles(30)
    views.header("Compuesto al Mes")
    for item in comp_month:
        spent_gas = gas * item["iter"]
        earnings = (cap * (1 + mpr/item["iter"])** item["iter"])
        item['earning'] = earnings - spent_gas - cap
        item['spent_gas'] = spent_gas
        views.comp_item(item)
    # Calculamos la frecuencia con mayor ganancia
    best = max(comp_month, key= lambda b: b['earning'])
    views.best_comp(best)


if __name__ == '__main__':
    command = ''
    while command.lower() != 'x':
        views.header("Calculadora para Stake pool")
        cap = float(input('Capital ($): '))
        apr = float(input('Interes (%): '))
        interest = input('Interes (S/C): ').lower()
        if interest == 'c':
            gas = float(input('Gas fee ($): '))
            compound(apr, cap, gas)
        else:
            simple_interest(cap, apr)
        views.separator()
        command = input('Any key to continue, X to Exit\n>')
