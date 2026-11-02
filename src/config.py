"""Paths and parameters shared by all notebooks."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]          # repository root
RESULTS = ROOT / "results"
TABLES = RESULTS / "tables"
FIGURES = RESULTS / "figures"
INTERMEDIATE = RESULTS / "intermediate"
for d in (TABLES, FIGURES, INTERMEDIATE):
    d.mkdir(parents=True, exist_ok=True)

DATA = ROOT / "data"
AUDIO = DATA / "raw" / "s2_2025-10-19_audio"                     # main session WAV files (19 Oct 2025)
ACCELEROMETER = DATA / "raw" / "s2_2025-10-19_accelerometer"     # phyphox XML files (19 Oct 2025)
REPLICATION = DATA / "raw" / "s1_2025-02-07_phyphox_audio"       # replication session (7 Feb 2025)
TUNING_FORK = DATA / "raw" / "s3_2025-11-25_tuning_fork"         # 256 Hz tuning fork (25 Nov 2025)
INSTRUMENT_CHECK = DATA / "raw" / "s4_2026-10-28_instrument_check"   # tuning forks and steel bowl (28 Oct 2026)
ZONE_INTERVALS = DATA / "annotation" / "zone_intervals.csv"     # interval of each zone in each recording
STRIKES = DATA / "derived" / "strikes.csv"                     # final strike table with quality indicators
RECORDING_SETS = DATA / "derived" / "recording_sets.csv"       # set (characterisation / validation) of each recording
ZONE_MAP = DATA / "geometry" / "strike_zone_map.png"
COORDINATES = DATA / "geometry" / "zone_coordinates.csv"

FS = 48000                 # Hz
HIGHPASS_HZ = 300.0        # Hz, 5th-order Butterworth, zero phase: removes wind noise, keeps the 384.9 Hz mode
FILTER_ORDER = 5
# Global modes of the stone (Hz), used only to decide whether a peak excites the stone (notebook 01);
# the catalogue is recomputed in notebook 03.
REFERENCE_MODES = [384.9, 599.5, 759.2, 848.8, 969.5, 1260.0, 1298.9, 1348.8, 1389.2, 1645.2, 1819.4, 1893.3, 1938.0]
STRIKE_WINDOW = 0.4        # s
PRE_PEAK = 0.005           # s before the strike maximum
STRIKE_SAMPLES = int(STRIKE_WINDOW * FS)   # 19200
SEED = 42                  # random seed for permutations, bootstraps and the random forest (reproducible results)
# Characterisation set (notebook 01, section 1.3): 11 of the 15 recordings with accelerometer data, chosen so that
# every zone appears in at least two of them and in at least one of the 7 validation recordings.
CHARACTERISATION_RECORDINGS = [f"20251019-{h}.wav" for h in (
    "140152", "140412", "140629", "141757", "142014", "143811", "144311", "150207", "150644", "151007", "151407")]
N_MFCC = 13
ZONE_FEATURES = [   # zone-mean features (Mantel test, notebook 04)
    "mfcc_0_mean", "mfcc_1_mean", "mfcc_2_mean", "mfcc_3_mean",
    "spectral_centroid_mean", "spectral_centroid_std",
    "spectral_bandwidth_mean", "spectral_bandwidth_std",
]
RF_FEATURES = ["spectral_centroid", "spectral_bandwidth"] + [f"mfcc_{i}" for i in range(N_MFCC)]
