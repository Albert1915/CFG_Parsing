# import streamlit as front end framework
import streamlit as st
import os
from PIL import Image

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
    
    upload_file = st.file_uploader(
        'Upload Set of Rules dalam format .txt', type=['txt'])
    col1, col2 = st.columns(2, gap='small')  # 2 columns

    if upload_file and upload_file.type == 'text/plain':  # check if file is .txt
        if upload_file is not None:
            file = upload_file.getvalue().decode('utf-8')
            with open('model/rules.txt', 'w') as secondFile:
                for line in file:
                    if line != '\n':
                        secondFile.write(line)
            st.success("File berhasil diupload!")
            secondFile.close()
        else:
            st.error("File tidak ada!")

    raw_cfg = open_file('model/rules.txt')
    cnf = raw_to_cfg(raw_cfg)
    st.write(cnf)


    # Untuk Menampilkan Judul
    st.write(f"<h1 style='text-align:center; '>{title}</h1>", unsafe_allow_html=True)
    st.write(f"<h2 style='text-align:center; '>{title2}</h2>", unsafe_allow_html=True)
    
    # Pisah web menjadi dua kolom, kolom kanan menampilkan cnf rule, kolom kiri menampilkan filling table
    kiri, kanan = st.columns(2, gap='small')

    # prepare the left column
    with kiri:
        st.write("### CNF Rules:")
        st.write(raw_cfg)

    # prepare the right column
    with kanan:
        # the input sentence text field
        string_input = st.text_input('Masukkan Kalimat:')
        # convert sentence into list
        list_string = string_input.split(' ')
        # check button
        button_click = st.button('Check', type='primary')

        # action if button clicked
        if button_click:
            # show error when no string or just one string entered
            if len(list_string) <= 1:
                st.error("Masukkan kalimat yang valid (minimal 2 kata)")
            # else, process the filing table
            elif string_input != '':
                st.write('<br><p>Mengisi Table:</p>', unsafe_allow_html=True)
                parse(cnf, string_input.split(' '))
