import streamlit as st

# إعداد الصفحة وتوسيع الشاشة
st.set_page_config(page_title="Nebulous Vision - القمر", page_icon="🌙", layout="wide")

# تصميم الواجهة بالألوان الداكنة (فضاء وظل القمر)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #05070b;
        color: white;
    }
    .main-title {
        font-size: 45px;
        font-weight: bold;
        color: #00d2ff;
        text-align: center;
        text-shadow: 0px 0px 10px rgba(0, 210, 255, 0.5);
    }
    .sub-title {
        font-size: 20px;
        color: #c0d0e0;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        background: linear-gradient(45deg, #00d2ff, #3a7bd5);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 15px;
        width: 100%;
        height: 60px;
        border: none;
        box-shadow: 0px 4px 10px rgba(0, 210, 255, 0.3);
    }
    .blind-button>button {
        background: linear-gradient(45deg, #ff9900, #ff5e62);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 15px;
        width: 100%;
        height: 60px;
        border: none;
        box-shadow: 0px 4px 10px rgba(255, 153, 0, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# قائمة اختيار اللغة في الشريط الجانبي (Sidebar)
lang = st.sidebar.selectbox(
    "🌍 Choose Language / اختر اللغة",
    ["العربية", "English", "Русский", "Français", "Deutsch"],
)

# تغيير النصوص بناءً على اللغة المتاحة
if lang == "العربية":
  title = "Nebulous Vision"
  subtitle = (
      "استعد لاكتشاف القمر وتفاصيله وموارده<br>من إنشاء فريق انحراف سديمي"
  )
  btn_normal = "🚀 أبدأ الاستكشاف (الوضع العادي)"
  btn_blind = "🎧 قسم المكفوفين (الاستكشاف الصوتي وتسهيل الوصول)"
elif lang == "Русский":
  title = "Nebulous Vision"
  subtitle = (
      "Приготовьтесь исследовать Луну, ее детали и ресурсы<br>Создано командой"
      " Nebulous Drift"
  )
  btn_normal = "🚀 Начать исследование"
  btn_blind = "🎧 Режим доступности (для слабовидящих)"
elif lang == "Français":
  title = "Nebulous Vision"
  subtitle = (
      "Préparez-vous à explorer la Lune, ses détails et ses ressources<br>Créé"
      " par l'équipe Nebulous Drift"
  )
  btn_normal = "🚀 Commencer l'exploration"
  btn_blind = "🎧 Mode accessibilité (Déficients visuels)"
elif lang == "Deutsch":
  title = "Nebulous Vision"
  subtitle = (
      "Bereiten Sie sich darauf vor, den Mond zu erkunden<br>Erstellt vom"
      " Nebulous Drift Team"
  )
  btn_normal = "🚀 Erkundung starten"
  btn_blind = "🎧 Barrierefreiheitsmodus (Sehbehinderte)"
else:  # English
  title = "Nebulous Vision"
  subtitle = (
      "Get ready to explore the Moon, its details, and resources<br>Created by"
      " Nebulous Drift Team"
  )
  btn_normal = "🚀 Start Exploration"
  btn_blind = "🎧 Accessibility Mode (For Visually Impaired)"

# عرض المحتوى في منتصف الشاشة بشكل منسق
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
  st.write("<br><br>", unsafe_allow_html=True)
  st.markdown(f"<h1 class='main-title'>{title}</h1>", unsafe_allow_html=True)
  st.markdown(f"<p class='sub-title'>{subtitle}</p>", unsafe_allow_html=True)
  st.write("<br>", unsafe_allow_html=True)

  # زر الاستكشاف العادي
  if st.button(btn_normal):
    st.success("تم تفعيل وضع الاستكشاف العادي بنجاح! جاري الانتقال...")

  st.write("<br>", unsafe_allow_html=True)

  # زر المكفوفين (تحت وزي ما طلبتي بالضبط)
  if st.button(btn_blind, key="blind_btn"):
    st.info(
        "🎧 جاري تشغيل واجهة الاستكشاف الصوتي وقراءة البيانات للمكفوفين..."
    )
