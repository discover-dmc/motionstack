---
name: locomotive-scroll
description: Comprehensive skill for Locomotive Scroll smooth scrolling library with parallax effects, viewport detection, and scroll-driven animations. Use this skill when implementing smooth scrolling experiences, creating parallax effects, building scroll-triggered animations, or developing immersive scrolling websites. Triggers on tasks involving Locomotive Scroll, smooth scrolling, parallax, scroll detection, scroll events, sticky elements, horizontal scrolling, or GSAP ScrollTrigger integration. Integrates with GSAP for advanced scroll-driven animations.
---

# Locomotive Scroll

Comprehensive guide for implementing smooth scrolling, parallax effects, and scroll-driven animations using Locomotive Scroll.

## Version & Status

**Current: v5.0.1** (Jan 2026). v5 is a complete rewrite built on top of [Lenis](https://github.com/darkroomengineering/lenis) — 9.4kB gzipped, TypeScript-first, no more `data-scroll-container`/`data-scroll-section` wrapper markup or CSS-transform scrolling. Actively maintained (8.8k stars, recent releases).

Patterns below are v5 (current) unless marked **Legacy (v4)**. Older production codebases still on v4 will use the container/section markup and `scrollerProxy` GSAP pattern — those are preserved under Legacy headings.

## Overview

Locomotive Scroll is a JavaScript library that provides:
- **Smooth scrolling**: Hardware-accelerated smooth scroll with customizable easing
- **Parallax effects**: Element-level speed control for depth
- **Viewport detection**: Track when elements enter/exit viewport
- **Scroll events**: Monitor scroll progress for animation synchronization
- **Sticky elements**: Pin elements within defined boundaries
- **Horizontal scrolling**: Support for horizontal scroll layouts

**When to use Locomotive Scroll:**
- Building immersive landing pages with parallax
- Creating smooth, Apple-style scroll experiences
- Implementing scroll-triggered animations
- Developing narrative/storytelling websites
- Adding depth and motion to long-form content

**Trade-offs:**
- Scroll-hijacking can impact accessibility (provide disable option)
- Performance overhead on low-end devices (detect and disable)
- Mobile touch scrolling feels different (test extensively)
- Fixed positioning requires workarounds

## Installation

```bash
npm install locomotive-scroll
```

```javascript
// ES6 (v5)
import LocomotiveScroll from 'locomotive-scroll';

const scroll = new LocomotiveScroll();
```

```css
@import 'locomotive-scroll/dist/locomotive-scroll.css';
```

```html
<!-- Or via CDN -->
<script src="https://cdn.jsdelivr.net/npm/locomotive-scroll/bundled/locomotive-scroll.min.js"></script>
<script>
  const locomotiveScroll = new LocomotiveScroll();
</script>
```

v5 scrolls the whole document by default — no wrapper markup required. To scroll a custom container, pass `lenisOptions: { wrapper, content }` (same shape as [Lenis](https://github.com/darkroomengineering/lenis)'s own options).

## Core Concepts

### 1. HTML Structure (v5)

No container/section wrapper attributes are needed. Mark individual elements for detection and parallax directly:

```html
<h1 data-scroll>Basic detection</h1>

<!-- Parallax element -->
<div data-scroll data-scroll-speed="2">
  Moves faster than scroll
</div>

<!-- Element with ID for tracking -->
<div data-scroll data-scroll-id="hero">
  Accessible via JavaScript
</div>

<!-- Call event trigger -->
<div data-scroll data-scroll-call="fadeIn">
  Triggers custom event
</div>
```

**Legacy (v4)**: v4 required `data-scroll-container` wrapping the page and `data-scroll-section` around each section for performance. Both attributes and the `data-scroll-sticky`/`data-scroll-target` sticky system are gone in v5 — use native CSS `position: sticky` instead.

### 2. Initialization (v5)

```javascript
const scroll = new LocomotiveScroll({
  lenisOptions: {
    lerp: 0.1,          // Smoothness (0-1, lower = smoother)
    duration: 1.2,
    wheelMultiplier: 1,
    touchMultiplier: 2,
  },
  triggerRootMargin: '-1px -1px -1px -1px', // IntersectionObserver margin for triggers
  rafRootMargin: '100% 100% 100% 100%',     // margin for continuously-animated elements
  autoStart: true,     // false if driving the raf loop externally (e.g. GSAP ticker)
});
```

**Legacy (v4)**:
```javascript
const scroll = new LocomotiveScroll({
  el: document.querySelector('[data-scroll-container]'),
  smooth: true,
  lerp: 0.1,
  multiplier: 1,
  class: 'is-inview',
  repeat: false,
  offset: [0, 0]
});
```

### 3. Data Attributes (v5)

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `data-scroll` | Enable detection | `data-scroll` |
| `data-scroll-speed` | Parallax speed | `data-scroll-speed="2"` |
| `data-scroll-position` | Parallax start reference | `data-scroll-position="top"` |
| `data-scroll-repeat` | Repeat detection | `data-scroll-repeat` |
| `data-scroll-call` | Event trigger | `data-scroll-call="myFunction"` |
| `data-scroll-class` | Custom class | `data-scroll-class="is-visible"` |
| `data-scroll-event-progress` | Fires progress on scroll callback | `data-scroll-event-progress` |

`data-scroll-container`, `data-scroll-section`, `data-scroll-sticky`, `data-scroll-target`, and `data-scroll-id` are v4-only. Consult [scroll.locomotive.ca/docs](https://scroll.locomotive.ca/docs/documentation/options) for the full current attribute list before shipping.

## Common Patterns

**Legacy (v4)**: the examples below use v4's `data-scroll-container`/`data-scroll-section` markup, `el`/`smooth`/`tablet`/`smartphone` options, and `data-scroll-sticky`. On v5, drop the container/section wrappers (scroll the document directly or pass `lenisOptions.wrapper`/`content`), replace sticky elements with native CSS `position: sticky`, and pass responsive tuning through `lenisOptions`.

### 1. Basic Smooth Scrolling

```javascript
import LocomotiveScroll from 'locomotive-scroll';

const scroll = new LocomotiveScroll({
  el: document.querySelector('[data-scroll-container]'),
  smooth: true
});
```

```html
<div data-scroll-container>
  <div data-scroll-section>
    <h1>Smooth scrolling enabled</h1>
  </div>
</div>
```

### 2. Parallax Effects

```html
<!-- Slow parallax -->
<div data-scroll data-scroll-speed="0.5">
  Moves slower than scroll (background effect)
</div>

<!-- Fast parallax -->
<div data-scroll data-scroll-speed="3">
  Moves faster than scroll (foreground effect)
</div>

<!-- Reverse parallax -->
<div data-scroll data-scroll-speed="-2">
  Moves in opposite direction
</div>

<!-- Horizontal parallax -->
<div data-scroll data-scroll-speed="2" data-scroll-direction="horizontal">
  Moves horizontally
</div>
```

### 3. Viewport Detection and Callbacks

```javascript
// Track scroll progress
scroll.on('scroll', (args) => {
  console.log(args.scroll.y); // Current scroll position
  console.log(args.speed);    // Scroll speed
  console.log(args.direction); // Scroll direction

  // Access specific element progress
  if (args.currentElements['hero']) {
    const progress = args.currentElements['hero'].progress;
    console.log(`Hero progress: ${progress}`); // 0 to 1
  }
});

// Call events
scroll.on('call', (value, way, obj) => {
  console.log(`Event triggered: ${value}`);
  // value = data-scroll-call attribute value
  // way = 'enter' or 'exit'
  // obj = {id, el}
});
```

```html
<div data-scroll data-scroll-id="hero">Hero section</div>
<div data-scroll data-scroll-call="playVideo">Video section</div>
```

### 4. Sticky Elements

```html
<!-- Stick within parent section -->
<div data-scroll-section>
  <div data-scroll data-scroll-sticky>
    I stick while section is in view
  </div>
</div>

<!-- Stick with specific target -->
<div id="sticky-container">
  <div data-scroll data-scroll-sticky data-scroll-target="#sticky-container">
    I stick within #sticky-container
  </div>
</div>
```

### 5. Programmatic Scrolling

```javascript
// Scroll to element
scroll.scrollTo('#target-section');

// Scroll to top
scroll.scrollTo('top');

// Scroll to bottom
scroll.scrollTo('bottom');

// Scroll with options
scroll.scrollTo('#target', {
  offset: -100,      // Offset in pixels
  duration: 1000,    // Duration in ms
  easing: [0.25, 0.0, 0.35, 1.0], // Cubic bezier
  disableLerp: true, // Disable smooth lerp
  callback: () => console.log('Scrolled!')
});

// Scroll to pixel value
scroll.scrollTo(500);
```

### 6. Horizontal Scrolling

```javascript
const scroll = new LocomotiveScroll({
  el: document.querySelector('[data-scroll-container]'),
  smooth: true,
  direction: 'horizontal'
});
```

```html
<div data-scroll-container>
  <div data-scroll-section style="display: flex; width: 300vw;">
    <div>Section 1</div>
    <div>Section 2</div>
    <div>Section 3</div>
  </div>
</div>
```

### 7. Mobile Responsiveness

```javascript
const scroll = new LocomotiveScroll({
  el: document.querySelector('[data-scroll-container]'),
  smooth: true,

  // Tablet settings
  tablet: {
    smooth: true,
    breakpoint: 1024
  },

  // Smartphone settings
  smartphone: {
    smooth: false, // Disable on mobile for performance
    breakpoint: 768
  }
});
```

## Integration with GSAP ScrollTrigger

v5 is built on Lenis, which moves the real scroll position instead of transforming a wrapper — so the v4 `scrollerProxy`/`pinType` dance is no longer needed. Drive Lenis's raf loop from GSAP's ticker and forward scroll events to `ScrollTrigger.update()`:

```javascript
import LocomotiveScroll from 'locomotive-scroll';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const scroll = new LocomotiveScroll({
  autoStart: false, // GSAP's ticker drives the raf loop instead
  scrollCallback: () => ScrollTrigger.update(),
  initCustomTicker: (render) => {
    gsap.ticker.add(render);
    gsap.ticker.lagSmoothing(0);
  },
  destroyCustomTicker: (render) => gsap.ticker.remove(render),
});

// Regular ScrollTrigger usage, no custom scroller needed
gsap.to('.fade-in', {
  scrollTrigger: {
    trigger: '.fade-in',
    start: 'top bottom',
    end: 'top center',
    scrub: true
  },
  opacity: 1,
  y: 0
});

ScrollTrigger.refresh();
```

**Legacy (v4)**: v4's transform-based scroll required telling ScrollTrigger how to read/write it via `scrollerProxy`:

```javascript
import LocomotiveScroll from 'locomotive-scroll';
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

const locoScroll = new LocomotiveScroll({
  el: document.querySelector('[data-scroll-container]'),
  smooth: true
});

// Sync Locomotive Scroll with ScrollTrigger
locoScroll.on('scroll', ScrollTrigger.update);

ScrollTrigger.scrollerProxy('[data-scroll-container]', {
  scrollTop(value) {
    return arguments.length
      ? locoScroll.scrollTo(value, 0, 0)
      : locoScroll.scroll.instance.scroll.y;
  },
  getBoundingClientRect() {
    return {
      top: 0,
      left: 0,
      width: window.innerWidth,
      height: window.innerHeight
    };
  },
  pinType: document.querySelector('[data-scroll-container]').style.transform
    ? 'transform'
    : 'fixed'
});

// GSAP animation with ScrollTrigger
gsap.to('.fade-in', {
  scrollTrigger: {
    trigger: '.fade-in',
    scroller: '[data-scroll-container]',
    start: 'top bottom',
    end: 'top center',
    scrub: true
  },
  opacity: 1,
  y: 0
});

// Update ScrollTrigger when Locomotive updates
ScrollTrigger.addEventListener('refresh', () => locoScroll.update());
ScrollTrigger.refresh();
```

## Instance Methods

Core lifecycle/navigation methods below are stable across v4 and v5 (v5 proxies most of them to Lenis). Confirm exact v5 signatures against [scroll.locomotive.ca/docs](https://scroll.locomotive.ca/docs) before relying on option details like `scrollTo`'s easing/offset shape.

```javascript
const scroll = new LocomotiveScroll();

// Lifecycle
scroll.init();     // Reinitialize
scroll.update();   // Refresh element positions
scroll.destroy();  // Clean up
scroll.start();    // Resume scrolling
scroll.stop();     // Pause scrolling

// Navigation
scroll.scrollTo(target, options);
scroll.setScroll(x, y);

// Events
scroll.on('scroll', callback);
scroll.on('call', callback);
scroll.off('scroll', callback);
```

## Performance Optimization

1. **Legacy (v4) only** — segment long pages with `data-scroll-section`:
```html
<div data-scroll-container>
  <div data-scroll-section>Section 1</div>
  <div data-scroll-section>Section 2</div>
  <div data-scroll-section>Section 3</div>
</div>
```
v5's dual IntersectionObserver strategy replaces this; no manual sectioning needed.

2. **Limit parallax elements** - Too many can impact performance

3. **Disable smooth scroll on mobile** if performance is poor — v5 auto-disables parallax on touch devices; to fully disable smoothing, tune `lenisOptions.smoothTouch: false`. (v4: `smartphone: { smooth: false }`)

4. **Update on resize**:
```javascript
window.addEventListener('resize', () => {
  scroll.update();
});
```

5. **Destroy when not needed**:
```javascript
scroll.destroy();
```

## Common Pitfalls

### 1. Fixed Positioning Issues

**Problem**: `position: fixed` elements break with smooth scroll

**Solution (v5)**: v5 doesn't transform a wrapper, so native `position: fixed` and `position: sticky` work without special attributes — no `data-scroll-sticky` needed.

**Legacy (v4)**: Use `data-scroll-sticky` instead or add fixed elements outside container:
```html
<!-- Fixed nav outside container -->
<nav style="position: fixed;">Navigation</nav>

<div data-scroll-container>
  <!-- Page content -->
</div>
```

### 2. Images Not Lazy Loading

**Problem**: All images load at once

**Solution**: Integrate with lazy loading:
```html
<img data-scroll data-src="image.jpg" class="lazy">
```

```javascript
scroll.on('call', (func) => {
  if (func === 'lazyLoad') {
    // Trigger lazy load
  }
});
```

### 3. Scroll Position Not Updating

**Problem**: Dynamic content doesn't update scroll positions

**Solution**: Call `update()` after DOM changes:
```javascript
// After adding content
addDynamicContent();
scroll.update();
```

### 4. Accessibility Concerns

**Problem**: Screen readers and keyboard navigation broken

**Solution (v5)**: Provide disable option via `lenisOptions`:
```javascript
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const scroll = new LocomotiveScroll({
  lenisOptions: {
    smoothWheel: !prefersReducedMotion,
    smoothTouch: !prefersReducedMotion
  }
});
```

**Legacy (v4)**: `new LocomotiveScroll({ smooth: !prefersReducedMotion })`

### 5. Memory Leaks

**Problem**: Scroll instance not cleaned up on route changes (SPAs)

**Solution**: Always destroy on unmount:
```javascript
// React example
useEffect(() => {
  const scroll = new LocomotiveScroll();

  return () => scroll.destroy();
}, []);
```

### 6. Z-Index Fighting

**Problem**: Parallax elements overlap incorrectly

**Solution**: Set explicit z-index on parallax layers:
```css
[data-scroll-speed] {
  position: relative;
  z-index: var(--layer-depth);
}
```

## Related Skills

- **gsap-scrolltrigger**: Advanced scroll-driven animations (use together)
- **barba-js**: Page transitions with Locomotive Scroll integration
- **scroll-reveal-libraries**: Simpler alternative for basic fade-in effects
- **react-three-fiber**: Scroll-driven 3D scenes (sync with Locomotive events)
- **motion-framer**: Alternative scroll animations in React

## Resources

- **Scripts**: `generate_config.py` - Configuration generator, `integration_helper.py` - GSAP integration code
- **References**: `api_reference.md` - Complete API, `gsap_integration.md` - GSAP ScrollTrigger patterns
- **Assets**: `starter_locomotive/` - Complete starter template with examples
