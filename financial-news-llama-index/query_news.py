import os, config
from llama_index import StorageContext, load_index_from_storage

# os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY

# new version of llama index uses StorageContext instead of load_from_disk
# index = GPTSimpleVectorIndex.load_from_disk('index_news.json')
storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

# new version of llama index uses query_engine.query()
query_engine = index.as_query_engine()
# response = query_engine.query("What are some near-term risks to Nvidia?")
# print(response)

# questions on current trends
# response = query_engine.query("Are the near-term risks of coscoin are positive or negative?")
# print(response)

response = query_engine.query("Is the current trend of SOL positive or negative ? ")
print(response)





