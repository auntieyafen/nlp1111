import streamlit as st
from .utils import clean_data
from ...components.form import form_controller
import requests
from bs4 import BeautifulSoup

url_food = 'https://www.ptt.cc/bbs/Food/index.html'
for i in range(5):
    print(f"第 {i+1} 頁")
    r = requests.get(url_food)
    sp = BeautifulSoup(r.text, 'html.parser')
    datas = sp.find_all("div", class_='r-ent')
    for data in datas:
        if data.a:
            print(data.a.text)


url_gossip = 'https://www.ptt.cc/bbs/Gossiping/index.html'
cookies = {'over18':'1'}
r = requests.get(url_gossip, cookies=cookies)
sp = BeautifulSoup(r.text, 'html.parser')
datas = sp.find_all("div", class_='r-ent')
for data in datas:
    if data.a:
        print(data.a.text)


def display_data_form():
    with st.form("my_form"):
        option = st.selectbox('請挑選文章標題', ['[問卦] 社會住宅一直延期？',
                                        '[問卦] 這女生484很會做家事更勝李子七?',
                                        'Re: [問卦] 美國是全球首惡實錘了吧？',
                                        '[問卦] 當初狂吹0050的人現在應該已經歐印了吧',
                                        '[新聞] 美陰謀論者謊稱桑迪胡克小學槍擊案是騙局',
                                        '[問卦] 台灣工程師真的會載去美國嗎',
                                        'Re: [問卦] 戴智慧手錶有什麼好處啊？',
                                        'Re: [問卦] 戴智慧手錶有什麼好處啊？',
                                        '[新聞] 馬斯克賣「燒焦頭髮」香水 短短幾小時賺3',
                                        'Re: [新聞] 被罵教改搞爛台灣高教 李遠哲嘆氣吐原因',
                                        '[問卦] 如果半導體背骨反過來挺中國會怎麼樣',
                                        '[問卦] 女生最大的武器是不是哭',
                                        'Re: [問卦] 為什麼香港人一副台灣一定要給身分證的樣',
                                        'Re: [問卦] 戴智慧手錶有什麼好處啊？',
                                        '[問卦] 開庭前就被判有罪',
                                        '[新聞] 中國清零存廢之爭：全世界都做得，為何',
                                        '[新聞] 柯建銘談高虹安論文脫口1句 林環牆氣炸：'
                                        '[問卦] 12點準備看天天開心配中飯',
                                        'Re: [問卦] 為什麼香港人一副台灣一定要給身分證的樣',
                                        '[公告] 八卦板板規(2022.02.21)',
                                        '[協尋] 新北市永和區環河東路三段76號(已徵到)',
                                        '[協尋] 9月12日晚間11：10-11：2台中大道七段與',
                                        'Re: [問卦] 有沒有詐騙集團女成員都長得很正的八',
                                        '[公告] 帳號定時改密碼 PTT禁止買賣帳號蛤 水桶'
                                        ])
        input_data: str = form_controller("text-area", title=" ")
        input_data = option
        
        submitted = st.form_submit_button("確定")

        if submitted:
            cleaned_data = clean_data(input_data.strip())

            if not cleaned_data:
                st.error("請輸入句子！")
                return False

            st.session_state["input_data"] = cleaned_data
            return cleaned_data
