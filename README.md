# Python Signal Graphs - Installation & Usage Guide

This project contains two Python files:
- `task1.py`: Basic signal generation and plotting
- `task2.py`: DTMF keypad and signal generation (modern GUI)

## Requirements

The following Python packages must be installed:
- numpy (for numerical operations and signal generation)
- matplotlib (for plotting graphs)
- sounddevice (only for `task2.py`, for audio playback)
- pillow (only for `task2.py`, for logo/image support in GUI)

## Installation

1. **Python 3.8+** must be installed. [Download Python](https://www.python.org/downloads/)
2. Open a terminal or PowerShell in the project folder.
3. Run the following command to install the required packages:

```
pip install numpy matplotlib sounddevice pillow
```

## Usage

### 1. Signal Graphs (`task1.py`)

```
python task1.py
```

- Displays the graphs of three different signals and their sum.

### 2. DTMF Keypad Application (`task2.py`)

```
python task2.py
```

- Opens a modern DTMF keypad GUI.
- You can click the keys to hear the corresponding DTMF signal and see its graph.
- The application uses the `istun_logo_red.png` file for the window icon and header. Make sure this file is present in the project folder.

## Notes
- `sounddevice` may require additional drivers on some systems. If you encounter issues, see the [sounddevice docs](https://python-sounddevice.readthedocs.io/).
- If the logo does not appear in the GUI, ensure Pillow is installed and the logo file name is correct.
