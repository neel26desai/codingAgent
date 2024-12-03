# codingAgent
In this repository we build complete GenAI application deployment related LLMOps principles. At the ccode we have built an application, that can help people write code for python as well write Infrastuctuer as Code in terraform. It also allows users to continue having the conservation and keep making changes to the same code , till the time they are satisfied with it. The code generation agent is built on top of GPT-4o-mini. by using prompt engineering techniques. 

## Architecture

1. Frontend: runs in its own docker container, using nginx 

2. Backed: runs in its own docker container, using python and flask

The user interacts with the fronend , which sends the message to the backed, which in turns invokes the Code generation agent.


## Instruction for running

To run this repo

1. Create a .env file in the backed directory

2. Put your Open AI key there as `OPENAI_API_KEY="<YOUR_KEY>"`

3. At the the main directory level run `docker-compose up --build`


Additionally you can change the model which is being used by the agent to gpt-4o ,by changing it in `backend/agent.py`
## Link to Demo Video
https://youtu.be/PqxiUalkSag