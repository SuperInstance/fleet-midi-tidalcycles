<div align="center">

# 🥁 fleet-midi-tidalcycles

> *Ternary strategy vectors become TidalCycles rhythmic patterns*

[![CI](https://img.shields.io/github/actions/workflow/status/SuperInstance/fleet-midi-tidalcycles/ci.yml?style=flat-square&logo=github&label=CI)](https://github.com/SuperInstance/fleet-midi-tidalcycles/actions)
[![npm](https://img.shields.io/badge/npm-%40superinstance%2Fmidi--tidalcycles-cb3837?style=flat-square&logo=npm)](https://www.npmjs.com/package/@superinstance/midi-tidalcycles)
[![Docker](https://img.shields.io/badge/docker-ghcr-2496ed?style=flat-square&logo=docker)](https://github.com/SuperInstance/fleet-midi-tidalcycles/pkgs/container/fleet-midi-tidalcycles)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](http://makeapullrequest.com)

---

Every ternary {-1, 0, +1} strategy vector maps to a percussive cycle: assertion → kick, sustain → hat, opposition → snare. Euclidean rhythm generator, density analysis, and I2I transport turn agent states into percussive flows.

---

## 📦 Installation

```bash
# npm
npm install @superinstance/midi-tidalcycles

# Docker
docker pull ghcr.io/superinstance/fleet-midi-tidalcycles:latest

# Clone
git clone https://github.com/SuperInstance/fleet-midi-tidalcycles.git
```

## 🚀 Quick Start

```bash
# Generate pattern from ternary vector:
curl -X POST localhost:3002/pattern \
  -H "Content-Type: application/json" \
  -d "{\"agent_id\":\"scout\",\"ternary_vector\":[1,0,-1,1,0,-1,1,1]}"

# Python directly:
from lib.pattern_engine import vector_to_pattern
print(vector_to_pattern([1,0,-1,1], "test"))
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│   ternary vector: [1, 0, -1, 1, 0, -1, 1, 1]       │
│         │                                           │
│         ▼                                           │
│   ┌──────────────────┐                              │
│   │ Pattern Engine   │───▶ s "bd", s "hh", s "sn"  │
│   │ euclidean(k=4,n=8)──▶ e(4, 8)                  │
│   │ density=0.625    │───▶ fast 2                  │
│   └───────┬──────────┘                              │
│           │                                         │
│           ▼                                         │
│   ┌──────────────┐    ┌──────────────┐              │
│   │ FastAPI:3002 │───▶│ I2I Bridge   │              │
│   │              │    │ → Harbor     │              │
│   └──────────────┘    └──────────────┘              │
│                                                     │
│   +1 → kick (bd)   0 → hat (hh)   -1 → snare (sn)  │
└─────────────────────────────────────────────────────┘
```

## 📡 API

### POST /pattern
Convert a ternary agent state vector to a TidalCycles rhythmic pattern.

```json
{"agent_id": "scout", "ternary_vector": [1,0,-1,1]}
```
→ Returns pattern string, Euclidean rhythm, speed modifier, and executable Tidal code.

### GET /health
```json
{"status": "ok", "service": "rhythmica"}
```

## 🧪 Beta Tested

Part of the [SuperInstance MIDI Fleet](https://github.com/SuperInstance/construct-coordination/blob/main/FLEET_MIDI.md). Every push verified via CI — zeroshot tests ensure zero-config operation out of the box.

## 🤝 Related

- [fleet-bridge](https://github.com/SuperInstance/fleet-bridge) — I2I bottle transport
- [construct-coordination](https://github.com/SuperInstance/construct-coordination) — Fleet catalog

---

<div align="center">
<sub>Built with 🥁 for the SuperInstance fleet • <a href="https://github.com/SuperInstance">github.com/SuperInstance</a></sub>
</div>
