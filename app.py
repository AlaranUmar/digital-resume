from pathlib import Path

import streamlit as st
from PIL import Image



# Path Setting
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "Umar.jpg"





# General settings
PAGE_TITLE = "Digital CV | ALARAN UMAR"
PAGE_ICON = "random"
NAME = "ALARAN UMAR"
DESCRIPTION = """
WEB DEVELOPER\n
WEB DESIGNER\n
GRAPHICS DESIGNER\n
UI/UX DESIGNER\n
FRONT-END DEVELOPER\n

"""
EMAIL = "alaranumar@gmail.com"
SOCIAL_MEDIA = {
    "Youtube": "https://youtube.com",
    "Github": "https://Github.com",
    "Instagram": "https://Instagram.com",
    "Portfolio": "https://Alaranumar.io"
}
PROJECTS = {
    "Youtube project": "https://youtube.com"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



st.header("MY DIGITAL RESUME")
# LOAD CSS,PDF & PROFILE PIC
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



# HERO SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

st.write(EMAIL)

#  SOCIAL LINKS
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index , (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# EXPERIENCE AND QUALIFICATION
st.write("#")
st.subheader("Experience and Qualification")
st.write("""
    - > 7 Years Experience
    - > Strong Hands Experience
    - > Excellent Team Player
         """)

# SKILLS
st.write("#")
st.subheader("HARD SKILLS")
st.write(
    """
    - > Web Developing: JavaScript, HTML
    - > Web Designig: CSS, Figma
    - > Graphics Designing: CorelDraw, Adobe Creative CLoud
    """
)

# WORK HISTORY
st.write("#")
st.subheader("WORK HISORY")
st.write("---")

# JOB 1
st.write("#")
st.write("***WEB DEVELOPER*** | Khattab Education | Khattab Fitness")
st.write("02/2024 - Present")
st.write("""
    - ֎ Used HTML
    - ֎ Used CSS
    - ֎ Used JAVASCRIPT
    - ֎ Used PYTHON
    """)


# JOB 2
st.write("#")
st.write("***GRAPHICS DESIGNER*** | Erudite Millenium ltd")
st.write("02/2024 - Present")
st.write("""
    - ֎ Used HTML
    - ֎ Used CSS
    - ֎ Used JAVASCRIPT
    - ֎ Used PYTHON
    """)


# JOB 3
st.write("#")
st.write("***WEB DESIGNER*** | Erudite Millenium ltd")
st.write("02/2020 - Present")
st.write("""
    - ֎ Used HTML
    - ֎ Used CSS
    - ֎ Used JAVASCRIPT
    - ֎ Used PYTHON
    """)



#  PROJECTS AND ACCOMPLISHMENT
st.write("#")
st.subheader("PROJECTS AND ACCOMPLISHMENTS")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")