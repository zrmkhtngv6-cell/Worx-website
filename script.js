// WhatsApp number used by the quote form (international format, digits only)
const WHATSAPP_NUMBER = '201117776327';

// Text set from script, per page language (index.html = en, ar.html = ar)
const STRINGS = {
  en: {
    openMenu: 'Open menu', closeMenu: 'Close menu',
    waIntro: 'Hello WORX, I would like a free quote.', waName: 'Name', waPhone: 'Phone', waAddress: 'Address', waMessage: 'Message',
  },
  ar: {
    openMenu: 'فتح القائمة', closeMenu: 'إغلاق القائمة',
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

// Gallery: swipeable carousel with filters, arrows and a progress bar
const gallery = document.querySelector('.gallery');
const galleryItems = [...gallery.querySelectorAll('.gallery__item')];
const prevBtn = document.querySelector('.carousel__prev');
const nextBtn = document.querySelector('.carousel__next');
const bar = document.querySelector('.carousel__bar');
// scrollLeft runs negative in right-to-left layouts
const scrollPos = () => Math.abs(gallery.scrollLeft);
const updateCarousel = () => {
  const max = gallery.scrollWidth - gallery.clientWidth;
  const ratio = gallery.clientWidth / gallery.scrollWidth;
  bar.style.width = `${Math.min(100, ratio * 100)}%`;
  bar.style.transform = `translateX(${(rtl ? -1 : 1) * (max > 0 ? scrollPos() / max : 0) * (1 / ratio - 1) * 100}%)`;
  prevBtn.disabled = scrollPos() < 5;
  nextBtn.disabled = scrollPos() > max - 5;
};
const step = dir => gallery.scrollBy({ left: dir * (rtl ? -1 : 1) * gallery.clientWidth * 0.8 });
prevBtn.addEventListener('click', () => step(-1));
nextBtn.addEventListener('click', () => step(1));
gallery.addEventListener('scroll', updateCarousel, { passive: true });
window.addEventListener('resize', updateCarousel);
document.querySelectorAll('.filter').forEach(btn => btn.addEventListener('click', () => {
  document.querySelectorAll('.filter').forEach(b => {
    b.classList.toggle('is-active', b === btn);
    b.setAttribute('aria-pressed', b === btn);
  });
  galleryItems.forEach(item => {
    item.hidden = btn.dataset.filter !== 'all' && item.dataset.cat !== btn.dataset.filter;
  });
  gallery.scrollTo({ left: 0, behavior: 'instant' });
  updateCarousel();
}));
galleryItems.forEach(item => item.querySelector('img').addEventListener('load', updateCarousel));
updateCarousel();

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

// All videos loop silently; play only while on screen to save data
const loopVideos = [...document.querySelectorAll('video[autoplay]')];
const videoObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.play().catch(() => {});
    else entry.target.pause();
  });
}, { threshold: 0.25 });
loopVideos.forEach(v => videoObserver.observe(v));

// WORX Kids links: leave empty to show "Coming soon"; add the address to send visitors there
const KIDS_LINKS = {
  kids: '', // e.g. 'https://worxkids.com'
  shop: '', // e.g. 'https://shop.worxkids.com'
};
const soon = document.getElementById('soon');
const closeSoon = () => { soon.hidden = true; };
document.querySelectorAll('[data-soon]').forEach(btn => {
  const url = KIDS_LINKS[btn.dataset.soon];
  if (url) {
    btn.href = url;
    btn.target = '_blank';
    btn.rel = 'noopener';
    return;
  }
  btn.addEventListener('click', e => {
    e.preventDefault();
    document.getElementById('soonLabel').textContent = btn.textContent.trim() || btn.querySelector('img').alt;
    soon.hidden = false;
    soon.querySelector('.soon__close').focus();
  });
});
soon.addEventListener('click', e => { if (e.target === soon || e.target.classList.contains('soon__close')) closeSoon(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape' && !soon.hidden) closeSoon(); });

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
