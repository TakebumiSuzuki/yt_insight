
YOUTUBE_API_KEY = 'YOUTUBE_API_KEY'
GEMINI_API_KEY = 'GEMINI_API_KEY'
GEMINI_MODEL_NAME = 'models/gemini-1.5-pro-latest'

MAX_TOP_VIDEOS = 7

PROMPT_TEMPLATE = """You are an expert YouTube content consultant. Below is a list of the most viewed videos from a specific channel over the past year. Based on this list, please generate 10 sets of video topic ideas with some title ideas for each idea, in the same language as the provided list, that are likely to attract a large audience for this channel in the future.
1. Always start with the following line: "### **10 Sets of YouTube Video Ideas Based on Your Popular Videos:**\n"
2. For all the rest, you have to write your topic ideas and title ideas in exactly the same language as the provided list.
Here is the list of videos:
"""


CSS = """
    <style>
        .stChat {
            width: 90% !important;  /* チャットウィジェットの幅を調整 */
        }
        header {visibility: hidden;}
        div[class^='block-container'] { padding-top: 2rem; }
        h1 {
        text-align: center;
        }
    </style>
    """

SAFETY_SETTINGS = [
    {
        "category": "HARM_CATEGORY_DANGEROUS",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

GENERATION_CONFIG = {
    "temperature" : 0.7,
}