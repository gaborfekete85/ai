import azure.functions as func
import logging
from openai import OpenAI
# import openai
import os, config
from llama_index import StorageContext, load_index_from_storage

os.environ['OPENAI_API_KEY'] = config.OPENAI_API_KEY

secret_key = config.OPENAI_API_KEY

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="fintamaAPI", auth_level=func.AuthLevel.ANONYMOUS)
def fintamaAPI(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info('Python HTTP trigger function processed a request.')
        client = OpenAI()
        client.api_key = secret_key
        req_body = req.get_json()
        logging.info('3.')
        storage_context = StorageContext.from_defaults(persist_dir="./storage")
        print("Indexing")
        index = load_index_from_storage(storage_context)
        print("Indexed 1")
        query_engine = index.as_query_engine()
        print(f"Request body: {req_body['prompt']['content']}")
        responseText = query_engine.query(req_body['prompt']['content'])
        print(f"Response received: {responseText}")
        return func.HttpResponse(str(responseText), status_code=200)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return func.HttpResponse(error_message, status_code=500)
    
@app.route(route="basicopenai")
def basicopenai(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="completionAPI", auth_level=func.AuthLevel.ANONYMOUS)
def completionAPI(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info('Python HTTP trigger function processed a request.')
        # give openAI our secret_key to authenticate
        logging.info('0.')
        client = OpenAI()
        logging.info('1.')
        client.api_key = secret_key
        logging.info('2.')
        # Get variables from the HTTP request body
        req_body = req.get_json()
        logging.info('3.')
        # Call the openAI API
        # output = client.completions.create(
        #     model="text-davinci-003" if req_body['model'] is None else req_body['model'],
        #     prompt=req_body['prompt'],
        #     max_tokens="200" if req_body['max_tokens'] is None else req_body['max_tokens'],
        #     temperature="0" if req_body['temperature'] is None else req_body['temperature'],
        # )
        output = client.chat.completions.create(
            model=req_body['model'],
            messages=[
              {
                "role": "system",
                "content": "You are a helpful assistant"
              },
              {
                "role": "user",
                "content": req_body['prompt']['content']
              }
            ],
            temperature=req_body['temperature'],
            max_tokens=req_body['max_tokens'],
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        # output = client.completions.create(
        #     model=req_body['model'],
        #     prompt=req_body['prompt']['content'],
        #     max_tokens=req_body['max_tokens'],
        #     temperature=req_body['temperature'],
        # )

        # Format the response
        responseText = output.choices[0].message.content

        # Provide the response
        return func.HttpResponse(responseText, status_code=200)
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        return func.HttpResponse(error_message, status_code=500)    