def getdata(day: str) -> str:
    contents = str
    with open(f'data/{day}.txt', 'r') as f:
        contents = f.read()
    return contents

def separarPorLineas(data: str) -> list:
    return data.split('\n')
def getMatrizDeNumeros(data):
    return [[*map(int,list(line))] for line in data]

def getMatrizDeStrings(data):
    return [list(line) for line in data]