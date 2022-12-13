# Open and read file
with open('input.txt') as file:
    lines = file.read().splitlines()
file.close()
lines = [line for line in lines if line.strip()]

class packet:
    def __init__(self, content):
        self.content = content

    def __lt__(self, other):
        return compare(self.content, other.content)

def compare(left, right):
    try:
        for i in range(max(len(left), len(right))):
            if isinstance(left[i], int) and isinstance(right[i], int):
                if left[i] < right[i]:
                    return True
                elif left[i] > right[i]:
                    return False
            elif isinstance(left[i], list) and isinstance(right[i], list):
                retval = compare(left[i], right[i])
                if retval != None:
                    return retval
            elif isinstance(left[i], list) and isinstance(right[i], int):
                retval = compare(left[i], [right[i]])
                if retval != None:
                    return retval
            elif isinstance(left[i], int) and isinstance(right[i], list):
                retval = compare([left[i]], right[i])
                if retval != None:
                    return retval

    except IndexError:
        if len(left) < len(right):
            return True
        elif len(left) > len(right):
            return False

indices = []

for i in range(len(lines) // 2):
    left = eval(lines[i*2])
    right = eval(lines[i * 2 + 1])

    if compare(left, right):
        indices.append(i+1)

print("Task 1: " + str(sum(indices)))

packets = []
for line in lines:
    packets.append(packet(eval(line)))
packets.append(packet([[2]]))
packets.append(packet([[6]]))
packets.sort()

decoder_key = 1
for i, packet in enumerate(packets):
    if packet.content == [[2]] or packet.content == [[6]]:
        decoder_key *= (i + 1)

print("Task 2: " + str(decoder_key))


