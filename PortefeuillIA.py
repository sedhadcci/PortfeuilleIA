def load_data():
    data = pd.read_excel('nom_du_fichier.xlsx', sheet_name='nom_de_la_feuille')
    return data

def search_ia_by_siren():
    data = load_data()
    siren = st.text_input('Entrez le SIREN à rechercher:')
    if siren:
        result = data[data['SIREN'] == siren]['IA'].values[0]
        st.write('L\'ingénieur d\'affaires correspondant à ce SIREN est:', result)

if __name__ == '__main__':
    st.set_page_config(page_title='Recherche IA par SIREN')
    st.title('Recherche IA par SIREN')
    search_ia_by_siren()
