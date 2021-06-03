def header(title):
    separator()
    print(title)
    separator()


def separator():
    print("--" * 17)


def comp_item(item):
    print(f'Cada {item["freq"]}: ${round(item["earning"], 4)}. Gas ${round(item["spent_gas"], 4) }')


def best_comp(item):
    print(f'*** La frecuencia óptima es:\nCada {item["freq"]} días -> ${round(item["earning"], 4)}')


if __name__ == '__main__':
    print('This is not main!')