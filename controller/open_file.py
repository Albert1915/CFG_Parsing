# open the uploaded cnf rule file
def open_file(uploaded_file):
    # prepare the empty list
    data = [] 
    # if the file is not empty
    if uploaded_file is not None:
        # read the file
        raw = uploaded_file.read().decode('utf-8').splitlines()
        # remove the empty line
        raw = list(filter(None, raw))
            

        # append each rule into data list while remove the new line
        for rule in raw:
            data.append(rule.strip('\n'))

    # return the raw cnf rules
    return data
