import streamlit as st
import yt_dlp

st.title("動画保存サイト")
"YouTubeやTwitter、ニコニコ動画やInstagram上にある動画を保存できます。"

URL_movie = st.text_input("ここに保存したい動画のURLを入力してください。")
"""
```Python
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL_movie])
```
"""


ydl_opts = {"format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    data = ydl.download([URL_movie])

#st.download_button(label = "ダウンロード", data = data)
if data == 0:
    f"ダウンロードが完了しました。"