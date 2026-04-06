import streamlit as st
import google.generativeai as genai
import PIL.Image

# إعداد الصفحة
st.set_page_config(page_title="مساعد كنان", page_icon="📚")
st.title("📚 مساعد الواجبات الذكي - كنان")

# إعداد الموديل الصحيح
genai.configure(api_key="AIzaSyAIrwvDQx47fH3NLM216qIP3qdu4IVlTsY")
model = genai.GenerativeModel('gemini-1.5-flash-latest')

uploaded_file = st.file_uploader("ارفعي صورة الواجب يا أمي", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = PIL.Image.open(uploaded_file)
    st.image(image, caption='تم رفع الصورة!')
    
    if st.button('حل الواجب'):
        with st.spinner('جاري التفكير...'):
            try:
                res = model.generate_content(["حل هذا الواجب بالتفصيل وبالعربي وبشرح بسيط", image])
                st.success("تم الحل!")
                st.write(res.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
