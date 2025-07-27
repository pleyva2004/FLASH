# FLASH
This project is focused on low-latency response assistant. FLASH  – Fast Listening and Speech Handler


## Run Instructions

### Prerequisites
- Python 3.12 or higher
- pip (Python package installer)

### Setup and Installation

1. **Install Poetry** (if not already installed):
   ```bash
   pip install poetry
   ```

2. **Install project dependencies**:
   ```bash
   poetry install
   ```

3. **Activate the Poetry virtual environment**:
   ```bash
   poetry shell
   ```

4. **Run the main application**:
   ```bash
   python main.py
   ```

### Alternative: Run without activating shell
If you prefer not to activate the shell, you can run the application directly:
```bash
python main.py
```

### Notes
- The `poetry.lock` file is already present, so `poetry install` will use the exact versions specified
- Make sure you have the required system dependencies for audio processing (sounddevice, soundfile)


