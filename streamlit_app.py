import streamlit as st

st.set_page_config(
    page_title="Conta Calorie",
    page_icon=":guardsman:",  # Add a page icon (optional)
    layout="wide",  # Choose between "centered" or "wide" layout
    initial_sidebar_state="expanded"  # Choose between "expanded" or "collapsed"
)

carboidrati = {
    "Gallette di riso": 35,
    "Pasta integrale": 50,
    "Riso basmati": 45,
    "Pane integrale": 60,
    "Tonno in scatola": 132,
    "Uova": 155,
    "Yogurt greco": 59,
    "Cracker integrali": 50,
    "Fette biscottate": 40,
    "Cereali": 60,
    "Farina d'avena": 60,
    "Patate": 77
}

st.title("Conta Calorie")
c1,c2,c3 = st.columns([10, 5, 10])

with c1:
    selected_carboidrati = st.selectbox(
        "Quale alimento vorresti mangiare?",
        carboidrati.keys(),
        key="carboidrati"
    )
    sel_qty = st.number_input(
        "Quante porzioni?",
        min_value=5,
        max_value=3000,
        step=5,
        key="carboidrati1"
    )
with c3:
    selected_variante_carboidrati = st.selectbox(
        "Quale pietanza vorresti al posto della precedente?",
        carboidrati.keys(),
        key="carboidrati2"
    )

qty_res =  (carboidrati[selected_variante_carboidrati] * sel_qty) / carboidrati[selected_carboidrati]
c1,c2 = st.columns([2,1])
with c2:
    st.markdown(f"""
                Devi mangiare {qty_res:.0f}gr"""
                )
    
proteine = {
    "Gallette di riso": 35,
    "Pasta integrale": 50,
    "Riso basmati": 45,
    "Pane integrale": 60,
    "Tonno in scatola": 132,
    "Uova": 155,
    "Yogurt greco": 59,
    "Cracker integrali": 50,
    "Fette biscottate": 40,
    "Cereali": 60,
    "Farina d'avena": 60,
    "Patate": 77
}

st.title("Conta Calorie")
c1,c2,c3 = st.columns([10, 5, 10])

with c1:
    selected_proteine = st.selectbox(
        "Quali proteine?",
        proteine.keys(),
        key="proteine"
    )
    sel_qty = st.number_input(
        "Quanti grammi?",
        min_value=5,
        max_value=3000,
        step=5,
        key="proteine1"
    )
with c3:
    selected_variante_proteine = st.selectbox(
        "Quale pietanza vorresti al posto della precedente?",
        proteine.keys(),
        key="proteine2"
    )

qty_res =  (proteine[selected_variante_proteine] * sel_qty) / proteine[selected_proteine]
c1,c2 = st.columns([2,1])
with c2:
    st.markdown(f"""
                Devi mangiare {qty_res:.0f}gr"""
                )
    
grassi = {
    "Gallette di riso": 35,
    "Pasta integrale": 50,
    "Riso basmati": 45,
    "Pane integrale": 60,
    "Tonno in scatola": 132,
    "Uova": 155,
    "Yogurt greco": 59,
    "Cracker integrali": 50,
    "Fette biscottate": 40,
    "Cereali": 60,
    "Farina d'avena": 60,
    "Patate": 77
}

st.title("Conta Calorie")
c1,c2,c3 = st.columns([10, 5, 10])

with c1:
    selected_grassi = st.selectbox(
        "Quali grassi?",
        grassi.keys(),
        key="grassi"
    )
    sel_qty = st.number_input(
        "Quanti grammi?",
        min_value=5,
        max_value=3000,
        step=5,
        key="grassi1"
    )
with c3:
    selected_variante_grassi = st.selectbox(
        "Quale pietanza vorresti al posto della precedente?",
        grassi.keys(),
        key="grassi2"
    )

qty_res =  (grassi[selected_variante_grassi] * sel_qty) / grassi[selected_grassi]
c1,c2 = st.columns([2,1])
with c2:
    st.markdown(f"""
                Devi mangiare {qty_res:.0f}gr"""
                )