# Strike table · session of 19 October 2025

`strikes.csv`: **the data set of the article**. One row per strike (613 strikes from 18 recordings; 13–31 per zone,
median 28; each zone in 3–6 recordings). It is produced by notebooks 01 (detection and features), 02 (accelerometer)
and 06 (quality) from `../raw/s2_2025-10-19_audio`, `../raw/s2_2025-10-19_accelerometer` and
`../annotation/zone_intervals.csv`.

**How a strike is obtained.** Peaks are detected in the band above 4 kHz (2 ms envelope > median + 40 MAD, at least
0.15 s apart). A peak is a strike if it falls within the interval of a zone, if its amplitude is at least 30 % of the
75th percentile of the peaks of its recording, if no other peak lies within 0.35 s and if it excites at least one mode
of the stone (peak ≥ 6 times the spectral median within ±40 Hz, between 30 and 400 ms after the strike).

| Group | Columns |
|---|---|
| Identification | `zone`, `strike` (number of the strike within the zone), `file`, `run` (zone × recording identifier), `set` (`characterisation` / `validation`), `t_s` (time of the peak in the WAV file, s), `i_peak` (sample of the strike maximum, 48 kHz) |
| Detection | `peak_amp_rel` (peak amplitude relative to the 75th percentile of its recording), `modes_present` (stone modes that stand out, of 13) |
| Audio quality | `clipped` (any sample ≥ 99 % of full scale), `snr_dB` (RMS of the 0.4 s window against the background noise of the recording: 10th percentile of the RMS in 100 ms frames), `prev_resonance_dB` (RMS of the 0.3 s before the strike relative to the window: tail of the previous strike), `other_peak_in_window` (another peak between 30 ms and 0.4 s after the strike maximum), `audio_peak_fs` (audio peak, fraction of full scale), `limiter` (peak ≥ 0.90: the iOS limiter acted in the first milliseconds) |
| Accelerometer | `acc_recorded` (an accelerometer record covers the strike), `acc_peak_ms2` (acceleration peak minus baseline, m/s²), `acc_snr` (peak / robust noise), `acc_clear_pulse` (`acc_snr` > 8) |
| Timbre | `spectral_centroid`, `spectral_bandwidth` (Hz) and `mfcc_0`…`mfcc_12`: frame means over 0.4 s from 5 ms before the peak, 300 Hz high-pass (librosa 0.11) |

## Characterisation set and validation set

`recording_sets.csv` (notebook 01, section 1.3) assigns each recording to a set; the split is by recording, never by
strike. Of the 18 recordings, 15 have a simultaneous accelerometer record (135332, 135632 and 135829 were recorded
before it was started). The **characterisation set** is 11 of them (371 strikes), chosen so that every zone appears in
at least two characterisation recordings and in at least one validation recording; it is used by all the analyses of
the sound (notebooks 02–05, 08, 11 and 12). The **validation set** is the remaining 7 recordings (242 strikes, all 24
zones), used only to test the zone classifier (notebook 07) and the grouping of zones (notebook 12) on recordings not
seen in the analysis.

| Column of `recording_sets.csv` | Description |
|---|---|
| `file` | WAV file in `../raw/s2_2025-10-19_audio` |
| `set` | `characterisation` or `validation` |
| `zones` | zones struck in the recording |
| `strikes` | strikes in the recording |
| `accelerometer` | the recording has an accelerometer record |

## Quality

| Indicator | Value |
|---|---|
| Strikes with clipped samples | 0 |
| Signal-to-noise ratio (against background noise) | median 21.4 dB; minimum 14.4 dB |
| Tail of the previous strike less than 10 dB below the strike | 268 strikes (44 %) |
| Another peak within the 0.4 s window | 22 strikes |
| Strikes that reached the iOS limiter (peak ≥ 0.90) | 534 (87 %) |
| Strikes with accelerometer record / with clear pulse | 486 (15 recordings) / 454 (352 in the characterisation set) |
| Sensitivity | without the strikes with a strong previous tail or another peak in the window (279), the zone means change little and the zone effect increases |

Levels are relative (uncalibrated microphone at ~5 cm). The limiter affects the first milliseconds of the strike, not
the decay of the modes.
