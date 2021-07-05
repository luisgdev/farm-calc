from rich.markdown import Markdown
from rich.console import Console
from rich.table import Table
from rich import box


def print_markdown(text):
    md = Markdown(text)
    Console().print(md)


def simple_interest(periods):
    print_markdown('***')
    table = Table(title='Interes Simple', box=box.SIMPLE)
    header = ['Period', 'Yield($)', 'Profit(%)']
    for item in header:
        table.add_column(item)
    for item in periods:
        income = round(item["income"], 4)
        interest = round(item["interest"] * 100, 4)
        table.add_row(item["period"], str(income), str(interest))
    Console().print(table)


def compound(periods):
    print_markdown('---')
    table = Table(title=f'Interes Compuesto por {periods[0]["freq"]} días', box=box.SIMPLE)
    header = ['Period', 'Yield($)', 'Gas($)', 'Earned($)', 'Dif($)', 'Dif Gas($)', 'Profit(%)']
    for item in header:
        table.add_column(item)
    for item in periods:
        _yield = str(round(item["yield"], 4))
        spent_gas = str(round(item["spent_gas"], 4))
        earned = str(round(item["earning"], 4))
        dif = str(round(item['dif'], 4))
        dif_gas = str(round(item['dif_gas'], 4))
        profit = str(round(item['profit'], 2))
        table.add_row(str(item["freq"]), _yield, spent_gas, earned, dif, dif_gas, profit)
    Console().print(table)


def best_comp(b_list):
    print_markdown('___')
    table = Table(title=f'Frecuencias Óptimas', box=box.SIMPLE)
    header = ['Period', 'Earnings($)', 'Profit(%)']
    for item in header:
        table.add_column(item)
    for item in b_list:
        period = f'Cada {item["freq"]} días'
        earned = str(round(item["earning"], 4))
        profit = str(round(item['profit'], 2))
        table.add_row(period, earned, profit)
    Console().print(table)


def recom_comp(item):
    recom = f'Recomendado: Cada {item["freq"]} días.'
    Console().print(recom, style="bold green")


if __name__ == '__main__':
    print('This is not main!')
