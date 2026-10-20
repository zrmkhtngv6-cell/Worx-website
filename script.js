// WhatsApp number used by the quote form (international format, digits only)
const WHATSAPP_NUMBER = '201117776589';

// Text set from script, per page language (index.html = en, ar.html = ar)
const STRINGS = {
  en: {
    openMenu: 'Open menu', closeMenu: 'Close menu', soundOn: 'Sound on', soundOff: 'Sound off',
    waIntro: 'Hello WORX, I would like a free quote.', waName: 'Name', waPhone: 'Phone', waAddress: 'Address', waMessage: 'Message',
  },
  ar: {
    openMenu: 'فتح القائمة', closeMenu: 'إغلاق القائمة', soundOn: 'تشغيل الصوت', soundOff: 'كتم الصوت',
    waIntro: 'مرحباً WORX، أود الحصول على عرض سعر مجاني.', waName: 'الاسم', waPhone: 'الهاتف', waAddress: 'العنوان', waMessage: 'الرسالة',
  },
};
const t = STRINGS[document.documentElement.lang] || STRINGS.en;
const rtl = document.documentElement.dir === 'rtl';

const header = document.querySelector('.header');
const nav = document.getElementById('nav');
const toggle = document.getElementById('navToggle');

// Mobile menu
toggle.addEventListener('click', () => {
  const open = nav.classList.toggle('is-open');
  toggle.setAttribute('aria-expanded', open);
  toggle.setAttribute('aria-label', open ? t.closeMenu : t.openMenu);
});
nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  nav.classList.remove('is-open');
  toggle.setAttribute('aria-expanded', 'false');
}));

// Header shadow on scroll
const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 10);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Highlight the nav link for the section in view
const links = [...nav.querySelectorAll('a[href^="#"]')];
const sectionObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    links.forEach(l => l.classList.toggle('is-active', l.getAttribute('href') === '#' + entry.target.id));
  });
}, { rootMargin: '-45% 0px -50% 0px' });
document.querySelectorAll('main section[id]').forEach(s => sectionObserver.observe(s));

// Fade sections in as they scroll into view
const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('is-visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.card, .service, .gallery__item, .review, .team li, .section__head').forEach(el => {
  el.classList.add('reveal');
  revealObserver.observe(el);
});

// Gallery filters; "All" starts collapsed to the first few projects
const GALLERY_PREVIEW = 12;
const galleryItems = [...document.querySelectorAll('.gallery__item')];
const showMore = document.getElementById('showMore');
let activeFilter = 'all';
let expanded = false;
const renderGallery = () => {
  const matches = galleryItems.filter(item => activeFilter === 'all' || item.dataset.cat === activeFilter);
  const limit = activeFilter === 'all' && !expanded ? GALLERY_PREVIEW : Infinity;
  galleryItems.forEach(item => { item.hidden = true; });
  matches.forEach((item, i) => { item.hidden = i >= limit; });
  showMore.parentElement.hidden = matches.length <= limit;
};
document.querySelectorAll('.filter').forEach(btn => btn.addEventListener('click', () => {
  document.querySelectorAll('.filter').forEach(b => {
    b.classList.toggle('is-active', b === btn);
    b.setAttribute('aria-pressed', b === btn);
  });
  activeFilter = btn.dataset.filter;
  renderGallery();
}));
showMore.addEventListener('click', () => { expanded = true; renderGallery(); });
renderGallery();

// Gallery lightbox with prev/next, keyboard and swipe
const lightbox = document.getElementById('lightbox');
const lightboxImg = lightbox.querySelector('img');
let current = 0;
const visibleItems = () => galleryItems.filter(i => !i.hidden);
const show = index => {
  const items = visibleItems();
  current = (index + items.length) % items.length;
  lightboxImg.src = items[current].dataset.full;
  lightboxImg.alt = items[current].querySelector('img').alt;
};
const closeLightbox = () => { lightbox.hidden = true; document.body.style.overflow = ''; };
galleryItems.forEach(item => item.addEventListener('click', () => {
  show(visibleItems().indexOf(item));
  lightbox.hidden = false;
  document.body.style.overflow = 'hidden';
}));
lightbox.querySelector('.lightbox__prev').addEventListener('click', e => { e.stopPropagation(); show(current - 1); });
lightbox.querySelector('.lightbox__next').addEventListener('click', e => { e.stopPropagation(); show(current + 1); });
lightbox.addEventListener('click', e => { if (e.target === lightbox || e.target.classList.contains('lightbox__close')) closeLightbox(); });
document.addEventListener('keydown', e => {
  if (lightbox.hidden) return;
  if (e.key === 'Escape') closeLightbox();
  if (e.key === 'ArrowLeft') show(current + (rtl ? 1 : -1));
  if (e.key === 'ArrowRight') show(current + (rtl ? -1 : 1));
});
let touchX = null;
lightbox.addEventListener('touchstart', e => { touchX = e.touches[0].clientX; }, { passive: true });
lightbox.addEventListener('touchend', e => {
  if (touchX === null) return;
  const dx = e.changedTouches[0].clientX - touchX;
  if (Math.abs(dx) > 50) show(current + ((dx < 0) !== rtl ? 1 : -1));
  touchX = null;
});

// Sound toggle for the kitchen tour (browsers only autoplay muted video)
const tour = document.getElementById('tourVideo');
const soundToggle = document.getElementById('soundToggle');
soundToggle.addEventListener('click', () => {
  tour.muted = !tour.muted;
  if (!tour.muted) tour.play();
  soundToggle.textContent = tour.muted ? t.soundOn : t.soundOff;
  soundToggle.setAttribute('aria-pressed', !tour.muted);
});

// Only one tour video plays at a time
const tourVideos = [...document.querySelectorAll('.video-card video')];
tourVideos.forEach(v => v.addEventListener('play', () => {
  tourVideos.forEach(other => { if (other !== v) other.pause(); });
}));

// Quote form → WhatsApp
document.getElementById('quoteForm').addEventListener('submit', e => {
  e.preventDefault();
  const data = new FormData(e.target);
  const lines = [
    t.waIntro,
    `${t.waName}: ${data.get('name')}`,
    `${t.waPhone}: ${data.get('phone')}`,
    data.get('address') && `${t.waAddress}: ${data.get('address')}`,
    data.get('message') && `${t.waMessage}: ${data.get('message')}`,
  ].filter(Boolean);
  window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(lines.join('\n'))}`, '_blank', 'noopener');
});

document.getElementById('year').textContent = new Date().getFullYear();
