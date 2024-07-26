# Setting Up the Paid Version (Google Cloud Speech-to-Text API)

Follow these steps to set up and use the paid version of the Audio-To-Text Transcription Tool:

1. Create a Google Cloud account:
   - Go to https://cloud.google.com/
   - Click on "Get started for free" or "Sign in" if you already have an account.
   - Follow the prompts to create a new account if needed.

2. Create a new project:
   - Once logged in, go to the Google Cloud Console (https://console.cloud.google.com/)
   - Click on the project dropdown at the top of the page.
   - Click "New Project" and give it a name (e.g., "Audio-To-Text-Transcription").
   - Click "Create".

3. Enable the Speech-to-Text API:
   - In the Google Cloud Console, use the search bar at the top to search for "Speech-to-Text API".
   - Click on "Speech-to-Text API" in the results.
   - Click the "Enable" button.

4. Create a service account and generate a key:
   - In the Google Cloud Console, go to "IAM & Admin" > "Service Accounts" from the navigation menu.
   - Click "Create Service Account" at the top of the page.
   - Enter a name for the service account (e.g., "audio-transcription-sa").
   - Click "Create and Continue".
   - For the role, you can select "Project" > "Owner" for full access, or "Cloud Speech Admin" for more restricted access.
   - Click "Continue" and then "Done".
   - Find your newly created service account in the list and click on it.
   - Go to the "Keys" tab.
   - Click "Add Key" > "Create new key".
   - Choose "JSON" as the key type and click "Create".
   - The JSON key file will be downloaded to your computer. Keep this file secure, as it contains sensitive information.

5. Set up Google Cloud SDK:
   - Install the Google Cloud SDK if you haven't already: https://cloud.google.com/sdk/docs/install
   - Open a terminal and run:
     ```
     gcloud auth application-default login
     ```
   - This command will open a browser window where you can log in to your Google account and authorize the SDK to access your Google Cloud resources.
   - After successful authentication, the credentials will be saved on your local machine, and your PATH will be updated.

6. Install the Google Cloud client library:
   - If you haven't already, install the Google Cloud client library for Python:
     ```
     pip install google-cloud-speech
     ```

7. Test the paid version:
   - Run your `main.py` script:
     ```
     python main.py
     ```
   - Choose option 2 for the paid version when prompted.
   - Provide the path to a longer audio file for transcription.

Remember to monitor your usage in the Google Cloud Console, as there may be costs associated with using the Speech-to-Text API beyond the free tier.

If you encounter any issues during setup or usage, please refer to the Google Cloud documentation or open an issue in this repository for assistance.




                                                                                                                                                 │
