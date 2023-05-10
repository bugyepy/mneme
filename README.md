# Mneme

Text Summarizer、つまり、文章を要約してくれます。  
形態素解析とマルコフ連鎖を用いてアルゴリズムを考えて作られたものとは異なり、これはGPTにテキストを投げるだけの簡易なものです。  
30分くらいで出来ました。  

## development

Requirements Python 3.10.6, OpenAI API Key

```shell
pip install -r requirements.txt
```

Next, create .env file in the root directory and define environment variable named OPENAI_APY_KEY.

```shell
streamlit run mneme.py
```

Enjoy ;)
