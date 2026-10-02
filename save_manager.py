"""THE CASE FILES - player-local save manager."""
import json
import os
import sys
from pathlib import Path

APP_NAME = "TheCaseFiles"


def get_save_directory():
    if sys.platform.startswith("win"):
        base = os.environ.get("LOCALAPPDATA") or (Path.home() / "AppData" / "Local")
        path = Path(base) / APP_NAME
    elif sys.platform == "darwin":
        path = Path.home() / "Library" / "Application Support" / APP_NAME
    else:
        base = os.environ.get("XDG_DATA_HOME") or (Path.home() / ".local" / "share")
        path = Path(base) / APP_NAME
    path.mkdir(parents=True, exist_ok=True)
    return path


SAVE_DIRECTORY = get_save_directory()
SAVE_FILE = SAVE_DIRECTORY / "progress.json"

DEFAULT_DATA = {
    "solved_cases": [],
    "total_solved": 0,
    "wrong_attempts": 0,
    "hints_used": 0,
    "rank_title": "NOVICE INVESTIGATOR",
}

RANKS = [
    (0, "NOVICE INVESTIGATOR"),
    (2, "JUNIOR DETECTIVE"),
    (5, "CRIME SCENE INSPECTOR"),
    (9, "SPECIAL ENQUIRY DETECTIVE"),
    (13, "CHIEF INVESTIGATOR"),
    (16, "MASTER DETECTIVE"),
]


def get_rank(solved_count):
    current = RANKS[0][1]
    for count, title in RANKS:
        if solved_count >= count:
            current = title
        else:
            break
    return current


def _fresh_data():
    return DEFAULT_DATA.copy()


def save_progress(data):
    try:
        SAVE_DIRECTORY.mkdir(parents=True, exist_ok=True)
        temp = SAVE_FILE.with_suffix(".tmp")
        with open(temp, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        os.replace(temp, SAVE_FILE)
    except OSError as error:
        print(f"[SAVE ERROR] Could not save progress: {error}")


def create_default_progress():
    data = _fresh_data()
    save_progress(data)
    return data


def load_progress():
    if not SAVE_FILE.exists():
        return create_default_progress()
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("Invalid save data")
        for key, value in DEFAULT_DATA.items():
            data.setdefault(key, value)
        if not isinstance(data.get("solved_cases"), list):
            data["solved_cases"] = []
        data["total_solved"] = len(data["solved_cases"])
        data["rank_title"] = get_rank(data["total_solved"])
        return data
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        return create_default_progress()


def mark_case_solved(case_id):
    data = load_progress()
    if case_id not in data["solved_cases"]:
        data["solved_cases"].append(case_id)
        data["total_solved"] = len(data["solved_cases"])
        data["rank_title"] = get_rank(data["total_solved"])
        save_progress(data)
    return data


def record_wrong_attempt():
    data = load_progress()
    data["wrong_attempts"] = data.get("wrong_attempts", 0) + 1
    save_progress(data)
    return data


def record_hint_used():
    data = load_progress()
    data["hints_used"] = data.get("hints_used", 0) + 1
    save_progress(data)
    return data


def reset_progress():
    data = _fresh_data()
    save_progress(data)
    return data


def get_save_file_path():
    return str(SAVE_FILE)
