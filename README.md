# Motionstack

**The motion and 3D web stack for Claude Code.**

A plugin marketplace of 22 skills covering the modern creative-web toolchain — Three.js, GSAP, React Three Fiber, Motion, Anime.js, Babylon.js, and more. Every skill is verified against the current library versions (last full refresh: July 2026).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Plugins: 27](https://img.shields.io/badge/Plugins-27-blue.svg)](#plugins)
[![Skills: 22](https://img.shields.io/badge/Skills-22-green.svg)](#skills)

## Quick Start

```bash
# Add the marketplace to Claude Code
/plugin marketplace add discover-dmc/motionstack

# Install a single plugin
/plugin install threejs-webgl

# Or a whole category bundle
/plugin install core-3d-animation
```

Each plugin ships the skill itself plus 1–3 slash commands and 1–2 specialized agents. Skills auto-activate when Claude detects relevant work — "create a Three.js scene", "add scroll-driven animations", "build an R3F product configurator".

## Skills

All skills track the current library versions and note honestly when a library is dormant or superseded.

### Core 3D & Animation
| Skill | Covers | Verified against |
|---|---|---|
| `threejs-webgl` | Three.js WebGL/WebGPU | r185, WebGPURenderer production-ready |
| `gsap-scrolltrigger` | GSAP + ScrollTrigger | 3.15, all plugins free (MIT) since the Webflow acquisition |
| `react-three-fiber` | R3F + drei | v9 / drei v10, React 19 |
| `motion-framer` | Motion (ex Framer Motion) | v12, `motion/react` |
| `babylonjs-engine` | Babylon.js | 9.x, Physics V2 |

### Extended 3D & Scroll
| Skill | Covers | Verified against |
|---|---|---|
| `aframe-webxr` | A-Frame WebXR | 1.8.0 |
| `pixijs-2d` | PixiJS 2D rendering | v8.19 |
| `playcanvas-engine` | PlayCanvas | v2.20, ESM Scripts |
| `locomotive-scroll` | Locomotive Scroll | v5 (Lenis-based), v4 documented as legacy |
| `barba-js` | Barba.js page transitions | 2.10, maintenance status noted |
| `lightweight-3d-effects` | Zdog, Vanta.js, Vanilla-Tilt | pinned versions, dormancy noted |

### Animation & Components
| Skill | Covers | Verified against |
|---|---|---|
| `animejs` | Anime.js | v4.5 (`animate()`, `createTimeline()`, `svg` module) |
| `lottie-animations` | Lottie / dotLottie | current runtimes, dotLottie-first |
| `react-spring-physics` | React Spring + Popmotion | v10 / React 19, Popmotion legacy status noted |
| `animated-component-libraries` | Magic UI + React Bits | 150+/130+ components, current CLI installs |
| `scroll-reveal-libraries` | AOS | 2.3.4, native CSS scroll-driven animations recommended for new work |

### 3D Authoring & Motion
| Skill | Covers | Verified against |
|---|---|---|
| `blender-web-pipeline` | Blender → glTF for web | Blender 5.1 |
| `spline-interactive` | Spline runtime/export | react-spline v4 |
| `rive-interactive` | Rive state machines | current wasm/react runtimes, data binding |
| `substance-3d-texturing` | Substance 3D Painter | 12.1, OpenPBR notes for web export |

### Meta
| Skill | Covers |
|---|---|
| `web3d-integration-patterns` | Combining Three.js, GSAP, R3F, Motion, React Spring |
| `modern-web-design` | 2026 platform baseline: container queries, View Transitions, Popover API, scroll-driven animations |

## Plugins

**22 individual plugins** (one per skill) plus **5 bundles**:

- `core-3d-animation` — Three.js, GSAP, R3F, Motion, Babylon.js
- `extended-3d-scroll` — A-Frame, lightweight effects, PlayCanvas, PixiJS, Locomotive, Barba
- `animation-components` — React Spring, Magic UI/React Bits, AOS, Anime.js, Lottie
- `authoring-motion` — Blender, Spline, Rive, Substance 3D
- `meta-skills` — integration patterns, modern web design

Full catalog with commands and agents: [MARKETPLACE.md](MARKETPLACE.md)

## Other Ways to Use

**claude.ai skill upload** — packaged `.zip` files for every skill are attached to [GitHub Releases](https://github.com/discover-dmc/motionstack/releases). Upload via **Settings → Features → Skills** on claude.ai, or build them yourself:

```bash
.claude/skills/skill-creator/scripts/package_skill.py .claude/skills/threejs-webgl
```

**Copy into a project** — drop any skill directory into your project's `.claude/skills/`.

## Development

Skills live in `.claude/skills/`, distributable plugins are generated into `plugins/`, and the marketplace manifest into `.claude-plugin/marketplace.json`.

```bash
# Create a skill
.claude/skills/skill-creator/scripts/init_skill.py my-skill --path .claude/skills

# Validate it
.claude/skills/skill-creator/scripts/quick_validate.py .claude/skills/my-skill

# Regenerate its plugin, the bundles, and the manifest
./scripts/marketplace/generate_plugin.py my-skill
./scripts/marketplace/generate_bundle.py --all
./scripts/marketplace/generate_marketplace.py

# Validate the whole marketplace
./scripts/marketplace/validate_marketplace.py
```

See [CLAUDE.md](CLAUDE.md) for skill-authoring standards (YAML frontmatter, naming, script requirements).

## Contributing

1. Fork, create or improve a skill with `init_skill.py`
2. Follow the [official skill guidelines](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
3. Validate with `quick_validate.py`, regenerate plugins, run `validate_marketplace.py`
4. Open a PR

Guidelines: imperative form in SKILL.md, runnable examples, executable scripts, Python 3 stdlib only, honest maintenance-status notes for the libraries you document.

## License

[MIT](LICENSE)
