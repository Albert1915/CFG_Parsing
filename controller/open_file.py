# open the uploaded file and return the raw cnf rules file
def open_file(file):
    # read the file
    raw = file.read().decode('utf-8')
    # split the file by line
    raw = raw.splitlines()
    # return the raw rules
    return raw

