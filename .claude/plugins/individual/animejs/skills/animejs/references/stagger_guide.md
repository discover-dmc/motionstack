# Anime.js Stagger Guide

Complete guide to Anime.js v4 stagger utilities for creating sequential and coordinated animations.

## Overview

`stagger()` distributes animation delays (or values) across multiple targets, creating cascading or wave-like effects. Anime.js provides grid-based staggering, directional control, jitter, and custom easing for the stagger progression itself.

```javascript
import { animate, stagger } from 'animejs'
```

## Basic Stagger

### Time-Based Stagger

```javascript
animate('.element', {
  x: 250,
  delay: stagger(100) // increment delay by 100ms
})
```

**Result:** Each element animates 100ms after the previous one.

### Value-Based Stagger

```javascript
animate('.element', {
  x: stagger([0, 100, 200, 300])
})
```

**Result:** Each element animates to a different x value.

## Stagger Options

### Complete Syntax

```javascript
stagger(value, {
  start: 0,              // starting delay (ms)
  from: 'first',          // starting point
  reversed: false,         // reverse the stagger order (was `direction: 'reverse'` in v3)
  ease: 'linear',           // easing for the stagger progression
  grid: [rows, cols],        // grid dimensions
  axis: null,                 // grid axis ('x', 'y', or null)
  modifier: v => v,             // transform each computed value
  total: 20,                     // override the element count used in the calculation
  jitter: 0                       // random variance, 0-1 (new in v4)
})
```

---

## Stagger From

Control where the stagger starts.

### from: 'first' (default)

```javascript
animate('.element', { scale: [0, 1], delay: stagger(100, { from: 'first' }) })
```

### from: 'last'

```javascript
animate('.element', { scale: [0, 1], delay: stagger(100, { from: 'last' }) })
```

### from: 'center'

```javascript
animate('.element', { scale: [0, 1], delay: stagger(100, { from: 'center' }) })
```

### from: index

```javascript
animate('.element', { scale: [0, 1], delay: stagger(100, { from: 5 }) }) // start from 6th element
```

### from: [x, y]

```javascript
animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, { grid: [10, 10], from: [5, 5] }) // start from center of grid
})
```

---

## Grid Stagger

### Basic Grid

```javascript
animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, { grid: [14, 5] }) // 14 columns, 5 rows
})
```

### Grid with from: 'center'

```javascript
animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, { grid: [14, 5], from: 'center' })
})
```

**Result:** Animates from center outward in all directions.

### Grid with Axis

```javascript
// horizontal waves
animate('.grid-item', {
  y: [-20, 0],
  delay: stagger(30, { grid: [10, 10], from: 'center', axis: 'x' })
})

// vertical waves
animate('.grid-item', {
  y: [-20, 0],
  delay: stagger(30, { grid: [10, 10], from: 'center', axis: 'y' })
})
```

---

## Stagger Direction (reversed)

`direction: 'reverse'` from v3 is now the boolean `reversed`:

```javascript
animate('.element', { scale: [0, 1], delay: stagger(100, { reversed: false }) })
animate('.element', { scale: [0, 1], delay: stagger(100, { from: 'first', reversed: true }) }) // last to first
```

---

## Stagger Easing

Apply easing to the stagger progression itself:

```javascript
animate('.element', {
  y: [-50, 0],
  delay: stagger(100, { ease: 'outQuad' })
})
```

**Effect:** Early elements have shorter delays, later elements have longer delays.

---

## Stagger Jitter (new in v4)

Add random variance to a stagger:

```javascript
animate('.element', {
  scale: [0, 1],
  delay: stagger(100, { jitter: 0.5 })
})
```

---

## Stagger Start

Add an initial delay before stagger begins:

```javascript
animate('.element', { scale: [0, 1], delay: stagger(100, { start: 500 }) })
```

**Result:**
- Element 1: 500ms delay
- Element 2: 600ms delay
- Element 3: 700ms delay

---

## Common Patterns

### 1. Sequential List Reveal

```javascript
animate('.list-item', {
  y: [30, 0],
  opacity: [0, 1],
  delay: stagger(80),
  ease: 'outQuad'
})
```

### 2. Grid Expand from Center

```javascript
animate('.grid-square', {
  scale: [0, 1],
  delay: stagger(30, { grid: [10, 10], from: 'center' }),
  ease: 'outElastic(1, .8)'
})
```

### 3. Wave Effect

```javascript
animate('.wave-element', {
  y: [
    { to: -20, duration: 300 },
    { to: 0, duration: 300 }
  ],
  delay: stagger(50),
  loop: true
})
```

### 4. Diagonal Wipe

```javascript
animate('.tile', {
  opacity: [0, 1],
  x: [-50, 0],
  delay: stagger(20, { grid: [10, 10], from: [0, 0], axis: null })
})
```

### 5. Text Character Reveal

```javascript
import { animate, stagger, splitText } from 'animejs'

const { chars } = splitText('.text', { chars: true })

animate(chars, {
  y: [100, 0],
  opacity: [0, 1],
  delay: stagger(30),
  ease: 'outExpo'
})
```

### 6. Circular Stagger

```javascript
animate('.circle-item', {
  scale: [0, 1],
  delay: stagger(100, { from: 'center', ease: 'linear' }),
  rotate: stagger([0, 360])
})
```

### 7. Alternating Direction

```javascript
animate('.row', {
  x: (el, i) => i % 2 === 0 ? [-250, 0] : [250, 0],
  opacity: [0, 1],
  delay: stagger(100)
})
```

---

## Stagger with Different Properties

### Stagger Delays, Same Values

```javascript
animate('.element', { x: 250, delay: stagger(100) })
```

### Stagger Values, Same Timing

```javascript
animate('.element', { x: stagger([0, 50, 100, 150]), duration: 1000 })
```

### Stagger Both

```javascript
animate('.element', {
  x: stagger([0, 50, 100, 150]),
  delay: stagger(100)
})
```

---

## Advanced Techniques

### Dynamic Grid Calculation

```javascript
function getGridSize() {
  const elements = document.querySelectorAll('.grid-item')
  const cols = Math.ceil(Math.sqrt(elements.length))
  const rows = Math.ceil(elements.length / cols)
  return [cols, rows]
}

animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, { grid: getGridSize(), from: 'center' })
})
```

### Stagger with a Modifier

```javascript
animate('.element', {
  x: stagger(100, { modifier: v => Math.round(v / 2) })
})
```

### Multi-Property Stagger

```javascript
animate('.element', {
  x: stagger([0, 100]),
  y: stagger([0, 50]),
  rotate: stagger([0, 360]),
  delay: stagger(100, { from: 'center' })
})
```

---

## Performance Tips

1. **Use transforms** - Stagger `x`, `y`, `scale`, `rotate` for GPU acceleration
2. **Limit element count** - Stagger works best with fewer than 100 elements
3. **Avoid layout properties** - Don't stagger `width`, `height`, `left`, `top`
4. **Use `will-change`** - Add `will-change: transform` for smoother animations
5. **Batch similar animations** - One stagger for multiple properties is more efficient than separate animations

---

## Common Mistakes

### Wrong: Stagger on Single Element

```javascript
animate('.single-element', { scale: [0, 1], delay: stagger(100) }) // no effect, only one element
```

### Correct: Multiple Elements

```javascript
animate('.multiple-elements', { scale: [0, 1], delay: stagger(100) })
```

### Wrong: Grid Without Dimensions

```javascript
animate('.grid-item', { scale: [0, 1], delay: stagger(50, { from: 'center' }) }) // missing grid dimensions
```

### Correct: Grid With Dimensions

```javascript
animate('.grid-item', { scale: [0, 1], delay: stagger(50, { grid: [10, 10], from: 'center' }) })
```

### Wrong: Using v3's `direction` option

```javascript
delay: stagger(100, { direction: 'reverse' }) // removed in v4
```

### Correct: Use `reversed`

```javascript
delay: stagger(100, { reversed: true })
```

---

## Debugging Tips

**Log stagger values as they're computed:**
```javascript
animate('.element', {
  x: 250,
  delay: stagger(100, {
    modifier: (v, i) => {
      console.log(`Element ${i}: delay ${v}ms`)
      return v
    }
  })
})
```

**Visualize stagger:**
```javascript
document.querySelectorAll('.element').forEach((el, i) => {
  el.setAttribute('data-index', i)
})
```

---

## Resources

- Official Stagger Documentation: https://animejs.com/documentation/utilities/stagger
- Official Documentation Home: https://animejs.com/documentation/
