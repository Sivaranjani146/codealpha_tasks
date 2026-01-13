from music21 import note, stream
import random

# Create a music stream
music_stream = stream.Stream()

# List of musical notes
notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']

# Generate random music notes
for i in range(30):
    n = note.Note(random.choice(notes))
    n.duration.quarterLength = random.choice([0.25, 0.5, 1])
    music_stream.append(n)

# Save as MIDI file
music_stream.write('midi', 'output.mid')

print("Music generated successfully! File saved as output.mid")
