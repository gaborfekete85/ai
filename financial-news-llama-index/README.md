
# Financial News AI service

Financial News Analysis with Llama Index, GPT-4, and Streamlit

# Pre condition
 - Python 3 installed

# Setup
Download dependencies: 
 - Run in the command line
```
pip3 install -r requirements.txt
```

# Step0 - Configuration
Configure the following environment variables: 
 - OPENAI_API_KEY: API Key of Open AI
 - CRYPTO_NEWS_TOKEN: Authentication token to access crypto news API

# Step1: Fetch the latest news
```
Run fetch_crypto_news.py as a python script
```
This will collect the content of HTML pages under the crypto_news folder with a date prefix.
By default it collects the news for the current day only.

# Step2:
```
Run index_crypto_news.py as a python script
```  
This will create a training set from the collected content under the crypto_news folder
The index is created under the storage folder

# Step3: 
Ask a question from the training set: 
```
Run the query_news.py as a pyhton script
```

Change the question in the sample request looks as below: 
```
response  =  query_engine.query("Is the current trend of SOL positive or negative ? ")
print(response)
```

# Step4: Start the UI
```
streamlit run app.py
```

API: Collection of financial news URLs
https://cryptonews-api.com/