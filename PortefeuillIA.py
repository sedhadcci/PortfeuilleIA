def load_data():
    url ='https://github.com/sedhadcci/PortfeuilleIA/blob/main/PFIA.xlsx'    
    data = pd.read_excel(url , sheet_name='Feuil1')
    return data
def search_ia_by_siren():
    st.title('Recherche IA par SIREN')
    siren = st.text_input('Entrez le SIREN à rechercher:')
    if siren:
        result = data[data['SIREN'] == siren]['IA'].values[0]
        st.write('L\'ingénieur d\'affaires correspondant à ce SIREN est:', result)

if __name__ == '__main__':
    data = load_data()
    st.set_page_config(page_title='Recherche IA par SIREN')
    search_ia_by_siren()
