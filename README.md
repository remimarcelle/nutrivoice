# NutriVoice

A Python CLI tool that converts nutrition and health content into audio using the ElevenLabs API.

## What it does

You type or paste in any health or nutrition content a tip, a meal summary, a training note and NutriVoice reads it back to you as a natural sounding MP3 file. The idea came from noticing that a lot of useful nutrition content exists in text form but never gets consumed because people do not sit down to read it. Audio makes it more accessible.

## Demo

```
=== NutriVoice: Nutrition Content to Audio ===

Type or paste your content below.
Press Enter on an empty line when you are done.

Eating enough protein is one of the most important things you can do to support
muscle repair and keep you feeling full between meals.

Converting text to audio...
Audio saved to: nutrivoice_output.mp3

Done. Open nutrivoice_output.mp3 to listen to your content.
```

## Tech Stack

- Python 3.10+
- ElevenLabs Python SDK
- python-dotenv

## Setup

**1. Clone the repo**

```bash
git clone https://github.com/remimarcelle/nutrivoice.git
cd nutrivoice
```

**2. Install dependencies**

```bash
pip install elevenlabs python-dotenv
```

**3. Add your API key**

Create a `.env` file in the root of the project (use `.env.example` as a template):

```
ELEVENLABS_API_KEY=your_api_key_here
```

You can get a free API key at https://elevenlabs.io. The free tier includes 10,000 characters per month.

**4. Run the app**

```bash
python nutrivoice.py
```

## Project Structure

```
nutrivoice/
├── nutrivoice.py       # Main application
├── .env.example        # Environment variable template
├── .gitignore
└── README.md
```

## Author

Remi Marcelle Braithwaite
[GitHub](https://github.com/remimarcelle)