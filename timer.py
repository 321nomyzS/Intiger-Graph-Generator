import os
import time

literation = [1, 10, 10, 10, 10, 10, 10, 3, 1, 1, 1, 1, 1, 1]

for vertex_acc in range(1, 9):
    for proces_acc in range(1, 9):
        times = []
        for _ in range(literation[vertex_acc]):
            start_time = time.time()
            os.system(f"./output.exe {vertex_acc} {proces_acc} > /dev/null")
            end_time = time.time()
            times.append(end_time - start_time)

        print(vertex_acc, proces_acc, round(sum(times) / literation[vertex_acc], 7))
