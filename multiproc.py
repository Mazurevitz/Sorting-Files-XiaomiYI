import multiprocessing

def spawn(num, num2):
    print('Sprawned! {} {}'.format(num, num2))

if __name__ == '__main__':
    for i in range(100):
        p = multiprocessing.Process(target = spawn, args=(i, i+1))
        p.start()
