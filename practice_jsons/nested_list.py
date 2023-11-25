if __name__ == '__main__':
    # students = {}
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students[name] = score


# def square(x):
#   return x * x

# # Apply the square() function to each element of the list.
# my_list = [1, 2, 3, 4, 5]
# squared_list = map(square, my_list)

    students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
    students = [['Prashant', 52.22], ['Kush', 52.223], ['Kant', 52.222], ['Kanti', 52.2222], ['Harshit', 52.22222]]
    result = []
    note = list(set([pereche[1] for pereche in students]))
    note = sorted(note)
    for pereche in students:
        if pereche[1] == note[2]:
            result.append(pereche[0])
    for name in sorted(result):
        print(name)