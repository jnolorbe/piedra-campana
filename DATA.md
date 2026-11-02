# Data description

Site: Piedra Campana, Cerro Campana, San Antonio (Cañete, Lima, Peru), 12°37'53.6" S, 76°39'43.0" W (−12.63156,
−76.66194; Plus Code 57V5989Q+96), ~144 m above sea level. Object: a rock slab that rings when struck, outdoors on the
slope of the hill; it rests near its centre on other stones of similar appearance and most of its edges are free.
3D model: `data/photos/stone_3d_model_2025-10-19.glb`, also at
<https://poly.cam/capture/53E74E72-5304-436D-99F4-4C9103481075>. Each data set has its own `metadata.md`;
columns in `data/data_dictionary.csv`.

| Data set | Folder | Contents | Use |
|---|---|---|---|
| S2 audio (19 Oct 2025) | `raw/s2_2025-10-19_audio` | 18 WAV files, 24 zones | modes, damping, timbre, classifier |
| S2 accelerometer | `raw/s2_2025-10-19_accelerometer` | 15 phyphox XML files | force of each strike |
| S2 intervals | `annotation` | 125 zone × recording intervals | locating the strikes |
| S2 strikes | `derived` | 613 strikes with quality, acceleration and features; set of each recording | data set of the article |
| S1 replication (7 Feb 2025) | `raw/s1_2025-02-07_phyphox_audio` | 52 records of 0.5 s, 12 zones | stability of the frequencies |
| S3 tuning fork (25 Nov 2025) | `raw/s3_2025-11-25_tuning_fork` | 5 WAV files, 256 Hz | frequency scale |
| S4 instrument check (28 Oct 2026) | `raw/s4_2026-10-28_instrument_check` | 8 WAV files: 256 and 329.6 Hz forks, steel bowl | frequency, decay, limiter |
| Geometry | `geometry` | zone map and coordinates | position and distance to the edge |
| Photographs and 3D model | `photos` | 3 photographs, Polycam 3D model (.glb) | shape and support of the slab |
| XRF | `xrf` | 14 elements | composition of the surrounding rock |

## Protocol of the main session (S2)

- **Audio:** iPhone 16e with Voice Record Pro 4.0.3; 16-bit PCM WAV, 48 kHz, 2 identical channels; "Advanced" engine,
  *Voice Processing* disabled, manual gain 0 dB, bottom omnidirectional microphone, no effects.
- **Microphone:** about **5 cm** from the surface, next to the struck zone (at larger distances the wind dominated).
- **Strikes:** rubber-covered hammer, swing of about 20 cm, strength kept as constant as possible; about 5
  consecutive strikes per zone; each recording covers several consecutive zones.
- **Accelerometer:** Xiaomi M2101K7AG resting on the stone, with phyphox (~200.7 Hz); started after the first three
  recordings.
- **Zones:** the zones struck in each recording were written down in the field notebook, in the order they were struck.

## Characterisation and validation sets

Eleven of the 15 recordings with accelerometer data (371 strikes; each zone in 2–4 of them) are used to characterise
the sound. They were chosen so that every zone appears in at least two of them and in at least one of the remaining
recordings. The other seven recordings (242 strikes, all 24 zones) form the validation set, used only to test the zone
classifier and the grouping of zones on recordings not seen in the analysis (`derived/recording_sets.csv`).

## Data quality

| Aspect | Indicator |
|---|---|
| Integrity | SHA-256 checksums of all files; duration of every WAV file equal to the wall-clock time (±2 s) |
| Frequency scale | 256 and 329.6 Hz tuning forks: errors of +0.09 % and −0.15 % (opposite signs: no clock error) |
| Frequency stability | standard deviation of each mode between strikes 0.03–0.48 Hz (< 0.04 %); in S1, eight months earlier, all 13 modes at −0.07 to −0.35 % |
| Decay | 67 % of the strike × mode measurements meet a decay ≥ 10 dB and R² ≥ 0.9; Hilbert and Schroeder agree within ~6 %; the T60 of the bowl does not depend on the microphone distance (~5 a 10 cm) |
| Signal-to-noise (S2) | against the background noise of each recording: median 21 dB, minimum 14 dB. In 268 strikes (44 %) the tail of the previous strike is less than 10 dB below the strike; without them the zone effect increases |
| Clipping and limiter | no clipped sample; 87 % of the strikes reach the iOS peak limiter (≈ 0.92 of full scale) in their first milliseconds; the Q of those strikes does not differ |
| Coverage | 13–31 strikes per zone (median 28), each zone in 3–6 recordings; accelerometer for 486 strikes (clear pulse for 454) |
| Repeatability | the recording within the zone explains 19–43 % of the variance of the timbre (position of the hand-held microphone and exact strike point) |

**Limitations:** relative levels (uncalibrated microphone); approximate microphone distance; hand-held strikes whose
force is measured only indirectly; S1 (February 2025) stores only the last 0.5 s of each record, enough for modal frequencies but not for decay times, and its 12 zones were numbered independently of the 24 zones of S2, so the two sessions can be compared only through the global modes, not zone by zone.