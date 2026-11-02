# Piedra Campana — data and code

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23898343.svg)](https://doi.org/10.5281/zenodo.23898343)

Field recordings and code for the acoustic analysis of the **Piedra Campana**, a natural lithophone (a rock slab that
rings when struck) on the Cerro Campana, San Antonio (Cañete, Lima, Peru). The slab rests near its centre on other
stones of similar appearance, and most of its edges are free. A 3D model of the stone is included
(`data/photos/stone_3d_model_2025-10-19.glb`) and can be viewed online at
<https://poly.cam/capture/53E74E72-5304-436D-99F4-4C9103481075>.

The data set contains 613 strikes at 24 positions with quality indicators, a phone accelerometer record, a replication
session, tuning-fork and steel-bowl checks of the recording chain, the geometry of the strike zones,
photographs and a 3D model of the stone, and an XRF analysis. Data: CC BY 4.0; code: MIT.

Juan Neil Mendoza Nolorbe and Félix Julián Acevedo Poma, Universidad Nacional del Callao (Peru).

## Questions and main results

| | Question | Main result | Notebook |
|---|---|---|---|
| Q1 | What are the global vibration modes of the stone? | 13 global modes between 384.9 and 1938 Hz; they reappear eight months earlier with another striker (−0.07 to −0.35 %) | 03, 06 |
| Q2 | How strongly is each mode damped? | Q between 378 and 1237 (the lowest mode is the most damped); T60 of 1 to 3 s | 03 |
| Q3 | How much does the sound change with the strike position? | the zone explains 23–62 % of the variance of the spectral features and the recording 19–43 %; a single strike identifies its zone (of 24) in 64 % of the strikes of a held-out recording and in 73 % of those of the validation recordings (chance, 95th percentile: 6 % and 8 %) | 02, 05, 07 |
| Q4 | Does this change follow a spatial pattern? | no dependence on the distance to the edge is detected (19 edge zones, 5 interior zones); neighbouring zones have similar modal purity (Moran's I = 0.32) | 04 |

**Data split.** The 18 recordings of 19 October 2025 contain 613 strikes in 24 zones; 15 of them also have an
accelerometer record. Eleven recordings with accelerometer data (371 strikes) are used to characterise the sound; the
other seven (242 strikes, all 24 zones) are used to validate the zone classifier and the grouping of zones
(`data/derived/recording_sets.csv`).

## Contents

```
data/
  raw/s2_2025-10-19_audio/            18 WAV files (48 kHz, 16 bit) with strikes at 24 zones + app metadata
  raw/s2_2025-10-19_accelerometer/    15 phyphox XML files (linear acceleration, ~200 Hz), phone resting on the stone
  raw/s1_2025-02-07_phyphox_audio/    52 phyphox zip files (0.5 s of audio, 48 kHz) at 12 zones: replication of frequencies
  raw/s3_2025-11-25_tuning_fork/      5 WAV files of a 256 Hz tuning fork
  raw/s4_2026-10-28_instrument_check/ 8 WAV files: 256 and 329.6 Hz tuning forks and a steel bowl
  annotation/                         interval of each zone in each recording
  derived/                            table of the 613 strikes and the set of each recording
  geometry/                           map of the 24 zones and their coordinates
  photos/                             three photographs of the stone and its 3D model (glTF, .glb)
  xrf/                                elemental composition by XRF (transcribed from IPEN report No. 1730)
notebooks/    notebooks 01–12 (executed, with their outputs)
src/config.py shared paths and parameters
results/      tables, figures and intermediate files produced by the notebooks
```

Each folder in `data/` has a **`metadata.md`** describing the data set, its origin, format and quality, and each
`data/raw/*` folder has a `files.csv` describing every file. General description in **[DATA.md](DATA.md)**; columns,
types and units in `data/data_dictionary.csv`; SHA-256 checksums in `data/SHA256SUMS.txt`
(check with `cd data && shasum -a 256 -c SHA256SUMS.txt`).

## How to reproduce

```bash
bash create_environment.sh            # environment "piedra-campana" (Python 3.12, pinned versions)
conda activate piedra-campana         # or: source .venv/bin/activate
jupyter lab notebooks/                # open and run each notebook in order
python run_all.py                     # or run all of them at once (≈ 5 min)
```

| Notebook | What it does |
|---|---|
| 01 | strike detection within the annotated intervals, strikes per zone and per run, characterisation and validation sets, review sheets of each recording (`results/figures/review/`) and spectral features (centroid, bandwidth, 13 MFCC); detection criteria illustrated and sensitivity to the thresholds |
| 02 | accelerometer: synchronisation, force of each strike and its effect on the timbre |
| 03 | mode catalogue and damping: Q and T60 of 13 modes |
| 04 | spatial structure: distance to the edge, edge versus interior zones, Moran, Mantel |
| 05 | differences between zones: Kruskal–Wallis, PERMANOVA, mixed model |
| 06 | quality of each strike and final table `data/derived/strikes.csv`; mode table; replication; 256 Hz tuning fork |
| 07 | zone identification with a random forest, validated leaving one recording out and with the validation recordings |
| 08 | figures of the article, including the conceptual model of the study |
| 09 | instrument check: tuning forks, steel bowl, iOS peak limiter |
| 10 | does the stone sound like a bell? Comparison with the bowl and intervals between modes |
| 11 | sensitivity of the results to the duration of the strike window (0.1–0.8 s) |
| 12 | exploratory: timbral grouping of the zones and musical map (dominant note, duration and type of sound per zone) |

## Licence and citation

Data: CC BY 4.0 ([LICENSE-DATA.md](LICENSE-DATA.md)). Code: MIT ([LICENSE](LICENSE)). Please cite the archived
version (details in [CITATION.cff](CITATION.cff)):

> Mendoza Nolorbe JN, Acevedo Poma FJ (2026) Piedra Campana: data and code for the acoustic analysis of a natural
> lithophone (San Antonio, Lima, Peru), version 1.0.0. Zenodo. https://doi.org/10.5281/zenodo.23898343
