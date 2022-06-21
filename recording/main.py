import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording_float = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
print(myrecording_float)
print("rows: {}".format(len(myrecording_float)))
print("colums: {}".format(len(myrecording_float[0])))

a = np.asarray(myrecording_float)
np.savetxt("recording/myrec_float.csv", a, delimiter=",")

write('recording/output.wav', fs, myrecording_float)  # Save as WAV file

myrecording_int = myrecording_float.astype(np.int16)
print(myrecording_int)
print("rows: {}".format(len(myrecording_int)))
print("colums: {}".format(len(myrecording_int[0])))

a = np.asarray(myrecording_int)
np.savetxt("recording/myrec_int.csv", a, delimiter=",")

myrecording_int_01 = np.int_(myrecording_float)
print(myrecording_int_01)
print("rows: {}".format(len(myrecording_int_01)))
print("colums: {}".format(len(myrecording_int_01[0])))

a = np.asarray(myrecording_int_01)
np.savetxt("recording/myrec_int_01.csv", a, delimiter=",")

myrecording_int_02 = []
for float in myrecording_float:
    myrecording_int_02.append(float.astype(np.int16))

print(myrecording_int_02)
print("rows: {}".format(len(myrecording_int_02)))
print("colums: {}".format(len(myrecording_int_02[0])))

a = np.asarray(myrecording_int_02)
np.savetxt("recording/myrec_int_02.csv", a, delimiter=",")