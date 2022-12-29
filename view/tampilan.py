# import streamlit as front end framework
import streamlit as st

# import necessary functions
from controller.open_file import open_file
from controller.raw_conversion import raw_to_cfg
from controller.cyk_algorithm.cyk_parse import parse

# prepare the web view
def run_streamlit():
    # setup the web title
    title = 'Algoritma CYK For CFG Parsing'
    title2 = 'KELOMPOK 2 KELAS E'
   
    # setup the web configuration
    st.set_page_config(layout='wide', page_title=title, menu_items={
        'About': f"""
        ### {title}
        GitHub: https://github.com/Albert1915/CFG_Parsing
        """
    })
    
    # prepare the cnf rules
    raw_cfg = open_file('rules/cnf.txt')
    # convert the raw cnf rules into readable format for Python
    cnf = raw_to_cfg(raw_cfg)

    # Untuk Menampilkan Judul
    st.write(f"<h1 style='text-align:center; '>{title}</h1>", unsafe_allow_html=True)
    st.write(f"<h2 style='text-align:center; '>{title2}</h2>", unsafe_allow_html=True)
    st.write("<h5 style='text-align: center;'> GitHub: <a href='https://github.com/Albert1915/CFG_Parsing'>Albert1915/CFG_Parsing</a></h2>", unsafe_allow_html=True)
    
    st.write("### CNF RULES:")
    st.write(raw_cfg)

    # the input sentence text field
    string_input = st.text_input('Masukkan Kalimat:')
    # convert sentence into list
    list_string = string_input.split(' ')
    # check button
    button_click = st.button('Check', type='primary')
    # untuk meminimize tabel yang muncul
    st.write('<br>', unsafe_allow_html=True)

        # action if button clicked
    if button_click:
            # show error when no string or just one string entered
            if len(list_string) <= 1:
                st.error("Masukkan kalimat yang valid (minimal 2 kata)")
            # else, process the filing table
            elif string_input != '':
                st.write('<br><p>Mengisi Table:</p>', unsafe_allow_html=True)
                st.write('<br>', unsafe_allow_html=True)
                # parse the sentence
                st.markdown('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
                # memilih apakah ingin menampilkan tabel atau tidak
                show_table = st.radio('Hapus Tabel?', ('Tidak', 'Ya'))
                if show_table == 'Tidak':
                    parse(cnf, string_input.split(' '))
             