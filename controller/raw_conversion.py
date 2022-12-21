# convert raw rules into readable by Python
def raw_to_cfg(raw_rules):
    # prepare the empty list
    cfg = []
    # for each rule
    for rule in raw_rules:
        # split the rule into left and right side
        left, right = rule.split('->')
        # split the right side into list
        right = right.split('|')
        # append the rule into cfg list
        cfg.append([left, right])
    
    # return the cfg rules
    return cfg

# convert raw rules into readable by Python
def raw_to_cnf(raw_rules):
    # prepare the empty list
    cnf = []
    # for each rule
    for rule in raw_rules:
        # split the rule into left and right side
        left, right = rule.split('->')
        # split the right side into list
        right = right.split('|')
        # append the rule into cnf list
        cnf.append([left, right])
    
    # return the cnf rules
    return cnf

# create rule in html format
def create_rule_html(rule):
    # prepare the empty string
    html = ''
    # for each rule
    for x in rule:
        # append the rule into html string
        html += x + '<br>'
    
    # return the html string
    return html
