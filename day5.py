from typing import List

from getdata import getdata


class Crate_stacks:
    crates: list

    def __init__(self):
        self.crates = []

    def add_to_bottom(self, crate: str):
        self.crates.insert(0, crate)

    def add_crate(self, crate: str):
        self.crates.append(crate)

    def remove_crate(self):
        return self.crates.pop()

    def get_top_crate(self):
        return self.crates[-1]

    def remove_n_crates(self, n):
        res = self.crates[len(self.crates) - n:]
        new_list = self.crates[: len(self.crates) - n]

        self.crates = new_list

        return res

    def add_n_crates(self, crates: List[str]):
        self.crates.extend(crates)

    def __repr__(self):
        return self.crates

class Cargo_crane:
    crate_stack_list: List[Crate_stacks]
    model: int

    def __init__(self, crate_structure: List[str], crane_model):
        self.model = crane_model
        self.crate_stack_list = []
        for i in range(self.get_num_of_stacks(crate_structure[-1])):
            self.crate_stack_list.append(Crate_stacks())

        crate_structure.pop()

        for i, line in enumerate(crate_structure):
            j = 0
            while j < len(line):
                if line[j].isalpha():
                    self.add_crate_to_stack(j//4, line[j])
                j+=1


    def add_crate_to_stack(self, stack_num: int, crate: str):
        self.crate_stack_list[stack_num].add_to_bottom(crate)


    def get_num_of_stacks(self, line: str):
        number_of_collums = line.replace(' ', '')
        return len(list(number_of_collums))

    def move(self, n_crates: int, stack_origin: int, stack_destination: int):
        if self.model == 1:
            i = 0
            while i < n_crates:
                crate = self.crate_stack_list[stack_origin-1].remove_crate()
                self.crate_stack_list[stack_destination-1].add_crate(crate)
                i+=1
        elif self.model == 2:
            crates = self.crate_stack_list[stack_origin-1].remove_n_crates(n_crates)
            self.crate_stack_list[stack_destination-1].add_n_crates(crates)


    def get_top_crates(self):
        top_crates = ''
        for crate in self.crate_stack_list:
            top_crates += crate.get_top_crate()

        return top_crates
def parse_instruction(instruction: str):
    list_instructions = instruction.split(' ')
    n_crates = int(list_instructions[1])
    origin = int(list_instructions[3])
    end = int(list_instructions[5])
    return n_crates, origin, end

content = getdata.getdata('day5')
content = getdata.separarPorLineas(content)

def stars(data, star_number):
    stack_structure = []
    i = 0
    while len(data[i]) != 0:
        stack_structure.append(data[i])
        i+=1

    cargo_crane = Cargo_crane(stack_structure, star_number)
    i += 1

    while i < len(data):
        instruction = data[i]
        n_crates, origin, end = parse_instruction(instruction)
        cargo_crane.move(n_crates, origin, end)
        i+=1

    return cargo_crane.get_top_crates()

print(stars(content, star_number=2))