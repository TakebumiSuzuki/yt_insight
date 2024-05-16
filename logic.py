import constants as K
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import google.generativeai as genai

load_dotenv()

# YouTube Data APIのサービスオブジェクトを構築
youtube = build(
    'youtube',
    'v3',
    developerKey = os.getenv(K.YOUTUBE_API_KEY)
)


def extract_handle(url):
    # 'youtube.com/'が存在するかを確認
    youtube_index = url.find('youtube.com/')
    if youtube_index != -1:
        url = url[youtube_index + len('youtube.com/'):] # 'youtube.com/'から左側を削除

    # 最初の'/'から右側を削除
    slash_index = url.find('/')
    if slash_index != -1:
        url = url[:slash_index]

    return url


def get_channel_id(handle):
    # ハンドルからチャンネルを検索。qパラメータは、検索クエリを指定するために使用されます。
    # つまり、qパラメータには、検索したいキーワードやフレーズを指定。
    response = youtube.search().list(
        part = 'snippet',
        q = handle,
        type = 'channel',
        maxResults = 1
    ).execute()

    # 検索結果からチャンネルIDを取得
    if 'items' in response and len(response['items']) > 0:
        channel_id = response['items'][0]['snippet']['channelId']
        return channel_id
    else:
        return None


def get_top_videos(channel_id, max_results):
    one_year_ago = (datetime.now() - timedelta(days=365)).isoformat("T") + "Z"

    # search.listを使って、過去一年間の動画をviewCount順に取得
    response = youtube.search().list(
        part = 'snippet',
        channelId = channel_id,
        maxResults = max_results,
        order = 'viewCount',
        publishedAfter = one_year_ago,
        type = 'video'
    ).execute()

    title_list = []
    for item in response['items']:
        title = item['snippet']['title']
        # video_id = item['id']['videoId']
        title_list.append(title)

    return title_list


# def get_top_shorts_videos(channel_id, max_results=7):
#     one_year_ago = (datetime.now() - timedelta(days=365)).isoformat("T") + "Z"

#     # search.listを使って、再生回数順に#shortsタグが付いた動画を取得
#     response = youtube.search().list(
#         part='snippet',
#         channelId=channel_id,
#         maxResults=max_results,  # 上位 max_results の結果を取得
#         order='viewCount',
#         q='#shorts',
#         publishedAfter=one_year_ago,
#         type='video'
#     ).execute()


def ask_youtube(url):
    handle = extract_handle(url)
    if handle is None:
        return 'handle is not included in the url'

    channel_id = get_channel_id(handle)
    if channel_id is None:
        return 'Channel id was not found'

    top_video_list = get_top_videos(channel_id, K.MAX_TOP_VIDEOS)
    print(top_video_list)
    return top_video_list


# def ask_llm(top_video_list):
#     prompt = K.PROMPT_TEMPLATE + top_video_list
#     response = model.generate_content(prompt)
#     return response.text

def ask_llm(top_video_list):
    genai.configure(
        api_key = os.getenv(K.GEMINI_API_KEY)
    )

    model = genai.GenerativeModel(
        model_name = K.GEMINI_MODEL_NAME
    )
    chat_model = model.start_chat(history = [])

    prompt = K.PROMPT_TEMPLATE + top_video_list
    print(prompt)
    return chat_model.send_message(prompt, stream = True)



