from typing import List, TypedDict

from rich import box
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

from models import Compound, Period, Simple, Span

CONSOLE: Console = Console()

NOTE: str = """
    NOTE:
    - dif_roi > dif_gas : Ganancia
    - dif_roi < dif_gas : Pérdida
    """
FAILED: str = """
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
    """


def print_markdown(text: str) -> None:
    markdown_formatted_text: Markdown = Markdown(text)
    CONSOLE.print(markdown_formatted_text)


def simple_interest(simple: Simple) -> None:
    print_markdown("***")
    table: Table = Table(title="Interes Simple", box=box.SIMPLE)
    header: List[str] = ["Period", "Income ($)", "ROI (%)"]
    for col in header:
        table.add_column(col)
    results = [
        Span(period="Annual", income=simple.annual_income, roi=simple.apr),
        Span(period="Monthly", income=simple.monthly_income, roi=simple.monthly),
        Span(period="Daily", income=simple.daily_income, roi=simple.daily),
        Span(period="Hourly", income=simple.hourly_income, roi=simple.hourly),
    ]
    for row in results:
        roi: str = f'{round(row["roi"] * 100, 4)}'
        income: str = f'{round(row["income"], 4)}'
        table.add_row(row["period"], income, roi)
    CONSOLE.print(table)


def compound_interest(comp: Compound) -> None:
    print_markdown("---")
    title = f"Interes Compuesto por {comp.periods[0].days} días"
    table = Table(title=title, box=box.SIMPLE)
    header = "Day,Yield($),Gas($),Profit($),Dif ROI($),Dif Gas($),ROI(%)"
    for col in header.split(","):
        table.add_column(col)
    for row in comp.periods:
        table.add_row(
            str(row.days),
            str(round(row._yield, 4)),
            str(round(row.spent_gas, 4)),
            str(round(row.profit, 4)),
            str(round(row.dif_profit, 4)),
            str(round(row.dif_gas, 4)),
            str(round(row.roi, 2)),
        )
    CONSOLE.print(table)
    print_markdown(NOTE)
    if comp.best:
        best_comp(comp.best)
        recom = f"Recomendado: Cada {comp.recom.days} días."
        CONSOLE.print(recom, style="bold green")
    else:
        print_markdown(FAILED)


def best_comp(best_pds: List[Period]) -> None:
    print_markdown("___")
    table = Table(title="Frecuencias Óptimas", box=box.SIMPLE)
    header = ["Period", "ROI ($)", "Profit (%)"]
    for item in header:
        table.add_column(item)
    for period in best_pds:
        duration = f"Cada {period.days} días"
        earned = str(round(period.profit, 4))
        profit = str(round(period.roi, 2))
        table.add_row(duration, earned, profit)
    CONSOLE.print(table)


if __name__ == "__main__":
    print("This is not main!")
