# open the uploaded file and return the raw cnf rules

def open_file(uploaded_file):
    # prepare empty list
    raw = []
    # if file is uploaded
    if uploaded_file is not None:
        # read the file
        raw = uploaded_file.read().decode('utf-8').split(' ')
    # return the raw cnf rules
    return raw
