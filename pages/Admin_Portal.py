import streamlit as st
import sqlite3
import pandas as pd

st.title("Admin Portal")

password = st.text_input(
    "Admin Password",
    type="password"
)

if password == "TBAdmin@2026":

    conn = sqlite3.connect(
        "talentvault.db"
    )

    df = pd.read_sql_query(
        "SELECT * FROM candidates",
        conn
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    if len(df) > 0:

        selected_name = st.selectbox(
            "Select Candidate to Delete",
            df["name"].tolist()
        )

        if st.button(
            "🗑 Delete Candidate"
        ):

            selected_id = df[
                df["name"] == selected_name
            ]["id"].iloc[0]

            cursor = conn.cursor()

            cursor.execute(
                """
                DELETE FROM candidates
                WHERE id=?
                """,
                (int(selected_id),)
            )

            conn.commit()

            st.success(
                f"{selected_name} deleted"
            )

            st.rerun()

    conn.close()