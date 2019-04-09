def generateFibonacci(length):
    if type(length) is not int:
        raise TypeError("Length parameter should be of integer type")
    elif length < 1:
        raise ValueError("Length cannot be less then 1")
    else:
        if length == 1:
            sequence = [1]
        else:
            sequence = [1, 1]
            for i in range(2, length):
                sequence.append(sequence[i-2] + sequence[i-1])
        return sequence


if __name__ == '__main__':
    print(generateFibonacci(2))
    print(generateFibonacci(10))
