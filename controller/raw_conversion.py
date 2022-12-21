# convert raw rules into readable by Python
def raw_to_cfg(raw):
    # create list to store the rules
    data = []
    # for every rule in raw rules
    for rule in raw:
        # split the rule by space
        rule = rule.split(' ')
        # append the rule into data list
        data.append(rule)
    # return the data
    return data

# convert raw rules into html format
def raw_to_html(raw):
    # create list to store the rules
    data = []
    # for every rule in raw rules
    for rule in raw:
        # split the rule by space
        rule = rule.split(' ')
        # append the rule into data list
        data.append(rule)
    # return the data
    return create_html(data)


# create rules in html format
def create_html(raw):
    # starting by <p> tag
    html_raw = '<p>'
    # for every rule in raw rules
    for line in raw:
        # append the rule to html_raw then end by <br>
        html_raw += f'{line}<br>'
    # end the html_raw by </p> tag
    html_raw += '</p>'

    # return the raw html rules
    return html_raw
