# StereoSense HUD

**StereoSense HUD** is a lightweight on-screen overlay that visualizes **stereo audio balance** and **directional confidence** in real time.  
It is designed for gaming scenarios (e.g. FPS shooters) where understanding *left vs right sound bias* can help situational awareness — without pretending to know exact enemy positions.

> ⚠️ This is **not** a true audio radar. It visualizes stereo output characteristics only.

---

## ✨ Features

### 🎚 Left & Right Level Bars
- Always-on-top vertical bars on the **left and right edges** of the screen
- Show real-time **audio energy per channel**
- Useful for quickly identifying which side sound is leaning toward

### 🧭 Pan Indicator (Top-Center)
- Semicircle “radar-style” HUD
- Needle shows **left/right stereo bias**, not absolute direction
- **Confidence-based scaling**:
  - Fades or shrinks for centered sounds (your own footsteps, UI, music)
  - More prominent for clearly lateral sounds

### 🧠 Confidence Awareness
- Uses **stereo correlation** to estimate whether directional cues are reliable
- Prevents misleading indicators during:
  - Player movement
  - Ambient sounds
  - Center-mixed audio

### ⚡ Lightweight & Non-Intrusive
- Python-based
- No game hooks or memory access
- Works via **system audio loopback**
- Safe for offline use and experimentation

---

## 📸 Screenshots

> _(Screenshots / GIFs coming soon)_

Suggested captures:
- Idle (no sound)
- Enemy footsteps clearly on left
- Centered sound suppressed in radar
- Combined bars + radar during gameplay

---

## 🔧 How It Works (High Level)

StereoSense HUD analyzes the **final stereo mix** sent to your audio device:

- **L/R bars**: RMS energy per channel
- **Pan needle**: Interaural Level Difference (ILD)
- **Confidence**: Stereo correlation (high correlation = centered sound)

This reflects *what reaches your ears*, not in-game world coordinates.

---

## ❗ Disclaimer (Important)

StereoSense HUD **does NOT**:
- Track enemies
- Read game memory
- Know front/back or vertical position
- Provide exact angles or distances

It **only visualizes stereo audio output**.

### Limitations
- Your own footsteps and actions are usually mixed **dead center**
- Multiple simultaneous sounds can interfere
- HRTF and audio compression can distort simple left/right metrics

This tool is intended as a **situational aid**, not a replacement for spatial hearing.

---

## ⚖️ Fair Play & Ethics

- No game data is accessed
- No hooks, injections, or network activity
- Uses OS-level audio capture only

**Always follow the terms of service of the games you play.**

---

## 🛠 Tech Stack

- Python
- `soundcard` (system audio loopback)
- `numpy`
- `tkinter`

---

## 🚀 Future Ideas

- Optional frequency-band focus (e.g. footsteps)
- Peak-hold visualization
- Calibration mode for channel bias
- Click-through overlay mode
- Packaged Windows executable

---

## 📄 License

MIT License (or choose one before publishing)
