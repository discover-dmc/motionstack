---
name: animejs
description: Versatile JavaScript animation engine for DOM, CSS, SVG, and JavaScript objects. Use when creating timeline-based animations, stagger effects, SVG morphing/drawing, keyframe sequences, draggable elements, scroll-linked animations, or complex choreographed animations. Triggers on tasks involving Anime.js, Anime.js v4, animate(), createTimeline, stagger, SVG path animations, morphing, createDraggable, createScope, onScroll, or multi-step animation choreography. Alternative to GSAP for SVG-heavy animations and React-independent projects.
---

# Anime.js

Lightweight JavaScript animation engine (v4) with modular named exports, powerful timeline/stagger tools, and dedicated SVG, scroll, and drag utilities.

## Overview

Anime.js v4 is a complete rewrite of the library as a set of modular, tree-shakeable named exports. There is no more single `anime()` factory: `animate()`, `createTimeline()`, `createTimer()`, `createDraggable()`, `createScope()`, `onScroll()`, `svg`, and `utils` are imported individually from `'animejs'`. It works with vanilla JavaScript and any framework.

**When to use this skill:**
- Timeline-based animation sequences with precise choreography
- Staggered animations across multiple elements
- SVG path morphing and line-drawing animations
- Keyframe animations (per-property or percentage-based)
- Framework-agnostic animation (works with React, Vue, vanilla JS) via `createScope()`
- Scroll-linked animations via `onScroll()`
- Draggable elements via `createDraggable()`
- Spring, cubic-bezier, and other custom easing

**Core features:**
- `animate(targets, params)` — two-argument animation function (targets no longer live inside the params object)
- `createTimeline()` — sequencing with label and relative-offset positioning
- `stagger()` — grid, from-center, jitter, and eased delay/value distribution
- `svg` module — `createDrawable()` for line drawing, `morphTo()` for shape morphing, `createMotionPath()` for path following
- `createDraggable()` and `onScroll()` for interaction and scroll-linked playback
- `createScope()` for framework-safe setup/teardown and media-query-driven animation

## Core Concepts

### Basic Animation

`animate()` takes targets as the first argument and parameters as the second — not a single options object with a `targets` key:

```javascript
import { animate } from 'animejs'

animate('.element', {
  x: 250,
  rotate: '1turn',
  duration: 800,
  ease: 'inOutQuad'
})
```

### Targets

```javascript
// CSS selector
animate('.box', { x: 250 })

// DOM elements
animate(document.querySelectorAll('.box'), { x: 250 })

// Array of elements
animate([el1, el2, el3], { x: 250 })

// JavaScript object
const obj = { x: 0 }
animate(obj, { x: 100 })
```

### Animatable Properties

**CSS transforms** — `x`/`y`/`z` are shorthand for `translateX`/`translateY`/`translateZ`; the fully-named transform properties still work:

```javascript
animate('.element', {
  x: 250,           // shorthand for translateX
  rotate: '1turn',
  scale: 2,
  opacity: 0.5,
  backgroundColor: '#FFF'
})
```

**SVG attributes and drawing/morphing:**
```javascript
import { animate, svg } from 'animejs'

animate(svg.createDrawable('path'), {
  draw: ['0 0', '0 1'],   // line drawing, replaces strokeDashoffset + setDashoffset
  duration: 2000,
  ease: 'inOutQuad'
})
```

**JavaScript objects:**
```javascript
const obj = { value: 0 }
animate(obj, {
  value: 100,
  round: 1,
  onUpdate: () => console.log(obj.value)
})
```

### Property Value Syntax

```javascript
animate('.element', {
  x: 250,                       // single value, animates from current to 250
  y: { from: 0, to: 100 },      // explicit from/to
  rotate: '+=1turn',            // relative value
  scale: () => Math.random() + 1 // function-based value
})
```

### Callbacks

All callbacks are prefixed with `on`:

```javascript
animate('.element', {
  x: 250,
  onBegin: () => {},
  onBeforeUpdate: () => {},
  onUpdate: () => {},
  onRender: () => {},
  onLoop: () => {},
  onPause: () => {},
  onComplete: () => {}
})
```

`animate()` also returns a promise-like instance: `animation.then(() => {})`.

### Timeline

```javascript
import { createTimeline } from 'animejs'

const tl = createTimeline({ defaults: { duration: 750, ease: 'outExpo' } })

tl.label('start')
  .add('.box1', { x: 250 })
  .add('.box2', { x: 250 }, '-=500')   // 500ms before previous ends
  .add('.box3', { x: 250 }, '+=200')   // 200ms after previous ends
  .add('.box4', { x: 250 }, 'start')   // at the "start" label
```

`timeline.add(target, params, position)` — target is a separate first argument, matching `animate()`. Timelines also support `.set()`, `.call()`, `.sync()`, and `.label()`.

## Common Patterns

### 1. Stagger Animation (Sequential Reveal)

```javascript
import { animate, stagger } from 'animejs'

animate('.stagger-element', {
  y: [100, 0],
  opacity: [0, 1],
  delay: stagger(100), // increase delay by 100ms per element
  ease: 'outQuad',
  duration: 600
})
```

### 2. Stagger from Center (Grid)

```javascript
animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, {
    grid: [14, 5],
    from: 'center', // also: 'first', 'last', index, [x, y]
    axis: 'x'       // also: 'y', null
  }),
  ease: 'outQuad'
})
```

### 3. SVG Line Drawing

```javascript
import { animate, svg, stagger } from 'animejs'

animate(svg.createDrawable('.line'), {
  draw: ['0 0', '0 1'],
  ease: 'inOutQuad',
  duration: 2000,
  delay: stagger(100)
})
```

### 4. SVG Morphing

```javascript
import { animate, svg, utils } from 'animejs'

const [$path1, $path2] = utils.$('polygon')

animate($path1, {
  points: svg.morphTo($path2),
  duration: 2000,
  ease: 'inOutQuad',
  loop: true,
  alternate: true
})
```

### 5. Timeline Sequence

```javascript
import { createTimeline } from 'animejs'

const tl = createTimeline({ defaults: { ease: 'outExpo', duration: 750 } })

tl.add('.title', { y: [-50, 0], opacity: [0, 1] })
  .add('.subtitle', { y: [-30, 0], opacity: [0, 1] }, '-=500')
  .add('.button', { scale: [0, 1], opacity: [0, 1] }, '-=300')
```

### 6. Keyframe Animation

Per-property waypoints:

```javascript
animate('.element', {
  x: [{ to: 100 }, { to: 0 }],
  y: [{ to: 100 }, { to: 0 }],
  duration: 4000,
  ease: 'inOutQuad',
  loop: true
})
```

Percentage-based, multiple properties per checkpoint:

```javascript
animate('.element', {
  keyframes: {
    '0%': { x: 0, y: 0 },
    '50%': { x: 100, y: 100 },
    '100%': { x: 0, y: 0 }
  },
  duration: 4000,
  loop: true
})
```

### 7. Scroll-Linked Animation

```javascript
import { animate, onScroll } from 'animejs'

animate('.scroll-element', {
  y: [100, 0],
  opacity: [0, 1],
  ease: 'outQuad',
  autoplay: onScroll({
    container: '.scroll-container',
    enter: 'bottom top',
    leave: 'top bottom',
    sync: true
  })
})
```

## Integration Patterns

### With React

`createScope()` handles setup and teardown safely inside `useEffect`:

```jsx
import { animate, createScope, createDraggable } from 'animejs'
import { useEffect, useRef } from 'react'

function AnimatedComponent() {
  const root = useRef(null)
  const scope = useRef(null)

  useEffect(() => {
    scope.current = createScope({ root }).add(() => {
      animate('.element', {
        x: 250,
        duration: 800,
        ease: 'inOutQuad'
      })

      createDraggable('.draggable')
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

### Responsive Animation with createScope

`createScope({ mediaQueries })` re-runs the scope callback when a query's match state changes — no manual `matchMedia` listeners:

```javascript
import { animate, utils, createScope } from 'animejs'

createScope({
  mediaQueries: {
    isSmall: '(max-width: 200px)',
    reduceMotion: '(prefers-reduced-motion)'
  }
}).add(self => {
  const { isSmall, reduceMotion } = self.matches

  if (isSmall) utils.set('.square', { scale: 0.5 })

  animate('.square', {
    x: isSmall ? 0 : ['-35vw', '35vw'],
    y: isSmall ? ['-40vh', '40vh'] : 0,
    loop: true,
    alternate: true,
    duration: reduceMotion ? 0 : isSmall ? 750 : 1250
  })
})
```

### Motion Path Following

```javascript
import { animate, svg } from 'animejs'

const { translateX, translateY, rotate } = svg.createMotionPath('#motion-path')

animate('.element', {
  translateX,
  translateY,
  rotate,
  ease: 'linear',
  duration: 2000,
  loop: true
})
```

## Advanced Techniques

### Spring Easing

```javascript
import { animate, spring } from 'animejs'

animate('.element', {
  x: 250,
  ease: spring({ bounce: 0.5, duration: 800 }) // perceived params
  // or physics params: spring({ mass: 1, stiffness: 100, damping: 10, velocity: 0 })
})
```

### Steps and Bezier Easing

```javascript
animate('.element', { x: 250, ease: 'steps(5)', duration: 1000 })
animate('.element', { x: 250, ease: 'cubicBezier(.5, .05, .1, .3)', duration: 1000 })
```

### Direction and Loop

`direction` no longer exists — use `alternate` and `reversed` booleans:

```javascript
animate('.element', {
  x: 250,
  alternate: true,   // ping-pong each loop, was direction: 'alternate'
  reversed: false,   // was direction: 'reverse'
  loop: true,         // or a number of iterations
  loopDelay: 200,      // was endDelay
  ease: 'inOutQuad'
})
```

### Playback Control

```javascript
const animation = animate('.element', { x: 250, autoplay: false })

animation.play()
animation.pause()
animation.restart()
animation.reverse()
animation.seek(500) // seek to 500ms
```

### Draggable Elements

```javascript
import { createDraggable, spring } from 'animejs'

createDraggable('.square', {
  container: [0, 0, 0, 0],
  releaseEase: spring({ bounce: 0.7 })
})
```

## Performance Optimization

### Use Transform and Opacity

```javascript
// Good: GPU-accelerated
animate('.element', { x: 250, opacity: 0.5 })

// Avoid: triggers layout
animate('.element', { left: '250px', width: '500px' })
```

### Batch Similar Animations

```javascript
// Good: single call for multiple targets
animate('.multiple-elements', { x: 250 })

// Avoid: separate calls per element
elements.forEach(el => animate(el, { x: 250 }))
```

### Use `will-change` for Complex Animations

```css
.animated-element {
  will-change: transform, opacity;
}
```

### Disable autoplay for Manually-Driven Animations

```javascript
const animation = animate('.element', { x: 250, autoplay: false })
```

## Common Pitfalls

### 1. Passing an options object with `targets` instead of two arguments

```javascript
// Wrong: v3 syntax, no longer valid
animate({ targets: '.element', x: 250 })

// Correct: targets is the first argument
animate('.element', { x: 250 })
```

### 2. Using `easing` instead of `ease`

```javascript
// Wrong
animate('.element', { x: 250, easing: 'easeInOutQuad' })

// Correct
animate('.element', { x: 250, ease: 'inOutQuad' })
```

### 3. Forgetting Unit Types

```javascript
// Wrong: no unit
animate('.element', { width: 200 })

// Correct: include unit
animate('.element', { width: '200px' })
```

### 4. Not Handling Animation Cleanup in Frameworks

```javascript
// Wrong: animation and its listeners outlive the component
useEffect(() => {
  animate(ref.current, { x: 250 })
}, [])

// Correct: wrap in createScope and revert on unmount
useEffect(() => {
  const scope = createScope({ root: ref }).add(() => {
    animate(ref.current, { x: 250 })
  })
  return () => scope.revert()
}, [])
```

### 5. Incorrect Timeline Timing

```javascript
// Wrong: missing offset operator, treated as absolute time
tl.add('.el2', { x: 250 }, '500')

// Correct: use relative operators or a label
tl.add('.el2', { x: 250 }, '-=500')
tl.add('.el3', { x: 250 }, '+=200')
```

### 6. Overusing Loop

```javascript
// Avoid: infinite JS-driven loops drain battery
animate('.element', { rotate: '1turn', loop: true, duration: 1000 })

// Better: use CSS animations for simple infinite loops
```

## Resources

### Scripts
- `animation_generator.py` - Generate Anime.js v4 animation boilerplate (8 types)
- `timeline_builder.py` - Build complex v4 timeline sequences

### References
- `api_reference.md` - Complete Anime.js v4 API documentation
- `stagger_guide.md` - Stagger utilities and patterns
- `timeline_guide.md` - Timeline sequencing deep dive

### Assets
- `starter_animejs/` - Vanilla JS + Vite template with examples
- `examples/` - Real-world patterns (SVG morphing, stagger grids, timelines)

## Related Skills

- **gsap-scrolltrigger** - More powerful timeline features and scroll integration
- **motion-framer** - React-specific declarative animations
- **react-spring-physics** - Physics-based spring animations
- **lightweight-3d-effects** - Simple 3D effects (Zdog, Vanta.js)

**Anime.js vs GSAP**: Use Anime.js for SVG-heavy animations, simpler projects, or when bundle size matters. Use GSAP for complex scroll-driven experiences, advanced timelines, and professional-grade control.

**Anime.js vs Framer Motion**: Use Anime.js for framework-agnostic projects or when working outside React. Use Framer Motion for React-specific declarative animations with gesture integration.
