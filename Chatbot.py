import streamlit as st
from datetime import datetime as dt
import os, glob, random
import json
import urllib.request as url

# Configure page layout
icon_url=r"https://static.vecteezy.com/system/resources/previews/019/786/706/original/chatbot-icon-cute-smiling-robot-cartoon-character-illustration-png.png"

st.set_page_config(
    page_title='Chat app',
    layout='wide')

st.image(icon_url,width=150)

# Intent lists
greetIntent = ["hi", "hello", "hey", "hello cody", "hi there"]
dateIntent = ["date", "tell me date", "please tell me date"]
timeIntent = ["time", "tell me time", "please tell me time"]
musicIntent = ["play song", "play music", "please play song"]
videoIntent = ["play video", "play movie", "please play a video"]
newsIntent = ["news", "tell me news"]
news_category_intent = ["sports", "politics", "entertainment", "science","business"]
byeIntent = {'bye', 'bye cody', 'goodbye', 'goodbye cody', 'adious', 'exit'}

# Main app
st.title("Hello my name is CODY and I'm your technical assistant")
st.write("How may I assist you?")
st.write("For instance try saying hi, play music or tell me date")
beg = st.form("chat_begin")
name = beg.text_input("Enter your name")
btn1 = beg.form_submit_button("Press ok")
form = st.form("chat_form")
msg = form.text_input("Enter your message...")
btn = form.form_submit_button("Send message")
if btn:
    msg = msg.lower()
    if msg in greetIntent:
        st.write("Hello",name)
    elif msg in dateIntent:
        date = dt.now().date()
        st.write("Today's Date is: ", date.strftime("%d %B, %Y, %a"))
    elif msg in timeIntent:
        time = dt.now().time()
        st.write("Time is:", time.strftime("%H:%M:%S, %p"))
    elif msg in musicIntent:
        path = r"D:\Music"  # Update with your music path
        os.chdir(path)
        songs = glob.glob("*.mp3")
        randomSong = random.choice(songs)
        st.write("Sure I'll play music for you",randomSong)
        os.startfile(randomSong)
    elif msg in videoIntent:
        path2 = r"D:\Movies"
        os.chdir(path2)
        video = glob.glob("*.mkv")
        randomvideo = random.choice(video)
        st.write("Sure I'll play videos for you",randomvideo)
        os.startfile(randomvideo)
    elif msg in newsIntent:
        st.write("Now loading latest News for",name)
        st.write("1. Politics")
        st.write("2. Entertainment")
        st.write("3. Sports")
        st.write("4. Science")
        st.write("5. Business")
    elif msg in news_category_intent:
        # News API
        path = f"https://newsapi.org/v2/top-headlines?country=in&category={msg}&apiKey=695e07af402f4b119f0703e9b19f4683"
        response = url.urlopen(path)
        data = json.load(response)
        articles = data['articles']
        for article in articles:
            st.write(article['title'])
            st.write("*" * 40)
    elif msg in byeIntent:
        st.write("Bye",name,"...I hope I was able to answer all of your queries")
        st.write("Please leave a rating from 1-5")
        form2 = st.form("chat_close")
        msg = form2.text_input("Enter here")
        btn = form2.form_submit_button("Confirm")
    else:
        st.write("I don't understand")