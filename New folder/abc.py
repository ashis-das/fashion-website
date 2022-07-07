try:
    file = open(filepath)
    data = file.read()
finally:
    file.close()