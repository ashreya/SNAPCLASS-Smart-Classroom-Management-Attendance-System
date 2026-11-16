import streamlit as st
import segno
import io

@st.dialog("Share Class link")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "http://localhost:8501"
    join_url = f"{app_domain}/?join-code={subject_code}"
    st.header("Scan to join")

    qr = segno.make(join_url)
    out = io.BytesIO()

    qr.save(out, kind = "png", scale = 10, border = 1)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Copy Link")
        st.code(join_url, language= "text")
        st.code(subject_code, language = "text")
        st.info("Copy this link to share on WhatsApp or Email")
    with col2:
        st.markdown("### Scan to join")
        st.image(out.getvalue(), caption = "QRCODE")
    # st.write("Enter the details of new subject")
    # sub_id = st.text_input("Subject Code", placeholder="CS101")
    # sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science")
    # sub_section = st.text_input("Section", placeholder = "A")

    # if st.button("Create Subject Now", type = "primary", width = "stretch"):
    #     if sub_id and sub_name and sub_section :
    #         try:
    #             create_subject(sub_id,sub_name,sub_section, teacher_id)
    #             st.toast("Subject Created Successfully!")
    #             st.rerun()
    #         except Exception as e:
    #             st.error(f"Error: {str(e)}")
    #         else:
    #             st.warning("Please fill all the fields")