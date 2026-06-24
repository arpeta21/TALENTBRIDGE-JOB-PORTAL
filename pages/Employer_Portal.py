import streamlit as st
import sqlite3
import pandas as pd
import os

st.title("Employer Portal")

password = st.text_input(
    "Employer Access Code",
    type="password"
)

if password == "talentbridge123":

    conn = sqlite3.connect(
        "talentvault.db"
    )

    df = pd.read_sql_query(
        "SELECT * FROM candidates",
        conn
    )

    conn.close()

    st.dataframe(
        df,
        use_container_width=True
    )

    for _, row in df.iterrows():

        if (
            row["resume_path"]
            and
            os.path.exists(
                row["resume_path"]
            )
        ):

            with open(
                row["resume_path"],
                "rb"
            ) as file:

                st.download_button(
                    f"Download CV - {row['name']}",
                    file.read(),
                    file_name=os.path.basename(
                        row["resume_path"]
                    ),
                    key=f"cv_{row['id']}"
                )