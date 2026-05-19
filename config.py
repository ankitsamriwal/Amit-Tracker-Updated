import os

# All files (Excel + HTML) are in the same folder as this script (repo root)
BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = BASE_DIR

TRACKER_FILES = {
    "Niyas":                "Niyas Tracker 2026 Format v2.xlsx",
    "Charlotte":            "Tracker 2026 - Charlotte_updated.xlsx",
    "Amit Gandhi":          "Tracker 2026 Format v2 (Amit Gandhi).xlsx",
    "Mitesh Sheth":         "Tracker 2026 Format v23Jan2026 (Mitesh Sheth)_updated.xlsx",
    "Mohammed Azharudheen": "Tracker_2026 Format v2_Azhar.xlsx",
}

USERS = {
    "admin": "AlphaData@2026",
    "mgmt":  "Review@2026",
}

SECRET_KEY = "aD!x9Kp2mZ$vQ7nL"
HOST  = "0.0.0.0"
PORT  = 5000
DEBUG = False
