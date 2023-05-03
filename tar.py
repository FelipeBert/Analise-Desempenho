import time
import os
import psutil
import tarfile
import sys

max_size = 16 * 1024 * 1024  # Tamanho do Dicionario: 512 MB em bytes
sys.setrecursionlimit(max_size)

nome_arquivo = 'arquivo.tar'

with tarfile.open('arquivo.tar', 'w') as tar_file:
    tar_file.add('Arquivo_teste 1MB')

start_time = time.time()
start_resources = psutil.Process(os.getpid()).memory_info()

with tarfile.open('arquivo.tar', 'a') as tar_file:
    tar_file.add('Arquivo_teste 1MB')

end_time = time.time()
end_resources = psutil.Process(os.getpid()).memory_info()

time_elapsed = end_time - start_time
cpu_time = time.process_time()
mem_usage = (end_resources.rss - start_resources.rss) / 1024 / 1024

print('Tempo de compactação: {:.2f} segundos'.format(time_elapsed))
print('Tempo de CPU utilizado: {:.2f} segundos'.format(cpu_time))
print('Uso máximo de memória: {:.2f} MB'.format(mem_usage))
