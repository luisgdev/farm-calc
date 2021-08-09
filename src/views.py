from typing import TypedDict, Dict, List

from rich import box
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

from models import Compound, Period, Simple

CONSOLE = Console()


def print_markdown(text: str) -> None:
    md: Markdown = Markdown(text)
    CONSOLE.print(md)


def simple_interest(si: Simple) -> None:
    print_markdown('***')
    table: Table = Table(title='Interes Simple', box=box.SIMPLE)
    header: List[str] = ['Period', 'Income ($)', 'ROI (%)']
    for head in header:
        table.add_column(head)
    Span = TypedDict('Span', {'period': str, 'income': float, 'roi': float})
    results: List[Span] = [
        {'period': 'Annual', 'income': si.annual_income, 'roi': si.apr},
        {'period': 'Monthly', 'income': si.monthly_income, 'roi': si.monthly},
        {'period': 'Daily', 'income': si.daily_income, 'roi': si.daily},
        {'period': 'Hourly', 'income': si.hourly_income, 'roi': si.hourly}
    ]
    for item in results:
        table.add_row(
            item["period"],
            f'{round(item["income"], 4)}',
            f'{round(item["roi"] * 100, 4)}'
        )
    CONSOLE.print(table)


def compound_interest(comp: Compound) -> None:
    print_markdown('---')
    table = Table(
        title=f'Interes Compuesto por {comp.periods[0].days} días',
        box=box.SIMPLE
    )
    header = 'Day,Yield ($),Gas ($),Profit ($),Dif ROI ($),Dif Gas ($),ROI (%)'
    for col in header.split(','):
        table.add_column(col)
    for row in comp.periods:
        table.add_row(
            str(row.days),
            str(round(row._yield, 4)),
            str(round(row.spent_gas, 4)),
            str(round(row.profit, 4)),
            str(round(row.dif_profit, 4)),
            str(round(row.dif_gas, 4)),
            str(round(row.roi, 2))
        )
    CONSOLE.print(table)
    comp_note()
    if comp.best:
        best_comp(comp.best)
        recom_comp(comp.recom)
    else:
        comp_failed()


def comp_note() -> None:
    print_markdown(
        '''
        NOTE:
        - dif_roi > dif_gas : Ganancia
        - dif_roi < dif_gas : Pérdida
        '''
    )


def comp_failed():
    print_markdown(
        '''
        No es factible! El costo del GAS fee supera al ROI en 
        todos los escenarios posibles.
        Causas:
        - Poco capital para obtener ganancias en el tiempo dado.
        - El APR no genera lo suficiente para cubrir el gas fee.
        Recomendaciones:
        - Hacer stake por un mayor periodo de tiempo.
        - Reducir el Gas fee.
        - Invertir en un Pool con mayor APR.
        - Interes simple en lugar de compuesto.\n
        '''
    )


def best_comp(best_pds: List[Period]) -> None:
    print_markdown('___')
    table = Table(title='Frecuencias Óptimas', box=box.SIMPLE)
    header = ['Period', 'ROI ($)', 'Profit (%)']
    for item in header:
        table.add_column(item)
    for period in best_pds:
        duration = f'Cada {period.days} días'
        earned = str(round(period.profit, 4))
        profit = str(round(period.roi, 2))
        table.add_row(duration, earned, profit)
    CONSOLE.print(table)


def recom_comp(pd: Period) -> None:
    recom = f'Recomendado: Cada {pd.days} días.'
    CONSOLE.print(recom, style="bold green")


if __name__ == '__main__':
    print('This is not main!')
