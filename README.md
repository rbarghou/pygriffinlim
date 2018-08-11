# pygriffinlim
A python implementation of the Griffin Lim Algorithm for audio reconstruction from magnitudes

## Overview
The Griffin Lim algorithm provides a way to approximate a waveform from a "modified STFT transform".
In practice, this means a STFT where the phase data has been lost or removed.  The Griffin Lim
Algorithm does not produce the original waveform, but rather a new waveform with a very similar
spectrogram.

Improvements on the Modified Fast Griffin Lim are still possible, as evidenced by recent work with
WaveNet.  However, in practice, the Modified Griffin Lim remains a robust, efficient and understandable
algorithm, which makes it useful in many audio pipelines.

This is an implementation of 3 different versions of the Griffin Lim algorithm.

1. The basic Griffin Lim which converges slowly
2. The Fast Griffin Lim which converges more quickly
3. The Modified Fast Griffin Lim which converges to slightly better values.