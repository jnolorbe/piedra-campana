# Zone intervals · session of 19 October 2025

`zone_intervals.csv`: the interval of each recording in `../raw/s2_2025-10-19_audio` in which each zone was struck.
One row per **run** (consecutive strikes on one zone within one recording): 125 intervals, 18 recordings, 24 zones.

| Column | Type | Unit | Description |
|---|---|---|---|
| `zone` | integer | | struck zone (1–24; map in `../geometry/strike_zone_map.png`) |
| `file` | text | | WAV file in `../raw/s2_2025-10-19_audio` |
| `start_s`, `end_s` | float | s | start and end of the interval from the beginning of the WAV file |

**Origin of the zones.** The zones struck in each recording, and their order, were written down in the author's field
notebook during the session. The numbering is that of the zone map (`../geometry/strike_zone_map.png`).

| Recordings | Zones |
|---|---|
| 135332, 135632, 140152, 140412, 140629 | Z1–Z10 |
| 135829 | Z1–Z6 |
| 140944, 141757, 142014 | Z11–Z19 |
| 143811, 144016, 144311 | Z20–Z24 |
| 150207, 150407, 150644 | Z15–Z19 |
| 151007, 151215, 151407 | Z11–Z14 |

Each zone appears in 3 to 6 recordings (Z20–Z24 in 3). Within a recording the runs are separated by pauses of more
than 2 s, and the intervals were placed on these groups of strikes. The modal profile of each run is consistent with the
assignment: recordings of the same circuit repeat the same zones in the same order. Within each interval the strikes are
detected automatically (notebook 01); the result is `../derived/strikes.csv`. Review sheets of each recording
(waveform, intervals, spectrogram and detected strikes) are in `results/figures/review/`; the strikes per run (3–6;
110 of the 125 runs have 5) in `results/tables/t01_strikes_per_run.csv`.
