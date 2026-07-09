#!/usr/bin/env python3
"""
Anime.js Animation Generator

Generates Anime.js v4 animation boilerplate code for common animation patterns.

Usage:
    ./animation_generator.py                    # Interactive mode
    ./animation_generator.py --type stagger     # Generate stagger animation
    ./animation_generator.py --type timeline    # Generate timeline sequence

Animation Types:
    basic           - Simple translateX/Y, opacity animation
    stagger         - Sequential reveal with stagger
    grid-stagger    - Grid-based stagger animation
    svg-line        - SVG line drawing animation
    svg-morph       - SVG path morphing animation
    timeline        - Multi-step timeline sequence
    keyframe        - Keyframe animation with multiple steps
    scroll          - Scroll-triggered animation
"""

import sys

ANIMATION_TYPES = {
    'basic': {
        'name': 'Basic Animation',
        'description': 'Simple x/y, opacity animation',
        'code': '''import { animate } from 'animejs'

animate('.element', {
  x: 250,
  rotate: '1turn',
  opacity: [0, 1],
  duration: 800,
  ease: 'inOutQuad'
})'''
    },

    'stagger': {
        'name': 'Stagger Animation',
        'description': 'Sequential reveal with stagger effect',
        'code': '''import { animate, stagger } from 'animejs'

animate('.stagger-element', {
  y: [100, 0],
  opacity: [0, 1],
  delay: stagger(100), // Increment delay by 100ms
  ease: 'outQuad',
  duration: 600
})'''
    },

    'grid-stagger': {
        'name': 'Grid Stagger Animation',
        'description': 'Grid-based stagger from center',
        'code': '''import { animate, stagger } from 'animejs'

animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, {
    grid: [14, 5],        // 14 columns, 5 rows
    from: 'center',       // Start from center
    axis: 'x'             // Primary axis
  }),
  ease: 'outElastic(1, .8)',
  duration: 600
})'''
    },

    'svg-line': {
        'name': 'SVG Line Drawing',
        'description': 'SVG path line drawing animation',
        'code': '''import { animate, svg } from 'animejs'

animate(svg.createDrawable('path'), {
  draw: ['0 0', '0 1'],
  ease: 'inOutQuad',
  duration: 2000,
  delay: (el, i) => i * 250
})'''
    },

    'svg-morph': {
        'name': 'SVG Path Morphing',
        'description': 'Morph between SVG path shapes',
        'code': '''import { animate, svg, utils } from 'animejs'

const [$path1, $path2] = utils.$('polygon')

animate($path1, {
  points: svg.morphTo($path2),
  duration: 2000,
  ease: 'inOutQuad',
  loop: true,
  alternate: true
})'''
    },

    'timeline': {
        'name': 'Timeline Sequence',
        'description': 'Multi-step timeline with overlapping animations',
        'code': '''import { createTimeline } from 'animejs'

const tl = createTimeline({
  defaults: { ease: 'outExpo', duration: 750 }
})

tl.add('.title', { y: [-50, 0], opacity: [0, 1] })
.add('.subtitle', { y: [-30, 0], opacity: [0, 1] }, '-=500')  // Start 500ms before previous ends
.add('.button', { scale: [0, 1], opacity: [0, 1] }, '-=300')'''
    },

    'keyframe': {
        'name': 'Keyframe Animation',
        'description': 'Multiple keyframes for complex motion',
        'code': '''import { animate } from 'animejs'

animate('.element', {
  keyframes: {
    '0%': { x: 100, y: 0 },
    '25%': { x: 100, y: 100 },
    '50%': { x: 0, y: 100 },
    '100%': { x: 0, y: 0 }
  },
  duration: 4000,
  ease: 'inOutQuad',
  loop: true
})'''
    },

    'scroll': {
        'name': 'Scroll-Linked Animation',
        'description': 'Animation controlled by scroll position',
        'code': '''import { animate, onScroll } from 'animejs'

animate('.scroll-element', {
  y: [100, 0],
  opacity: [0, 1],
  ease: 'outQuad',
  autoplay: onScroll({
    enter: 'bottom top',
    leave: 'top bottom',
    sync: true
  })
})'''
    }
}

def print_header():
    """Print script header"""
    print("\n" + "="*60)
    print("Anime.js Animation Generator")
    print("="*60 + "\n")

def list_animation_types():
    """List all available animation types"""
    print("Available Animation Types:\n")
    for key, anim in ANIMATION_TYPES.items():
        print(f"  {key:15} - {anim['description']}")
    print()

def generate_animation(anim_type):
    """Generate animation code for given type"""
    if anim_type not in ANIMATION_TYPES:
        print(f"Error: Unknown animation type '{anim_type}'")
        print("Use --list to see available types")
        sys.exit(1)

    anim = ANIMATION_TYPES[anim_type]

    print(f"\n{anim['name']}")
    print("-" * 60)
    print(f"\n{anim['description']}\n")
    print("Generated Code:")
    print("-" * 60)
    print(anim['code'])
    print("\n" + "="*60 + "\n")

def interactive_mode():
    """Run in interactive mode"""
    print_header()
    list_animation_types()

    print("Enter animation type (or 'quit' to exit): ", end='')
    choice = input().strip().lower()

    if choice == 'quit':
        sys.exit(0)

    generate_animation(choice)

def main():
    """Main entry point"""
    args = sys.argv[1:]

    # No arguments - interactive mode
    if not args:
        interactive_mode()
        return

    # Parse arguments
    if '--list' in args:
        print_header()
        list_animation_types()
        return

    if '--type' in args:
        try:
            type_index = args.index('--type')
            anim_type = args[type_index + 1]
            print_header()
            generate_animation(anim_type)
        except IndexError:
            print("Error: --type requires an animation type")
            print("Usage: ./animation_generator.py --type <type>")
            sys.exit(1)
        return

    # Help or unknown arguments
    print(__doc__)

if __name__ == '__main__':
    main()
