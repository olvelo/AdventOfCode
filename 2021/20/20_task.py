def enhance_image(input_image, enhancement_algorithm, step):
    """
    Algorithm for enhancing image
    Args:
        input_image: The input image
        enhancement_algorithm: The enhancement algorithm, an array of 1's and 0's
        step: The enhancement step

    Returns: The output image
    """
    # Create empty output image
    output_image = []

    # For all lines in input image, plus outer edges
    for i in range(-1, len(input_image) + 1):
        output_line = []

        # For all pixels on this line, plus outer edges
        for j in range(-1, len(input_image[0]) + 1):

            # Create number string to calculate new pixel from enhancement algorithm, looping over adjacent pixels
            number_string = ''
            for k in [i-1, i, i+1]:
                for l in [j-1, j, j+1]:
                    if 0 <= k < len(input_image) and 0 <= l < len(input_image[0]):
                        number_string += str(input_image[k][l])
                    else:
                        # The catch: Need to take into account what happens to pixels in the background
                        number_string += str(1 if enhancement_algorithm[0] == 1 and step % 2 != 0 else 0)

            output_line.append(enhancement_algorithm[int(number_string, 2)])

        output_image.append(output_line)

    return output_image

# Open and read file to an image enhancement algorithm and an input image
input = open('20_input.txt', 'r')

# First line is enhancement algorithm, second is just empty. Read as 0's and 1's immediately
enhancement_algorithm = []
for char in input.readline().strip():
    if char == '#':
        enhancement_algorithm.append(1)
    elif char == '.':
        enhancement_algorithm.append(0)
    else:
        raise ValueError(f'Unexpected character: {char}')
input.readline()

# Build up input image, also reading it as 0's and 1's
image = []
for i, line in enumerate(input):
    chars = line.strip()
    if chars != '':
        image.append([])
        for char in chars:
            image[i].append(1 if char == '#' else 0)
input.close()

# For a certain number of steps, do image enhancement
steps = 50
for i in range(steps):
    image = enhance_image(image, enhancement_algorithm, i)

    # Print number of blinking pixels after 2 and 50 steps
    if i == 1 or i == 49:
        blinking = 0
        for j in range(len(image)):
            blinking += sum(image[j])
        print(f'After {i + 1} steps, number of blinking pixels is {blinking}')
