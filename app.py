import streamlit as st

# إعداد الصفحة وتوسيعها
st.set_page_config(
    page_title="Nebulous Vision", page_icon="🌙", layout="wide"
)

# تصميم الواجهة الاحترافي والمطابق لطلباتك بدقة
st.markdown(
    """
    <style>
    .stApp {
        background-color: #020408;
        color: white;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    
    /* شعار ناسا الأصلي في الأعلى على الجنب */
    .top-header {
        width: 100%;
        display: flex;
        justify-content: flex-end;
        padding: 20px 40px;
        position: absolute;
        top: 0;
        right: 0;
        z-index: 10;
    }
    .nasa-logo {
        width: 75px;
        height: auto;
        filter: drop-shadow(0 0 12px rgba(0, 210, 255, 0.5));
    }

    /* حاوية المنتصف الشاملة للقمر والعنوان */
    .hero-wrapper {
        position: relative;
        width: 100%;
        min-height: 80vh;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 40px 20px;
    }

    /* قمر 3D احترافي في الخلفية بظلال وتجسيم كروي مذهل */
    .moon-3d {
        position: absolute;
        width: 390px;
        height: 390px;
        background: radial-gradient(circle at 35% 35%, #64748b 0%, #334155 35%, #0f172a 70%, #020408 95%);
        border-radius: 50%;
        z-index: 0;
        box-shadow: inset -50px -50px 80px rgba(0, 0, 0, 0.95), 0 0 60px rgba(0, 210, 255, 0.25);
        -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 55%, rgba(0,0,0,0) 95%);
        mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 55%, rgba(0,0,0,0) 95%);
        opacity: 0.9;
    }

    /* اسم التطبيق في المنتصف، كبير ولامع بتدريج الأزرق والرمادي */
    .main-title {
        font-size: 64px;
        font-weight: 900;
        background: linear-gradient(135deg, #00d2ff 20%, #cbd5e1 80%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 40px rgba(0, 210, 255, 0.5);
        margin-bottom: 15px;
        position: relative;
        z-index: 2;
        letter-spacing: 1px;
    }

    /* الوصف تحت العنوان */
    .sub-title {
        font-size: 20px;
        color: #94a3b8;
        margin-bottom: 40px;
        position: relative;
        z-index: 2;
        line-height: 1.6;
        font-weight: 500;
    }

    /* الأزرار في المنتصف، ضخمة وبدون أي إيموجي */
    .stButton > button {
        background: linear-gradient(135deg, #00d2ff, #1d4ed8);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 18px;
        width: 420px;
        max-width: 100%;
        height: 65px;
        border: none;
        box-shadow: 0px 6px 20px rgba(0, 210, 255, 0.35);
        transition: all 0.3s ease;
        position: relative;
        z-index: 2;
        margin: 10px auto;
    }
    
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0px 8px 25px rgba(0, 210, 255, 0.55);
        background: linear-gradient(135deg, #38bdf8, #2563eb);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# الشريط الجانبي لاختيار اللغات
lang = st.sidebar.selectbox(
    "🌍 Choose Language / اختر اللغة",
    ["العربية", "English", "Русский", "Français", "Deutsch"],
)

# النصوص بدون أي إيموجي
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

# عرض شعار ناسا الأصلي في الجنب
st.markdown(
    """
    <div class="top-header">
        <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo" alt="NASA Logo">
    </div>
    """,
    unsafe_allow_html=True,
)

# القمر الـ 3D في الخلفية واسم التطبيق في النص
st.markdown(
    f"""
    <div class="hero-wrapper">
        <div class="moon-3d"></div>
        <h1 class="main-title">Nebulous Vision</h1>
        <p class="sub-title">{subtitle}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# الأزرار في المنتصف وبحجم كبير ومنسق
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  if st.button(btn_normal):
    st.success("تم تفعيل وضع الاستكشاف بنجاح!")
  if st.button(btn_blind, key="blind_btn"):
    st.info("جاري تفعيل واجهة الاستكشاف الصوتي وقراءة البيانات للمكفوفين...")
