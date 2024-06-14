import json
import logging
import os
import sys

from flywheel import Client
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger('__main__')

def main():
    # 0. Loading api key from the .env file
    load_dotenv()

    # 1. The Flywheel SDK uses a Client object to interact with Flywheel.
    #    First get the API key from the environment variable FW_API_KEY
    if 'FW_API_KEY' not in os.environ:
        log.error("environment variable FW_API_KEY not found")
        sys.exit(1)

    # 2. Create the Client object using the API key.
    #    The key determines which instance you are using.
    client = Client(os.environ['FW_API_KEY'])
    if not client:
        log.error("not connected to Flywheel")
        sys.exit(1)

    # 3. NACC has published dataviews for center use in the nacc/metadata
    #    project. Get the project to start.
    metadata_project = client.lookup("nacc/metadata")

    # 4. You can see the list of available dataviews using
    for view in client.get_views(metadata_project.id):
        print(f"label: {view.label} description:\t{view.description}")
    
    # 5. We need the dataview ID. You can do one of the following:
    #    a. use the label you want and call get_views again
    views = client.get_views(metadata_project.id, filter='label=center-participant-identifers')
    view_id = views[0].id

    #    b. change the print command above to include `view.id` and copy it by hand
    #       e.g., `view_id = '666c673ec85af74e67f985e`

    # 6. You now need to know the Flywheel group and project the data is coming from.
    #    This is a detail covered in the form-upload-demo.
    #    The following uses the NACC Sample Center we use for testing and needs
    #    to be changed for your situation
    source_project = client.lookup("sample-center/ingest-enrollment")

    # 6. To get the data as JSON in the variable `data_extract`
    with client.read_view_data(view_id, source_project.id) as response:
        data_extract = json.load(response) 

    # 7. Alternatively, to save to a CSV file
    client.save_view_data(view_id, source_project.id, 'sample-center-identifiers.csv', format='csv')

if __name__ == "__main__":
    main()