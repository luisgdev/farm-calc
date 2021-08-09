from typing import Callable, Dict, List


class Interest:
    """
    Interest includes: 
    - Capital invested
    - Annual Percentage Rate (APR)
    - Daily interest from APR 
    """
    def __init__(self, capital: float, apr: float) -> None:
        self.cap = capital
        self.apr = apr / 100
        self.daily = self.apr / 365


class Simple(Interest):
    """
    Simple interest includes: 
    - Additional Monthly and Hourly interests from APR 
    - Income for each period of time (year, month, day, hour)
    """
    def __init__(self, capital: float, apr: float) -> None:
        Interest.__init__(self, capital, apr)
        self.monthly: float = self.daily * 30
        self.hourly: float = self.daily / 24
        self.annual_income: float = self.cap * self.apr
        self.monthly_income: float = self.cap * self.monthly
        self.daily_income: float = self.cap * self.daily
        self.hourly_income: float = self.cap * self.hourly


class Compound(Interest):
    """
    Compound interest includes: 
    - List of possible Periods for a given number of days and their performance.
    - Top 3 Periods with the best performance and the recomended one.
    - Explanation of relevant indicators (dif)
    """
    def __init__(self, cap: float, apr: float, gas: float, days: int) -> None:
        Interest.__init__(self, cap, apr)
        self.periods: List[Period] = []
        self.best: List[Period] = []
        self.recom: Period
        self._calc_periods(gas, days)

    def _comp_cycles(self, cap: float, days: int) -> None:
        # Do Compund every x number of days
        for x in range(1, days - 1):
            if days % x == 0:
                pd = Period(cap=cap, days=int(days/x), cycles=x)
                self.periods.append(pd)

    def _calc_periods(self, gas: float, days: int):
        # INTERES COMPUESTO A LOS N DIAS
        simple_int: float = days * self.daily
        self._comp_cycles(self.cap, days)
        # Diferencia entre valor actual y anterior para: roi y gas
        prev_profit: float = 0
        prev_gas: float = 0
        for pd in self.periods:
            pd.set_gas(gas)
            pd.set_interest(simple_int / pd.cycles)
            if prev_profit != 0:
                pd.dif_profit = pd.profit - prev_profit
                pd.dif_gas = pd.spent_gas - prev_gas
            else:
                pd.dif_profit = prev_profit
                pd.dif_gas = prev_gas
            prev_profit = pd.profit
            prev_gas = pd.spent_gas
        # Filtramos, descartando las pérdidas
        cond: Callable[[Period], bool] = lambda p: p.dif_profit > p.dif_gas
        self.best = list(filter(cond, self.periods))
        # Mostramos las frecuencias con mayor ganancia
        if len(self.best) > 0:
            self.best = self.best[-3:]
            self.recom = max(self.best, key=lambda x: x.days)


class Period:
    """
    Time Period of the Compound interest.
    It includes: 
    - Frequency days to execute a cycle (making the compound)
    - Spent gas fee, Profit, ROI and 
    - Difference between last and new compound cycle performance (profit and spent gas).

    """
    def __init__(self, cap: float, days: int, cycles: int):
        self.cap = cap
        self.days = days
        self.cycles = cycles
        self.spent_gas: float
        self._yield: float
        self.profit: float
        self.roi: float
        self.dif_profit: float
        self.dif_gas: float

    def set_gas(self, gas: float) -> None:
        self.spent_gas = self.cycles * gas

    def set_interest(self, interest: float) -> None:
        self._yield = (self.cap * (1 + interest) ** self.cycles) - self.cap
        self.profit = self._yield - self.spent_gas
        self.roi = (self.profit / self.cap) * 100


if __name__ == '__main__':
    print('This is not main!')
