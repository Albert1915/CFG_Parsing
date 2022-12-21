# import streamlit as front end framework
import streamlit as st
import os


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

    with col1:
        string_input = st.text_input(
            'Kalimat Yang Dicek : ', placeholder='Masukan Kalimat')
        list_string = string_input.split(' ')
        button_click = st.button('Cek Kalimat', type='primary')

        if button_click:
            if len(list_string) <= 1:
                st.error("Kalimat tidak boleh kosong!")
            elif string_input != '':
                st.write('<br><p>Filling Table:</p>', unsafe_allow_html=True)
                parse(cnf, string_input.split(' '))

    with col2:
        st.write("### Set of Rules :")
        # checking if rules.txt is empty
        if os.stat('model/rules.txt').st_size == 0:
            st.info("Upload rules terlebih dahulu!")
            contoh = Image.open('model/contoh.jpg')
            st.image(contoh, caption='Contoh Format Set of Rules')
        else:
            st.write(raw_cfg)
