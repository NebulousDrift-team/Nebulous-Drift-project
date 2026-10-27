import streamlit as st

# إعداد الصفحة وتوسيعها
st.set_page_config(
    page_title="Nebulous Vision - القمر", page_icon="🌙", layout="wide"
)

# تصميم الواجهة المطور (مطابق تماماً لرسوماتك الفنية)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #05070b;
        color: white;
    }
    
    /* حاوية المحتوى الرئيسي في المنتصف */
    .hero-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        position: relative;
        padding-top: 20px;
    }

    /* تأثير القمر الخلفي المتدرج الذي يختفي من الأسفل */
    .moon-bg {
        position: absolute;
        width: 350px;
        height: 350px;
        background: radial-gradient(circle, #2a344a 0%, #151a24 60%, #05070b 90%);
        border-radius: 50%;
        top: 80px;
        z-index: 0;
        opacity: 0.6;
        box-shadow: 0 0 50px rgba(0, 210, 255, 0.15);
        /* تدرج لإخفاء القمر من الأسفل */
        -webkit-mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 60%, rgba(0,0,0,0) 100%);
        mask-image: linear-gradient(to bottom, rgba(0,0,0,1) 60%, rgba(0,0,0,0) 100%);
    }

    /* عنوان التطبيق: أزرق مدرج مع رمادي ويلمع */
    .main-title {
        font-size: 52px;
        font-weight: 900;
        background: linear-gradient(135deg, #00d2ff 20%, #8a99ad 80%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 25px rgba(0, 210, 255, 0.4);
        margin-bottom: 10px;
        position: relative;
        z-index: 1;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }

    /* الوصف تحت العنوان */
    .sub-title {
        font-size: 19px;
        color: #b0c4de;
        margin-bottom: 40px;
        position: relative;
        z-index: 1;
        line-height: 1.6;
    }

    /* تنسيق الأزرار لتكون أكبر وفي المنتصف */
    .stButton > button {
        background: linear-gradient(135deg, #00d2ff, #3a7bd5);
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 18px;
        width: 450px;
        max-width: 100%;
        height: 65px;
        border: none;
        box-shadow: 0px 6px 20px rgba(0, 210, 255, 0.35);
        transition: 0.3s ease;
        position: relative;
        z-index: 1;
        margin: 10px auto;
    }
    
    .stButton > button:hover {
        transform: scale(1.03);
        box-shadow: 0px 8px 25px rgba(0, 210, 255, 0.5);
    }

    /* زر المكفوفين بتصميم مميز */
    .blind-btn > button {
        background: linear-gradient(135deg, #ff9900, #ff5e62) !important;
        box-shadow: 0px 6px 20px rgba(255, 153, 0, 0.35) !important;
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

# ترجمة النصوص حسب اللغة المختارة
if lang == "العربية":
  subtitle = (
      "استعد لاكتشاف القمر وتفاصيله وموارده<br>من إنشاء فريق انحراف سديمي"
  )
  btn_normal = "🚀 أبدأ الاستكشاف"
  btn_blind = "🎧 قسم المكفوفين (الاستكشاف الصوتي)"
elif lang == "Русский":
  subtitle = (
      "Приготовьтесь исследовать Луну, ее детали и ресурсы<br>Создано командой"
      " Nebulous Drift"
  )
  btn_normal = "🚀 Начать исследование"
  btn_blind = "🎧 Режим доступности (для слабовидящих)"
elif lang == "Français":
  subtitle = (
      "Préparez-vous à explorer la Lune, ses détails et ses ressources<br>Créé"
      " par l'équipe Nebulous Drift"
  )
  btn_normal = "🚀 Commencer l'exploration"
  btn_blind = "🎧 Mode accessibilité"
elif lang == "Deutsch":
  subtitle = (
      "Bereiten Sie sich darauf vor, den Mond zu erkunden<br>Erstellt vom"
      " Nebulous Drift Team"
  )
  btn_normal = "🚀 Erkundung starten"
  btn_blind = "🎧 Barrierefreiheitsmodus"
else:
  subtitle = (
      "Get ready to explore the Moon, its details, and resources<br>Created by"
      " Nebulous Drift Team"
  )
  btn_normal = "🚀 Start Exploration"
  btn_blind = "🎧 Accessibility Mode"

# تنظيم الواجهة العلوية (شعار ناسا في الجنب وعنوان التطبيق في المنتصف)
top_col1, top_col2, top_col3 = st.columns([1, 4, 1])

with top_col3:
  # شعار ناسا البسيط في الجنب
  st.markdown(
      """
        <div style="text-align: left; padding-top: 10px;">
            <span style="background: #0b3d91; color: white; padding: 8px 14px; border-radius: 50px; font-weight: bold; font-family: sans-serif; box-shadow: 0 0 10px rgba(11,61,145,0.8); border: 2px solid #fc3d21;">NASA</span>
        </div>
        """,
      unsafe_allow_html=True,
  )

# المحتوى الرئيسي والمنتصف (القمر والعنوان والأزرار)
st.markdown("<div class='hero-container'>", unsafe_allow_html=True)
st.markdown("<div class='moon-bg'></div>", unsafe_allow_html=True)
st.markdown(
    "<h1 class='main-title'>Nebulous Vision</h1>", unsafe_allow_html=True
)
st.markdown(f"<p class='sub-title'>{subtitle}</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# أزرار البدء في المنتصف وبحجم كبير
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
  st.write("<br>", unsafe_allow_html=True)
  if st.button(btn_normal, key="normal_btn"):
    st.success("تم تفعيل وضع الاستكشاف بنجاح!")

  st.write("<br>", unsafe_allow_html=True)
  # وضعنا كلاس خاص لزر المكفوفين لتمييزه باللون البرتقالي
  if st.button(btn_blind, key="blind_btn"):
    st.info("جاري تفعيل واجهة الاستكشاف الصوتي وقراءة البيانات للمكفوفين...")
