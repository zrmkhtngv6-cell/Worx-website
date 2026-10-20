// WhatsApp number used by the quote form (international format, digits only)
const WHATSAPP_NUMBER = '201117776589';

const header = document.querySelector('.header');
const nav = document.getElementById('nav');
const toggle = document.getElementById('navToggle');

// Mobile menu
toggle.addEventListener('click', () => {
  const open = nav.classList.toggle('is-open');
  toggle.setAttribute('aria-expanded', open);
  toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
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

// Gallery filters
const galleryItems = [...document.querySelectorAll('.gallery__item')];
document.querySelectorAll('.filter').forEach(btn => btn.addEventListener('click', () => {
  document.querySelectorAll('.filter').forEach(b => {
    b.classList.toggle('is-active', b === btn);
    b.setAttribute('aria-pressed', b === btn);
  });
  galleryItems.forEach(item => {
    item.hidden = btn.dataset.filter !== 'all' && item.dataset.cat !== btn.dataset.filter;
  });
}));

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
  if (e.key === 'ArrowLeft') show(current - 1);
  if (e.key === 'ArrowRight') show(current + 1);
});
let touchX = null;
lightbox.addEventListener('touchstart', e => { touchX = e.touches[0].clientX; }, { passive: true });
lightbox.addEventListener('touchend', e => {
  if (touchX === null) return;
  const dx = e.changedTouches[0].clientX - touchX;
  if (Math.abs(dx) > 50) show(current + (dx < 0 ? 1 : -1));
  touchX = null;
});

// Quote form → WhatsApp
document.getElementById('quoteForm').addEventListener('submit', e => {
  e.preventDefault();
  const data = new FormData(e.target);
  const lines = [
    'Hello WORX, I would like a free quote.',
    `Name: ${data.get('name')}`,
    `Phone: ${data.get('phone')}`,
    data.get('address') && `Address: ${data.get('address')}`,
    data.get('message') && `Message: ${data.get('message')}`,
  ].filter(Boolean);
  window.open(`https://wa.me/${WHATSAPP_NUMBER}?text=${encodeURIComponent(lines.join('\n'))}`, '_blank', 'noopener');
});

document.getElementById('year').textContent = new Date().getFullYear();
