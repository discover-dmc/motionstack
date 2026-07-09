# Anime.js Timeline Guide

Complete guide to creating complex animation sequences with Anime.js v4 timelines.

## Overview

Timelines chain multiple animations with precise control over timing and sequencing, using `createTimeline()`. They provide a declarative way to choreograph complex multi-step animations, and can hold animations, timers, labels, and callbacks.

```javascript
import { createTimeline } from 'animejs'
```

## Creating a Timeline

### Basic Timeline

```javascript
const timeline = createTimeline()
```

### Timeline with Default Parameters

```javascript
const timeline = createTimeline({
  defaults: {
    duration: 1000,     // default duration for all children
    ease: 'outExpo'       // default ease for all children
  },
  loop: false,             // loop the entire timeline
  alternate: false,         // ping-pong each loop (was direction: 'alternate')
  autoplay: true             // auto-start
})
```

---

## Adding Animations

### .add() Method

`timeline.add(target, parameters, position)` — target is passed as a separate argument, the same as `animate()`:

```javascript
timeline.add('.element', { x: 250, duration: 800 })
```

### Chaining Animations

```javascript
timeline
  .add('.box1', { x: 250 })
  .add('.box2', { x: 250 })
  .add('.box3', { x: 250 })
```

---

## Timeline Position (Offset)

Control when each animation starts relative to the timeline or the previous item.

### Absolute Time

```javascript
timeline.add('.element', { x: 250 }, 1000) // start at 1000ms from timeline start
```

### Relative to Previous End (+=)

```javascript
timeline
  .add('.box1', { x: 250, duration: 1000 })
  .add('.box2', { x: 250 }, '+=500') // start 500ms AFTER box1 completes
```

### Overlap with Previous End (-=)

```javascript
timeline
  .add('.box1', { x: 250, duration: 1000 })
  .add('.box2', { x: 250 }, '-=500') // start 500ms BEFORE box1 completes (overlap)
```

### Relative to Previous Start (<)

```javascript
timeline
  .add('.box1', { x: 250, duration: 1000 })
  .add('.box2', { y: 250 }, '<')       // start at the exact same time as box1
  .add('.box3', { y: 250 }, '<-=200')  // start 200ms before box1's own start
```

### Labels

```javascript
timeline
  .label('start')
  .add('.box1', { x: 250 })
  .add('.box2', { x: 250 }, 'start')       // start exactly at the label
  .add('.box3', { x: 250 }, 'start+=300')  // 300ms after the label
```

---

## Common Patterns

### 1. Sequential Animations

```javascript
const tl = createTimeline()

tl.add('.title', { y: [-50, 0], opacity: [0, 1] })
  .add('.subtitle', { y: [-30, 0], opacity: [0, 1] })
  .add('.button', { scale: [0, 1] })
```

### 2. Overlapping Animations

```javascript
const tl = createTimeline()

tl.add('.section1', { opacity: [1, 0], duration: 600 })
  .add('.section2', { opacity: [0, 1], duration: 600 }, '-=300') // crossfade
```

### 3. Staggered Timeline

```javascript
import { createTimeline, stagger } from 'animejs'

const tl = createTimeline()

tl.add('.card', { y: [100, 0], opacity: [0, 1], delay: stagger(100) })
  .add('.button', { scale: [0, 1] }, '-=200')
```

### 4. Multi-Stage Animation

```javascript
const tl = createTimeline({ defaults: { ease: 'outExpo', duration: 750 } })

tl.add('.modal', { scale: [0, 1], opacity: [0, 1] })
  .add('.modal-header', { y: [-20, 0], opacity: [0, 1] }, '-=500')
  .add('.modal-body', { y: [20, 0], opacity: [0, 1] }, '-=400')
  .add('.modal-footer', { opacity: [0, 1] }, '-=300')
```

### 5. Looping Timeline

```javascript
const tl = createTimeline({ loop: true, alternate: true })

tl.add('.ball', { y: -200, duration: 1000 })
  .add('.ball', { x: 200, duration: 1000 })
```

### 6. Loading Sequence

```javascript
const tl = createTimeline()

tl.add('.loader-bg', { scaleY: [0, 1], duration: 400, ease: 'inOutQuad' })
  .add('.loader-text', { opacity: [0, 1], y: [20, 0], duration: 600 }, '-=200')
  .add('.loader-spinner', { rotate: '1turn', duration: 800, loop: 3 }, '-=400')
  .add('.loader', { opacity: 0, duration: 400 }, '+=500')
  .add('.content', { y: [50, 0], opacity: [0, 1], duration: 600 })
```

### 7. Page Transition

```javascript
import { createTimeline } from 'animejs'

function pageTransition(oldPage, newPage) {
  const tl = createTimeline()

  tl.add(oldPage, { x: [0, -100], opacity: [1, 0], duration: 400, ease: 'inQuad' })
    .add(newPage, { x: [100, 0], opacity: [0, 1], duration: 400, ease: 'outQuad' }, '-=200')

  return tl
}
```

---

## Timeline Controls

### Playback Methods

```javascript
const tl = createTimeline({ autoplay: false })

tl.play()       // play from current position
tl.pause()      // pause
tl.restart()    // restart from beginning
tl.reverse()    // reverse direction
tl.seek(2000)   // seek to 2000ms
```

### Properties

```javascript
tl.duration
tl.currentTime
tl.progress      // 0-100
tl.paused
tl.began
tl.completed
```

---

## Advanced Techniques

### .set() — Instant Value Changes

```javascript
const tl = createTimeline()

tl.add('.intro', { opacity: [0, 1] })
  .set('.intro', { pointerEvents: 'none' }) // apply instantly at this point
  .add('.content', { y: [50, 0], opacity: [0, 1] })
```

### .call() — Run Arbitrary Code at a Position

```javascript
const tl = createTimeline()

tl.add('.intro', { opacity: [0, 1] })
  .call(() => console.log('intro finished'), '+=0')
  .add('.content', { y: [50, 0], opacity: [0, 1] })
```

### Nested Timelines via .sync()

```javascript
function createIntroTimeline() {
  const tl = createTimeline({ autoplay: false })
  tl.add('.logo', { scale: [0, 1] })
    .add('.tagline', { opacity: [0, 1] })
  return tl
}

const mainTimeline = createTimeline()
mainTimeline.sync(createIntroTimeline())
```

### Timeline Callbacks

```javascript
const tl = createTimeline({
  onBegin: () => console.log('timeline begins'),
  onUpdate: (tl) => console.log('progress:', tl.progress),
  onComplete: () => console.log('timeline completes')
})
```

### Conditional Timeline

```javascript
const tl = createTimeline()

tl.add('.element1', { x: 250 })

if (condition) {
  tl.add('.element2', { opacity: [0, 1] })
}

tl.add('.element3', { scale: [0, 1] })
```

---

## Timeline vs Individual Animations

### Without Timeline (Hard to Manage)

```javascript
animate('.box1', { x: 250, duration: 1000 })

setTimeout(() => animate('.box2', { x: 250, duration: 1000 }), 1000)
setTimeout(() => animate('.box3', { x: 250, duration: 1000 }), 2000)
```

### With Timeline (Clean and Maintainable)

```javascript
const tl = createTimeline()

tl.add('.box1', { x: 250, duration: 1000 })
  .add('.box2', { x: 250, duration: 1000 })
  .add('.box3', { x: 250, duration: 1000 })
```

---

## Performance Optimization

### 1. Use Relative Offsets

```javascript
// Good: flexible timing
.add('.el', {...}, '-=500')

// Avoid: brittle absolute timing
.add('.el', {...}, 1500)
```

### 2. Batch Similar Animations

```javascript
// Good: single call
tl.add(['.el1', '.el2', '.el3'], { x: 250 })

// Avoid: separate calls
tl.add('.el1', { x: 250 })
  .add('.el2', { x: 250 })
  .add('.el3', { x: 250 })
```

### 3. Set Defaults Once

```javascript
// Good: DRY
const tl = createTimeline({ defaults: { ease: 'outExpo', duration: 800 } })

// Avoid: repetition
tl.add('.el1', { ease: 'outExpo', duration: 800 })
  .add('.el2', { ease: 'outExpo', duration: 800 })
```

---

## Common Mistakes

### Wrong: Missing Offset Operator

```javascript
tl.add('.box1', { x: 250 })
  .add('.box2', { x: 250 }, '500') // treated as absolute time!
```

### Correct: Use Relative Operator

```javascript
tl.add('.box1', { x: 250 })
  .add('.box2', { x: 250 }, '+=500') // relative to previous
```

### Wrong: Passing an Options Object with `targets`

```javascript
tl.add({ targets: '.box1', x: 250 }) // v3 syntax, no longer valid
```

### Correct: Target as First Argument

```javascript
tl.add('.box1', { x: 250 })
```

### Wrong: Forgetting autoplay: false

```javascript
const tl = createTimeline() // starts immediately

button.addEventListener('click', () => {
  tl.play() // already playing!
})
```

### Correct: Disable autoplay

```javascript
const tl = createTimeline({ autoplay: false })

button.addEventListener('click', () => tl.play())
```

---

## Real-World Examples

### Hero Section Animation

```javascript
const heroTimeline = createTimeline({ defaults: { ease: 'outExpo' } })

heroTimeline
  .add('.hero-bg', { scale: [1.2, 1], opacity: [0, 1], duration: 1200 })
  .add('.hero-title', { y: [100, 0], opacity: [0, 1], duration: 800 }, '-=800')
  .add('.hero-subtitle', { y: [50, 0], opacity: [0, 1], duration: 600 }, '-=400')
  .add('.hero-cta', { scale: [0, 1], duration: 400 }, '-=200')
```

### Card Flip Animation

```javascript
function flipCard(card) {
  const tl = createTimeline({ autoplay: false })

  tl.add(card.querySelector('.front'), { rotateY: [0, 90], duration: 300, ease: 'inQuad' })
    .add(card.querySelector('.back'), { rotateY: [-90, 0], duration: 300, ease: 'outQuad' }, '<')

  return tl
}
```

### Notification Toast

```javascript
function showToast(toast) {
  const tl = createTimeline()

  tl.add(toast, { x: [400, 0], opacity: [0, 1], duration: 400, ease: 'outBack' })
    .add(toast, { opacity: [1, 0], duration: 300, ease: 'inQuad' }, '+=3000')

  return tl
}
```

---

## Debugging Timelines

### Log Timeline Progress

```javascript
const tl = createTimeline({
  onUpdate: (tl) => {
    console.log(`Progress: ${tl.progress.toFixed(2)}%`)
    console.log(`Current time: ${tl.currentTime}ms`)
  }
})
```

### Visualize Timeline

```javascript
const tl = createTimeline()

tl.add('.box1', {
  x: 250,
  duration: 1000,
  onBegin: () => console.log('[0ms] Box1 begins'),
  onComplete: () => console.log('[1000ms] Box1 completes')
})
.add('.box2', {
  x: 250,
  duration: 1000,
  onBegin: () => console.log('[1000ms] Box2 begins'),
  onComplete: () => console.log('[2000ms] Box2 completes')
}, '-=500')
```

---

## Resources

- Official Timeline Documentation: https://animejs.com/documentation/timeline
- Official Documentation Home: https://animejs.com/documentation/
