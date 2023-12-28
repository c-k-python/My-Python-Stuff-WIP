import pygame
from pygame.locals import *
import os

class AudioMixer:
    def __init__(self):
        pygame.mixer.init()

        self.tracks = []

    def load_track(self, file_path):
        if os.path.exists(file_path):
            pygame.mixer.music.load(file_path)
            self.tracks.append(file_path)
            print(f"Loaded track: {file_path}")
        else:
            print(f"Error: File not found - {file_path}")

    def play(self):
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def print_tracks(self):
        print("Loaded Tracks:")
        for track in self.tracks:
            print(track)

if __name__ == "__main__":
    mixer = AudioMixer()

    while True:
        print("\nOptions:")
        print("1. Load Track")
        print("2. Play")
        print("3. Stop")
        print("4. Set Volume")
        print("5. Print Loaded Tracks")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            track_path = input("Enter the path of the audio track: ")
            mixer.load_track(track_path)

        elif choice == "2":
            mixer.play()

        elif choice == "3":
            mixer.stop()

        elif choice == "4":
            volume = float(input("Enter the volume (0.0 to 1.0): "))
            mixer.set_volume(volume)

        elif choice == "5":
            mixer.print_tracks()

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please enter a valid option.")
