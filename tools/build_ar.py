#!/usr/bin/env python3
"""Generate ar.html (Arabic, right-to-left) from index.html.

Edit the English page, update the matching pair below, then run:
    python3 tools/build_ar.py
Every English string must be found exactly once, so a changed sentence
fails loudly instead of being left untranslated.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PAIRS = [
    # Document
    ('<html lang="en">', '<html lang="ar" dir="rtl">'),
    ('<title>WORX | Kitchen &amp; Dressing — New Cairo</title>', '<title>WORX | مطابخ وغرف ملابس — القاهرة الجديدة</title>'),
    ('content="WORX Kitchen & Dressing — custom kitchens, dressing rooms, remodels and repairs in New Cairo. Call for a free quote."',
     'content="WORX للمطابخ وغرف الملابس — مطابخ وغرف ملابس حسب الطلب، تجديد وإصلاح في القاهرة الجديدة. اتصل بنا لعرض سعر مجاني."'),
    ('<meta property="og:title" content="WORX | Kitchen & Dressing">', '<meta property="og:title" content="WORX | مطابخ وغرف ملابس">'),
    ('content="Your fantasies, our realities. Custom kitchens and dressing rooms in New Cairo."',
     'content="خيالكم، واقعنا. مطابخ وغرف ملابس حسب الطلب في القاهرة الجديدة."'),

    # Top bar and header
    ('<span class="topbar__label">Call for a free quote today</span><span class="topbar__short">Free quote</span>',
     '<span class="topbar__label">اتصل الآن لعرض سعر مجاني</span><span class="topbar__short">عرض سعر مجاني</span>'),
    ('aria-label="WORX Kitchen and Dressing — home"', 'aria-label="WORX للمطابخ وغرف الملابس — الرئيسية"'),
    ('<img src="assets/img/logo.png" alt="WORX Kitchen and Dressing"', '<img src="assets/img/logo.png" alt="WORX للمطابخ وغرف الملابس"'),
    ('<nav class="nav" id="nav" aria-label="Main">', '<nav class="nav" id="nav" aria-label="القائمة الرئيسية">'),
    ('<a href="#about">About</a>', '<a href="#about">من نحن</a>'),
    ('<a href="#services">Services</a>', '<a href="#services">خدماتنا</a>'),
    ('<a href="#work">Our Work</a>', '<a href="#work">أعمالنا</a>'),
    ('<a href="#videos">Videos</a>', '<a href="#videos">فيديوهات</a>'),
    ('<a href="#team">Team</a>', '<a href="#team">فريقنا</a>'),
    ('<a href="#reviews">Reviews</a>', '<a href="#reviews">آراء العملاء</a>'),
    ('<a href="#contact">Contact</a>', '<a href="#contact">تواصل معنا</a>'),
    ('class="btn btn--dark nav__cta">Free Quote</a>', 'class="btn btn--dark nav__cta">عرض سعر مجاني</a>'),
    ('<a href="ar.html" class="lang-switch" lang="ar" hreflang="ar">عربي</a>',
     '<a href="index.html" class="lang-switch" lang="en" hreflang="en">English</a>'),
    ('aria-label="Open menu"', 'aria-label="فتح القائمة"'),

    # Hero
    ('alt="Modern WORX kitchen with wood finishes, white island and glass cabinets"', 'alt="مطبخ حديث من WORX بتشطيبات خشبية وجزيرة بيضاء وخزائن زجاجية"'),
    ('<p class="eyebrow eyebrow--light">Kitchen &amp; Dressing · New Cairo</p>', '<p class="eyebrow eyebrow--light">مطابخ وغرف ملابس · القاهرة الجديدة</p>'),
    ('<h1>Your fantasies,<br><em>our realities.</em></h1>', '<h1>خيالكم،<br><em>واقعنا.</em></h1>'),
    ('Custom kitchens and dressing rooms — designed, built and installed by one dedicated team.',
     'مطابخ وغرف ملابس حسب الطلب — تصميم وتصنيع وتركيب بفريق واحد متخصص.'),
    ('class="btn btn--light">Get a free quote</a>', 'class="btn btn--light">اطلب عرض سعر مجاني</a>'),
    ('class="btn btn--ghost">See our work</a>', 'class="btn btn--ghost">شاهد أعمالنا</a>'),

    # Why WORX
    ('<p class="eyebrow">Why WORX</p>', '<p class="eyebrow">لماذا WORX</p>'),
    ('<h2>Built right, delivered on time</h2>', '<h2>تنفيذ متقن وتسليم في الموعد</h2>'),
    ('alt="Contractor cutting wood with a mitre saw"', 'alt="نجار يقطع الخشب بمنشار"'),
    ('<h3>Licensed Contractors</h3>', '<h3>مقاولون مرخّصون</h3>'),
    ('As a company dedicated to providing great service, it is important to us to deliver unparalleled workmanship on every assignment. We are accredited, licensed, bonded, and insured. With experience and expertise, we provide the support your project needs.',
     'كشركة تلتزم بتقديم أفضل خدمة، يهمنا أن نقدم جودة تنفيذ لا مثيل لها في كل مشروع. نحن معتمدون ومرخّصون ومؤمَّن علينا، وبخبرتنا وتخصصنا نقدم لمشروعك كل الدعم الذي يحتاجه.'),
    ('alt="Designer drafting kitchen plans"', 'alt="مصمم يرسم مخططات مطبخ"'),
    ('<h3>On-time Completion</h3>', '<h3>التسليم في الموعد</h3>'),
    ('We work with you to meet deadlines and coordinate with other related projects. We maintain open communication on the status of your job. We do this to guarantee that the project is completed with the transparent scheduling.',
     'نعمل معك للالتزام بالمواعيد والتنسيق مع باقي الأعمال المرتبطة بمشروعك، ونحافظ على تواصل مستمر لنطلعك على سير العمل، لنضمن إنجاز المشروع وفق جدول زمني واضح وشفاف.'),
    ('alt="Finished WORX kitchen with stove and island"', 'alt="مطبخ منفّذ من WORX بموقد وجزيرة"'),
    ('<h3>Great Service</h3>', '<h3>خدمة مميزة</h3>'),
    ('We combine our industry knowledge, the highest quality building supplies and equipment, and our dedication to deliver exceptional service to our clients. We will stay in touch, keeping you up to date on both the paperwork and renovation process.',
     'نجمع بين خبرتنا في المجال وأعلى جودة في الخامات والمعدات والتزامنا بتقديم خدمة استثنائية لعملائنا. سنبقى على تواصل دائم معك لنطلعك على كل خطوة، من الأوراق والتصاريح حتى انتهاء التجديد.'),

    # Services
    ('<p class="eyebrow eyebrow--light">Services</p>', '<p class="eyebrow eyebrow--light">خدماتنا</p>'),
    ('<h2>What we do</h2>', '<h2>ماذا نقدم</h2>'),
    ('<h3>Permits Simplified</h3>', '<h3>تصاريح بلا تعقيد</h3>'),
    ('Renovations and installation require paperwork and permits. As certified contractors, we know what papers need to be filed and what permits need to be obtained.',
     'أعمال التجديد والتركيب تحتاج إلى أوراق وتصاريح. وكمقاولين معتمدين، نعرف جيداً الأوراق المطلوب تقديمها والتصاريح اللازم استخراجها.'),
    ('<h3>Remodels &amp; Renovations</h3>', '<h3>تجديد وإعادة تصميم</h3>'),
    ("Still in love with your kitchen, but feel like it's a little outdated? Need a more functional kitchen for the chef of the house? Let's talk about a kitchen remodel.",
     'ما زلت تحب مطبخك لكنك تشعر أنه أصبح قديماً بعض الشيء؟ تحتاج مطبخاً عملياً أكثر لطاهي البيت؟ دعنا نتحدث عن تجديد مطبخك.'),
    ('<h3>Repair Expertise</h3>', '<h3>خبرة في الإصلاح</h3>'),
    ('Every kitchen needs some repairs at some point. From wood rot to hinge damage, kitchen repairs need to be handled in such a way that they do not cover up related problems.',
     'كل مطبخ يحتاج إلى بعض الإصلاحات في وقت ما. من تلف الخشب إلى أعطال المفصلات، يجب التعامل مع الإصلاحات بطريقة لا تُخفي المشكلات المرتبطة بها.'),

    # In the details
    ('aria-label="Tour of a WORX kitchen: pull-out pantry, fold-out table, under-sink organizer, appliance cabinet and vegetable drawers"',
     'aria-label="جولة في مطبخ من WORX: مخزن منزلق، طاولة قابلة للطي، منظم أسفل الحوض، خزانة للأجهزة وأدراج للخضروات"'),
    ('aria-pressed="false">Sound on</button>', 'aria-pressed="false">تشغيل الصوت</button>'),
    ('aria-label="Drawer with a custom wooden cutlery organizer sliding open"', 'aria-label="درج بمنظم خشبي مخصص لأدوات المائدة يُفتح"'),
    ('<p class="eyebrow">In the details</p>', '<p class="eyebrow">في التفاصيل</p>'),
    ('<h2>Made to be used every day</h2>', '<h2>مصمَّم للاستخدام كل يوم</h2>'),
    ('Pull-out pantries, fold-out tables, under-sink organizers, hidden appliance cabinets and divided vegetable drawers — every detail is planned around how you cook, store and live.',
     'مخازن منزلقة، طاولات قابلة للطي، منظمات أسفل الحوض، خزائن مخفية للأجهزة وأدراج مقسّمة للخضروات — كل تفصيلة مصممة حول طريقة طهيك وتخزينك وحياتك.'),
    ('class="btn btn--dark">Plan your space</a>', 'class="btn btn--dark">خطّط لمساحتك</a>'),

    # Gallery
    ('<p class="eyebrow">Our Work</p>', '<p class="eyebrow">أعمالنا</p>'),
    ('<h2>Recent projects</h2>', '<h2>أحدث المشاريع</h2>'),
    ('aria-label="Filter projects"', 'aria-label="تصفية المشاريع"'),
    ('aria-pressed="true">All</button>', 'aria-pressed="true">الكل</button>'),
    ('aria-pressed="false">Kitchens</button>', 'aria-pressed="false">مطابخ</button>'),
    ('aria-pressed="false">Dressing rooms</button>', 'aria-pressed="false">غرف ملابس</button>'),
    ('aria-pressed="false">Details</button>', 'aria-pressed="false">تفاصيل</button>'),
    ('aria-pressed="false">Living</button>', 'aria-pressed="false">معيشة</button>'),
    ('aria-pressed="false">Utility</button>', 'aria-pressed="false">غرف خدمات</button>'),
    ('alt="Walk-in dressing room with lit glass-door wardrobes in walnut"', 'alt="غرفة ملابس بخزائن من خشب الجوز بأبواب زجاجية مضاءة"'),
    ('alt="Walnut wardrobe wall with lit glass doors, shelves and hanging rails"', 'alt="جدار خزائن ملابس من خشب الجوز بأبواب زجاجية مضاءة ورفوف وعلاقات"'),
    ('alt="Grey gloss and oak kitchen with white island, wood bar and black pendant lights"', 'alt="مطبخ رمادي لامع وخشب البلوط بجزيرة بيضاء وبار خشبي وإضاءة معلقة سوداء"'),
    ('alt="Mint green and oak kitchen with grey marble backsplash and built-in oven"', 'alt="مطبخ بالأخضر النعناعي وخشب البلوط بتكسية رخام رمادي وفرن مدمج"'),
    ('alt="Glass-door walnut wardrobes with a fold-out vanity desk"', 'alt="خزائن ملابس من خشب الجوز بأبواب زجاجية ومكتب تسريحة قابل للطي"'),
    ('alt="Grey gloss kitchen with lit glass upper cabinets and a set dining bar"', 'alt="مطبخ رمادي لامع بخزائن علوية زجاجية مضاءة وبار طعام"'),
    ('alt="Grey gloss kitchen at night with LED lines and a lit glass display column"', 'alt="مطبخ رمادي لامع ليلاً بخطوط إضاءة وعمود عرض زجاجي مضاء"'),
    ('alt="Grey gloss drawers, oak tall units and plinth lighting"', 'alt="أدراج رمادية لامعة ووحدات طويلة من البلوط وإضاءة سفلية"'),
    ('alt="Grey gloss and oak U-shaped kitchen with LED ceiling lines"', 'alt="مطبخ على شكل U باللون الرمادي اللامع وخشب البلوط مع خطوط إضاءة في السقف"'),
    ('alt="White kitchen with marble waterfall peninsula and bouclé bar stools"', 'alt="مطبخ أبيض بجزيرة رخامية منسدلة وكراسي بار بوكليه"'),
    ('alt="Oak and white gloss TV wall unit with lit shelves"', 'alt="وحدة تلفزيون من خشب البلوط والأبيض اللامع برفوف مضاءة"'),
    ('alt="Kitchen with black-framed open shelving and a stone peninsula table"', 'alt="مطبخ برفوف مفتوحة بإطار أسود وطاولة حجرية"'),
    ('alt="Granite breakfast bar with a lit glass-door display cabinet"', 'alt="بار إفطار من الجرانيت مع خزانة عرض زجاجية مضاءة"'),
    ('alt="Grey gloss kitchen with oak panelling and lit floating shelves"', 'alt="مطبخ رمادي لامع بتكسيات من خشب البلوط ورفوف عائمة مضاءة"'),
    ('alt="Open-plan kitchenette with oak bar table and lit shelving"', 'alt="مطبخ صغير مفتوح بطاولة بار من خشب البلوط ورفوف مضاءة"'),
    ('alt="Stone waterfall dining peninsula with open shelving in daylight"', 'alt="طاولة طعام حجرية منسدلة مع رفوف مفتوحة في ضوء النهار"'),
    ('alt="Open kitchen with gold pendant lights and bouclé stools"', 'alt="مطبخ مفتوح بإضاءة معلقة ذهبية وكراسي بوكليه"'),
    ('alt="Oak and white TV wall unit with display niches"', 'alt="وحدة تلفزيون من خشب البلوط والأبيض بفتحات عرض"'),
    ('alt="Stone dining peninsula with lit black-framed shelves and hood"', 'alt="طاولة طعام حجرية مع رفوف مضاءة بإطار أسود وشفاط"'),
    ('alt="Cream gloss U-shaped kitchen with granite worktops and built-in ovens"', 'alt="مطبخ كريمي لامع على شكل U بأسطح جرانيت وأفران مدمجة"'),
    ('alt="L-shaped stone dining counter with black-framed shelving"', 'alt="طاولة طعام حجرية على شكل L مع رفوف بإطار أسود"'),
    ('alt="Bright kitchen with waterfall peninsula and wood panelling"', 'alt="مطبخ مشرق بجزيرة منسدلة وتكسيات خشبية"'),
    ('alt="Stone waterfall peninsula and gloss cabinets in the evening"', 'alt="جزيرة حجرية منسدلة وخزائن لامعة في المساء"'),
    ('alt="Peninsula kitchen with open shelves looking toward a glass staircase"', 'alt="مطبخ بجزيرة ورفوف مفتوحة يطل على درج زجاجي"'),
    ('alt="Beige fluted kitchen with granite waterfall island"', 'alt="مطبخ بيج بواجهات مضلّعة وجزيرة جرانيت منسدلة"'),
    ('alt="Sage green and oak kitchen with smoked-glass upper cabinets"', 'alt="مطبخ باللون الأخضر الهادئ وخشب البلوط بخزائن علوية من الزجاج المدخّن"'),
    ('alt="Oak and matte black kitchen with breakfast bar and pendant lights"', 'alt="مطبخ من خشب البلوط والأسود المطفي ببار إفطار وإضاءة معلقة"'),
    ('alt="White gloss L-shaped kitchen with black-framed glass display cabinets"', 'alt="مطبخ أبيض لامع على شكل L بخزائن عرض زجاجية بإطار أسود"'),
    ('alt="Walnut and grey L-shaped kitchen with lit glass niches"', 'alt="مطبخ على شكل L من خشب الجوز والرمادي بفتحات زجاجية مضاءة"'),
    ('alt="Fluted cabinet fronts over a granite backsplash"', 'alt="واجهات خزائن مضلّعة فوق تكسية جرانيت"'),
    ('alt="Handleless white kitchen with solid wood breakfast bar"', 'alt="مطبخ أبيض بدون مقابض مع بار إفطار من الخشب"'),
    ('alt="Tall walnut units with fridge housing and lit glass display column"', 'alt="وحدات طويلة من خشب الجوز بحاضنة للثلاجة وعمود عرض زجاجي مضاء"'),
    ('alt="Sage green base cabinets, oak uppers and grey marble backsplash"', 'alt="خزائن سفلية خضراء وعلوية من البلوط وتكسية رخام رمادي"'),
    ('alt="Light grey kitchen with oak tall units and built-in ovens"', 'alt="مطبخ رمادي فاتح بوحدات طويلة من البلوط وأفران مدمجة"'),
    ('alt="Built-in oven in sage green cabinetry under a granite worktop"', 'alt="فرن مدمج في خزائن خضراء أسفل سطح جرانيت"'),
    ('alt="Fluted beige kitchen with open shelving and built-in ovens"', 'alt="مطبخ بيج بواجهات مضلّعة ورفوف مفتوحة وأفران مدمجة"'),
    ('alt="Handleless white kitchen with angled black glass hood"', 'alt="مطبخ أبيض بدون مقابض مع شفاط زجاجي أسود مائل"'),
    ('alt="Laundry room with washer housing, sink and marble worktop"', 'alt="غرفة غسيل بحاضنة للغسالة وحوض وسطح رخامي"'),
    ('alt="Kitchen island with pendant lights and wood cabinetry"', 'alt="جزيرة مطبخ بإضاءة معلقة وخزائن خشبية"'),
    ('alt="Dark wood kitchen with lit glass display cabinet"', 'alt="مطبخ خشبي داكن بخزانة عرض زجاجية مضاءة"'),
    ('alt="Corner cabinet with pull-out carousel shelves"', 'alt="خزانة ركنية برفوف دوّارة منزلقة"'),
    ('id="showMore">Show more projects</button>', 'id="showMore">عرض المزيد من المشاريع</button>'),

    # Videos
    ('<p class="eyebrow eyebrow--light">Watch</p>', '<p class="eyebrow eyebrow--light">شاهد</p>'),
    ('<h2>Take the tour</h2>', '<h2>جولة داخل أعمالنا</h2>'),
    ('Step inside finished WORX projects. Tap a video to play it with sound.', 'ادخل إلى مشاريع WORX المنفّذة. اضغط على أي فيديو لتشغيله بالصوت.'),
    ('aria-label="Tour of four WORX dressing rooms and a vanity"', 'aria-label="جولة في أربع غرف ملابس وتسريحة من WORX"'),
    ('<strong>The WORX Collection: Dressing</strong><span>Four dressing rooms and a vanity</span>',
     '<strong>مجموعة WORX: غرف الملابس</strong><span>أربع غرف ملابس وتسريحة</span>'),
    ('aria-label="Tour of a beige fluted WORX kitchen with a granite island"', 'aria-label="جولة في مطبخ بيج بواجهات مضلّعة وجزيرة جرانيت من WORX"'),
    ('<strong>Fluted kitchen tour</strong><span>Granite island, fluted cabinets, built-in ovens</span>',
     '<strong>جولة في مطبخ بواجهات مضلّعة</strong><span>جزيرة جرانيت، خزائن مضلّعة، أفران مدمجة</span>'),

    # Reviews (each review stays in the language it was written in)
    ('<p class="eyebrow">Reviews</p>', '<p class="eyebrow">آراء العملاء</p>'),
    ('<h2>What our clients say</h2>', '<h2>ماذا يقول عملاؤنا</h2>'),
    ('''          <figure class="review">
            <div class="stars" aria-label="5 out of 5 stars">''', '''          <figure class="review" dir="ltr" lang="en">
            <div class="stars" aria-label="5 out of 5 stars">'''),

    # Team
    ('<p class="eyebrow">Our Team</p>', '<p class="eyebrow">فريقنا</p>'),
    ('<h2>The people behind WORX</h2>', '<h2>الفريق وراء WORX</h2>'),
    ('<strong>Marawan Mostafa</strong><span>Quality Control Expert</span>', '<strong>مروان مصطفى</strong><span>خبير مراقبة الجودة</span>'),
    ('<span class="initials">TH</span><strong>Tarek Hossam</strong><span>Lead Showroom Designer</span>', '<span class="initials">ط</span><strong>طارق حسام</strong><span>كبير مصممي المعرض</span>'),
    ('<span class="initials">AM</span><strong>Amr Mohy</strong><span>Installation &amp; Inspection Engineer</span>', '<span class="initials">ع</span><strong>عمرو محيي</strong><span>مهندس التركيب والمعاينة</span>'),
    ('<span class="initials">MR</span><strong>Mahmoud Radwan</strong><span>Showroom Designer</span>', '<span class="initials">م</span><strong>محمود رضوان</strong><span>مصمم المعرض</span>'),
    ('<strong>Esraa Alsahar</strong><span>Content Creator &amp; Social Media Specialist</span>', '<strong>إسراء الساحر</strong><span>صانعة محتوى وأخصائية سوشيال ميديا</span>'),
    ('<strong>Basma Ashraf</strong><span>HR</span>', '<strong>بسمة أشرف</strong><span>الموارد البشرية</span>'),
    ('<strong>Mahmoud Mostafa</strong><span>Professional Legal Accountant</span>', '<strong>محمود مصطفى</strong><span>محاسب قانوني</span>'),
    ('<span class="initials">SM</span><strong>Salsabil Mohamed</strong><span>Social Media Interior Designer</span>', '<span class="initials">س</span><strong>سلسبيل محمد</strong><span>مصممة ديكور داخلي للسوشيال ميديا</span>'),
    ('<strong>Al Sayed Ibrahim</strong><span>Interior Designer</span>', '<strong>السيد إبراهيم</strong><span>مصمم ديكور داخلي</span>'),
    ('<span class="initials">AA</span><strong>Abd-Allah</strong><span>Price Estimation Accountant</span>', '<span class="initials">ع</span><strong>عبدالله</strong><span>محاسب تسعير</span>'),
    ('<span class="initials">AS</span><strong>Ahmad Salah</strong><span>Purchases</span>', '<span class="initials">أ</span><strong>أحمد صلاح</strong><span>المشتريات</span>'),

    # FAQ
    ('<p class="eyebrow">FAQ</p>', '<p class="eyebrow">الأسئلة الشائعة</p>'),
    ('<h2>Frequently asked questions</h2>', '<h2>أسئلة متكررة</h2>'),
    ("Can't find your answer? Give us a call — we're happy to help.", 'لم تجد إجابتك؟ اتصل بنا — يسعدنا مساعدتك.'),
    ('<summary>What types of kitchen countertops do you offer?</summary>', '<summary>ما أنواع أسطح المطابخ التي تقدمونها؟</summary>'),
    ('Countertop options depend on your design and budget. Visit our showroom or call us and our designers will walk you through the materials available for your project.',
     'تعتمد خيارات الأسطح على تصميمك وميزانيتك. زر معرضنا أو اتصل بنا وسيعرض عليك مصممونا الخامات المتاحة لمشروعك.'),
    ('<summary>How much is the price per meter?</summary>', '<summary>كم سعر المتر؟</summary>'),
    ('Pricing per meter depends on the materials, finishes and hardware you choose. Contact us for a free, no-obligation quote tailored to your space.',
     'يعتمد سعر المتر على الخامات والتشطيبات والإكسسوارات التي تختارها. تواصل معنا لعرض سعر مجاني ودون أي التزام يناسب مساحتك.'),
    ('<summary>What is the process for installing kitchens?</summary>', '<summary>ما هي خطوات تركيب المطبخ؟</summary>'),
    ('We start with measurements and a design consultation, agree the design and quote, manufacture your kitchen, then install it — keeping you updated at every step.',
     'نبدأ بأخذ المقاسات وجلسة استشارة للتصميم، ثم نتفق على التصميم والسعر، ثم نصنّع مطبخك ونركّبه — مع إطلاعك على كل خطوة.'),

    # Contact
    ('<p class="eyebrow eyebrow--light">Contact</p>', '<p class="eyebrow eyebrow--light">تواصل معنا</p>'),
    ('<h2>Get a free quote</h2>', '<h2>اطلب عرض سعر مجاني</h2>'),
    ('We strive to be in constant communication with our customers until the job is done. To get a free quote, or if you have questions or special requests, just drop us a line. We look forward to serving you!',
     'نحرص على التواصل المستمر مع عملائنا حتى انتهاء العمل. للحصول على عرض سعر مجاني، أو إذا كانت لديك أسئلة أو طلبات خاصة، راسلنا. يسعدنا خدمتك!'),
    ('<dt>Showroom</dt><dd>G 32 AB Park Mall, 90th St, New Cairo</dd>', '<dt>المعرض</dt><dd><bdi dir="ltr">G 32 AB</bdi> بارك مول، شارع التسعين، القاهرة الجديدة</dd>'),
    ('<dt>Phone</dt>', '<dt>الهاتف</dt>'),
    ('<dt>Hours</dt><dd>All week: 12am – 11:45pm</dd>', '<dt>مواعيد العمل</dt><dd>طوال أيام الأسبوع: 12 ص – 11:45 م</dd>'),
    ('aria-label="WORX on Facebook"', 'aria-label="WORX على فيسبوك"', 2),
    ('aria-label="WORX on Instagram"', 'aria-label="WORX على إنستجرام"', 2),
    ('<h3>Send a message</h3>', '<h3>أرسل رسالة</h3>'),
    ('<label>Name<input', '<label>الاسم<input'),
    ('<label>Phone<input', '<label>الهاتف<input'),
    ('<label>Address<input name="address" autocomplete="street-address" placeholder="Street, city">', '<label>العنوان<input name="address" autocomplete="street-address" placeholder="الشارع، المدينة">'),
    ('<label>Message<textarea name="message" rows="4" placeholder="Tell us about your kitchen or dressing room">', '<label>الرسالة<textarea name="message" rows="4" placeholder="أخبرنا عن مطبخك أو غرفة ملابسك">'),
    ('btn--block">Send via WhatsApp</button>', 'btn--block">إرسال عبر واتساب</button>'),
    ('<p class="form__note">Opens WhatsApp with your message ready to send to +20 111 777 6589.</p>',
     '<p class="form__note">يفتح واتساب ورسالتك جاهزة للإرسال إلى <bdi dir="ltr">+20 111 777 6589</bdi>.</p>'),
    ('title="WORX showroom location — Park Mall, New Cairo"', 'title="موقع معرض WORX — بارك مول، القاهرة الجديدة"'),
    ('src="https://www.google.com/maps?q=Park+Mall,+90th+Street,+New+Cairo&output=embed"', 'src="https://www.google.com/maps?q=Park+Mall,+90th+Street,+New+Cairo&hl=ar&output=embed"'),
    ('New+Cairo">Get directions</a>', 'New+Cairo">احصل على الاتجاهات</a>'),

    # Footer and overlays
    ('<img src="assets/img/logo-white.png" alt="WORX Kitchen and Dressing"', '<img src="assets/img/logo-white.png" alt="WORX للمطابخ وغرف الملابس"'),
    ('<p>Copyright © <span id="year">2026</span> WORX I Kitchen &amp; Dressing — All rights reserved.</p>',
     '<p>© <span id="year">2026</span> WORX للمطابخ وغرف الملابس — جميع الحقوق محفوظة.</p>'),
    ('aria-label="Call WORX"', 'aria-label="اتصل بـ WORX"'),
    ('aria-label="Close">×</button>', 'aria-label="إغلاق">×</button>'),
    ('aria-label="Previous photo"', 'aria-label="الصورة السابقة"'),
    ('aria-label="Next photo"', 'aria-label="الصورة التالية"'),
]


def main():
    html = (ROOT / 'index.html').read_text(encoding='utf-8')
    for pair in PAIRS:
        en, ar, count = pair if len(pair) == 3 else (*pair, 1)
        found = html.count(en)
        if found != count:
            raise SystemExit(f'Expected {count} match(es), found {found}: {en[:80]!r}')
        html = html.replace(en, ar)
    (ROOT / 'ar.html').write_text(html, encoding='utf-8')
    print(f'Wrote ar.html ({len(PAIRS)} translations)')


if __name__ == '__main__':
    main()
