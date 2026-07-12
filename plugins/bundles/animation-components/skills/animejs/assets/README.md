# Anime.js - Assets

This directory contains starter templates and example documentation for Anime.js v4 animations.

## Contents

### Starter Template (Recommended)

For a complete Anime.js starter template with Vite:

```bash
# Create new project with Vite (vanilla JS)
npm create vite@latest my-anime-app -- --template vanilla

# Navigate and install
cd my-anime-app
npm install

# Add Anime.js
npm install animejs
```

### Official Examples

The Anime.js team maintains excellent examples at:
- **Documentation**: https://animejs.com/documentation/
- **CodePen Examples**: https://codepen.io/collection/DxpqGJ/
- **Official Repository**: https://github.com/juliangarnier/anime

### Recommended Examples by Category

**Basic Animations:**
- Property values: https://animejs.com/documentation/animation
- Keyframes: https://animejs.com/documentation/animation/keyframes

**Stagger Animations:**
- Stagger utility: https://animejs.com/documentation/utilities/stagger

**Timeline Animations:**
- Timeline: https://animejs.com/documentation/timeline

**SVG Animations:**
- Line drawing: https://animejs.com/documentation/svg/createdrawable
- Path morphing: https://animejs.com/documentation/svg/morphto
- Motion path: https://animejs.com/documentation/svg/createmotionpath

**Interaction and Scroll:**
- Draggable: https://animejs.com/documentation/draggable
- Scroll-linked: https://animejs.com/documentation/events/onscroll
- Scope (React/Vue): https://animejs.com/documentation/scope

## Quick Start Template

Minimal Anime.js setup:

### package.json
```json
{
  "name": "animejs-starter",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "animejs": "^4.5.0"
  },
  "devDependencies": {
    "vite": "^5.0.8"
  }
}
```

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Anime.js Starter</title>
  <link rel="stylesheet" href="/style.css">
</head>
<body>
  <div class="container">
    <h1>Anime.js Animation Demo</h1>

    <div class="example basic-animation">
      <h2>Basic Animation</h2>
      <div class="box box1"></div>
      <button id="basic-btn">Play</button>
    </div>

    <div class="example stagger-animation">
      <h2>Stagger Animation</h2>
      <div class="stagger-grid">
        <div class="stagger-item"></div>
        <div class="stagger-item"></div>
        <div class="stagger-item"></div>
        <div class="stagger-item"></div>
        <div class="stagger-item"></div>
        <div class="stagger-item"></div>
      </div>
      <button id="stagger-btn">Play</button>
    </div>

    <div class="example timeline-animation">
      <h2>Timeline Animation</h2>
      <div class="timeline-elements">
        <div class="timeline-box box1"></div>
        <div class="timeline-box box2"></div>
        <div class="timeline-box box3"></div>
      </div>
      <button id="timeline-btn">Play</button>
    </div>
  </div>

  <script type="module" src="/main.js"></script>
</body>
</html>
```

### main.js
```javascript
import { animate, stagger, createTimeline } from 'animejs'

// Basic Animation
document.getElementById('basic-btn').addEventListener('click', () => {
  animate('.box1', {
    x: 250,
    rotate: '1turn',
    scale: [0.75, 1],
    duration: 800,
    ease: 'inOutQuad'
  })
})

// Stagger Animation
document.getElementById('stagger-btn').addEventListener('click', () => {
  animate('.stagger-item', {
    scale: [0, 1],
    delay: stagger(100),
    ease: 'outElastic(1, .8)',
    duration: 600
  })
})

// Timeline Animation
document.getElementById('timeline-btn').addEventListener('click', () => {
  const tl = createTimeline({
    defaults: { ease: 'outExpo', duration: 750 }
  })

  tl.add('.timeline-box.box1', { x: 250 })
  .add('.timeline-box.box2', { x: 250 }, '-=500')
  .add('.timeline-box.box3', { x: 250 }, '-=500')
})
```

### style.css
```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  min-height: 100vh;
  padding: 2rem;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
}

h1 {
  text-align: center;
  margin-bottom: 3rem;
  font-size: 3rem;
}

.example {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  padding: 2rem;
  margin-bottom: 2rem;
}

h2 {
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
}

.box {
  width: 80px;
  height: 80px;
  background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  border-radius: 8px;
  margin-bottom: 1rem;
}

.stagger-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 1rem;
}

.stagger-item {
  width: 100%;
  aspect-ratio: 1;
  background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
  border-radius: 8px;
}

.timeline-elements {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.timeline-box {
  width: 60px;
  height: 60px;
}

.timeline-box.box1 { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
.timeline-box.box2 { background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); }
.timeline-box.box3 { background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); }

button {
  background: white;
  color: #764ba2;
  border: none;
  padding: 0.75rem 2rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.2s;
}

button:hover {
  transform: scale(1.05);
}

button:active {
  transform: scale(0.95);
}
```

## Common Patterns

### Pattern 1: Sequential List Reveal

```javascript
import { animate, stagger } from 'animejs'

animate('.list-item', {
  y: [30, 0],
  opacity: [0, 1],
  delay: stagger(80),
  ease: 'outQuad',
  duration: 600
})
```

### Pattern 2: Grid Expand from Center

```javascript
animate('.grid-square', {
  scale: [0, 1],
  delay: stagger(30, { grid: [10, 10], from: 'center' }),
  ease: 'outElastic(1, .8)',
  duration: 600
})
```

### Pattern 3: SVG Line Drawing

```javascript
import { animate, svg } from 'animejs'

animate(svg.createDrawable('path'), {
  draw: ['0 0', '0 1'],
  ease: 'inOutQuad',
  duration: 2000,
  delay: (el, i) => i * 250
})
```

### Pattern 4: Timeline Sequence

```javascript
import { createTimeline } from 'animejs'

const tl = createTimeline({
  defaults: { ease: 'outExpo', duration: 750 }
})

tl.add('.title', { y: [-50, 0], opacity: [0, 1] })
.add('.subtitle', { y: [-30, 0], opacity: [0, 1] }, '-=500')
.add('.button', { scale: [0, 1] }, '-=300')
```

## Framework Integration

### With React

```jsx
import { animate, createScope } from 'animejs'
import { useEffect, useRef } from 'react'

function AnimatedComponent() {
  const root = useRef(null)
  const scope = useRef(null)

  useEffect(() => {
    scope.current = createScope({ root }).add(() => {
      animate('.element', { x: 250, duration: 800, ease: 'inOutQuad' })
    })

    return () => scope.current.revert()
  }, [])

  return <div ref={root}><div className="element">Animated</div></div>
}
```

### With Vue

```javascript
import { animate } from 'animejs'

export default {
  mounted() {
    animate(this.$el, { x: 250, duration: 800 })
  }
}
```

## TypeScript Support

Anime.js v4 ships its own TypeScript definitions — no separate `@types/animejs` package needed.

## Performance Tips

1. **Use transforms and opacity** - GPU-accelerated properties
2. **Batch similar animations** - One animation for multiple targets
3. **Add will-change** to CSS for complex animations
4. **Use `onScroll()`** for scroll-linked animations instead of manual scroll listeners
5. **Revert `createScope()` instances** on cleanup in frameworks
6. **Limit element count** - Stagger works best with fewer than 100 elements

## Additional Resources

- **Official Documentation**: https://animejs.com/documentation/
- **GitHub Repository**: https://github.com/juliangarnier/anime
- **CodePen Collection**: https://codepen.io/collection/DxpqGJ/

---

For more patterns and reference documentation, see:
- `api_reference.md` - Complete Anime.js v4 API
- `stagger_guide.md` - Stagger utilities deep dive
- `timeline_guide.md` - Timeline sequencing guide
