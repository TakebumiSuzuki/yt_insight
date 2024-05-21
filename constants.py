
YOUTUBE_API_KEY = 'YOUTUBE_API_KEY'
GEMINI_API_KEY = 'GEMINI_API_KEY'
GEMINI_MODEL_NAME = 'models/gemini-1.5-pro-latest'

MAX_TOP_VIDEOS = 7

PROMPT_TEMPLATE = """You are an expert YouTube content consultant. Below is a list of the most viewed videos from a specific channel over the past year. Based on this list, please generate 10 sets of video title ideas that are likely to attract a large audience for this channel in the future. Please write your suggestions in the same language as the provided list.
Here is the list of videos:"""


CSS = """
    <style>
        header {visibility: hidden;}
        div[class^='block-container'] { padding-top: 2rem; }
        h1 {
        text-align: center;
        }
    </style>
    """