import argparse

from imageio import imread

from librosa.output import write_wav

from . import gla, fgla


parser = argparse.ArgumentParser(
    description="Welcome to PyGriffinLim.  Reconstruct audio from spectrogram data in image formats."
)
parser.add_argument(
    "-i",
    dest="input_file",
    required=True,
    help="Input file of image."
)
parser.add_argument(
    "-o",
    dest="output_file",
    required=True,
    help="Output wav file."
)
parser.add_argument(
    "-a",
    dest="algorithm",
    required=False,
    help="Algorithm chosen choices: gla, fgla, fgla.",
    default="fgla"
)
parser.add_argument(
    "-n",
    dest="n_iterations",
    required=False,
    type=int,
    help="Number of iterations.",
    default=20
)
parser.add_argument(
    "--hop_length",
    dest="hop_length",
    required=False,
    type=int,
    help="The hop length between frames, measured in samples, usually n_fft / 2.",
    default=512
)
parser.add_argument(
    "--n_fft",
    dest="n_fft",
    required=False,
    type=int,
    help="The width of the frame in samples.",
    default=2048
)
parser.add_argument(
    "--sample_rate",
    dest="sample_rate",
    required=False,
    type=int,
    help="The samplerate of the output file.",
    default=22050
)


def main():
    args = parser.parse_args()
    spectrogram_im = imread(args.input_file)
    algo = {
        "gla": gla,
        "fgla": fgla
    }[args.algorithm]
    signal = algo(
        spectrogram_im,
        args.n_iterations,
        stft_kwargs={
            "n_fft": args.n_fft,
            "hop_length": args.hop_length
        },
        istft_kwargs={
            "hop_length": args.hop_length
        },
    )
    write_wav(args.output_file, signal, args.sample_rate)
