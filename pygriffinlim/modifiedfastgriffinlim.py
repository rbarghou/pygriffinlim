import librosa
import numpy as np


def modified_fast_griffin_lim_generator(
        spectrogram,
        iterations,
        approximated_signal=None,
        alpha_loc=.1,
        alpha_scale=.4,
        stft_kwargs={},
        istft_kwargs={}):
    """

    :param spectrogram:
    :param iterations:
    :param approximated_signal:
    :param alpha_loc:
    :param alpha_scale:
    :param stft_kwargs:
    :param istft_kwargs:
    :return:
    """
    _M = spectrogram
    for k in range(iterations):
        if approximated_signal is None:
            _P = np.random.randn(*_M.shape)
        else:
            _D = librosa.stft(approximated_signal, **stft_kwargs)
            _P = np.angle(_D)

        _D = _M * np.exp(1j * _P)
        alpha = np.random.normal(alpha_loc, alpha_scale)
        _M = spectrogram + (alpha * np.abs(_D))
        approximated_signal = librosa.istft(_D, **istft_kwargs)
        yield approximated_signal


def mfgla(
        spectrogram,
        iterations,
        approximated_signal=None,
        alpha_loc=.1,
        alpha_scale=.4,
        stft_kwargs={},
        istft_kwargs={}):
    """

    :param spectrogram:
    :param iterations:
    :param approximated_signal:
    :param alpha_loc:
    :param alpha_scale:
    :param stft_kwargs:
    :param istft_kwargs:
    :return:
    """
    generator = modified_fast_griffin_lim_generator(
        spectrogram, iterations, approximated_signal, alpha_loc, alpha_scale, stft_kwargs, istft_kwargs)
    for approximated_signal in generator:
        pass
    return approximated_signal
