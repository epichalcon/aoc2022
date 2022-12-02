def getdata(day: str) -> str:
    contents = str
    with open(f'data/{day}.txt', 'r') as f:
        contents = f.read()
    return contents

def separarPorLineas(data: str):
    return data.split('\n')

def getMatrizDeNumeros(data: str):
    return [[*map(int,list(line))] for line in data]