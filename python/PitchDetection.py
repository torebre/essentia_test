import matplotlib.pyplot as plt

import essentia.standard as ess
import numpy as np

M = 1024
N = 1024
H = 512
fs = 44100

x = ess.MonoLoader(filename='output3.wav', sampleRate=fs)()
ess.AudioLoader()

spectrum = ess.Spectrum(size=N)
window = ess.Windowing(size=M, type='hann')

pitchYin = ess.PitchYin()


hpcp = ess.HPCP()
hpcps = []

spectralPeaks = ess.SpectralPeaks()
pitches = []
pitchConfidences = []



for frame in ess.FrameGenerator(x, frameSize=M, hopSize=H, startFromZero=True):
    pitch, pitchConfidence = pitchYin(frame)
    if pitchConfidence < 0.9:
        pitches.append(None)
    else:
        pitches.append(pitch)

    pitchConfidences.append(pitchConfidence)

    mX = spectrum(window(frame))
    spectralPeaks_freqs, spectralPeaks_mags = spectralPeaks(mX)
    hpcp_vals = hpcp(spectralPeaks_freqs, spectralPeaks_mags)
    hpcps.append(hpcp_vals)

pitches = np.array(pitches)
pitchConfidences = np.array(pitchConfidences)

hpcps = np.array(hpcps)

figure = plt.figure(1, figsize=(9.5, 7))

plt.subplot(4, 1, 1)
plt.plot(np.arange(x.size) / float(fs), x, 'b')
plt.axis([0, x.size / float(fs), min(x), max(x)])
plt.ylabel('amplitude')
plt.title('output2')


plt.subplot(4, 1, 2)
plt.plot(pitchConfidences)
plt.title('pitch confidences')

plt.subplot(4, 1, 3)
plt.plot(pitches)
plt.ylabel('pitch')
plt.title('PitchYin')
plt.autoscale(tight=True)
plt.tight_layout()


plt.subplot(4, 1, 4)
numFrames = int(hpcps[:, 0].size)
frmTime = H * np.arange(numFrames) / float(fs)
plt.pcolormesh(frmTime, np.arange(12), np.transpose(hpcps))
plt.ylabel('spectral bins')
plt.title('HPCP')
plt.autoscale(tight=True)



# TODO Does not work
def on_plot_hover(event):
    for curve in plt.get_lines():
        if curve.contains(event)[0]:
            print "over %s" % curve.get_gid()

figure.canvas.mpl_connect('motion_notify_event', on_plot_hover)



plt.savefig('pitch_yin.png')
plt.show()
