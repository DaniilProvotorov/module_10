import threading
import time


def write_words(word_count, file_name):
    with (open(file_name, 'a', encoding='utf-8')) as file:
        for i in range(word_count):
            time.sleep(0.1)
            file.write(f'Какое-то слово № {i+1}\n')
    print(f'Завершилась запись в файл {file_name}')


thr = threading.Thread(target=write_words, args= (10, 'example5.txt'))
thr2 = threading.Thread(target=write_words, args=(30,'example6.txt') )
thr3 = threading.Thread(target=write_words, args=(200,'example7.txt' ))
thr4 = threading.Thread(target=write_words, args=(100,'example8.txt' ))


t1 = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
t2 = time.time()
t3 = time.time()
thr.start()
thr2.start()
thr3.start()
thr4.start()
thr.join()
thr2.join()
thr3.join()
thr4.join()
t4 = time.time()
print(t2-t1)
print(t4-t3)