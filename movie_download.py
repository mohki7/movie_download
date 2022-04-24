import streamlit as st
import yt_dlp

st.title("動画保存サイト")
"YouTubeやTwitter、ニコニコ動画やInstagram上にある動画を保存できます。"

URL_movie = st.text_input("ここに保存したい動画のURLを入力してください。")

ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URL_movie])
    