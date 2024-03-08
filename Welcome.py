import streamlit as st


st.set_page_config(page_title = "Personal Portfolio")
st.title("Welcome.")





# sidebar
st.write(f':blue[{'Explore Projects, Internship using Sidebar'}]')
sidebar_image_path = "profile1.png"
st.sidebar.image(sidebar_image_path,caption='Dhruv Rajput', width=100)
st.sidebar.success("Thank You for Visiting us")
st.write('\n')
st.write('\n')
# st.subheader('Thank you for Visiting my Portfolio')
# st.title('My title')

# apply image
image_path = "profile1.png"
st.image(image_path, width=200)

st.write('Name : Dhruv Rajput')
st.write('Location : Ghaziabad')
st.write('Phone Number : +91 8755930662')
st.write('Email : dhruvrajput583@gmail.com')
st.write('Github : https://github.com')
st.write('Linkedin : https://www.linkedin.com/in/dhruv-rajput-7429b3227/')
st.write('\n')
st.write('\n')
st.subheader('Download Updated Resume Here')
pdf_path = "5_resume.pdf"

# download Pdf
# if st.button("Download PDF"):
#     with open(pdf_path, "rb") as f:
#         pdf_bytes = f.read()
#     st.download_button(label="Download PDF", data=pdf_bytes, file_name="5_resume.pdf", mime="application/pdf")

with open(pdf_path, "rb") as f:
    pdf_bytes = f.read()
st.download_button(label="Download PDF", data=pdf_bytes, file_name="5_resume.pdf", mime="application/pdf")


# * optional kwarg unsafe_allow_html = True