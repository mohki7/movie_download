import streamlit as st
import yt_dlp

st.title("動画保存サイト")
"・YouTubeやTwitter、ニコニコ動画やInstagram上にある動画を保存できます。"

ffmpeg = st.checkbox(label = "ffmpegをダウンロード済み")
"※ffmpegをダウンロードしている方は、高画質・高音質で動画をダウンロード可能です。"
"※ffmpegをダウンロードしていない方は、基本的に720pでダウンロードします。"


URL_movie = st.text_input("ここに保存したい動画のURLを入力してください。")
act = st.button("実行")
if act:
    if ffmpeg:
        ydl_opts = {"format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"}
    else:
        ydl_opts ={}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        data = ydl.download([URL_movie])


#st.download_button(label = "ダウンロード", data = data)
