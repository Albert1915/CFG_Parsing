# Library Yang Digunakan
import streamlit as st

# import necessary functions
from controller.open_file import open_file
from controller.raw_conversion import raw_to_cfg
from controller.cyk_algorithm.cyk_parse import parse

# prepare the web view
def run_streamlit():
    # title for the web
    title = 'PARSING INDONESIAN SENTENCE WITH CYK ALGORITHM'
    title2 = 'KELOMPOK 2 KELAS E'

    # setup the web configuration
    st.set_page_config(layout='wide', page_title=title, menu_items={
        'About': f"""
        ### {title}
        Made by Group 2 in Class E  
        GitHub: https://github.com/Albert1915/CYK_Algorithm
        """
    })
    
    # Menyiapkan Cnf Rule
    raw_cfg = open_file('model/cnf.txt')
    # convert the raw cnf rules into readable format for Python
    cnf = raw_to_cfg(raw_cfg)

    # Memanggil Title pada web
    st.write(f"<h1 style='text-align:center; '>{title}</h1>", unsafe_allow_html=True)
    st.write(f"<h2 style='text-align:center; '>{title2}</h2>", unsafe_allow_html=True)
    # Link
    st.write("<h5 style='text-align: center;'><a href='https://github.com/Albert.1915/CFG_Parsing'>Albert1915/CFG_Parsing</a></h2>", unsafe_allow_html=True)

    # Menampilkan Rules diweb
    st.write("### CNF Rules:")
    st.write(raw_cfg)

        # the input sentence text field
    string_input = st.text_input('Input Sentence')
        # convert sentence into list
    list_string = string_input.split(' ')
        # check button
    button_click = st.button('Check', type='primary')

    
        # action if button clicked
    if button_click:
            # show error when no string or just one string entered
            if len(list_string) <= 1:
                st.error("Sentence can't be null or a word.")
            # else, process the filing table
            # markdown to clear the previous table
            elif string_input != '':
                # close table or not
                st.checkbox('Close Table', value=False)
                st.write('<br><p>Filling Table:</p>', unsafe_allow_html=True)
                parse(cnf, string_input.split(' '))
