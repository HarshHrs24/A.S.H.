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
openai.api_key = ""


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

Third_model_messages = [
    {
            'role': 'system',
            'content': """
            you are a chatbot whose job is to just write type.
            so whenever i write any thing related to food or eating you give me following as output and in a single word only-
            ### 
            food
            ###
            and whenever i write any thing related to academic you give me following as output and in a single word only-
            ### 
            academic 
            ###
            and whenever i write any thing related to extracurricular or clubs or Community Service or Sports and Athletics or festivals, you give me following as output and in a single word only-
            ### 
            extracurricular
            ###
            and whenever i write any thing related to careerguidance or Career Counseling or Internship and Job Placement Support or Networking Events or Professional Development Workshops or Research and Academic Opportunities or Alumni Mentorship Program or Job Search Platforms and Resources, you give me following as output and in a single word only-
            ### 
            careerguidance
            ###      
            and whenever i write any thing related to study strategies or time management or personal development, you give me following as output and in a single word only-
            ### 
            strategies
            ###
                
            and whenever i write any thing related to Office Locations or Official Work Procedures, you give me following as output and in a single word only-
            ### 
            official
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
food
            '''
        }

]
fourth_model_messages = [
    {
            'role': 'system',
            'content': """
            '''
You are a specialized chatbot tasked with following two rigid response categories:

For Questions: If a user's query seems to be directly seeking an answer, explanation, or assistance, you must classify it as a question. This includes queries like "What is X?", "Tell me about X", or "How does X work?". For every such inquiry, your only response should be: "No".

For Non-Questions: Whenever a user inputs a topic, keyword, or phrase that doesn't directly ask for a specific answer but mentions a subject or field of interest, it's a non-question. These usually are singular or plural nouns or standalone phrases. even if keyword exits in this hashmap = {
    # Academic related
    1: "syllabus", 2: "lectures", 3: "tutorials", 4: "seminars", 5: "textbooks",
    6: "assignments", 7: "exams", 8: "grades", 9: "GPA", 10: "major",
    11: "minor", 12: "electives", 13: "thesis", 14: "dissertation", 15: "professor",
    # ... continue in the same manner

    # Extracurricular related
    51: "drama", 52: "music", 53: "art", 54: "debate", 55: "dance",
    # ...

    # Clubs
    101: "robotics", 102: "book", 103: "coding", 104: "environmental", 105: "photography",
    # ...

    # Community Service
    151: "volunteering", 152: "nonprofits", 153: "blood donation", 154: "food drive", 155: "clean-up",
    # ...

    # Sports and Athletics
    201: "football", 202: "basketball", 203: "volleyball", 204: "track", 205: "gymnastics",
    # ...

    # Career related
    251: "resume", 252: "interview", 253: "job fair", 254: "portfolio", 255: "internship",
    256: "placement", 257: "career counseling", 258: "mentorship", 259: "networking", 260: "workshops",
    # ...

    # Research and Academic Opportunities
    301: "lab", 302: "fieldwork", 303: "conference", 304: "publication", 305: "presentation",
    # ...

    # Personal Development
    351: "soft skills", 352: "leadership", 353: "communication", 354: "critical thinking", 355: "teamwork",
    # ...

    # Campus Facilities
    401: "library", 402: "dining hall", 403: "dormitories", 404: "recreation center", 405: "health center",
    # ...

    # Food or Eating
    451: "cafeteria", 452: "coffee shop", 453: "snacks", 454: "meals", 455: "dietary options",
    # ...



    # Others
    501: "festivals", 502: "study strategies", 503: "time management", 504: "alumni", 505: "job search platforms",
    506: "resources", 507: "office locations", 508: "official procedures", 509: "tutoring", 510: "advising", 511:"academic", 512:"Extracurricular", 513:"Clubs", 514:"Community Service", 515:"Sports", 516:"Athletics", 517:"Career", 518:"careerguidance", 519:"Research", 520:Academic Opportunities, 521:"Personal Development", 522:"Campus Facilities",523:"Food", 524:"Eating"
    # ... and so on
}
For such inputs, your duty is to generate a comma-separated list of the top 10 related questions regarding that topic or keyword.
and again remem ber iif it exist in haspmap== {
    # Academic related
    1: "syllabus", 2: "lectures", 3: "tutorials", 4: "seminars", 5: "textbooks",
    6: "assignments", 7: "exams", 8: "grades", 9: "GPA", 10: "major",
    11: "minor", 12: "electives", 13: "thesis", 14: "dissertation", 15: "professor",
    # ... continue in the same manner

    # Extracurricular related
    51: "drama", 52: "music", 53: "art", 54: "debate", 55: "dance",
    # ...

    # Clubs
    101: "robotics", 102: "book", 103: "coding", 104: "environmental", 105: "photography",
    # ...

    # Community Service
    151: "volunteering", 152: "nonprofits", 153: "blood donation", 154: "food drive", 155: "clean-up",
    # ...

    # Sports and Athletics
    201: "football", 202: "basketball", 203: "volleyball", 204: "track", 205: "gymnastics",
    # ...

    # Career related
    251: "resume", 252: "interview", 253: "job fair", 254: "portfolio", 255: "internship",
    256: "placement", 257: "career counseling", 258: "mentorship", 259: "networking", 260: "workshops",
    # ...

    # Research and Academic Opportunities
    301: "lab", 302: "fieldwork", 303: "conference", 304: "publication", 305: "presentation",
    # ...

    # Personal Development
    351: "soft skills", 352: "leadership", 353: "communication", 354: "critical thinking", 355: "teamwork",
    # ...

    # Campus Facilities
    401: "library", 402: "dining hall", 403: "dormitories", 404: "recreation center", 405: "health center",
    # ...

    # Food or Eating
    451: "cafeteria", 452: "coffee shop", 453: "snacks", 454: "meals", 455: "dietary options",
    # ...

    # Others
    501: "festivals", 502: "study strategies", 503: "time management", 504: "alumni", 505: "job search platforms",
    506: "resources", 507: "office locations", 508: "official procedures", 509: "tutoring", 510: "advising", 511:"academic", 512:"Extracurricular", 513:"Clubs", 514:"Community Service", 515:"Sports", 516:"Athletics", 517:"Career", 518:"careerguidance", 519:"Research", 520:Academic Opportunities, 521:"Personal Development", 522:"Campus Facilities",523:"Food", 524:"Eating"
    # ... and so on
}
Your duty is to generate a comma-separated list of the top 10 related questions regarding that topic or keyword.

Examples to Guide You:

User Query: "academics"
Your Response: "What courses are offered in academics?, How does one excel in academics?, ... , What's the importance of academics?"

User Query: "tell me about time management"
Your Response: "No"

User Query: "semester"
Your Response: "What courses are offered in the semester?, How many credits are required in a semester?, ... , How long does a semester typically last?"

User Query: "time management"
Your Response: "How can one improve their time management skills?, What are common time management techniques?, ... , Why is time management essential for professionals?"

User Query: "certification"
Your Response: "What are the benefits of getting certified?, How does one choose the right certification?, ... , Can certifications boost one's career prospects?"

Be exacting in following these guidelines. Your categorization should strictly align with the intent behind the user's query based on the categories provided.


'''
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
No
            '''
        }
        ,
            {
            'role': 'user',
            'content': "tell me subjects in semester one"
        }
        ,
            {
            'role': 'assistant',
            'content': '''
No
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

def insertion(type,text):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["GenAthon"]
    collection = db[type]
    inserted_id = collection.insert_one(text).inserted_id
    return str(inserted_id)



def checker(query):
    message= fourth_model_messages
    new_query={"role": "user", "content": f"{query}"}
    message.append(new_query)
    fourth_model = openai.ChatCompletion.create(
    messages= message,
    temperature=0,
    model="gpt-3.5-turbo"
    )
    print("checked")
    return fourth_model["choices"][0]["message"]["content"]
    
# # Define a function for generating responses using the second chat model
# def gpt(query):
#     if(checker(query)=="No"):
#         experience=db_query(query)
#         message=Second_model_messages(experience)
#         new_query={"role": "user", "content": f"{query}"}
#         message.append(new_query)
#         second_model = openai.ChatCompletion.create(
#         messages=message,
#         temperature=1,
#         max_tokens=500,
#         model="gpt-3.5-turbo"
#         )      
#         return  second_model["choices"][0]["message"]["content"]
#     else:
#         data=checker(query)
#         questions = data.split(", ")
        


# Define a route for making predictions using the second chat model
@app.post("/predict")
def predict():
    query = request.get_json().get("message")
    # TODO: check if text is valid
    print("sirf ",end="")
    check=checker(query)
    print(check)
    if(check=="No"):
        print("No----")
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
        output=  second_model["choices"][0]["message"]["content"]
        message = {"type":"string","answer": output}
        return jsonify(message)
    else:
        print("Yes")
        data=check
        print(data)
        questions = data.split(", ")
        message = {"type":"array","answer": questions}
        return jsonify(message)


@app.post("/insert")
def insert():
    data=request.get_json().get("text")
    new_query={"role": "user", "content": f"{data}"}
    Third_model_messages.append(new_query)
    Third_model = openai.ChatCompletion.create(
    messages=Third_model_messages,
    temperature=0,
    model="gpt-3.5-turbo"
    )
    type=Third_model["choices"][0]["message"]["content"]
    text={"title":data}
    return insertion(type,text)

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)
    







