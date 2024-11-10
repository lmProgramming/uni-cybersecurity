import os

file_size_in_mega_bytes = 5
with open(f"local files\{file_size_in_mega_bytes} megabytes", 'wb') as fout:
    fout.write(os.urandom(file_size_in_mega_bytes * 1024 * 1024))
