# Pulling Dataviews from Flywheel

Demonstrates how to retrieve data from the NACC Data Platform using a Flywheel dataview.

A Flywheel dataview is tabular data built from data stored within Flywheel.
The system allows us to define a dataview and publish it so that it can be applied in different contexts to extract data.

So, for instance, to make participant identifer information available, we created a dataview with the label `center-participant-identifiers` in the `nacc/metadata` project that will extract all of the identifier data attached to participants ("subjects" in Flywheel).

This repository shows how to pull this data using Python.
R user see below.

## Reporting issues

If you run into a problem with the demo, please see the [issues page](https://github.com/naccdata/flywheel-dataview-demo/issues) of this repository and either chime in on an existing issue or [create a new one](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue).

## Setting up demo environment

> The instructions assume a Unix/Linux environment.

You will need to run this demo within an environment with Python installed.
The repository is configured with a Python VSCode devcontainer that could be used.

Start by [cloning this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to your computer using Git.

## API key

You will need an API Key from the Flywheel system of the NACC Data Platform.

### Finding your API key

Each API key is associated with a particular user.
To get the API key, login as the user to the NACC Flywheel instance.

1. Find the "avatar" in the upper right corner (generally a circle with your initials).
2. Click the avatar dropdown, and select "Profile".
3. Under "Flywheel Access" at the bottom of the resulting page, click "Generate API Key".
4. Choose a key name relevant to upload, set the expiration date, and create the API Key.
5. Copy the API Key since you wont be able to access the value later.
6. Keep the key secret  

## Storing your API key

For this particular demo, we are storing the API key in a `.env` file.

>Note: The `.gitignore` is set to ignore this file, which helps prevent the key value from being checked into the repository.
> Take care to protect your key like any other secret in your work environment.
> A deployment should use more robust secret management to ensure the secret is not easily accessible.

Run the command 

```bash
touch .env
```

and then edit the file to add your key in a line like

```bash
FW_API_KEY=<the value of the API key>
```

The Python demo script uses the `dotenv` package to load environment variables from the `.env` file.

> The `.env` file is included in the `.gitignore` file intentionally to prevent inclusion of the API token in a Git repository.

## Python demo

Start by installing dependencies by running `pip install`.

> Be cautious here.
> Running `pip install` can polute your global Python environment and mess things up. 
> You should either be using a virtual environment, or running in a docker container like the VSCode devcontainer.
> We are running this in the VSCode devcontainer, so buyer beware...

```bash
pip install -r requirements.txt
```

The demo script is `demo/src/python/pull_dataview.py`

You will need to set the line

```python
source_project = client.lookup("sample-center/ingest-enrollment")
```

This value can be handled in a similar way to the form-upload-demo, which has code for creating this string.
While we are working out details to help you with this, if anything is unclear please just reach out to the NACC tech team via Discourse.

## Options for getting data

The Flywheel Python SDK provides three ways to pull data using a dataview:

1. get the data as JSON
2. write the data to a file
3. get the data as a Pandas dataframe

The demo only shows the first two.

See the Flywheel [Data Views](https://flywheel-io.gitlab.io/product/backend/sdk/tags/18.3.0/python/data_views.html#) documentation for more details.

## R guidance

We don't yet have an R demo built out, but we expect it will follow the form-upload-demo example closely.
An R version of t
You can use the [reticulate](https://rstudio.github.io/reticulate/) package to use the Flywheel Python SDK within R.

## Need help?

If anything is unclear, please feel free to ask the NACC Tech Team questions via Discourse or the `nacchelp` email address.