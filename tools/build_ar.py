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
    ('content="WORX Kitchen & Dressing — custom kitchens and dressing rooms in New Cairo. Call for a free quote."',
     'content="WORX للمطابخ وغرف الملابس — مطابخ وغرف ملابس حسب الطلب في القاهرة الجديدة. اتصل بنا لعرض سعر مجاني."'),
    ('<meta property="og:url" content="https://worxegypt.com/">', '<meta property="og:url" content="https://worxegypt.com/ar.html">\n  <meta property="og:locale" content="ar_EG">'),
    ('<link rel="canonical" href="https://worxegypt.com/">', '<link rel="canonical" href="https://worxegypt.com/ar.html">'),
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
    ('<p class="eyebrow eyebrow--light">Kitchens, Dressings &amp; More</p>', '<p class="eyebrow eyebrow--light">مطابخ، غرف ملابس والمزيد</p>'),
    ('<h1>Your fantasies,<br><em>our realities.</em></h1>', '<h1>خيالكم،<br><em>واقعنا.</em></h1>'),
    ('Custom kitchens and dressing rooms — designed, built and installed by our dedicated team.',
     'مطابخ وغرف ملابس حسب الطلب — تصميم وتصنيع وتركيب بأيدي فريقنا المتخصص.'),
    ('class="btn btn--light">Get a free quote</a>', 'class="btn btn--light">اطلب عرض سعر مجاني</a>'),
    ('class="btn btn--ghost">See our work</a>', 'class="btn btn--ghost">شاهد أعمالنا</a>'),

    # Why WORX
    ('<h2>Why WORX?</h2>', '<h2>لماذا WORX؟</h2>'),
    ('From design to delivery, your satisfaction is our top priority.', 'من التصميم حتى التسليم، رضاك هو أولويتنا الأولى.'),
    ('alt="WORX technician assembling kitchen parts at the counter"', 'alt="فني من WORX يجمّع قطع المطبخ على سطح العمل"'),
    ('aria-label="WORX team members installing a kitchen sink"', 'aria-label="فريق WORX أثناء تركيب حوض مطبخ"'),
    ('<strong>Our team at work</strong><span>Installation in progress</span>', '<strong>فريقنا أثناء العمل</strong><span>أعمال التركيب</span>'),
    ('<h3>Manufacturing Specialists</h3>', '<h3>متخصصون في التصنيع</h3>'),
    ('Having our own factory contributes to our ability to offer our customers the best quality, the best prices, and the strongest warranties.',
     'امتلاكنا لمصنعنا الخاص يمكّننا من تقديم أفضل جودة وأفضل الأسعار وأقوى الضمانات لعملائنا.'),
    ('alt="Two WORX designers reviewing a project on a laptop in the showroom"', 'alt="اثنان من مصممي WORX يراجعان مشروعاً على اللابتوب في المعرض"'),
    ('<h3>On-time Completion</h3>', '<h3>التسليم في الموعد</h3>'),
    ('We work with you to meet deadlines. Maintaining open communication is a must, that is why we have a customer support team available 24/7, and a WhatsApp group available once you sign the contract to help you with all your inquiries.',
     'نعمل معك للالتزام بالمواعيد. التواصل المستمر أمر أساسي، لذلك لدينا فريق خدمة عملاء متاح على مدار الساعة طوال أيام الأسبوع، ومجموعة واتساب خاصة بك فور توقيع العقد لمساعدتك في جميع استفساراتك.'),
    ('alt="Finished WORX kitchen with a walnut dining bar and lit display cabinet"', 'alt="مطبخ منفّذ من WORX بطاولة طعام من خشب الجوز وخزانة عرض مضاءة"'),
    ('<h3>Great Service</h3>', '<h3>خدمة مميزة</h3>'),
    ('We combine our industry knowledge, the highest quality equipment, and our dedication to deliver exceptional service to our clients. We will stay in touch, keeping you up to date on every step of your project.',
     'نجمع بين خبرتنا في المجال وأعلى جودة في المعدات والتزامنا بتقديم خدمة استثنائية لعملائنا. سنبقى على تواصل دائم معك لنطلعك على كل خطوة في مشروعك.'),

    # Services
    ('<p class="eyebrow eyebrow--light">Services</p>', '<p class="eyebrow eyebrow--light">خدماتنا</p>'),
    ('<h2>What we do</h2>', '<h2>ماذا نقدم</h2>'),
    ('<h3>Made in Our Factory</h3>', '<h3>صُنع في مصنعنا</h3>'),
    ('Every piece is manufactured in our own factory using quality materials and precise machinery, giving you a perfect finish and fair prices.',
     'كل قطعة تُصنع في مصنعنا الخاص بخامات عالية الجودة وماكينات دقيقة، لتحصل على تشطيب مثالي وأسعار عادلة.'),
    ('<h3>Professional Installation</h3>', '<h3>تركيب احترافي</h3>'),
    ('Our own trained team installs every kitchen and dressing room, on schedule and with care for your home, leaving everything clean and ready to use.',
     'فريقنا المدرَّب يركّب كل مطبخ وغرفة ملابس في الموعد المحدد وبعناية بمنزلك، ويترك كل شيء نظيفاً وجاهزاً للاستخدام.'),
    ('<h3>10-Year Warranty</h3>', '<h3>ضمان 10 سنوات</h3>'),
    ('Every WORX kitchen and dressing room is covered by a 10-year warranty. If anything needs attention — from a hinge to a drawer — our team comes back and fixes it properly.',
     'كل مطابخ وغرف ملابس WORX مشمولة بضمان لمدة 10 سنوات. وإذا احتاج أي شيء إلى صيانة — من مفصلة إلى درج — يعود فريقنا لإصلاحه كما يجب.'),

    # In the details
    ('aria-label="Tour of a WORX kitchen: pull-out pantry, fold-out table, under-sink organizer, appliance cabinet and vegetable drawers"',
     'aria-label="جولة في مطبخ من WORX: مخزن منزلق، طاولة قابلة للطي، منظم أسفل الحوض، خزانة للأجهزة وأدراج للخضروات"'),
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
    ('alt="Grey gloss and oak kitchen with white island, wood bar and black pendant lights"', 'alt="مطبخ رمادي لامع وخشب البلوط بجزيرة بيضاء وبار خشبي وإضاءة معلقة سوداء"'),
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
    ('alt="Peninsula kitchen with open shelves looking toward a glass staircase"', 'alt="مطبخ بجزيرة ورفوف مفتوحة يطل على درج زجاجي"'),
    ('alt="Oak and matte black kitchen with breakfast bar and pendant lights"', 'alt="مطبخ من خشب البلوط والأسود المطفي ببار إفطار وإضاءة معلقة"'),
    ('alt="White gloss L-shaped kitchen with black-framed glass display cabinets"', 'alt="مطبخ أبيض لامع على شكل L بخزائن عرض زجاجية بإطار أسود"'),
    ('alt="Fluted cabinet fronts over a granite backsplash"', 'alt="واجهات خزائن مضلّعة فوق تكسية جرانيت"'),
    ('alt="Sage green base cabinets, oak uppers and grey marble backsplash"', 'alt="خزائن سفلية خضراء وعلوية من البلوط وتكسية رخام رمادي"'),
    ('alt="Light grey kitchen with oak tall units and built-in ovens"', 'alt="مطبخ رمادي فاتح بوحدات طويلة من البلوط وأفران مدمجة"'),
    ('alt="Built-in oven in sage green cabinetry under a granite worktop"', 'alt="فرن مدمج في خزائن خضراء أسفل سطح جرانيت"'),
    ('alt="Fluted beige kitchen with open shelving and built-in ovens"', 'alt="مطبخ بيج بواجهات مضلّعة ورفوف مفتوحة وأفران مدمجة"'),
    ('alt="Kitchen island with pendant lights and wood cabinetry"', 'alt="جزيرة مطبخ بإضاءة معلقة وخزائن خشبية"'),
    ('alt="Dark wood kitchen with lit glass display cabinet"', 'alt="مطبخ خشبي داكن بخزانة عرض زجاجية مضاءة"'),
    ('alt="Corner cabinet with pull-out carousel shelves"', 'alt="خزانة ركنية برفوف دوّارة منزلقة"'),
    ('aria-label="Previous projects"', 'aria-label="المشاريع السابقة"'),
    ('aria-label="Next projects"', 'aria-label="المشاريع التالية"'),
    ('aria-label="Project photos, swipe to see more"', 'aria-label="صور المشاريع، اسحب لرؤية المزيد"'),

    # Videos
    ('<p class="eyebrow eyebrow--light">Watch</p>', '<p class="eyebrow eyebrow--light">شاهد</p>'),
    ('<h2>Take the tour</h2>', '<h2>جولة داخل أعمالنا</h2>'),
    ('Step inside finished WORX projects.', 'ادخل إلى مشاريع WORX المنفّذة.'),
    ('aria-label="Tour of four WORX dressing rooms and a vanity"', 'aria-label="جولة في أربع غرف ملابس وتسريحة من WORX"'),
    ('<strong>The WORX Collection: Dressing</strong><span>Four dressing rooms and a vanity</span>',
     '<strong>مجموعة WORX: غرف الملابس</strong><span>أربع غرف ملابس وتسريحة</span>'),
    ('aria-label="Tour of a beige fluted WORX kitchen with a granite island"', 'aria-label="جولة في مطبخ بيج بواجهات مضلّعة وجزيرة جرانيت من WORX"'),
    ('<strong>Fluted kitchen tour</strong><span>Granite island, fluted cabinets, built-in ovens</span>',
     '<strong>جولة في مطبخ بواجهات مضلّعة</strong><span>جزيرة جرانيت، خزائن مضلّعة، أفران مدمجة</span>'),

    # Reviews (each review stays in the language it was written in)
    ('<small class="review__src">Google review</small>', '<small class="review__src" lang="ar" dir="rtl">تقييم على جوجل</small>', 9),
    ('Real reviews from our customers on Google.', 'تقييمات حقيقية من عملائنا على جوجل.'),
    ('<span>on Google</span></a>', '<span>على جوجل</span></a>'),
    ('rel="noopener">Read all our reviews on Google</a>', 'rel="noopener">اقرأ جميع تقييماتنا على جوجل</a>'),
    ('<p class="eyebrow">Reviews</p>', '<p class="eyebrow">آراء العملاء</p>'),
    ('<h2>What our clients say</h2>', '<h2>ماذا يقول عملاؤنا</h2>'),

    # Team
    ('<h3 class="team-group__title">Engineers &amp; Leaders</h3>', '<h3 class="team-group__title">المهندسون والقيادات</h3>'),
    ('<h3 class="team-group__title">Factory Team</h3>', '<h3 class="team-group__title">فريق المصنع</h3>'),
    ('<h3 class="team-group__title">Finance Team</h3>', '<h3 class="team-group__title">فريق الحسابات</h3>'),
    ('<h3 class="team-group__title">Social Media Team</h3>', '<h3 class="team-group__title">فريق السوشيال ميديا</h3>'),
    ('<p class="eyebrow">Our Team</p>', '<p class="eyebrow">فريقنا</p>'),
    ('<h2>The people behind WORX</h2>', '<h2>الفريق وراء WORX</h2>'),
    ('<strong>Marawan Mostafa</strong><span>Quality Control Engineer</span>', '<strong>مروان مصطفى</strong><span>مهندس مراقبة الجودة</span>'),
    ('<strong>Tarek Hossam</strong><span>Lead Showroom Designer</span>', '<strong>طارق حسام</strong><span>كبير مصممي المعرض</span>'),
    ('<strong>Muhammed Mahmoud</strong><span>Factory Manager</span>', '<strong>محمد محمود</strong><span>مدير المصنع</span>'),
    ('<strong>Youssef Shaaban</strong><span>Lead Manufacturing Engineer</span>', '<strong>يوسف شعبان</strong><span>كبير مهندسي التصنيع</span>'),
    ('<span class="initials">AM</span><strong>Amr Mohy</strong><span>Installation &amp; Inspection Engineer</span>', '<span class="initials">ع</span><strong>عمرو محيي</strong><span>مهندس التركيب والمعاينة</span>'),
    ('<strong>Mahmoud Radwan</strong><span>Showroom Designer</span>', '<strong>محمود رضوان</strong><span>مصمم المعرض</span>'),
    ('<strong>Esraa Alsahar</strong><span>Content Creator &amp; Social Media Specialist</span>', '<strong>إسراء الساحر</strong><span>صانعة محتوى وأخصائية سوشيال ميديا</span>'),
    ('<strong>Basma Ashraf</strong><span>HR</span>', '<strong>بسمة أشرف</strong><span>الموارد البشرية</span>'),
    ('<strong>Mahmoud Mostafa</strong><span>Professional Legal Accountant</span>', '<strong>محمود مصطفى</strong><span>محاسب قانوني</span>'),
    ('<strong>Salsabil Mohamed</strong><span>Social Media Interior Designer</span>', '<strong>سلسبيل محمد</strong><span>مصممة ديكور داخلي للسوشيال ميديا</span>'),
    ('<strong>Nada Alsahhar</strong><span>Customer Service</span>', '<strong>ندى السحار</strong><span>خدمة العملاء</span>'),
    ('<strong>Al Sayed Ibrahim</strong><span>Interior Designer</span>', '<strong>السيد إبراهيم</strong><span>مصمم ديكور داخلي</span>'),
    ('<strong>Abd-Allah Fekry</strong><span>Price Estimation Accountant</span>', '<strong>عبدالله فكري</strong><span>محاسب تسعير</span>'),
    ('<strong>Ahmad Salah</strong><span>Purchases</span>', '<strong>أحمد صلاح</strong><span>المشتريات</span>'),

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
    ('<dt>Hours</dt><dd>All week: 12pm – 11:45pm</dd>', '<dt>مواعيد العمل</dt><dd>طوال أيام الأسبوع: 12 ظهراً – 11:45 مساءً</dd>'),
    ('aria-label="WORX on Facebook"', 'aria-label="WORX على فيسبوك"', 2),
    ('aria-label="WORX on Instagram"', 'aria-label="WORX على إنستجرام"', 2),
    ('<h3>Send a message</h3>', '<h3>أرسل رسالة</h3>'),
    ('<label>Name<input', '<label>الاسم<input'),
    ('<label>Phone<input', '<label>الهاتف<input'),
    ('<label>Address<input name="address" autocomplete="street-address" placeholder="Street, city">', '<label>العنوان<input name="address" autocomplete="street-address" placeholder="الشارع، المدينة">'),
    ('<label>Message<textarea name="message" rows="4" placeholder="Tell us about your kitchen or dressing room">', '<label>الرسالة<textarea name="message" rows="4" placeholder="أخبرنا عن مطبخك أو غرفة ملابسك">'),
    ('btn--block">Send via WhatsApp</button>', 'btn--block">إرسال عبر واتساب</button>'),
    ('<p class="form__note">Opens WhatsApp with your message ready to send to 01117776327.</p>',
     '<p class="form__note">يفتح واتساب ورسالتك جاهزة للإرسال إلى <bdi dir="ltr">01117776327</bdi>.</p>'),
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
