import time
import multiprocessing

def read_info(name):
    all_data = []
    with(open(name, 'r', encoding= 'utf-8') as file):
        for line in file:
            #line = file.readline()
            all_data.append(line)
    print(all_data.__sizeof__())

filenames = [f'./file {number}.txt' for number in range(1, 5)]

#линейный вызов
t1 = time.time()
read_info('file 1.txt')
read_info('file 2.txt')
read_info('file 3.txt')
read_info('file 4.txt')
t2 = time.time()
print(f'Время выполнения линейно:{t2-t1}')

#мультипроцессорный вызов

if __name__ == '__main__':
    t3 = time.time()
    for filename in filenames:
        multiprocessing.Process(target=read_info, args= filename).start()
    t4 = time.time()
    print(f'Время выполнения мультипроцессорно:{t4-t3}')