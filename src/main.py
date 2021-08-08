from typing import Dict, List
import views


class Interest:
    def __init__(self, capital: float, apr: float) -> None:
        self.apr = apr / 100
        self.cap = capital
        self.daily = self.apr / 365


    def simple_interest(self) -> None:
        # INTERES SIMPLE
        periods: List[Dict[str, float]] = [
            {'period': 'Year ', 'interest': self.apr },
            {'period': 'Month', 'interest': self.daily * 30 },
            {'period': 'Daily', 'interest': self.daily },
            {'period': 'Hour ', 'interest': self.daily /24 }
        ]
        for item in periods:
            item.update({'income': self.cap * item["interest"]})
        views.simple_interest(periods)


    def _compound_iters(self, days: int) -> List[Dict[str, int]]:
        # Compund every x number of days
        res: List[Dict[str, int]] = []
        for x in range(1, days - 1):
            if days % x == 0:
                res.append({'freq': int(days/x), 'iter': x})
        return res


    def compound(self, gas: float, days: int):
        # INTERES COMPUESTO A LOS N DIAS
        simple_int: float = days * self.daily
        periods: List[Dict[str, any]] = self._compound_iters(days)
        # Diferencia entre valor actual y anterior para: earned y gas
        prev_earned: float = 0
        prev_gas: float = 0
        for item in periods:
            iters: int = item["iter"]
            period_int: float = simple_int / iters
            spent_gas: float = gas * iters
            earned: float = (cap * (1 + period_int) ** iters)
            item['yield'] = earned - cap
            item['earning'] = earned - spent_gas - cap
            item['spent_gas'] = spent_gas
            if prev_earned != 0:
                item['dif'] = item['earning'] - prev_earned
                item['dif_gas'] = spent_gas - prev_gas
            else:
                item['dif'] = prev_earned
                item['dif_gas'] = prev_gas
            prev_earned = item['earning']
            prev_gas = spent_gas
            item['profit'] = item['earning'] / cap * 100
        views.compound(periods)
        # Filtramos, descartando las pérdidas
        cond = lambda item: item['dif'] > item['dif_gas']
        periods = list(filter(cond, periods))
        # Mostramos las frecuencias con mayor ganancia
        if len(periods) > 0:
            best: List[Dict[str, any]] = periods[-3:]
            views.best_comp(best)
            recom: Dict[str, any] = max(best, key= lambda x: x['freq'])
            views.recom_comp(recom)
        else:
            views.comp_failed()


if __name__ == '__main__':
    command: str = ''
    while command.lower() != 'x':
        views.print_markdown("# Calculadora para Staking pool")
        i_type = input(' • Interes, (S)imple o (C)ompuesto: ').lower()
        cap = float(input(' • Capital($): '))
        apr = float(input(' • APR....(%): '))
        farm: Interest = Interest(cap, apr)
        if i_type.startswith('c'):
            days = int(input(' • Stake days: '))
            gas = float(input(' • Gas fee($): '))
            farm.compound(gas, days)
        else:
            farm.simple_interest()
        command = input('Any key to continue, (X) to Exit\n>')
