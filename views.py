def header(title):
    separator()
    print(title)
    separator()


def separator():
    print("--" * 17)


def comp_item(item):
    print(f'A {item["freq"]} días: ${round(item["yield"], 4)} - ${round(item["spent_gas"], 4) } = ${round(item["earning"], 4)}')


def best_comp(item):
    separator()
    print(f'La frecuencia óptima es:\n\tCada {item["freq"]} días -> ${round(item["earning"], 4)}')


if __name__ == '__main__':
    print('This is not main!')
