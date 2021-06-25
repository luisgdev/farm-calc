from rich.markdown import Markdown
from rich.console import Console
from rich.table import Table
from rich import box


def simple_interest(periods):
    table = Table(title='Interes Simple', box=box.SIMPLE)
    header = ['Period', 'Income($)', 'Profit(%)']
    for item in header:
        table.add_column(item)
    for item in periods:
        income = round(item["income"], 4)
        interest = round(item["interest"] * 100, 4)
        #print(f'{item["period"]}: ${income} ({interest}%)')
        table.add_row(item["period"], str(income), str(interest))
    Console().print(table)


def header(title):
    md = Markdown(f'# {title}')
    Console().print(md)


def separator():
    md = Markdown('___')
    Console().print(md)


def comp_item(item):
    print(f'A {item["freq"]} días: ${round(item["yield"], 4)} - ${round(item["spent_gas"], 4) } = ${round(item["earning"], 4)}')


def best_comp(b_list):
    separator()
    print('Frecuencias óptimas:')
    for item in b_list:
        print(f'\tCada {item["freq"]} días -> ${round(item["earning"], 4)}')


def recom_comp(item):
    separator()
    print(f'Recomendado:\n\tCada {item["freq"]} días -> ${round(item["earning"], 4)}')



if __name__ == '__main__':
    print('This is not main!')
