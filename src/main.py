import views
from models import Compound, Simple

if __name__ == '__main__':
    command: str = ''
    while command.lower() != 'x':
        views.print_markdown("# Calculadora para Staking pool")
        cap = float(input(' • Capital($): '))
        apr = float(input(' • APR....(%): '))
        i_type = input(' • Interes (S)imple o (C)ompuesto: ')
        if i_type in ['s', 'S']:
            s_i: Simple = Simple(cap, apr)
            views.simple_interest(s_i)
        elif i_type in ['c', 'C']:
            days = int(input(' • Stake days: '))
            gas = float(input(' • Gas fee($): '))
            comp_i: Compound = Compound(cap, apr, gas, days)
            views.compound_interest(comp_i)
        else:
            print('Debe indicar el tipo de interés.')
        command = input('Cualquier tecla para continuar, (X) para Salir\n> ')
