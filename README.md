# 🥁 tidalcycles

**Ternary strategy vectors become percussive patterns.**

---

A vector like `[1, 0, -1, 1, 0, -1, 1, 1]` produces:

```
Pattern: s "bd", s "hh", s "sn", s "bd", s "hh", s "sn", s "bd", s "bd"
Euclidean: e(4, 8)
Density: fast 2
```

+1 = kick drum (assertion). 0 = hi-hat (sustain). -1 = snare drum (opposition).

Your agent's decisions literally become a rhythm.

---

## Quick start

```bash
curl -X POST localhost:3002/pattern \
  -H 'Content-Type: application/json' \
  -d '{"ternary_vector":[1,0,-1,1,0,-1,1,1]}'
```

Returns: TidalCycles pattern string, Euclidean rhythm, speed modifier, executable code.

---

## What you can build

- **Real-time rhythm from agent states** — every decision is a beat
- **Euclidean rhythms** — `e(4,8)` = the classic cuatro pattern in world music
- **Density analysis** — pattern density tells you how "active" an agent is
- **Cross-pollination:** → [strudel-connector](https://github.com/SuperInstance/fleet-strudel-connector) for browser playback

**Ensign Rhythmica** — Fleet Rhythm Officer.
