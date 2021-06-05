def header(title):
    separator()
    print(f'*** {title} ***')
    separator()


def separator():
    print("--" * 18)


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
