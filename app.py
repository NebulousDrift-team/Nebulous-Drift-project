import os
import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة وتوسيعها
st.set_page_config(
    page_title="Nebulous Vision - Dynamic NASA GIS", page_icon="🌙", layout="wide"
)

# تتبع حالة التطبيق
if "started" not in st.session_state:
  st.session_state.started = False

if "selected_category" not in st.session_state:
  st.session_state.selected_category = "اماكن المياه"

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
        <p>• <b>الهدف الرئيسي:</b> نظام تحليل مكاني تفاعلي مستوحى من أرشيف ناسا لاكتشاف الموارد ومواقع الهبوط.</p>
        <p>• <b>فريق العمل:</b> فريق <b>انحراف سديمي (Nebulous Drift)</b> لمشاركة ناسا سبيس أبس.</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

# ==========================================
# الحالة الثانية: الداشبورد التفاعلي الكامل لكل الفئات
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
    .crater-card {
        background: #0f172a;
        border: 1px solid rgba(0, 210, 255, 0.4);
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

  col_back, col_title = st.columns([1, 4])
  with col_back:
    if st.button("⬅ العودة للرئيسية"):
      st.session_state.started = False
      st.rerun()
  with col_title:
    st.markdown(
        "<h3 style='color: #00d2ff; margin:0;'>🌙 أطلس ناسا العلمي للتضاريس"
        " والموارد القمرية</h3>",
        unsafe_allow_html=True,
    )

  st.write("---")

  # قائمة التصنيفات الشاملة (حسب رسمتك بالمللي)
  categories = [
      "اماكن المياه",
      "الجليد",
      "درجات الحرارة",
      "الاماكن المضيئه",
      "الاماكن المظلمه",
      "المواد الطيف الضوئي",
      "الصلابه",
      "المعادن",
      "توقعات الإشعاع الشمسي",
      "وضع القمر",
  ]

  st.markdown(
      "<h4 style='color: #94a3b8;'>اختر التصنيف أو الظاهرة للتحليل من أرشيف"
      " ناسا:</h4>",
      unsafe_allow_html=True,
  )

  # عرض الأزرار في صفوف منظمة
  cols = st.columns(5)
  for i, cat in enumerate(categories):
    with cols[i % 5]:
      if st.button(
          cat,
          use_container_width=True,
          key=f"cat_{i}",
          type=(
              "primary"
              if st.session_state.selected_category == cat
              else "secondary"
          ),
      ):
        st.session_state.selected_category = cat
        st.rerun()

  st.write("")
  st.markdown(
      f"<h3 style='color: #00d2ff; margin-top: 10px;'>📊 نتائج أرشيف ناسا"
      f" (LRO): تحليل ({st.session_state.selected_category})</h3>",
      unsafe_allow_html=True,
  )

  # قاعدة بيانات ديناميكية تتغير فوراً حسب التصنيف المختار
  data_sources = {
      "اماكن المياه": [
          {
              "name": "فوهة ساكلتون (Shackleton Crater)",
              "coords": "89.9° جنوباً / 129° شرقاً",
              "report": (
                  "رصد مسبار ناسا ترسبات هيدروجينية ومياه محتملة بنسبة تركيز"
                  " عالية داخل الظل الدائم."
              ),
              "status": "تركيز عالي جداً للمورد",
              "type": "high",
          },
          {
              "name": "فوهة فاوستيني (Faustini Crater)",
              "coords": "87.2° جنوباً / 77.0° شرقاً",
              "report": (
                  "تحليل طيفي يظهر مؤشرات قوية لوجود جزيئات جليد مائي في القاع."
              ),
              "status": "موقع مرشح بقوة",
              "type": "safe",
          },
      ],
      "الجليد": [
          {
              "name": "فوهة شوميتكر (Shoemaker Crater)",
              "coords": "88.1° جنوباً / 44.9° شرقاً",
              "report": (
                  "تعتبر من أبرد المناطق القطبية مع تراكم طبقات جليدية سميكة"
                  " محمية من الشمس."
              ),
              "status": "جليد قطبي دائم",
              "type": "high",
          },
          {
              "name": "فوهة كابيوس (Cabeus Crater)",
              "coords": "84.9° جنوباً / 35.9° غرباً",
              "report": (
                  "الموقع التاريخي لاصطدام مركبة LCROSS والذي أكد وجود نسب معتبرة"
                  " من المياه والجليد."
              ),
              "status": "مؤكد علمياً من ناسا",
              "type": "safe",
          },
      ],
      "درجات الحرارة": [
          {
              "name": "حواف فوهة هيرميتاج (Hermite Rim)",
              "coords": "86.0° شمالاً / 326.0° شرقاً",
              "report": (
                  "تسجيل أدنى درجات حرارة في النظام الشمسي (-250 درجة مئوية) في"
                  " القاع المظلم."
              ),
              "status": "برودة فائقة (ظل دائم)",
              "type": "high",
          },
          {
              "name": "مرتفعات القطب الجنوبي (Peak of Eternal Light)",
              "coords": "88.5° جنوباً / 110.0° شرقاً",
              "report": (
                  "تتعرض لإضاءة شمسية مستمرة بنسبة تزيد عن 85%، درجات حرارة"
                  " معتدلة ومستقرة."
              ),
              "status": "مناسب لتوليد الطاقة",
              "type": "safe",
          },
      ],
      "الاماكن المضيئه": [
          {
              "name": "قمة الأبدية الضوئية (Peak of Eternal Light)",
              "coords": "88.5° جنوباً / 110.0° شرقاً",
              "report": (
                  "قمة جبلية ترتفع بشكل يمنع حجب عنها الشمس، مما يجعلها مثالية"
                  " لمحطات الطاقة الشمسية."
              ),
              "status": "إضاءة شمسية شبه دائمة",
              "type": "safe",
          },
      ],
      "الاماكن المظلمه": [
          {
              "name": "قاع فوهة أوسكي (Amundsen Crater Floor)",
              "coords": "84.3° جنوباً / 83.3° شرقاً",
              "report": (
                  "مناطق غارقة في ظلام تام منذ مليارات السنين، تحافظ على المركبات"
                  " المتطايرة والجليد النقي."
              ),
              "status": "ظلام دائم - حظر شمسي",
              "type": "high",
          },
      ],
      "المواد الطيف الضوئي": [
          {
              "name": "حوض أيتكين (South Pole-Aitken Basin)",
              "coords": "53.0° جنوباً / 170.0° شرقاً",
              "report": (
                  "تحليل الطيف الضوئي يكشف عن تواجد مواد غنية بالبيروكسين"
                  " والزبرجد الخريطي من وشاح القمر."
              ),
              "status": "تنوع معدني وطيفي فريد",
              "type": "safe",
          },
      ],
      "الصلابه": [
          {
              "name": "سهول ماري ترانكويليتاتيس (Mare Tranquillitatis)",
              "coords": "0.8° شمالاً / 23.4° شرقاً",
              "report": (
                  "تربة بازلتية متماسكة وصلبة، مناسبة جداً لهبوط المركبات الثقيلة"
                  " دون خطر الانغماس."
              ),
              "status": "صلابة عالية واستقرار تربة",
              "type": "safe",
          },
      ],
      "المعادن": [
          {
              "name": "فوهة كوبرنيكوس (Copernicus Crater)",
              "coords": "9.7° شمالاً / 20.0° غرباً",
              "report": (
                  "تركز عالي للمعادن السيليكاتية والمادة المقذوفة الناتجة عن"
                  " الاصطدام العميق."
              ),
              "status": "احتياطي معدني مكتشف",
              "type": "high",
          },
      ],
      "توقعات الإشعاع الشمسي": [
          {
              "name": "القطب الشمالي القمري (North Pole Sectors)",
              "coords": "85.0° شمالاً / 0.0° شرقاً",
              "report": (
                  "معدلات تعرض متوسطة للإشعاع الشمسي والرياح الشمسية، مع وجود"
                  " تحذيرات أثناء العواصف الشمسية."
              ),
              "status": "مستوى إحصائي آمن للمهام",
              "type": "safe",
          },
      ],
      "وضع القمر": [
          {
              "name": "الموقع المداري الحالي (Earth-Moon System)",
              "coords": "المسافة: 384,400 كم / الطور: أحادي تناظري",
              "report": (
                  "القمر في وضعية الإضاءة القياسية بالنسبة لمحطات الرصد الأرضية"
                  " التابعة لناسا."
              ),
              "status": "اتصال مباشر ومستقر",
              "type": "safe",
          },
      ],
  }

  current_craters = data_sources.get(st.session_state.selected_category, [])

  col_info, col_img = st.columns([3, 2])

  with col_info:
    for crater in current_craters:
      badge_class = (
          "badge-high" if crater["type"] == "high" else "badge-safe"
      )
      st.markdown(
          f"""
            <div class="crater-card">
                <h4 style="color: #00d2ff; margin-top:0;">{crater['name']}</h4>
                <p><b>الإحداثيات من أرشيف ناسا:</b> {crater['coords']}</p>
                <p><b>تقرير التحليل:</b> {crater['report']}</p>
                <span class="{badge_class}">{crater['status']}</span>
            </div>
            """,
          unsafe_allow_html=True,
      )

  with col_img:
    st.markdown(
        f"""
        <div class="crater-card" style="text-align: center;">
            <p style="color: #00d2ff; font-weight: bold;">خريطة التحليل الحراري والتركز ({st.session_state.selected_category})</p>
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg" style="width: 100%; border-radius: 10px; opacity: 0.85; border: 1px solid #00d2ff; box-shadow: 0 0 15px rgba(0,210,255,0.3);">
            <p style="font-size: 13px; color: #94a3b8; margin-top: 10px;">🔴 النقاط الشفافة والحمراء توضح محاكاة لبيانات استشعار ناسا لمواقع تركز ({st.session_state.selected_category}).</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

  # شريط التنقل السفلي
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
