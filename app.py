# Import necessary libraries and modules
from urllib import response
from flask import Flask, render_template, request, jsonify
import pymongo
import openai


# Define a route for the root URL ("/") using the GET HTTP method
app = Flask(__name__)
@app.get("/")
def index_get():
    return render_template("base.html")

# Set OpenAI API key
openai.api_key = "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"


# Define a list of messages for the first chat model
First_model_messages = [
    {
            'role': 'system',
            'content': """
            you are a chatbot whose job is to just write a Mongo db query
            so whenever i write any thing related to food or eating you give me following python code as output with perfect indentation-
            ### 
            import pymongo
            output=""
            client = pymongo.MongoClient("mongodb://localhost:27017")
            my_collection =client.get_database('GenAthon').food
            cursor = my_collection.find()
            for document in cursor:
               output+=document['title']

            ###
            and whenever i write any thing related to academic you give me following python code as output with perfect indentation-
            ### 
            import pymongo
            output=""
            client = pymongo.MongoClient("mongodb://localhost:27017")
            my_collection =client.get_database('GenAthon').academic
            cursor = my_collection.find()
            for document in cursor:
                output+=document['title']

            ###
            and whenever i write any thing related to extracurricular or clubs or Community Service or Sports and Athletics or festivals, you give me following python code as output with perfect indentation-
            ### 
            import pymongo
            output=""
            client = pymongo.MongoClient("mongodb://localhost:27017")
            my_collection =client.get_database('GenAthon').extracurricular
            cursor = my_collection.find()
            for document in cursor:
                output+=document['title']

            ###
            and whenever i write any thing related to careerguidance or Career Counseling or Internship and Job Placement Support or Networking Events or Professional Development Workshops or Research and Academic Opportunities or Alumni Mentorship Program or Job Search Platforms and Resources, you give me following python code as output with perfect indentation-
            ### 
            import pymongo
            output=""
            client = pymongo.MongoClient("mongodb://localhost:27017")
            my_collection =client.get_database('GenAthon').careerguidance
            cursor = my_collection.find()
            for document in cursor:
                output+=document['title']

            ###
                
            and whenever i write any thing related to study strategies or time management or personal development, you give me following python code as output with perfect indentation-
            ### 
            import pymongo
            output=""
            client = pymongo.MongoClient("mongodb://localhost:27017")
            my_collection =client.get_database('GenAthon').strategies
            cursor = my_collection.find()
            for document in cursor:
                output+=document['title']

            ###
                
            and whenever i write any thing related to Office Locations or Official Work Procedures, you give me following python code as output with perfect indentation-
            ### 
            import pymongo
            output=""
            client = pymongo.MongoClient("mongodb://localhost:27017")
            my_collection =client.get_database('GenAthon').official
            cursor = my_collection.find()
            for document in cursor:
                output+=document['title']

            ###

                
            ...
            """
        },
            {
            'role': 'user',
            'content': "so i was eating jelly bean what do you eat"
        }
        ,
            {
            'role': 'assistant',
            'content': '''
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
output=""
my_collection =client.get_database('GenAthon').food
cursor = my_collection.find()
for document in cursor:
    output+=document['title']

            '''
        }

]

# Define a function for generating messages for the second chat model based on a given experience
def Second_model_messages(experience):
    return [
    {
            'role': 'system',
            'content': f"""
            You are a friendly chatbot whose primary role is to help junior students by providing guidance and advice based solely on the experiences of senior students. Your responses should be derived exclusively from the content provided in the senior's experience section. Your purpose is to offer practical solutions, insights, and suggestions based on the wisdom and experiences shared by seniors.
            /// again remember, you will only answer based on experience provided by seniors, you won't be generating anything new on your own, whatever is written in experienceprovided by senior, you will only answer that.
            Junior students often face a wide range of doubts and uncertainties as they embark on their educational journeys, both academically and in non-academic aspects of their lives. These doubts could encompass subject-related questions, study strategies, career guidance, time management, extracurricular activities, and even personal development issues. While teachers and mentors are available to help, their time and resources are often limited.
            /// again remember, you will only answer based on experience provided by seniors, you won't be generating anything new on your own, whatever is written in experienceprovided by senior, you will only answer that.
            Your role is to act as a conduit for the valuable insights and experiences shared by seniors. You should be capable of providing answers and guidance on a variety of topics, offering practical examples and solutions. For instance, it should be able to explain mathematical concepts, suggest effective study techniques, recommend suitable extracurricular activities, and provide motivational advice.
            /// again remember, you will only answer based on experience provided by seniors, you won't be generating anything new on your own, whatever is written in experienceprovided by senior, you will only answer that.
            The goal is to empower junior students with a virtual assistant that can assist them 24/7, helping them overcome hurdles and make informed decisions throughout their academic and personal journeys.



            following is the senior's experirnce, you will only answer based on experience provided by senior, you won't be generating anything new on your own, whatever is written in experience provided by senior, you will only answer that
            {experience}
            
            /// again remember, you will only answer based on experience provided by seniors, you won't be generating anything new on your own, whatever is written in experienceprovided by senior, you will only answer that.
            """
        },
            {
            'role': 'user',
            'content': "hey, I am hungry tell me a place, suggest me a place where i can eat spicy food,"
        }
        ,
            {
            'role': 'assistant',
            'content': '''
you can go to Spice Delight, This stall specializes in cuisine from various regions, from Thai to Mexican. Their Pad Thai noodles and chicken fajitas are particularly outstanding.
            '''
        }

]


# Define a function to query the first chat model and execute its generated code
def db_query(query):
    new_query={"role": "user", "content": f"{query}"}
    First_model_messages.append(new_query)
    first_model = openai.ChatCompletion.create(
    messages=First_model_messages,
    temperature=0,
    model="gpt-3.5-turbo"
    )
    new_answer={"role": "assistant", "content": f'{first_model ["choices"][0]["message"]["content"]}'}
    First_model_messages.append(new_answer)
    print(first_model["choices"][0]["message"]["content"])
    output=""
    try:
        namespace = {}
        exec(compile(first_model ["choices"][0]["message"]["content"], "<string>", "exec"), namespace)
        output = namespace.get("output", None)
    except Exception as e:
        print("normal command") 
    return output


    

# Define a function for generating responses using the second chat model
def gpt(query):
    experience=db_query(query)
    message=Second_model_messages(experience)
    new_query={"role": "user", "content": f"{query}"}
    message.append(new_query)
    second_model = openai.ChatCompletion.create(
    messages=message,
    temperature=1,
    max_tokens=500,
    model="gpt-3.5-turbo"
    )
    
    return  second_model["choices"][0]["message"]["content"]


# Define a route for making predictions using the second chat model
@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    # TODO: check if text is valid
    output=gpt(text)

    message = {"answer": output}
    return jsonify(message)

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
    



 



