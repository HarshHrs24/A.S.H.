
# Gen-A-Thon
  <p align="center">
<strong>Gen-A-Thon IIIT Nagpur</strong>
  </p>

<img src="https://drive.google.com/uc?export=view&id=1oSLMk97FfqcBpxOy9yNDx0_fgp1yRUQt" alt=" " width="1010" height="200">

<a name="readme-top"></a>
<!--
***  Gen-A-Thon

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/HarshHrs24/Team-cl_AI_mate"></a>

  <img src="https://drive.google.com/uc?export=view&id=1eISmQoJ9JYrpczM67SNHTP75aWQ5THT8" alt="Logo" width="110" height="110">

    
  <h3 align="center">Chatbot: ASH</h3>

</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
     <li>
      <a href="#problem-statement">Problem Statement</a>
    </li>
    <li>
      <a href="#installation">Installation Steps</a>
    </li>
     <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#our-approach">Our Approach</a></li>
    <li><a href="#features">Features</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#our-team">Our Team</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>




# Problem Statement
<strong>Track 1: "Creating an Educational Chatbot for Juniors: Empowering Students to Navigate
Academic and Non-Academic Challenges"</strong>
<br>
Create an intelligent chatbot to support junior students on their academic and personal journeys. This chatbot should offer guidance on various topics, including academics, study strategies, career advice, time management, extracurricular activities, and personal development. The aim is to provide a reliable 24/7 resource for junior students, empowering them with answers, practical solutions, and motivation to enhance their educational experiences and personal growth.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Installation

### 1. Local installation
Clone the repository or download the zip file in your machine and setup virtual environment

Make sure you have `python version >=3.9.0`, it's always good to follow the [docs](https://docs.textbase.ai/get-started/installation) 👈🏻
```bash
$ git clone https://github.com/Shivansh1203/Gen-A-Thon
$ cd Gen-A-Thon(your directory name)
$ python3 -m venv venv
$ . venv/bin/activate
```

### 2. Install dependencies

 ```bash
  $ (venv) pip install Flask torch torchvision nltk
 ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Screenshots 
## Your Friendly Chatbot/Senior ASH

## Subject-Related Questions and Study Strategies:
<img width="365" alt="Screenshot 2023-09-28 at 9 48 08 PM" src="https://github.com/HarshHrs24/A.S.H./assets/107180900/d311d133-57bb-492d-835c-40ecf4aa4cfd">


## Career Guidance and Time Management:
<img width="379" alt="Screenshot 2023-09-28 at 10 02 18 PM" src="https://github.com/HarshHrs24/A.S.H./assets/107180900/1a935522-d4b0-44c8-a074-9f9e8b609cee">


## Extracurricular Activities and Personal Development:
<img width="376" alt="Screenshot 2023-09-28 at 9 52 08 PM" src="https://github.com/HarshHrs24/A.S.H./assets/107180900/55cdbb02-ee7c-48f7-91ab-23c217b86d15">


## Food:
<img width="378" alt="Screenshot 2023-09-28 at 10 03 43 PM" src="https://github.com/HarshHrs24/A.S.H./assets/107180900/88b601b4-87df-4e1a-99cf-c04df62866ec">





<!-- Approach -->
## Our Approach
Our approach to building an intelligent chatbot using the OpenAI GPT-3.5 Turbo model involves harnessing the power of real-life experiences from seniors to assist junior students. However, we recognize the challenges posed by the token limits of the model when dealing with a vast array of experiences. To overcome this challenge, we have implemented a structured approach involving MongoDB and two instances of the GPT-3.5.Turbo model:

### MongoDB Database for Experience Collection:
We have set up a MongoDB database to systematically collect and organize various experiences shared by seniors into different categories.
Each category corresponds to a specific area of concern for junior students, such as academics, study strategies, career advice, time management, extracurricular activities, and personal development.
Within the database, we maintain separate collections for each category to efficiently manage and access relevant experiences.

### First Model Instance - Query Executor:
The first instance of our chatbot model is responsible for handling user queries and retrieving relevant experiences from the MongoDB database.
When a junior student poses a question or seeks guidance, this instance executes a MongoDB query tailored to the specific category of the question (e.g., subject-related queries).
The query retrieves pertinent experiences stored in the corresponding collection, ensuring that the responses are closely aligned with the user's query.

### Second Model Instance - Experience Enhancement:
The second instance of our model comes into play after the first instance has retrieved relevant experiences.
Its primary role is to further refine the responses based on the real-life experiences of seniors.
It takes the retrieved experiences as input and fine-tunes its responses to provide more contextually accurate and valuable guidance to the junior student.
This fine-tuning process is crucial in tailoring the chatbot's responses to the specific nuances and details of the user's query.
By implementing this structured approach with two GPT-3.5.Turbo model's instances, we aim to provide junior students with comprehensive and contextually relevant guidance. The first instance efficiently retrieves relevant experiences from the MongoDB database, while the second instance enhances these responses, taking into account the valuable insights and context shared by seniors. This combined approach ensures that our chatbot can deliver high-quality assistance to junior students, facilitating their academic and personal growth effectively.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Features -->
## Features
* <strong>Subject-Related Questions:</strong>
  <br>
Our chatbot can help junior students by instantly answering their subject-related questions. Whether it's understanding complex topics or clarifying doubts in economics or psychology, it's there to provide clear explanations.

* <strong>Study Strategies:</strong>
  <br>
Our chatbot offers study strategies tailored to individual learning styles. It can suggest effective techniques to tackle challenging subjects, helping students optimize their study habits for academic success.

* <strong>Career Guidance:</strong>
  <br>
For those juniors considering their future, our chatbot provides career guidance. It can offer insights into different career paths and trends, assisting students in making informed decisions about majors and career choices.

* <strong>Time Management:</strong>
  <br>
Time management is a critical skill, and our chatbot in Track 1 can share tips and strategies for effective time management. It helps students balance their academic commitments, assignments, and extracurricular activities efficiently.

* <strong>Extracurricular Activities:</strong>
  <br>
To foster a well-rounded education, our chatbot recommends suitable extracurricular activities. It aligns students' interests with relevant options, encouraging their participation in activities beyond academics.

* <strong>Personal Development:</strong>
  <br>
To foster a well-rounded education, our chatbot recommends suitable extracurricular activities. It aligns students' interests with relevant options, encouraging their participation in activities beyond academics.

  
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Built With

### Technology Used                                                                  
* Python
* Flask
* OpenAI
* GPT 3.5 Turbo
* JavaScript
* MongoDB
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Our Team

* [Harsh Soni](https://github.com/HarshHrs24)
* [Shivansh Rastogi](https://github.com/Shivansh1203)
* [Akhil](https://github.com/akhilupadhyay18)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [IIIT Nagpur](https://iiitn.ac.in/)
* [Gen-A-Thon](https://unstop.com/hackathons/gen-a-thon-tantrafiesta-23-iiit-nagpur-760544)


<p align="right">(<a href="#readme-top">back to top</a>)</p>





