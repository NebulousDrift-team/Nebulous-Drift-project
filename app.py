import os
import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة وتوسيعها
st.set_page_config(
    page_title="Nebulous Vision - 2D NASA Atlas", page_icon="🌙", layout="wide"
)

# تتبع حالة التطبيق
if "started" not in st.session_state:
  st.session_state.started = False

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
# الحالة الأولى: الواجهة الرئيسية بكامل تفاصيلها
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
    }
    .btn-normal > button {
        background: linear-gradient(135deg, #cbd5e1 0%, #94a3b8 50%, #64748b 100%) !important;
        color: #0f172a !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        box-shadow: 0px 6px 25px rgba(148, 163, 184, 0.4) !important;
    }
    .btn-normal > button:hover {
        transform: scale(1.02);
        background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%) !important;
        color: #000000 !important;
    }
    .btn-blind > button {
        background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #cbd5e1 100%) !important;
        color: #020617 !important;
        border: 1px solid rgba(255, 255, 255, 0.8) !important;
        box-shadow: 0px 6px 25px rgba(248, 250, 252, 0.35) !important;
    }
    .btn-blind > button:hover {
        transform: scale(1.02);
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 50%, #e2e8f0 100%) !important;
        color: #0f172a !important;
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
        letter-spacing: 0.5px;
    }
    .clean-section p {
        color: #94a3b8;
        font-size: 16px;
        line-height: 1.8;
        margin-bottom: 10px;
    }
    </style>
    """,
      unsafe_allow_html=True,
  )

  header_col1, header_col2, header_col3 = st.columns([2, 2, 2])
  with header_col1:
    st.image(logo_file, width=65)
  with header_col2:
    st.markdown(
        """
        <div style="text-align: center; padding-top: 5px;">
            <span style="color: #cbd5e1; font-weight: bold; font-size: 14px;">🌐 اللغات / Languages</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    lang = st.selectbox(
        "",
        ["العربية", "English", "Русский", "Français", "Deutsch"],
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

  if lang == "العربية":
    subtitle = (
        "استعد لاكتشاف القمر وتفاصيله وموارده<br>من إنشاء فريق انحراف سديمي"
    )
    btn_normal = "أبدأ الاستكشاف (أطلس 2D العلمي)"
    btn_blind = "قسم المكفوفين (الاستكشاف الصوتي)"
    card_title = "ما هو تطبيق نيبلوز فيشون؟"
    card_text1 = (
        "• <b>الهدف الرئيسي:</b> تطبيق متطور لمساعدة الباحثين والهواة والرحلات"
        " المستقبلية على اكتشاف القمر، دراسة تفاصيله السطحية، وتحليل موارده بدقة"
        " عالية."
    )
    card_text2 = (
        "• <b>فريق العمل:</b> تم تطوير هذا المشروع الإبداعي بواسطة فريق"
        " <b>انحراف سديمي (Nebulous Drift S/W Analytics Grp)</b> خصيصاً للمشاركة"
        " في مسابقة ناسا العالمية (NASA Space Apps Challenge)."
    )
    card_text3 = (
        "• <b>التواصل والدعم:</b> نعمل باستمرار على تقديم تجربة استثنائية؛ لو"
        " واجهتكم أي مشاكل تقنية أو استفسارات، يسعدنا تواصلكم معنا."
    )
    blind_title = "شرح قسم المكفوفين (الاستكشاف الصوتي)"
    blind_desc = (
        "يوفر هذا القسم واجهة وصول كاملة مجهزة بالاستكشاف الصوتي، وتحويل البيانات"
        " البصرية ومنحنيات الإضاءة إلى إشارات صوتية مساعدة، لتمكين المكفوفين وضعاف"
        " البصر من استكشاف تفاصيل القمر وبياناته بكل سهولة."
    )
  else:
    subtitle = (
        "Get ready to explore the Moon, its details, and resources<br>Created"
        " by Nebulous Drift Team"
    )
    btn_normal = "Start Exploration (2D Scientific Atlas)"
    btn_blind = "Accessibility Mode"
    card_title = "What is Nebulous Vision?"
    card_text1 = (
        "• <b>Main Goal:</b> An advanced application to help researchers, hobbyists,"
        " and lunar missions explore the Moon and its resources."
    )
    card_text2 = (
        "• <b>Team:</b> Developed by the <b>Nebulous Drift</b> team for the NASA"
        " Space Apps Challenge."
    )
    card_text3 = (
        "• <b>Support:</b> Contact us if you encounter any technical issues."
    )
    blind_title = "Accessibility Section"
    blind_desc = (
        "Provides full voice and audio assistance for visually impaired users."
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
    st.markdown('<div class="btn-normal">', unsafe_allow_html=True)
    if st.button(btn_normal, key="normal_btn"):
      st.session_state.started = True
      st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

  st.markdown(
      f"""
    <div class="clean-section">
        <h3>{card_title}</h3>
        <p>{card_text1}</p>
        <p>{card_text2}</p>
        <p>{card_text3}</p>
    </div>
    <div class="clean-section">
        <h3>{blind_title}</h3>
        <p>{blind_desc}</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  with col2:
    st.markdown('<div class="btn-blind">', unsafe_allow_html=True)
    if st.button(btn_blind, key="blind_btn"):
      st.info(
          "جاري تفعيل واجهة الاستكشاف الصوتي وقراءة البيانات للمكفوفين..."
      )
    st.markdown("</div>", unsafe_allow_html=True)

  st.write("<br><br>", unsafe_allow_html=True)

# ==========================================
# الحالة الثانية: الأطلس القمري التفاعلي الثنائي الأبعاد (2D Professional Scientific Viewer)
# ==========================================
else:
  st.markdown(
      """
    <style>
    .stApp {
        background-color: #020408;
        color: white;
        font-family: 'Segoe UI', Tahoma, sans-serif;
    }
    .top-controls {
        position: fixed;
        top: 15px;
        left: 20px;
        z-index: 999;
    }
    .info-panel {
        background: rgba(15, 23, 42, 0.9);
        border: 1px solid rgba(0, 210, 255, 0.3);
        padding: 15px 20px;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    </style>
    """,
      unsafe_allow_html=True,
  )

  st.markdown('<div class="top-controls">', unsafe_allow_html=True)
  if st.button("⬅ العودة للواجهة الرئيسية"):
    st.session_state.started = False
    st.rerun()
  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown(
      """
    <div style="text-align: center; padding-top: 10px;">
        <h2 style="color: #00d2ff; margin-bottom: 5px;">أطلس ناسا العلمي للتضاريس القمرية (2D High-Res Explorer)</h2>
        <p style="color: #94a3b8; font-size: 16px;">استكشف تفاصيل الفوهات، البحار القمرية، ومواقع الهبوط بدقة مذهلة دون أي تشوهات هندسية.</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  # استخدام Leaflet الخريطة التفاعلية العلمية الثنائية الأبعاد لعرض بيانات ناسا بسلاسة
  atlas_2d_html = """<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        html, body { margin: 0; height: 100%; background: #020408; overflow: hidden; }
        #map { width: 100%; height: 100vh; background: #020408; }
        .leaflet-container { background: #020408 !important; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script>
        // إعداد خريطة تفاعلية بنظام إحداثيات بسيط لعرض الخريطة الكورية الفلكية بوضوح تام
        var map = L.map('map', {
            crs: L.CRS.Simple,
            minZoom: -2,
            maxZoom: 4,
            zoomSnap: 0.5
        });

        // أبعاد خريطة ناسا الرسمية
        var w = 4096, h = 2048;
        var southWest = map.unproject([0, h], map.getMaxZoom());
        var northEast = map.unproject([w, 0], map.getMaxZoom());
        var bounds = new L.LatLngBounds(southWest, northEast);

        // تحميل خريطة ناسا الفلكية الرسمية عالية الدقة (LRO / Wikimedia Moon Map)
        var moonImageUrl = 'https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg';
        L.imageOverlay(moonImageUrl, bounds).addTo(map);

        map.setMaxBounds(bounds);
        map.fitBounds(bounds);

        // إضافة علامات تفاعلية لأهم الفوهات والمواقع (لإثراء المشروع علمياً)
        var craters = [
            {name: "فوهة تيخو (Tycho Crater)", coords: [700, 1500], desc: "فوهة صدمية بارزة ذات نظام شعاعي ضخم."},
            {name: "فوهة كوبرنيكوس (Copernicus)", coords: [900, 2200], desc: "من المعالم البارزة في وجه القمر المرئي."},
            {name: "بحر الهدوء (Sea of Tranquility)", coords: [1100, 2800], desc: "موقع هبوط مركبة أبوللو 11 التاريخي."}
        ];

        craters.forEach(function(c) {
            var marker = L.marker(map.unproject(c.coords, map.getMaxZoom())).addTo(map);
            marker.bindPopup("<b>" + c.name + "</b><br>" + c.desc);
        });
    </script>
</body>
</html>"""

  components.html(atlas_2d_html, height=720)
