# Audio of the main session · 19 October 2025

18 recordings of strikes at 24 zones of the upper face of the Piedra Campana (map in
`../../geometry/strike_zone_map.png`), with a rubber-covered hammer (swing of about 20 cm). About 5 consecutive strikes
per zone; each recording covers several consecutive zones. Intervals of each zone in
`../../annotation/zone_intervals.csv`; strikes in `../../derived/strikes.csv`.

**Equipment:** iPhone 16e, Voice Record Pro 4.0.3 ("Advanced" engine, *Voice Processing* disabled, manual gain 0 dB,
no effects), bottom omnidirectional microphone about 5 cm from the surface, next to the struck zone.
**Format:** PCM WAV, 48 kHz, 16 bit, 2 identical channels (a single microphone). Name = local start time (UTC−05:00),
`YYYYMMDD-HHMMSS.wav`. Each WAV file has its app record (`.wav.meta.txt`). The duration of each WAV file equals the
wall-clock time of the recording (±2 s).
**Limiter:** the iOS audio input limits the peaks to ≈ 0.92–0.94 of full scale, without clipping.

## Files (`files.csv`)

| Column | Meaning |
|---|---|
| `file` | name of the WAV file |
| `start_local`, `duration_s`, `channels` | start time (UTC−05:00), duration (s) and channels |
| `zones`, `strikes` | zones struck and number of strikes in `../../derived/strikes.csv` |
| `set` | `characterisation` or `validation` (see `../../derived/metadata.md`) |
| `accelerometer_record` | record of `../s2_2025-10-19_accelerometer` covering the recording (empty for 135332, 135632 and 135829) |
| `strikes_with_accelerometer`, `strikes_clear_pulse` | strikes covered by the accelerometer and strikes with a clear pulse (SNR > 8) |
| `app_metadata`, `sha256` | Voice Record Pro record and SHA-256 checksum |

Summary: 18 recordings of 43–119 s (13:53–15:14), 613 strikes. The zones of each recording are listed in
`../../annotation/metadata.md`.
