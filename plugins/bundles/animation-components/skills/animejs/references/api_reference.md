# Anime.js API Reference

Complete API documentation for Anime.js v4 (v4.5.x, current as of mid-2026).

## Table of Contents

- [Import Syntax](#import-syntax)
- [animate() Function](#animate-function)
- [Targets](#targets)
- [Properties](#properties)
- [Property Value Syntax](#property-value-syntax)
- [Animation Parameters](#animation-parameters)
- [Callbacks](#callbacks)
- [Timeline](#timeline)
- [Timer](#timer)
- [Stagger](#stagger)
- [SVG Module](#svg-module)
- [Draggable](#draggable)
- [Scope](#scope)
- [ScrollObserver (onScroll)](#scrollobserver-onscroll)
- [Easing Functions](#easing-functions)
- [Utilities](#utilities)

---

## Import Syntax

Anime.js v4 exports named functions from the root package, or from subpaths for smaller bundles:

```javascript
import { animate, stagger, createTimeline, createTimer, createDraggable,
         createScope, onScroll, svg, utils, spring } from 'animejs'

// Subpath imports (smaller bundles)
import { animate } from 'animejs/animation'
import { createTimeline } from 'animejs/timeline'
import { onScroll } from 'animejs/events'
import { morphTo, createDrawable, createMotionPath } from 'animejs/svg'
```

There is no default export and no `anime()` factory. There is also a lightweight Web Animations API adapter:

```javascript
import { waapi } from 'animejs'
waapi.animate(targets, parameters) // ~3KB, uses the browser's WAAPI engine
```

---

## animate() Function

```javascript
animate(targets, parameters)
```

Two arguments: targets first, parameters object second. **Returns:** an animation instance with playback controls and a `.then()` promise.

---

## Targets

**CSS Selector:**
```javascript
animate('.element', { x: 250 })
animate('#myId', { x: 250 })
```

**DOM Element/NodeList:**
```javascript
animate(document.querySelector('.element'), { x: 250 })
animate(document.querySelectorAll('.elements'), { x: 250 })
```

**JavaScript Object:**
```javascript
const obj = { prop: 0 }
animate(obj, { prop: 100 })
```

**Array:**
```javascript
animate([el1, el2, el3], { x: 250 })
animate([obj1, obj2], { prop: 100 })
```

---

## Properties

### CSS Properties

**Transform (shorthand + full names):**
```javascript
x: 250              // shorthand for translateX, pixels
y: '10em'           // shorthand for translateY, units
z: '50vh'           // shorthand for translateZ
translateX, translateY, translateZ  // full names still valid
rotate: '1turn'      // turns, deg, rad
rotateX, rotateY, rotateZ
scale: 2
scaleX, scaleY, scaleZ
skew: '10deg'
skewX, skewY
perspective: 1000
```

**Other CSS:**
```javascript
opacity: 0.5
backgroundColor: '#FFF'  // colors
borderRadius: '50%'
width: '100px'
left: '50%'
// Any valid CSS property (camelCase), including CSS variables
```

### SVG Attributes

```javascript
points: 'M10 80 Q 77.5 10, 145 80'  // via svg.morphTo() for morph animations
draw: ['0 0', '0 1']                 // via svg.createDrawable() for line drawing
fill: '#FF0000'
r: 50                                 // circle radius
cx, cy                                // circle center
// Any SVG attribute
```

### DOM Attributes

```javascript
value: 100              // input value
volume: 0.5              // audio/video
textContent: 'Hello'
innerHTML: '<div></div>'
```

### JavaScript Object Properties

```javascript
const obj = { x: 0, y: 0 }
animate(obj, { x: 100, y: 200 })
```

---

## Property Value Syntax

### Single Value

```javascript
animate('.el', { x: 250 }) // animate from current to 250
```

### From-To

```javascript
animate('.el', { x: { from: 0, to: 250 } })
animate('.el', { x: [0, 250] }) // shorthand array form
```

### Function-Based

```javascript
animate('.el', {
  x: (el, i) => 50 + (i * 50),
  delay: (el, i, total) => i * 100
})
```

### Keyframes (Per-Property)

```javascript
animate('.el', {
  x: [
    { to: 100, duration: 500 },
    { to: 200, duration: 500 },
    { to: 0, duration: 500 }
  ]
})
```

### Keyframes (Percentage-Based, Multi-Property)

```javascript
animate('.el', {
  keyframes: {
    '0%': { x: 0, y: 0 },
    '50%': { x: 100, y: 100 },
    '100%': { x: 0, y: 0 }
  },
  duration: 3000
})
```

### Units

```javascript
'250px'      // pixels
'10em'       // ems
'50%'        // percentage
'100vh'      // viewport
'1turn'      // turns
'45deg'      // degrees
'1.5rad'     // radians
```

### Relative Values

```javascript
x: '+=250'   // add 250 to current
x: '-=100'   // subtract 100
x: '*=2'     // multiply by 2
```

### Colors

```javascript
'#FF0000'
'rgb(255, 0, 0)'
'rgba(255, 0, 0, 0.5)'
'hsl(0, 100%, 50%)'
```

---

## Animation Parameters

Global animation settings, passed as the second argument to `animate()`:

```javascript
animate('.element', {
  x: 250,

  // Timing
  duration: 1000,        // milliseconds
  delay: 500,             // start delay
  loopDelay: 200,          // delay between loop iterations (was endDelay in v3)

  // Easing
  ease: 'inOutQuad',        // was `easing` in v3, and used an `easeInOutQuad`-style name

  // Playback
  alternate: true,          // ping-pong each loop (was direction: 'alternate')
  reversed: false,           // play backwards (was direction: 'reverse')
  loop: 3,                    // number, or true for infinite
  autoplay: true,              // true, false, or onScroll(...) for scroll-linked playback

  // Advanced
  round: 1,                     // round values to 1 decimal
  playbackRate: 1,                // speed multiplier
  frameRate: 60,                    // cap frame rate

  // Property-specific overrides
  x: {
    to: 100,
    duration: 2000,
    delay: 500,
    ease: 'linear'
  }
})
```

---

## Callbacks

All callback names are prefixed with `on`:

```javascript
animate('.element', {
  x: 250,

  onBegin: (anim) => console.log('animation begins'),
  onBeforeUpdate: (anim) => console.log('before each frame update'),
  onUpdate: (anim) => console.log('animation updates', anim.progress),
  onRender: (anim) => console.log('rendered a frame'),
  onLoop: (anim) => console.log('loop iteration completed'),
  onPause: (anim) => console.log('animation paused'),
  onComplete: (anim) => console.log('animation completes')
})

// Promise-based
animate('.element', { x: 250 }).then(() => console.log('done'))
```

### Instance Properties

```javascript
const animation = animate('.element', { x: 250 })

animation.progress      // 0-100
animation.currentTime   // milliseconds
animation.duration      // milliseconds
animation.paused        // boolean
animation.began         // boolean
animation.completed     // boolean
```

### Instance Methods

```javascript
animation.play()
animation.pause()
animation.restart()
animation.reverse()
animation.seek(time)   // seek to time (ms)
animation.cancel()
```

---

## Timeline

### Create Timeline

```javascript
import { createTimeline } from 'animejs'

const tl = createTimeline({
  defaults: {
    duration: 1000,   // default duration for all children
    ease: 'outExpo'    // default ease for all children
  },
  loop: false,
  alternate: false,
  autoplay: true
})
```

### Adding Animations

`timeline.add(target, parameters, position)` — target is a separate argument, matching `animate()`:

```javascript
tl.add('.el1', { x: 250 })
  .add('.el2', { x: 250 })
  .add('.el3', { x: 250 })
```

### Timeline Position (Offset)

```javascript
tl.add('.el', { x: 250 }, 1000)      // absolute: start at 1000ms from timeline start
tl.add('.el', { x: 250 }, '+=500')   // relative: 500ms after previous ends
tl.add('.el', { x: 250 }, '-=500')   // relative: 500ms before previous ends (overlap)
tl.add('.el', { x: 250 }, '<')       // start at the same time as the previous item
tl.add('.el', { x: 250 }, '<-=500')  // 500ms before the previous item's own start
```

### Labels

```javascript
tl.label('start')
  .add('.el1', { x: 250 })
  .add('.el2', { x: 250 }, 'start')       // start at the label
  .add('.el3', { x: 250 }, 'start+=200')  // 200ms after the label
```

### Other Timeline Methods

```javascript
tl.set(target, parameters, position)     // set values instantly at a position
tl.call(callback, position)              // run a function at a position
tl.sync(otherTimeline, position)         // synchronize another timeline into this one
```

### Timeline Playback

```javascript
tl.play()
tl.pause()
tl.restart()
tl.reverse()
tl.seek(1000)
```

### Timeline Properties

```javascript
tl.duration
tl.currentTime
tl.progress
tl.paused
tl.began
tl.completed
```

---

## Timer

A timer runs on the same playback engine as animations but has no properties to tween — useful for scheduling callbacks.

```javascript
import { createTimer } from 'animejs'

const timer = createTimer({
  duration: 1000,
  loop: true,
  onUpdate: (t) => console.log(t.currentTime),
  onComplete: () => console.log('done')
})

timer.play()
timer.pause()
```

---

## Stagger

Distribute delays or values across multiple targets.

### Basic Stagger

```javascript
import { animate, stagger } from 'animejs'

animate('.element', { x: 250, delay: stagger(100) }) // increment delay by 100ms per element
```

### Stagger Options

```javascript
delay: stagger(100, {
  start: 500,             // starting delay (ms)
  from: 'center',          // 'first', 'last', 'center', index, [x, y]
  reversed: false,          // was direction: 'reverse' in v3
  ease: 'outQuad',           // easing applied to the stagger distribution
  grid: [10, 10],              // grid dimensions
  axis: 'x',                    // 'x', 'y', or null
  modifier: v => v,               // transform each computed value
  total: 20,                       // override element count used for calculations
  jitter: 0.3                       // random variance (new in v4)
})
```

### Stagger Values (not just delays)

```javascript
x: stagger([0, 100, 200, 300])          // each element gets a different x
scale: stagger([1, 0.1])                 // interpolated range across targets
```

### Grid Stagger

```javascript
animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, { grid: [14, 5], from: 'center' })
})
```

---

## SVG Module

```javascript
import { svg } from 'animejs'
// or: import { morphTo, createDrawable, createMotionPath } from 'animejs'
// or: import { morphTo, createDrawable, createMotionPath } from 'animejs/svg'
```

### svg.createDrawable(target)

Prepares SVG line/path/polyline/rect elements for line-drawing animation. Replaces `strokeDashoffset` + `anime.setDashoffset` from v3.

```javascript
animate(svg.createDrawable('.line'), {
  draw: ['0 0', '0 1'],   // 'start end', 0-1 range; '0 1' = fully drawn
  duration: 2000,
  ease: 'inOutQuad'
})
```

Target types: CSS selector, `SVGLineElement`, `SVGPathElement`, `SVGPolylineElement`, or `SVGRectElement`. Returns an array of proxy elements with an added `draw` property.

### svg.morphTo(targetShape, precision)

Morphs one SVG shape's points/path into another's. Replaces manual `d`/`points` array morphing from v3.

```javascript
const [$path1, $path2] = utils.$('polygon')

animate($path1, {
  points: svg.morphTo($path2),
  duration: 500,
  ease: 'inOutCirc'
})
```

`precision` (optional, 0-1, default 0.33) controls point interpolation density.

### svg.createMotionPath(path)

Returns `translateX`/`translateY`/`rotate` functions derived from an SVG path, for moving an element along it. Replaces `anime.path()` from v3.

```javascript
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

---

## Draggable

```javascript
import { createDraggable } from 'animejs'

createDraggable('.square')

createDraggable('.square', {
  container: [0, 0, 0, 0],
  releaseEase: spring({ bounce: 0.7 })
})
```

Configurable axes (`x`, `y` with `snap`/`modifier`/`mapTo`), and settings for `trigger`, `container`, `containerPadding`, `friction`, release physics, velocity, `ease`, and drag/scroll thresholds. Emits its own callbacks (`onGrab`, `onDrag`, `onRelease`, etc.) and exposes playback-style methods.

---

## Scope

`createScope()` groups animations for safe setup/teardown, and can re-run its callback when media queries change.

```javascript
import { animate, utils, createScope } from 'animejs'

const scope = createScope({
  root: document.querySelector('#app'),  // optional root element
  mediaQueries: {
    isSmall: '(max-width: 200px)',
    reduceMotion: '(prefers-reduced-motion)'
  }
}).add(self => {
  const { isSmall, reduceMotion } = self.matches

  animate('.square', {
    x: isSmall ? 0 : ['-35vw', '35vw'],
    loop: true,
    duration: reduceMotion ? 0 : 1250
  })

  // expose a method callable from outside the scope
  self.add('rotateSquare', (deg) => {
    animate('.square', { rotate: deg })
  })
})

scope.methods.rotateSquare(180)
scope.revert() // cleanup: reverts all animations/listeners declared inside
```

---

## ScrollObserver (onScroll)

```javascript
import { animate, onScroll } from 'animejs'

animate('.square', {
  x: '15rem',
  rotate: '1turn',
  duration: 2000,
  alternate: true,
  loop: true,
  autoplay: onScroll({
    container: '.scroll-container',  // scroll container, defaults to viewport
    target: '.square',                // element that triggers the observer
    axis: 'y',                         // 'x' or 'y'
    enter: 'bottom top',                // when the animation starts
    leave: 'top bottom',                 // when the animation ends
    sync: true,                           // scrub animation progress to scroll position
    debug: false
  })
})
```

`onScroll()` is passed as the `autoplay` value of an `animate()`, `createTimeline()`, or `createTimer()` call — it replaces manually reading `window.scrollY` and calling `.seek()` from v3.

---

## Easing Functions

### Built-in Eases

Names dropped the `ease`/`In`/`Out` prefix style of v3 in favor of short camelCase power-of-ten style names:

```javascript
'linear'
'in', 'out', 'inOut', 'outIn'
'inQuad', 'outQuad', 'inOutQuad', 'outInQuad'
'inCubic', 'outCubic', 'inOutCubic', 'outInCubic'
'inQuart', 'outQuart', 'inOutQuart', 'outInQuart'
'inQuint', 'outQuint', 'inOutQuint', 'outInQuint'
'inSine', 'outSine', 'inOutSine', 'outInSine'
'inExpo', 'outExpo', 'inOutExpo', 'outInExpo'
'inCirc', 'outCirc', 'inOutCirc', 'outInCirc'
'inBack', 'outBack', 'inOutBack', 'outInBack'
'inElastic', 'outElastic', 'inOutElastic', 'outInElastic'
'inBounce', 'outBounce', 'inOutBounce', 'outInBounce'

// power/exponent variants take a parameter, e.g.
'out(3)'
'inOutElastic(.8, 1.2)'
```

### Custom Easings

**Cubic Bezier:**
```javascript
ease: 'cubicBezier(.5, .05, .1, .3)'
```

**Spring Physics:**
```javascript
import { spring } from 'animejs'

ease: spring({ bounce: 0.5, duration: 800 })          // perceived params
ease: spring({ mass: 1, stiffness: 100, damping: 10, velocity: 0 }) // physics params
```

**Steps:**
```javascript
ease: 'steps(5)'
```

**Linear Keyframes:**
```javascript
ease: 'linear(0, 0.5, 1)'
```

---

## Utilities

```javascript
import { utils } from 'animejs'
```

```javascript
utils.$(selector)                    // query selector, returns an array of elements
utils.set(targets, values)           // set values without animating
utils.get(targets, prop)             // get current value
utils.remove(targets)                 // stop and remove animations on targets
utils.cleanInlineStyles(targets)       // strip inline styles left by an animation
utils.sync(callback)                    // sync a function to the render loop
utils.random(min, max)                   // random number
utils.createSeededRandom(seed)            // deterministic random generator
utils.randomPick(array)                    // pick a random array item
utils.shuffle(array)                        // shuffle an array in place
utils.round(value, decimals)                 // round to N decimals
utils.clamp(value, min, max)
utils.snap(value, increment)
utils.wrap(value, min, max)
utils.mapRange(value, inLow, inHigh, outLow, outHigh)
utils.lerp(start, end, amount)
utils.damp(start, end, factor, deltaTime)
utils.roundPad(value, decimals)
utils.padStart(value, length, char)
utils.padEnd(value, length, char)
utils.degToRad(degrees)
utils.radToDeg(radians)
```

Most numeric utilities are chainable, e.g. `utils.random(0, 100).round(2)`.

---

## Examples

### Basic Animation

```javascript
import { animate } from 'animejs'

animate('.box', { x: 250, rotate: '1turn', duration: 800, ease: 'inOutQuad' })
```

### From-To Animation

```javascript
animate('.element', { x: [0, 250], opacity: [0, 1], duration: 1000 })
```

### Keyframe Animation

```javascript
animate('.element', {
  keyframes: {
    '0%': { x: 100, y: 0 },
    '50%': { x: 100, y: 100 },
    '100%': { x: 0, y: 0 }
  },
  duration: 4000,
  loop: true
})
```

### Timeline Animation

```javascript
import { createTimeline } from 'animejs'

createTimeline()
  .add('.box1', { x: 250 })
  .add('.box2', { x: 250 }, '-=500')
```

### Stagger Animation

```javascript
import { animate, stagger } from 'animejs'

animate('.stagger-item', {
  y: [-50, 0],
  opacity: [0, 1],
  delay: stagger(100, { from: 'center' })
})
```

### SVG Path Morph Animation

```javascript
import { animate, svg, utils } from 'animejs'

const [$a, $b] = utils.$('polygon')

animate($a, { points: svg.morphTo($b), duration: 2000, ease: 'inOutQuad' })
```

### JavaScript Object Animation

```javascript
const obj = { count: 0 }

animate(obj, {
  count: 100,
  round: 1,
  onUpdate: () => {
    document.querySelector('.counter').textContent = obj.count
  }
})
```
