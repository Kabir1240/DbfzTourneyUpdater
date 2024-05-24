from google.oauth2 import service_account
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os.path

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents']

# The ID of the Google Doc you want to update
DOCUMENT_ID = '1MzH4hoyyOq-lQf4sjPSWQBa8XFeV6wPiFwnbv4EsYKs'

def authenticate():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is created
    # automatically when the authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def clear_document(service, document_id):
    # Retrieve the document to get the current content length
    document = service.documents().get(documentId=document_id).execute()
    doc_content_length = document.get('body').get('content')[-1]['endIndex']

    # If the document has content, delete it
    if doc_content_length > 2:
        requests = [
            {
                'deleteContentRange': {
                    'range': {
                        'startIndex': 1,
                        'endIndex': doc_content_length - 1
                    }
                }
            }
        ]
        result = service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
        print(f"Cleared document content. Update result: {result}")
    else:
        print("Document is already empty.")


def update_document(service, document_id, message):
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': f'{message}'
            }
        }
    ]
    result = service.documents().batchUpdate(
        documentId=document_id, body={'requests': requests}).execute()
    print(f'Updated the document: {result}')

def upload_doc(message):
    creds = authenticate()
    service = build('docs', 'v1', credentials=creds)

    # clear doc
    clear_document(service, DOCUMENT_ID)

    # Update the document
    update_document(service, DOCUMENT_ID, message)

