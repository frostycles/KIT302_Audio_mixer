from pydub import AudioSegment
import os
import random

signalDirectory = 'data/signal' # Change for new Signal file location
noiseDirectory = 'data/noise' # Leave unless new Noise files are being used
outputDirectory = 'data/mixed' # Change for new Save location

# Get a list of all the audio files in the signal directory
signalFiles = [f for f in os.listdir(signalDirectory) if f.endswith('.mp3')]
print("Signal file location.")

# Get a list of all the audio files in the noise directory
noiseFiles = [f for f in os.listdir(noiseDirectory) if f.endswith('.mp3')]
print("Noise file location.")

# Mix each signal file with a random noise file and save the output to the output directory
for signalFile in signalFiles:
    signalPath = os.path.join(signalDirectory, signalFile)
    signal = AudioSegment.from_mp3(signalPath)
    #print("Signal file found.")
    
    # Choose a random noise file
    noiseFile = random.choice(noiseFiles)
    noisePath = os.path.join(noiseDirectory, noiseFile)
    noise = AudioSegment.from_mp3(noisePath)
    #print("Noise file found.")
    
    # If the noise file is shorter than the signal file, repeat it to match the signal length
    while len(noise) < len(signal):
        noise += noise
        print("Noise not long enough.")
    
    # Choose a random starting point in the noise file
    start_time = random.randint(0, len(noise) - len(signal))
    #print("Setting random start time.")
    
    # Extract the portion of the noise file that matches the signal length
    noise_segment = noise[start_time:start_time + len(signal)]
    #print("Extracting noise.")
    
    # Mix the signal and noise segments
    mixed = signal.overlay(noise_segment)
    #print("Mixing signal and noise.")
    
    # Save the mixed file to the output directory
    outputFilePath = os.path.join(outputDirectory, f"{signalFile[:-4]}_mixed.mp3")  # Change this last part if you don't want '_mixed' at the end of the file name
    mixed.export(outputFilePath, format='mp3')
    #print("Saved.")

print("Mixing Completed.")