import random

import streamlit as st
import streamlit_extras as stx

st.title("Welcome to KizCombos!")

# Streamlit app goes here
st.write("Your source of endless combos for your Kizomba practice routines.")

moves = [
    "Side Opening",
    "Virgula",
    "Virgula Shuffle",
    "Virgula Double Shuffle",
    "Hesitation",
    "Quarter Turn Shuffle",
    "Quarter Turn",
    "Buddha Suave",
    "Man's Saida",
    "Lady's Saida",
    "Casamento",
    "Lady's Saida Shuffle",
    "Lady's Saida Tap",
    "Block Block Turn",
    "Walk Walk Turn",
    "Around The World",
    "Lady's Saida Opening",
    "Diamond Step",
]

selected_moves = st.multiselect(
    "Select the moves you want to include in your combo:", moves
)

# Generate a random sequence of moves of length `combo_length`
if selected_moves:
    st.write("Select the number of moves you want in your combo:")
    combo_length = st.slider(
        "Combo length",
        min_value=2,
        max_value=10,
        value=3,
    )
    generate = st.button("Generate New Combo!")
    if not generate:
        st.stop()
    else:
        sequence = random.choices(selected_moves, k=combo_length)
        st.divider()
        for i, move in enumerate(sequence):
            # st.write(f"{i+1}. {move}")
            st.write(f"{move}")
            if i < len(sequence) - 1:
                st.write(":arrow_down_small:")

        st.divider()
        st.write("Enjoy your dance!")
