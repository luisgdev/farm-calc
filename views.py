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
        #print(f'{item["period"]}: ${income} ({interest}%)')
        table.add_row(item["period"], str(income), str(interest))
    Console().print(table)


def compound(periods):
    print_markdown('---')
    table = Table(title=f'Interes Compuesto por {periods[0]["freq"]} días', box=box.SIMPLE)
    header = ['Period', 'Yield($)', 'Gas($)', 'Earned($)']
    for item in header:
        table.add_column(item)
    for item in periods:
        _yield = round(item["yield"], 4)
        spent_gas = round(item["spent_gas"], 4)
        earned = round(item["earning"], 4)
        table.add_row(str(item["freq"]), str(_yield), str(spent_gas), str(earned))
    Console().print(table)


def best_comp(b_list):
    print_markdown('___')
    table = Table(title=f'Frecuencias Óptimas', box=box.SIMPLE)
    header = ['Period', 'Earnings($)']
    for item in header:
        table.add_column(item)
    for item in b_list:
        table.add_row(f'Cada {item["freq"]} días', str(round(item["earning"], 4)))
    Console().print(table)


def recom_comp(item):
    recom = f'Recomendado: Cada {item["freq"]} días, para obtener ${round(item["earning"], 4)}'
    Console().print(recom, style="bold green")


if __name__ == '__main__':
    print('This is not main!')
