import streamlit as st

# إعداد الصفحة وتوسيعها
st.set_page_config(
    page_title="Nebulous Vision", page_icon="🌙", layout="wide"
)

# تصميم الواجهة المطور بدقة مطابقة لطلباتك وصورة القمر الحقيقية
st.markdown(
    """
    <style>
    .stApp {
        background-color: #020408;
        color: white;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    
    /* شعار ناسا الأصلي مكبر وفي مكانه في الزاوية */
    .top-header {
        width: 100%;
        display: flex;
        justify-content: flex-end;
        padding: 25px 45px;
        position: absolute;
        top: 0;
        right: 0;
        z-index: 20;
    }
    .nasa-logo {
        width: 110px;
        height: auto;
        filter: drop-shadow(0 0 15px rgba(0, 210, 255, 0.6));
    }

    /* حاوية المنتصف المتوازنة بدون فراغات مزعجة */
    .hero-wrapper {
        position: relative;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding-top: 30px;
        padding-bottom: 20px;
    }

    /* قمر ضخم جداً في الخلفية بتفاصيل وفوهات حقيقية وتدريج فخم */
    .moon-huge {
        position: absolute;
        width: 520px;
        height: 520px;
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg');
        background-size: cover;
        background-position: center;
        border-radius: 50%;
        z-index: 0;
        opacity: 0.75;
        box-shadow: inset -70px -70px 100px rgba(0, 0, 0, 0.9), 0 0 70px rgba(0, 210, 255, 0.3);
        -webkit-mask-image: radial-gradient(circle, rgba(0,0,0,1) 50%, rgba(0,0,0,0) 85%);
        mask-image: radial-gradient(circle, rgba(0,0,0,1) 50%, rgba(0,0,0,0) 85%);
    }

    /* اسم التطبيق في النص، ضخم ولامع بتدريج الأزرق والرمادي الفخم */
    .main-title {
        font-size: 68px;
        font-weight: 900;
        background: linear-gradient(135deg, #00d2ff 25%, #e2e8f0 85%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 45px rgba(0, 210, 255, 0.6);
        margin-bottom: 10px;
        position: relative;
        z-index: 2;
        letter-spacing: 1px;
    }

    /* الوصف تحت العنوان مباشرة بدون فراغات */
    .sub-title {
        font-size: 20px;
        color: #cbd5e1;
        margin-bottom: 25px;
        position: relative;
        z-index: 2;
        line-height: 1.5;
        font-weight: 500;
    }

    /* تنسيق الأزرار لتكون متناسقة وقريبة من المحتوى من غير مساحات فاضية */
    .stButton {
        display: flex;
        justify-content: center;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00d2ff, #1d4ed8);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 18px;
        width: 400px;
        max-width: 100%;
        height: 60px;
        border: none;
        box-shadow: 0px 6px 22px rgba(0, 210, 255, 0.4);
        transition: all 0.3s ease;
        position: relative;
        z-index: 2;
        margin: 6px auto;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0px 8px 30px rgba(0, 210, 255, 0.6);
        background: linear-gradient(135deg, #38bdf8, #2563eb);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# القائمة الجانبية للغات
lang = st.sidebar.selectbox(
    "🌍 Choose Language / اختر اللغة",
    ["العربية", "English", "Русский", "Français", "Deutsch"],
)

# النصوص بدون أي إيموجي نهائياً
if lang == "العربية":
  subtitle = (
      "استعد لاكتشاف القمر وتفاصيله وموارده<br>من إنشاء فريق انحراف سديمي"
  )
  btn_normal = "أبدأ الاستكشاف"
  btn_blind = "قسم المكفوفين (الاستكشاف الصوتي)"
elif lang == "Русский":
  subtitle = (
      "Приготовьтесь исследовать Луну, ее детали и ресурсы<br>Создано командой"
      " Nebulous Drift"
  )
  btn_normal = "Начать исследование"
  btn_blind = "Для слабовидящих"
elif lang == "Français":
  subtitle = (
      "Préparez-vous à explorer la Lune, ses détails et ses ressources<br>Créé"
      " par l'équipe Nebulous Drift"
  )
  btn_normal = "Commencer l'exploration"
  btn_blind = "Mode accessibilité"
elif lang == "Deutsch":
  subtitle = (
      "Bereiten Sie sich darauf vor, den Mond zu erkunden<br>Erstellt vom"
      " Nebulous Drift Team"
  )
  btn_normal = "Erkundung starten"
  btn_blind = "Barrierefreiheit"
else:
  subtitle = (
      "Get ready to explore the Moon, its details, and resources<br>Created by"
      " Nebulous Drift Team"
  )
  btn_normal = "Start Exploration"
  btn_blind = "Accessibility Mode"

# عرض شعار ناسا الأصلي مكبر في الزاوية
st.markdown(
    """
    <div class="top-header">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo" alt="NASA Logo">
    </div>
    """,
    unsafe_allow_html=True,
)

# القمر الضخم الحقيقي في الخلفية واسم التطبيق والوصف متقاربين وبدون فراغات
st.markdown(
    f"""
    <div class="hero-wrapper">
        <div class="moon-huge"></div>
        <h1 class="main-title">Nebulous Vision</h1>
        <p class="sub-title">{subtitle}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# الأزرار مترتبة تحت بعضها بمسافات مضبوطة
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  if st.button(btn_normal):
    st.success("تم تفعيل وضع الاستكشاف بنجاح!")
  if st.button(btn_blind, key="blind_btn"):
    st.info("جاري تفعيل واجهة الاستكشاف الصوتي وقراءة البيانات للمكفوفين...")
