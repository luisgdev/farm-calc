import views


def gen_comp_cycles(_n):
    # Compund i times within _n period of time
    res = []
    for i in range(1, _n-1):
        if _n%i == 0:
            res.append({'freq': int(_n/i), 'iter': i})
    return res


def simple_interest(cap, apr):
    # INTERES SIMPLE
    apr /= 100
    periods = [
        {'period': 'Year ', 'interest': apr },
        {'period': 'Month', 'interest': (apr/365)*30 },
        {'period': 'Daily', 'interest': apr/365 },
        {'period': 'Hour ', 'interest': (apr/365)/24 }
    ]
    views.header("Interes Simple")
    for item in periods:
        income = round(cap * item["interest"], 4)
        interest = round(item["interest"] * 100, 4)
        print(f'{item["period"]}: ${income} ({interest}%)')


def compound(apr, cap, gas, days):
    apr /= 100
    dpr = apr/365
    # INTERES COMPUESTO A LOS N DIAS
    interest = days * dpr
    comp_month = gen_comp_cycles(days)
    views.header(f'Compuesto a los {days} días')
    for item in comp_month:
        spent_gas = gas * item["iter"]
        earnings = (cap * (1 + interest/item["iter"])** item["iter"])
        item['yield'] = earnings - cap
        item['earning'] = earnings - spent_gas - cap
        item['spent_gas'] = spent_gas
        views.comp_item(item)
    # Calculamos las frecuencias con mayor ganancia
    best = sorted(comp_month, key= lambda b: b['earning'], reverse=True)[:3]
    views.best_comp(best)
    # Calculamos la frecuencia recomendada (mayor freq, menos ciclos)
    recom = max(best, key= lambda x: x['freq'])
    views.recom_comp(recom)


if __name__ == '__main__':
    command = ''
    while command.lower() != 'x':
        views.header("Calculadora para Staking pool")
        cap = float(input('Capital  ($): '))
        apr = float(input('APR      (%): '))
        interest = input('Tipo   (S/C): ').lower()
        if interest == 'c':
            days = int(input('Staking days: '))
            gas = float(input('Gas fee  ($): '))
            compound(apr, cap, gas, days)
        else:
            simple_interest(cap, apr)
        views.separator()
        command = input('Any key to continue, X to Exit\n>')
