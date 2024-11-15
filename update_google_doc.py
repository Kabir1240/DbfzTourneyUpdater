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
    """
    Authenticates Google credentials from credentials.json. Requires a one-time login to Google.
    Automatically refreshes the token if expired and creates/updates token.json to store authentication details.

    :return: credentials
    """
    creds = None
    # Check if token.json exists to load access and refresh tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If no (valid) credentials are available, or if they need to be refreshed
    if not creds or not creds.valid:
        # If credentials have expired but there's a refresh token, refresh the access token
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # If no valid credentials or refresh token exists, initiate the login flow
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save or update the credentials in token.json for future sessions
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())
    
    return creds


def clear_document(service, document_id:str) -> None:
    """
    clears google document completely
    :param service: resource for interacting with google docs API
    :param document_id: document id str
    :return: None
    """

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


def update_document(service, document_id:str, message:str) -> None:
    """
    writes a message to a google doc
    :param service:  Resource for interacting with an API
    :param document_id: document id
    :param message: message to write to document
    :return: None
    """

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


def upload_doc(message:str, clear:bool=True) -> None:
    """
    Clears google doc and writes a message to it.
    :param message: message to write
    :param clear: set to True if you want to clear the document before uploading. True by default.
    :return: None
    """

    # authenticate credentials
    creds = authenticate()
    service = build('docs', 'v1', credentials=creds)

    if clear:
        # clear doc
        clear_document(service, DOCUMENT_ID)

    # Update the document
    update_document(service, DOCUMENT_ID, message)
