# fleet-midi-tidalcycles 🥁

> *Ternary strategy vectors → TidalCycles rhythmic patterns*

Bridges the SuperInstance fleet to TidalCycles, treating every agent state as a rhythmic pattern. Conservation laws become voice-leading rules, strategy vectors become polyrhythms.

## Architecture

```
fleet agent state → ternary vector → TidalCycles pattern string → SuperDirt sound
```

Each of the three ternary states maps to a Tidal cycle function:
- **+1** → `s "bd"` (kick / assertion)
- **0** → `s "hh"` (hat / sustain)
- **-1** → `s "sn"` (snare / opposition)

## Related
- [fleet-midi-text2midi](https://github.com/SuperInstance/fleet-midi-text2midi)
- [fleet-bridge](https://github.com/SuperInstance/fleet-bridge)
