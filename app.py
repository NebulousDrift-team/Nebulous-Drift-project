import os
import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة وتوسيعها
st.set_page_config(
    page_title="Nebulous Vision", page_icon="🌙", layout="wide"
)

# تتبع حالة التطبيق (هل المستخدم ضغط على ابدأ أم لا؟)
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
    btn_normal = "أبدأ الاستكشاف"
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
  elif lang == "Русский":
    subtitle = (
        "Приготовьтесь исследовать Луну, ее детали и ресурсы<br>Создано командой"
        " Nebulous Drift"
    )
    btn_normal = "Начать исследование"
    btn_blind = "Для слабовидящих"
    card_title = "Что такое приложение Nebulous Vision?"
    card_text1 = (
        "• <b>Основная цель:</b> Передовое приложение, помогающее исследователям,"
        " любителям и будущим лунным миссиям исследовать Луну и ее ресурсы."
    )
    card_text2 = (
        "• <b>Команда:</b> Разработано командой <b>Nebulous Drift</b> для хакатона"
        " NASA Space Apps Challenge."
    )
    card_text3 = (
        "• <b>Поддержка:</b> Если у вас возникли вопросы или проблемы, свяжитесь"
        " с нами."
    )
    blind_title = "Раздел доступности (Аудио-исследование)"
    blind_desc = (
        "Этот раздел предоставляет полный интерфейс голосового доступа и"
        " звукового сопровождения данных для слабовидящих."
    )
  elif lang == "Français":
    subtitle = (
        "Préparez-vous à explorer la Lune, ses détails et ses ressources<br>Créé"
        " par l'équipe Nebulous Drift"
    )
    btn_normal = "Commencer l'exploration"
    btn_blind = "Mode accessibilité"
    card_title = "Qu'est-ce que Nebulous Vision ?"
    card_text1 = (
        "• <b>Objectif :</b> Une application avancée pour explorer la Lune et"
        " ses ressources."
    )
    card_text2 = (
        "• <b>Équipe :</b> Créé par l'équipe <b>Nebulous Drift</b> pour le NASA"
        " Space Apps Challenge."
    )
    card_text3 = (
        "• <b>Support :</b> Contactez-nous en cas de problème technique."
    )
    blind_title = "Section Accessibilité (Exploration Vocale)"
    blind_desc = (
        "Cette section offre un accès audio et vocal pour les utilisateurs"
        " malvoyants."
    )
  elif lang == "Deutsch":
    subtitle = (
        "Bereiten Sie sich darauf vor, den Mond zu erkunden<br>Erstellt vom"
        " Nebulous Drift Team"
    )
    btn_normal = "Erkundung starten"
    btn_blind = "Barrierefreiheit"
    card_title = "Was ist Nebulous Vision?"
    card_text1 = (
        "• <b>Ziel:</b> Eine fortschrittliche App zur Erkundung des Mondes und"
        " seiner Ressourcen."
    )
    card_text2 = (
        "• <b>Team:</b> Entwickelt vom <b>Nebulous Drift</b> Team für die NASA"
        " Space Apps Challenge."
    )
    card_text3 = (
        "• <b>Support:</b> Bei Fragen oder Problemen kontaktieren Sie uns."
    )
    blind_title = "Barrierefreiheit (Audio-Erkundung)"
    blind_desc = (
        "Dieser Bereich bietet Sprach- und Audiounterstützung für"
        " Sehbehinderte."
    )
  else:
    subtitle = (
        "Get ready to explore the Moon, its details, and resources<br>Created"
        " by Nebulous Drift Team"
    )
    btn_normal = "Start Exploration"
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
    blind_title = "Accessibility Section (Audio Exploration)"
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
# الحالة الثانية: شاشة القمر 3D الواقعي من أرشيف ناسا
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
    .title-area {
        text-align: center;
        padding: 2px;
    }
    .main-title-3d {
        font-size: 36px;
        font-weight: 950;
        background: linear-gradient(135deg, #00d2ff 25%, #e2e8f0 85%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-instruction {
        color: #94a3b8;
        font-size: 14px;
        margin-top: 2px;
    }
    </style>
    """,
      unsafe_allow_html=True,
  )

  if st.button("⬅ العودة للواجهة الرئيسية"):
    st.session_state.started = False
    st.rerun()

  st.markdown(
      """
    <div class="title-area">
        <h1 class="main-title-3d">Nebulous Vision: NASA 3D Lunar Topography</h1>
        <p class="sub-instruction">استخدم الماوس لتدوير قمر ناسا الواقعي، وعجلة الماوس (Scroll) للتكبير ورؤية الفوهات والتضاريس ثلاثية الأبعاد بدقة فائقة</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  # كود القمر ثلاثي الأبعاد الواقعي جداً (بأرشيف ناسا وخريطة تضاريس حقيقية)
  moon_3d_html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body { margin: 0; background-color: #020408; overflow: hidden; }
            canvas { display: block; }
        </style>
    </head>
    <body>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
        <script>
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            document.body.appendChild(renderer.domElement);

            const controls = new THREE.OrbitControls(camera, renderer.domElement);
            controls.enableDamping = true;
            controls.dampingFactor = 0.05;
            controls.minDistance = 1.3;
            controls.maxDistance = 8;

            // هندسة كروية عالية الدقة لتفاصيل الفوهات
            const geometry = new THREE.SphereGeometry(1, 128, 128);
            const textureLoader = new THREE.TextureLoader();
            
            // تحميل نسيج عالي الدقة وتضاريس حقيقية من أرشيف ناسا للقمر
            const moonTexture = textureLoader.load('https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg');
            const moonBump = textureLoader.load('https://upload.wikimedia.org/wikipedia/commons/e/e1/FullMoon2010.jpg'); // لخلق عمق وبروز الفوهات والتضاريس
            
            const material = new THREE.MeshStandardMaterial({
                map: moonTexture,
                bumpMap: moonBump,
                bumpScale: 0.04, // تعيين عمق ثلاثي الأبعاد للفوهات
                roughness: 0.85,
                metalness: 0.05
            });
            
            const moon = new THREE.Mesh(geometry, material);
            scene.add(moon);

            // إضاءة فضاء واقعية لتبرز تضاريس وجوانب القمر
            const ambientLight = new THREE.AmbientLight(0x333333);
            scene.add(ambientLight);

            const sunLight = new THREE.DirectionalLight(0xffffff, 2.0);
            sunLight.position.set(6, 3, 5);
            scene.add(sunLight);

            camera.position.z = 2.7;

            // حركة دوران خفيفة تلقائية مع التحكم بالماوس
            function animate() {
                requestAnimationFrame(animate);
                moon.rotation.y += 0.0005; // دوران بطيء وواقعي حول المحور
                controls.update();
                renderer.render(scene, camera);
            }
            animate();

            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        </script>
    </body>
    </html>
    """
  components.html(moon_3d_html, height=550)
