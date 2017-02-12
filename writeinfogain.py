i = 500

with open('3.3output.txt', 'w') as output:
    while i <= 10000:
        filename = 'info-train-' + str(i)
        with open(filename) as inpt:
            output.write('n = ' + str(i) + '\n')
            output.write(inpt.read())

        i += 500
