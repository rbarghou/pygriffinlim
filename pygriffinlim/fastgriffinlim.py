import librosa
import numpy as np

from .settings import DEFAULT_STFT_KWARGS


def fast_griffin_lim_generator(
        spectrogram,
        iterations=10,
        approximated_signal=None,
        alpha=.1,
        stft_kwargs=DEFAULT_STFT_KWARGS):
    _M = spectrogram
    for k in range(iterations):
        if approximated_signal is None:
            _P = np.random.randn(*_M.shape)
        else:
            _D = librosa.stft(approximated_signal, **stft_kwargs)
            _P = np.angle(_D)

        _D = _M * np.exp(1j * _P)
        _M = spectrogram + (alpha * np.abs(_D))
        approximated_signal = librosa.istft(_D, **stft_kwargs)
        yield approximated_signal


def fgla(spectrogram,
         iterations=10,
         approximated_signal=None,
         alpha=.1,
         stft_kwargs=DEFAULT_STFT_KWARGS):
    generator = fast_griffin_lim_generator(spectrogram, iterations, approximated_signal, alpha, stft_kwargs)
    for approximated_signal in generator:
        pass
    return approximated_signal
