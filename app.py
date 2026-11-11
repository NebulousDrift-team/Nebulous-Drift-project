import os
import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة وتوسيعها
st.set_page_config(
    page_title="Nebulous Vision - Lunar GIS Atlas", page_icon="🌙", layout="wide"
)

# تتبع حالة التطبيق
if "started" not in st.session_state:
  st.session_state.started = False

if "selected_category" not in st.session_state:
  st.session_state.selected_category = "المياه"

# اكتشاف صورة الشعار تلقائياً
logo_file = "logo.png"
for f in [
    "logo.png",
    "logo.jpg",
    "logo.jpeg",
    "WhatsApp Image 2026-10-27 at 7.26.05 PM.jpeg",
]:
  if os.path.exists(f):
    logo_file = f
    break

# ==========================================
# الحالة الأولى: الواجهة الرئيسية
# ==========================================
if not st.session_state.started:

  st.markdown(
      """
    <style>
    .stApp {
        background-color: #020408;
        color: white;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    .nasa-logo {
        width: 100px;
        height: auto;
        filter: drop-shadow(0 0 15px rgba(0, 210, 255, 0.6));
    }
    .hero-wrapper {
        position: relative;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding-top: 20px;
        padding-bottom: 10px;
    }
    .moon-huge {
        position: absolute;
        width: 700px;
        height: 700px;
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg');
        background-size: cover;
        background-position: center;
        border-radius: 50%;
        z-index: 0;
        opacity: 0.85;
        box-shadow: inset -100px -100px 140px rgba(0, 0, 0, 0.95), 0 0 100px rgba(0, 210, 255, 0.4);
        -webkit-mask-image: radial-gradient(circle, rgba(0,0,0,1) 45%, rgba(0,0,0,0) 85%);
        mask-image: radial-gradient(circle, rgba(0,0,0,1) 45%, rgba(0,0,0,0) 85%);
    }
    .main-title {
        font-size: 76px;
        font-weight: 900;
        background: linear-gradient(135deg, #00d2ff 25%, #e2e8f0 85%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 50px rgba(0, 210, 255, 0.6);
        margin-bottom: 10px;
        position: relative;
        z-index: 2;
        letter-spacing: 1px;
    }
    .sub-title {
        font-size: 21px;
        color: #cbd5e1;
        margin-bottom: 20px;
        position: relative;
        z-index: 2;
        line-height: 1.5;
        font-weight: 500;
    }
    .stButton > button {
        font-size: 20px !important;
        font-weight: bold !important;
        border-radius: 18px !important;
        width: 420px !important;
        max-width: 100% !important;
        height: 65px !important;
        transition: all 0.3s ease !important;
        margin: 15px auto !important;
        background: linear-gradient(135deg, #cbd5e1 0%, #94a3b8 50%, #64748b 100%) !important;
        color: #0f172a !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        box-shadow: 0px 6px 25px rgba(148, 163, 184, 0.4) !important;
    }
    .stButton > button:hover {
        transform: scale(1.02);
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%) !important;
        color: #000000 !important;
    }
    .clean-section {
        max-width: 750px;
        margin: 30px auto;
        text-align: right;
        position: relative;
        z-index: 2;
        padding: 0 20px;
    }
    .clean-section h3 {
        color: #94a3b8;
        font-size: 22px;
        margin-bottom: 12px;
        font-weight: 700;
        text-align: center;
    }
    .clean-section p {
        color: #94a3b8;
        font-size: 16px;
        line-height: 1.8;
    }
    </style>
    """,
      unsafe_allow_html=True,
  )

  header_col1, header_col2, header_col3 = st.columns([2, 2, 2])
  with header_col1:
    st.image(logo_file, width=65)
  with header_col2:
    lang = st.selectbox(
        "",
        ["العربية", "English"],
        label_visibility="collapsed",
    )
  with header_col3:
    st.markdown(
        """
        <div style="text-align: left;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg" class="nasa-logo" alt="NASA Logo">
        </div>
        """,
        unsafe_allow_html=True,
    )

  subtitle = (
      "استعد لاكتشاف القمر وتفاصيله وموارده<br>من إنشاء فريق انحراف سديمي"
  )

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

  col1, col2, col3 = st.columns([1, 2, 1])
  with col2:
    if st.button("أبدأ الاستكشاف", key="normal_btn"):
      st.session_state.started = True
      st.rerun()

  st.markdown(
      """
    <div class="clean-section">
        <h3>ما هو تطبيق نيبلوز فيشون؟</h3>
        <p>• <b>الهدف الرئيسي:</b> تطبيق متطور لمساعدة الباحثين ومخططي المهمات على استكشاف الموارد وتحليل مواقع الهبوط القمري بدقة عالية.</p>
        <p>• <b>فريق العمل:</b> فريق <b>انحراف سديمي (Nebulous Drift)</b> للمشاركة في مسابقة ناسا العالمية.</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

# ==========================================
# الحالة الثانية: لوحة التحليل والمواقع (حسب تصميمك الرهيب)
# ==========================================
else:
  st.markdown(
      """
    <style>
    .stApp {
        background-color: #070d1b;
        color: white;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 20px;
    }
    .category-box {
        background: #0f172a;
        border: 2px solid #00d2ff;
        border-radius: 14px;
        padding: 12px;
        text-align: center;
        cursor: pointer;
        transition: 0.3s;
    }
    .crater-card {
        background: #0f172a;
        border: 1px solid rgba(0, 210, 255, 0.3);
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5);
    }
    .badge-safe {
        background: rgba(16, 185, 129, 0.2);
        color: #34d399;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: bold;
    }
    .badge-high {
        background: rgba(239, 68, 68, 0.2);
        color: #f87171;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 13px;
        font-weight: bold;
    }
    </style>
    """,
      unsafe_allow_html=True,
  )

  # زر العودة والشعار
  col_back, col_title = st.columns([1, 4])
  with col_back:
    if st.button("⬅ العودة للرئيسية"):
      st.session_state.started = False
      st.rerun()
  with col_title:
    st.markdown(
        "<h3 style='color: #00d2ff; margin:0; text-align: left;'>🌙 أطلس"
        " الاستكشاف والموارد القطبية (NASA LRO Data)</h3>",
        unsafe_allow_html=True,
    )

  st.write("---")

  # شريط التصنيفات (Categories)
  st.markdown(
      "<h4 style='color: #94a3b8;'>Categories</h4>", unsafe_allow_html=True
  )
  cat_col1, cat_col2, cat_col3, cat_col4 = st.columns(4)

  with cat_col1:
    if st.button(
        "💧 المياه",
        use_container_width=True,
        key="c1",
    ):
      st.session_state.selected_category = "المياه"
  with cat_col2:
    if st.button(
        "❄ الجليد",
        use_container_width=True,
        key="c2",
    ):
      st.session_state.selected_category = "الجليد"
  with cat_col3:
    if st.button(
        "📐 المنحدرات",
        use_container_width=True,
        key="c3",
    ):
      st.session_state.selected_category = "المنحدرات"
  with cat_col4:
    if st.button(
        "🌡 الحرارة",
        use_container_width=True,
        key="c4",
    ):
      st.session_state.selected_category = "درجة الحرارة"

  st.markdown(
      f"<h3 style='margin-top: 20px; color: #f8fafc;'>توصيات المواقع القطبية:"
      f" تركيز ({st.session_state.selected_category})</h3>",
      unsafe_allow_html=True,
  )

  # عرض الكروت بناءً على تصميمك الرهيب
  col_info, col_img = st.columns([3, 2])

  with col_info:
    st.markdown(
        """
        <div class="crater-card">
            <h4 style="color: #00d2ff; margin-top:0;">فوهة ساكلتون (Shackleton Crater)</h4>
            <p><b>الإحداثيات:</b> 89.9° جنوباً / 129° شرقاً</p>
            <p><b>تقرير المهمة:</b> ظل دائم، جليد محتمل، إضاءة شمسية قريبة على الحواف الجبلية.</p>
            <span class="badge-high">تركيز عالي جداً للمورد</span>
        </div>
        
        <div class="crater-card">
            <h4 style="color: #00d2ff; margin-top:0;">فوهة هاوورث (Haworth Crater)</h4>
            <p><b>الإحداثيات:</b> 87.4° جنوباً / 0.1° شرقاً</p>
            <p><b>تقرير المهمة:</b> منحدرات آمنة للهبوط، فوهة باردة مناسبة لحفظ عينات الجليد.</p>
            <span class="badge-safe">موقع هبوط آمن ومرشح</span>
        </div>

        <div class="crater-card">
            <h4 style="color: #00d2ff; margin-top:0;">فوهة نوبيل (Nobile Crater)</h4>
            <p><b>الإحداثيات:</b> 85.2° جنوباً / 154° شرقاً</p>
            <p><b>تقرير المهمة:</b> موقع مستهدف لرحلات فالكريب ومهمات ناسا القادمة لاكتشاف الموارد السطحية.</p>
            <span class="badge-high">إضاءة عالية وتركيز جيد</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

  with col_img:
    st.markdown(
        """
        <div class="crater-card" style="text-align: center;">
            <p style="color: #00d2ff; font-weight: bold;">خريطة التركيز الحراري (Heatmap)</p>
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg" style="width: 100%; border-radius: 10px; opacity: 0.8; border: 1px solid #00d2ff;">
            <p style="font-size: 13px; color: #94a3b8; margin-top: 10px;">🔴 النقاط الحمراء توضح بؤر التركيز العالي للموارد المستهدفة في القطب الجنوبي للقمري.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

  # شريط التنقل السفلي المحاكي لتصميمك
  st.write("<br>", unsafe_allow_html=True)
  nav1, nav2, nav3, nav4 = st.columns(4)
  with nav1:
    st.button("🗺 خرائط", use_container_width=True)
  with nav2:
    st.button("📊 تحليل", use_container_width=True)
  with nav3:
    st.button("📋 مهمات", use_container_width=True)
  with nav4:
    st.button("⚙ إعدادات", use_container_width=True)
