# THE CASE FILES

A Python + Tkinter murder mystery investigation game.

## Run

Python 3.13+ recommended.

```bash
python main.py
```

No third-party Python packages are required.

## Player progress

Player progress is intentionally **not stored inside this project folder**. `save_manager.py` stores each player's save in their own operating-system application-data directory.

This means the Git repository stays clean and every new player starts with zero solved cases. A player who closes and reopens the game on the same computer keeps their own progress.

Do not commit a `progress.json` file to GitHub.

## Reset progress

To reset the local player's progress, run:

```python
import save_manager
save_manager.reset_progress()
```

or delete the `progress.json` located at the path printed by:

```python
import save_manager
print(save_manager.get_save_file_path())
```

## Project files

- `main.py` — game interface and flow
- `cases.py` — case content
- `save_manager.py` — player-local save system
- `.gitignore` — keeps local/generated files out of Git
