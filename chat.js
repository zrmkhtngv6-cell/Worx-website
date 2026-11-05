// WORX chat assistant: answers common questions from site info, hands off to WhatsApp.
// Works without a server. Language follows the page (index.html = en, ar.html = ar).
(() => {
  const WHATSAPP = '201117776327';
  const PHONE = '+201117776327';
  const MAPS = 'https://www.google.com/maps/dir/?api=1&destination=Park+Mall,+90th+Street,+New+Cairo';
  const REVIEWS = 'https://share.google/TGDEe9j6qtUxFVQCB';
  const ar = document.documentElement.lang === 'ar';

  // Each topic: quick-reply label, keywords (English + Arabic, incl. Egyptian spellings), answer, optional link button.
  const TOPICS = [
    {
      id: 'price',
      label: ['Prices', 'الأسعار'],
      keys: ['price', 'cost', 'how much', 'meter', 'budget', 'expensive', 'cheap', 'quote', 'سعر', 'اسعار', 'أسعار', 'بكام', 'كام', 'تكلفة', 'المتر', 'متر', 'عرض سعر', 'ميزانية'],
      answer: [
        'We don’t price per meter — we price per unit. The cost depends on the materials, finishes and hardware you choose. Send us your space details and we’ll give you a free, no-obligation quote.',
        'لا نحسب السعر بالمتر، بل بالوحدة. ويعتمد السعر على الخامات والتشطيبات والإكسسوارات التي تختارها. ابعت لنا تفاصيل مساحتك ونقدّم لك عرض سعر مجاني ودون أي التزام.',
      ],
      action: 'whatsapp',
    },
    {
      id: 'warranty',
      label: ['Warranty', 'الضمان'],
      keys: ['warranty', 'guarantee', 'repair', 'broken', 'fix', 'maintenance', 'ضمان', 'صيانة', 'اصلاح', 'إصلاح', 'عطل', 'مكسور'],
      answer: [
        'Every WORX kitchen and dressing room comes with a 10-year warranty. If anything needs attention — from a hinge to a drawer — our team comes back and fixes it properly.',
        'كل مطابخ وغرف ملابس WORX عليها ضمان 10 سنوات. وإذا احتاج أي شيء لصيانة — من مفصلة لدرج — فريقنا يرجع ويصلّحه كما يجب.',
      ],
    },
    {
      id: 'location',
      label: ['Showroom location', 'عنوان المعرض'],
      keys: ['where', 'location', 'address', 'showroom', 'visit', 'map', 'directions', 'park mall', 'new cairo', 'فين', 'عنوان', 'العنوان', 'مكان', 'المعرض', 'معرض', 'لوكيشن', 'خريطة', 'بارك مول', 'التجمع'],
      answer: [
        'Our showroom is at G 32 AB, Park Mall, 90th Street, New Cairo. You’re welcome to visit any day from 12pm to 11:45pm.',
        'معرضنا في G 32 AB بارك مول، شارع التسعين، القاهرة الجديدة. أهلاً بيك أي يوم من 12 ظهراً لحد 11:45 مساءً.',
      ],
      action: 'map',
    },
    {
      id: 'hours',
      label: ['Opening hours', 'مواعيد العمل'],
      keys: ['hour', 'open', 'close', 'time', 'when', 'friday', 'today', 'مواعيد', 'ميعاد', 'امتى', 'إمتى', 'مفتوح', 'بتفتحوا', 'بتقفلوا', 'الجمعة', 'النهارده'],
      answer: [
        'We’re open every day of the week, from 12pm to 11:45pm.',
        'مفتوحين كل أيام الأسبوع من 12 ظهراً لحد 11:45 مساءً.',
      ],
    },
    {
      id: 'services',
      label: ['What do you make?', 'بتعملوا إيه؟'],
      keys: ['service', 'kitchen', 'dressing', 'wardrobe', 'closet', 'bathroom', 'vanity', 'tv unit', 'make', 'do you', 'مطبخ', 'مطابخ', 'دريسنج', 'دريسينج', 'غرفة ملابس', 'غرف ملابس', 'دولاب', 'حمام', 'وحدة', 'خدمات', 'بتعملوا'],
      answer: [
        'We design, manufacture and install custom kitchens, dressing rooms, wardrobes, bathroom vanities, TV units and more — all made in our own factory.',
        'بنصمم ونصنّع ونركّب مطابخ وغرف ملابس ودواليب ووحدات حمامات ووحدات تلفزيون وأكتر — وكلها بتتصنع في مصنعنا.',
      ],
      action: 'work',
    },
    {
      id: 'process',
      label: ['How does it work?', 'إيه الخطوات؟'],
      keys: ['process', 'step', 'how long', 'install', 'installation', 'duration', 'delivery', 'measure', 'design', 'خطوات', 'تركيب', 'مدة', 'قد ايه', 'قد إيه', 'تسليم', 'مقاسات', 'تصميم', 'معاينة'],
      answer: [
        'We start with measurements and a design consultation, agree the design and quote, manufacture everything in our factory, then our own team installs it. Once you sign, you get a WhatsApp group with our team, and customer support is available 24/7.',
        'بنبدأ بأخذ المقاسات وجلسة تصميم، بعدها نتفق على التصميم والسعر، ونصنّع كل حاجة في مصنعنا، وبعدين فريقنا يركّب. وبعد توقيع العقد بيكون لك جروب واتساب مع فريقنا، وخدمة العملاء متاحة 24 ساعة.',
      ],
    },
    {
      id: 'materials',
      label: ['Materials & countertops', 'الخامات والأسطح'],
      keys: ['material', 'countertop', 'worktop', 'marble', 'granite', 'quartz', 'wood', 'finish', 'color', 'colour', 'خامات', 'خامة', 'سطح', 'رخام', 'جرانيت', 'كوارتز', 'خشب', 'لون', 'ألوان', 'الوان'],
      answer: [
        'Countertop and finish options depend on your design and budget — marble, granite, quartz, wood finishes, gloss, matte, fluted and more. Visit the showroom or message us and our designers will walk you through them.',
        'خيارات الأسطح والتشطيبات بتعتمد على تصميمك وميزانيتك — رخام، جرانيت، كوارتز، خشب، لامع، مطفي، مضلّع وأكتر. زورنا في المعرض أو ابعت لنا ومصممينا هيعرضوا عليك الخيارات.',
      ],
    },
    {
      id: 'reviews',
      label: ['Reviews', 'آراء العملاء'],
      keys: ['review', 'rating', 'google', 'trust', 'customers', 'تقييم', 'تقييمات', 'آراء', 'اراء', 'جوجل'],
      answer: [
        'We’re rated 5.0 ★ on Google by our customers.',
        'تقييمنا 5.0 ★ على جوجل من عملائنا.',
      ],
      action: 'reviews',
    },
    {
      id: 'contact',
      label: ['Talk to the team', 'كلّم الفريق'],
      keys: ['contact', 'call', 'phone', 'number', 'whatsapp', 'talk', 'human', 'person', 'agent', 'رقم', 'تليفون', 'تلفون', 'موبايل', 'اتصل', 'واتس', 'واتساب', 'كلم', 'أكلم', 'اكلم'],
      answer: [
        'You can reach our team on WhatsApp or by phone at +20 111 777 6327 — every day, 12pm to 11:45pm.',
        'تقدر تكلم فريقنا على واتساب أو تليفون على 01117776327 — كل يوم من 12 ظهراً لحد 11:45 مساءً.',
      ],
      action: 'whatsapp',
    },
  ];

  const T = {
    title: ['WORX Assistant', 'مساعد WORX'],
    status: ['Usually replies instantly', 'يرد فوراً'],
    hello: ['Hi! 👋 I’m the WORX assistant. Ask me about prices, our warranty, the showroom — or pick a question below.', 'أهلاً! 👋 أنا مساعد WORX. اسألني عن الأسعار أو الضمان أو المعرض — أو اختار سؤال من تحت.'],
    placeholder: ['Type your question…', 'اكتب سؤالك…'],
    send: ['Send', 'إرسال'],
    open: ['Chat with us', 'تحدث معنا'],
    close: ['Close chat', 'إغلاق المحادثة'],
    fallback: ['I’m not sure about that one — our team will be happy to help. Tap below to message them on WhatsApp.', 'مش متأكد من الإجابة دي — فريقنا هيساعدك بكل سرور. اضغط تحت عشان تكلمهم على واتساب.'],
    thanks: ['You’re welcome! Anything else?', 'العفو! أقدر أساعدك في حاجة تانية؟'],
    btnWhatsapp: ['Message us on WhatsApp', 'كلّمنا على واتساب'],
    btnMap: ['Get directions', 'الاتجاهات للمعرض'],
    btnReviews: ['Read our reviews', 'اقرأ التقييمات'],
    btnWork: ['See our work', 'شوف أعمالنا'],
    btnCall: ['Call us', 'اتصل بنا'],
    waText: ['Hello WORX, I have a question:', 'مرحباً WORX، عندي سؤال:'],
  };
  const t = key => T[key][ar ? 1 : 0];

  // Arabic normalisation so أ/إ/آ, ة/ه and ى/ي spellings all match
  const norm = s => s.toLowerCase()
    .replace(/[ً-ْ]/g, '')
    .replace(/[أإآ]/g, 'ا').replace(/ة/g, 'ه').replace(/ى/g, 'ي');

  const findTopic = text => {
    const q = norm(text);
    let best = null, score = 0;
    TOPICS.forEach(topic => {
      const s = topic.keys.reduce((n, k) => n + (q.includes(norm(k)) ? norm(k).length : 0), 0);
      if (s > score) { score = s; best = topic; }
    });
    return best;
  };

  // --- UI ---
  const root = document.createElement('div');
  root.className = 'chat';
  root.innerHTML = `
    <button class="chat__bubble" type="button" aria-expanded="false" aria-controls="chatPanel" aria-label="${t('open')}">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 4h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H9l-5 4v-4H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zm3 6.5a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zm5 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3zm5 0a1.5 1.5 0 1 0 0 3 1.5 1.5 0 0 0 0-3z"/></svg>
    </button>
    <section class="chat__panel" id="chatPanel" role="dialog" aria-label="${t('title')}" hidden>
      <header class="chat__head">
        <img src="assets/img/logo-white.png" alt="" class="chat__logo">
        <div><strong>${t('title')}</strong><small>${t('status')}</small></div>
        <button class="chat__close" type="button" aria-label="${t('close')}">×</button>
      </header>
      <div class="chat__log" aria-live="polite"></div>
      <div class="chat__chips"></div>
      <form class="chat__form">
        <input type="text" autocomplete="off" placeholder="${t('placeholder')}" aria-label="${t('placeholder')}" maxlength="300">
        <button type="submit" aria-label="${t('send')}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 20l18-8L3 4v6l12 2-12 2z"/></svg></button>
      </form>
    </section>`;
  document.body.appendChild(root);

  const bubble = root.querySelector('.chat__bubble');
  const panel = root.querySelector('.chat__panel');
  const log = root.querySelector('.chat__log');
  const chips = root.querySelector('.chat__chips');
  const form = root.querySelector('.chat__form');
  const input = form.querySelector('input');
  let lastQuestion = '';

  const scroll = () => { log.scrollTop = log.scrollHeight; };
  const addMsg = (text, who) => {
    const el = document.createElement('div');
    el.className = `chat__msg chat__msg--${who}`;
    el.textContent = text;
    log.appendChild(el);
    scroll();
    return el;
  };
  const addAction = kind => {
    const links = {
      whatsapp: [`https://wa.me/${WHATSAPP}?text=${encodeURIComponent(`${t('waText')} ${lastQuestion}`.trim())}`, t('btnWhatsapp')],
      map: [MAPS, t('btnMap')],
      reviews: [REVIEWS, t('btnReviews')],
      work: ['#work', t('btnWork')],
      call: [`tel:${PHONE}`, t('btnCall')],
    };
    const [href, label] = links[kind];
    const a = document.createElement('a');
    a.className = 'chat__action';
    a.href = href;
    a.textContent = label;
    if (href.startsWith('http')) { a.target = '_blank'; a.rel = 'noopener'; }
    if (kind === 'work') a.addEventListener('click', () => toggle(false));
    log.appendChild(a);
    scroll();
  };
  const reply = (text, action) => {
    const typing = addMsg('…', 'bot');
    typing.classList.add('chat__msg--typing');
    setTimeout(() => {
      typing.remove();
      addMsg(text, 'bot');
      if (action) addAction(action);
    }, 450);
  };

  const answerTopic = topic => reply(topic.answer[ar ? 1 : 0], topic.action);
  const ask = text => {
    lastQuestion = text;
    addMsg(text, 'user');
    if (/^(thanks?|thank you|ty|شكرا|شكراً|متشكر|تسلم)/i.test(text.trim())) return reply(t('thanks'));
    const topic = findTopic(text);
    if (topic) answerTopic(topic);
    else reply(t('fallback'), 'whatsapp');
  };

  TOPICS.forEach(topic => {
    const b = document.createElement('button');
    b.type = 'button';
    b.className = 'chat__chip';
    b.textContent = topic.label[ar ? 1 : 0];
    b.addEventListener('click', () => {
      lastQuestion = topic.label[ar ? 1 : 0];
      addMsg(lastQuestion, 'user');
      answerTopic(topic);
    });
    chips.appendChild(b);
  });

  let greeted = false;
  const toggle = open => {
    panel.hidden = !open;
    root.classList.toggle('is-open', open);
    bubble.setAttribute('aria-expanded', open);
    if (open && !greeted) { greeted = true; addMsg(t('hello'), 'bot'); }
    if (open && window.matchMedia('(min-width: 700px)').matches) input.focus();
  };
  bubble.addEventListener('click', () => toggle(panel.hidden));
  root.querySelector('.chat__close').addEventListener('click', () => toggle(false));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && !panel.hidden) toggle(false); });
  form.addEventListener('submit', e => {
    e.preventDefault();
    const text = input.value.trim();
    if (!text) return;
    input.value = '';
    ask(text);
  });
})();
