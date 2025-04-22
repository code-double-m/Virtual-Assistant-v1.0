# MM350: My Attempt at Building an AlterEgo

This project represents a deeply personal and experimental journey in creating a digital AlterEgo — a virtual avatar with a voice, a personality, and a presence. I called it **MM350**, and it’s more than just an animated model. It listens, it talks back, and it learns from me. It's my first meaningful step toward building a conversational agent with emotional resonance and a visual identity.

## What is MM350?

MM350 is a 3D OpenGL-based avatar built using Python and Pygame that:
- Animates facial expressions using .obj frame sequences
- Listens to spoken input via microphone
- Responds using a local corpus and TTS (text-to-speech)
- Learns from conversations and updates its knowledge base
- Levitates and idly blinks like it’s alive
- Operates in its own windowed universe with lighting and camera control

## Inspiration

The idea stemmed from wanting to build a more expressive AI assistant — not just a voice or a chatbot on a screen, but something I could see and feel. I wanted an assistant that felt alive, something I could project emotion into and feel some sort of connection with. MM350 is my take on what that first version of a digital companion might look like.

## Key Features

- **Speech Recognition**: Uses `speech_recognition` to understand what I say.
- **Voice Output**: Speaks back using `pyttsx3`, with threaded delivery to sync with animation.
- **Reactive Animation**: OBJ-based 3D animation that syncs mouth movement with speech and blinks when idle.
- **Memory and Learning**: Poorly understood responses are added to a corpus file (`custom_conversations.txt`) for future reference.
- **OpenGL Rendering**: Real-time 3D rendering using `PyOpenGL`, complete with dynamic lighting and subtle motion (levitation).

## File Structure

- `main.py`: The main execution file with all logic (MM350 class, window rendering, and main loop).
- `camera.py`: Manages camera positioning and control (assumed included).
- `objloader.py`: Loads and renders OBJ files for animations.
- `responseAdapter.py`: Handles conversational response logic, using a text corpus.
- `Corpus/`: Stores pre-defined and user-augmented conversations.
- `3Dmodels/Avatar/animations/`: Stores animation frame sequences in `.obj` format.

## How It Works

1. When launched, MM350 appears in a 3D rendered scene.
2. It starts listening in a background thread using a microphone.
3. When a voice input is detected, it’s processed and responded to via TTS.
4. During speech, a "talking" animation is played; when idle, it blinks randomly.
5. If it doesn't understand you, it asks how it *should* respond next time, learns from your correction, and saves it.

## Why I Built This

I’ve always been fascinated by digital identity, consciousness, and personality. MM350 was my attempt to bring a part of that curiosity to life. I wanted something I could talk to — not just type at — and something that could grow with me. It’s rough around the edges, but it feels like the beginning of something deeply human.

## Requirements

- Python 3.x
- `pygame`
- `speechrecognition`
- `pyttsx3`
- `PyOpenGL`
- Microphone input
- `.obj` animation files for avatar actions

## To Run

```bash
python main.py
