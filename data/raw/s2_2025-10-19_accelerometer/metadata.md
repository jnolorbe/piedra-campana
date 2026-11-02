# Accelerometer · 19 October 2025

A second phone (Xiaomi M2101K7AG) **resting on the stone** recorded the linear acceleration with phyphox (experiment
"Acceleration (without g)", ≈ 200.7 Hz) while the audio was being recorded. It only sees frequencies below ~100 Hz:
it is used as an indirect measure of the force of each strike (notebook 02). Its clock differs from that of the audio
by ≈ 1 s; notebook 02 corrects the offset recording by recording.

**Format:** phyphox XML. The data are in the `init` attribute of the `<container>` elements: `acc_time` (s), `accX`,
`accY`, `accZ` and `acc` (magnitude) in m/s²; the start time in the `systemTime` attribute (Unix ms).
**Name:** `S2_acc_<start time>_phyphox<n>.xml` (n = number of the file exported by phyphox).

## Files (`files.csv`)

`file`, `start_local`, `duration_s`, `samples`, `audio_recording` (WAV file of `../s2_2025-10-19_audio` that it
covers), `sha256`. 15 records, one per audio recording except 135332, 135632 and 135829 (recorded before the first
accelerometer record).

**Coverage:** 486 of the 613 strikes have a record; 454 show a clear pulse (SNR > 8); details per recording in the
column `strikes_clear_pulse` of `../s2_2025-10-19_audio/files.csv`.
