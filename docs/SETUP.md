# Setup Guide

## Prerequisites

### Required Software

(See [the brief installation guide video](https://drive.google.com/file/d/11_yJP0YBUW8Pn0Rp5z4C88p87Da7taG9/view?usp=sharing).)

For this class, you will need [Python](https://www.python.org/downloads/), [VSCode](https://code.visualstudio.com/download), [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [`uv`](https://docs.astral.sh/uv/), [`ruff`](https://docs.astral.sh/ruff/), and the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install). Prior to proceeding to the setup instructions, make sure you have all of these installed for your OS (see the hyperlinks to the setup instructions).

All of this should take no more than 15-20 minutes, assuming you have none of the software installed. (Python and Git ship by default on all computers running macOS or Linux.)

#### For Windows Users

For Windows users, installation will be a little more challenging. Specifically, I find Python installations annoying because Python isn't automatically added to your system path. To add it, try the following (you may have to change the precise path to your Python installation, and you might need to consult with online references and/or ChatGPT). Run this in PowerShell:

```
# Get the latest Python version installed
$pythonVersion = (Get-ChildItem "$env:USERPROFILE\AppData\Local\Programs\Python" -Directory | Sort-Object Name -Descending | Select-Object -First 1).Name
$pythonPath = "$env:USERPROFILE\AppData\Local\Programs\Python\$pythonVersion"
[System.Environment]::SetEnvironmentVariable('PATH', $env:PATH + ";" + $pythonPath + ";" + $pythonPath + "\Scripts", "User")
```

### Google Cloud Account

We will use Google Earth Engine at different points in this course. In order to do so, please [follow these instructions](https://towardsai.net/p/machine-learning/how-to-set-up-a-google-earth-engine-cloud-project) to make sure you have a Google Cloud account set up for use with Google Earth Engine.

## Setup Instructions

Once you have installed the required software and set up your Google Cloud account, [fork this repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo). Then, open a git terminal and clone your fork to your desired location. Once done, use `uv` to install all project dependencies into a virtual environment:

```
git clone <this-repo-path>
cd musa-650-spring-2025
uv sync
```

Finally, run `uv run earthengine authenticate` to set up Google Earth Engine access (see these instructions for more information).

_It is likely that you will run into issues here; please troubleshoot as a class in person or on the discussion board on GitHub so we can solve problems collectively._

Congrats! You're ready to go. :)
