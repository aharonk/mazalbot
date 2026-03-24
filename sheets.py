import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

SHEET_ID = "1K4Os4DP4WWF_PsGPcbbIQDMP3tCLl1PhdGBaN4sgwGc"
RANGE = "Sheet1!C2:E"

ERROR_CHANNEL = "938127502327570433"

def get_data():
    creds = get_credentials()

    if creds is None:
        send_error("No Credentials.")
        return None

    try:
        service = build("sheets", "v4", credentials=creds)

        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SHEET_ID, range=RANGE)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            send_error("No data found.")
            return None

        return values
    except HttpError as err:
        send_error(err)
        return None


def get_credentials():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return creds

def send_error(msg):
    print("MazalBot Error:\n```\n" + msg + "\n```")