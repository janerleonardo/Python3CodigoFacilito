def run():
    counter = 0
    with open('aleph.txt', encoding="utf8") as f:
        for line in f:
            counter += line.count('1')

    print('Beatriz se encuentra {} en el texto'.format(counter))


if __name__ == '__main__':
    run()