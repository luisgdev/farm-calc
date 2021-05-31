# APR: interes simple anual
# mpr: interes mensual
# dpr: interes diario
# hpr: interes por hora


def simple_interest(cap, apr):
    # INTERES SIMPLE
    apr /= 100
    periods = [
        {'period': 'Year ', 'interest': apr },
        {'period': 'Month', 'interest': apr/12 },
        {'period': 'Daily', 'interest': apr/365 },
        {'period': 'Hour ', 'interest': (apr/365)/24 }
    ]
    print(f'{"--"*17}\n*** Interes Simple ***\n{"--"*17}')
    for item in periods:
        income = round(cap * item["interest"], 4)
        interest = round(item["interest"] * 100, 4)
        print(f'{item["period"]}: $ {income} ({interest}%)')


def compound(apr, cap, gas):
    apr /= 100
    mpr = apr/12
    dpr = apr/365
    hpr = dpr/24
    # INTERES COMPUESTO AL MES
    comp_month = [
        {'freq': '30 dias ', 'iter': 1},
        {'freq': '15 dias ', 'iter': 2},
        {'freq': '07 dias ', 'iter': 30/4},
        {'freq': '03 dias ', 'iter': 10},
        {'freq': '01 dias ', 'iter': 30},
        {'freq': '12 horas', 'iter': 60},
        {'freq': '06 horas', 'iter': 120},
        {'freq': '01 horas', 'iter': 720}
    ]
    print(f'{"--"*17}\n*** Ingreso Mensual Compuesto ***\n{"--"*17}')
    for item in comp_month:
        spent_gas = gas * item["iter"]
        earnings = (cap * (1 + mpr/item["iter"])** item["iter"]) - spent_gas
        item['earning'] = earnings
        item['spent_gas'] = spent_gas
        print(f'Cada {item["freq"]}: $ {round(earnings, 4)}. Gas $ {round(spent_gas, 4)}')
    # Calculamos la refuencia óptima
    best = max(comp_month, key= lambda b: b['earning'])
    print(f'*** La frecuencia óptima es:\nCada {best["freq"]}, para generar $ {round(best["earning"], 4)}.')
    # INTERES COMPUESTO AL DIA
    comp_daily = [
        {'freq': '12 horas', 'iter': 2},
        {'freq': '06 horas', 'iter': 4},
        {'freq': '04 horas', 'iter': 6},
        {'freq': '03 horas', 'iter': 8},
        {'freq': '02 horas', 'iter': 12},
        {'freq': '01 horas', 'iter': 24}
    ]
    print(f'{"--"*17}\n*** Ingreso diario compuesto***\n{"--"*17}')
    for item in comp_daily:
        spent_gas = gas * item["iter"]
        earnings = (cap * (1 + dpr/item["iter"])** item["iter"]) - spent_gas
        item['earning'] = earnings
        item['spent_gas'] = spent_gas
        print(f'Cada {item["freq"]}: $ {round(earnings, 4)}. Gas $ {round(spent_gas, 4)}')
    best = max(comp_daily, key= lambda b: b['earning'])
    print(f'*** La frecuencia óptima es:\nCada {best["freq"]}, para generar $ {round(best["earning"], 4)}.')


if __name__ == '__main__':
    command = ''
    while command.lower() != 'x':
        print(f'{"--"*17}\n*** Calculadora para Stake pool ***\n{"--"*17}')
        cap = float(input('Capital ($): '))
        apr = float(input('Interes (%): '))
        interest = input('Interes (S/C): ').lower()
        if interest == 'c':
            gas = float(input('Gas fee ($): '))
            compound(apr, cap, gas)
        else:
            simple_interest(cap, apr)
        command = input(f'{"--"*17}\nAny key to continue, X to Exit\n>')
