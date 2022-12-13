# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()

class Monkey:
    def __init__(self, items, operation, divisor, monkey_true, monkey_false, inspect_counter):
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.inspect_counter = inspect_counter

    def __lt__(self, other):
        return self.inspect_counter < other.inspect_counter

    def inspect(self):
        to_true, to_false = [], []
        for i in range(len(self.items)):
            self.inspect_counter += 1
            old = self.items.pop(0)
            new = eval(self.operation)
            if new % self.divisor == 0:
                to_true.append(new % (17*3*5*7*11*19*2*13))
            else:
                to_false.append(new % (17*3*5*7*11*19*2*13))
        return to_true, to_false

monkeys = []
for line in lines:
    words = line.strip().split(" ")
    if words[0] == "Monkey":
        monkeys.append(Monkey([], "", 1, -1, -1, 0))
    elif words[0] == "Starting":
        for i in range(2, len(words)):
            monkeys[len(monkeys) - 1].items.append(int(words[i].strip(",")))
    elif words[0] == "Operation:":
        monkeys[len(monkeys) - 1].operation = words[3] + words[4] + words[5]
    elif words[0] == "Test:":
        monkeys[len(monkeys) - 1].divisor = int(words[3])
    elif len(words) < 2:
        continue
    elif words[1] == "true:":
        monkeys[len(monkeys) - 1].monkey_true = int(words[5])
    elif words[1] == "false:":
        monkeys[len(monkeys) - 1].monkey_false = int(words[5])

for round in range(10000):
    for monkey in monkeys:
        to_true, to_false = monkey.inspect()
        for item in to_true:
            monkeys[monkey.monkey_true].items.append(item)
        for item in to_false:
            monkeys[monkey.monkey_false].items.append(item)

monkeys.sort(reverse=True)
monkey_business = monkeys[0].inspect_counter * monkeys[1].inspect_counter
print("Task 2: " + str(monkey_business))
