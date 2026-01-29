import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDS_FILE = os.path.join(BASE_DIR, "config", "google_credentials.json")

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

def save_student_to_google_sheet(data: dict):
    """
    Saves registration details to Google Sheet.
    data: dict with keys ['name', 'email', 'phone', 'course']
    """
    creds = Credentials.from_service_account_file(
        CREDS_FILE,
        scopes=SCOPES
    )
    client = gspread.authorize(creds)

    # Open sheet by name
    sheet = client.open("Academy Registrations").sheet1

    sheet.append_row([
        data.get("name"),
        data.get("email"),
        data.get("phone"),
        data.get("course"),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ])

    print("✅ Data saved to Google Sheet")
