def getpacketheader(message):
    """
    Separate packet header from the rest
    Args:
        message: The bit-encoded message

    Returns: Version, TYPE_ID and rest of the message
    """
    version = int(message[:3], 2)
    type_id = int(message[3:6], 2)
    message = message[6:]
    return version, type_id, message

def getdecodedliteral(literal):
    """
    Separate decoded literal value and the rest of the message
    Args:
        literal: The literal value encoded as binary number

    Returns: The decoded literal value and the remaining message, removing tracing zeros
    """
    literal_binary = ''
    prefix, message = literal[0], literal[1:]

    # All groups except last is prefixed by a 1
    while prefix == '1':
        literal_binary += message[:4]
        message = message[4:]
        prefix, message = message[0], message[1:]

    # Also add last group and remove that from the message
    literal_binary += message[:4]
    message = message[4:]
    return int(literal_binary, 2), message

def getlengthtypeid(message):
    """
    Separate length type ID and rest of the message
    Args:
        message: The message

    Returns: The length type ID and the remaining message
    """
    return int(message[0]), message[1:]

def getsubpackets(message):
    """
    For length type ID == 0, separate out sub packets
    Args:
        message: The message

    Returns: The subpackets and the remaining message
    """
    subpackets_length, message = int(message[:15], 2), message[15:]
    subpackets, message = message[:subpackets_length], message[subpackets_length:]
    return subpackets, message

def getsubpacketsnumber(message):
    """
    For length type ID == 1, separate out number of sub packets
    Args:
        message: The message

    Returns: The number of sub packets and the remaining message
    """
    subpackets_number, message = int(message[:11], 2), message[11:]
    return subpackets_number, message

def getpacket(message):
    """
    Separate first packet from rest of the message
    Args:
        message: The message

    Returns: The first packet and rest of the message
    """
    if '1' in message:
        original_message = message
        version, type_id, message = getpacketheader(message)

        if type_id == 4:
            literal, message = getdecodedliteral(message)
        else:
            lengthtype_id, message = getlengthtypeid(message)

            if lengthtype_id == 0:
                subpackets, message = getsubpackets(message)

            elif lengthtype_id == 1:
                subpacketsnumber, message = getsubpacketsnumber(message)

                # Need to not repeat on the same sub package
                for i in range(subpacketsnumber):
                    packet, message = getpacket(message)

        if message == '':
            return original_message, message
        else:
            return original_message[:-len(message)], message
    else:
        return '', ''

def calculate(calculationpackets, type_id):
    """
    Calculate value of packets
    Args:
        calculationpackets: Packets to calculate
        type_id: Type id

    Returns: The calculated value
    """
    if type_id == 0:
        return sum(calculationpackets)
    elif type_id == 1:
        retval = 1
        for packet in calculationpackets:
            retval *= packet
        return retval
    elif type_id == 2:
        return min(calculationpackets)
    elif type_id == 3:
        return max(calculationpackets)
    elif type_id == 5:
        return 1 if calculationpackets[0] > calculationpackets[1] else 0
    elif type_id == 6:
        return 1 if calculationpackets[0] < calculationpackets[1] else 0
    elif type_id == 7:
        return 1 if calculationpackets[0] == calculationpackets[1] else 0

def recursiveversionsum(message):
    """
    Recursive function to sum up all version numbers of a message
    Args:
        message: The message

    Returns: The sum of version numbers
    """
    if '1' in message:
        version, type_id, message = getpacketheader(message)

        if type_id == 4:
            literal, message = getdecodedliteral(message)
            version_increment, message = recursiveversionsum(message)
            version += version_increment
        else:
            lengthtype_id, message = getlengthtypeid(message)

            if lengthtype_id == 0:
                subpackets, message = getsubpackets(message)

                version_increment = recursiveversionsum(subpackets)[0]
                version += version_increment

                version_increment, message = recursiveversionsum(message)
                version += version_increment

            elif lengthtype_id == 1:
                subpacketsnumber, message = getsubpacketsnumber(message)

                # Need to not repeat on the same sub package
                for i in range(subpacketsnumber):
                    packet, message = getpacket(message)
                    version_increment = recursiveversionsum(packet)[0]
                    version += version_increment

                version_increment, message = recursiveversionsum(message)
                version += version_increment

        return version, message
    else:
        return 0, message

def recursivepacketvalue(message):
    """
    Recursive function to calculate value of a message
    Args:
        message: The message

    Returns: The value and the remaining message
    """
    version, type_id, message = getpacketheader(message)

    if type_id == 4:
        value, message = getdecodedliteral(message)
        return value, message
    else:
        calculationpackets = []
        lengthtype_id, message = getlengthtypeid(message)

        if lengthtype_id == 0:
            subpackets, message = getsubpackets(message)

            # Iterate over subpackets
            while '1' in subpackets:
                subpacketsvalue, subpackets = recursivepacketvalue(subpackets)
                calculationpackets.append(subpacketsvalue)

        elif lengthtype_id == 1:
            subpacketsnumber, message = getsubpacketsnumber(message)

            # Need to not repeat on the same sub package
            for i in range(subpacketsnumber):
                packet, message = getpacket(message)
                calculationpackets.append(recursivepacketvalue(packet)[0])

        value = calculate(calculationpackets, type_id)

        return value, message


# Open and read file to a message
message = ''
input = open('16_input.txt', 'r')
for line in input:
    for char in line:
        message += format((int(char, 16)), '04b')
input.close()

versionsum = recursiveversionsum(message)[0]
print(f'Sum of version number in packets is: {versionsum}')

value = recursivepacketvalue(message)[0]
print(f'Value of packet is: {value}')
