import openai
import streamlit
import loadEnv

openai.api_key = loadEnv.OPENAI_API_KEY

def generate_summarizer(
		max_tokens,
		temperature,
		top_p,
		frequency_penalty,
		prompt,
		person_type,
):
		res = openai.ChatCompletion.create(
				model="gpt-3.5-turbo",
				max_tokens=1000,
				temperature=0.7,
				top_p=0.5,
				frequency_penalty=0.5,
				messages=
			 [
				 {
					"role": "system",
					"content": "あなたは文章を要約するアシスタントです。",
				 },
				 {
					"role": "user",
					"content": f"{person_type}が読むことを念頭に置き、以下の文章を要約してください。{person_type}が理解できない難しい言葉は言い換えてください。: {prompt}",
				 },
				],
		)
		return res["choices"][0]["message"]["content"]

# サイト名
streamlit.title("Mneme - Text Summarizer")

# タブで表示する
tab1, tab2 = streamlit.tabs(["要約", "設定"])

# 設定タブでは各パラメータをスライダーで設定できる
with tab2:
  col1, col2 = streamlit.columns(2)
  with col2:
    streamlit.text("パラメータを設定する")
    token = streamlit.slider("Token", min_value=0.0, max_value=1000.0, value=50.0, step=1.0)
    temp = streamlit.slider("Temperature", min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    top_p = streamlit.slider("Nucleus Sampling", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    f_pen = streamlit.slider("Frequency Penalty", min_value=-1.0, max_value=1.0, value=0.0, step=0.01)
  with col1:
    streamlit.text("現在のパラメータ")
    streamlit.write("Current Token :", token)
    streamlit.write("Current Temperature :", temp)
    streamlit.write("Current Nucleus Sampling :", top_p)
    streamlit.write("Current Frequency Penalty :", f_pen)

# 要約タブで文章を入力して要約する
with tab1:
  # テキストの入力欄
  input_text = streamlit.text_area("下記に要約したい文章を入力してください。", height=200)
  # 誰向けに要約するかを設定するセレクトボックス
  option = streamlit.selectbox(
    "要約した文章は誰が読みますか？",
    (
      "幼稚園児",
      "中学生",
      "大学生",
      "熟達したデータ・サイエンティスト",
    ),
  )
  if streamlit.button("要約する"):
    streamlit.write(generate_summarizer(token, temp, top_p, f_pen, input_text, option))
