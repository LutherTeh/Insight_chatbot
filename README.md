# Basic Chatbot using RASA


![alt text](https://github.com/LutherTeh/chatbot/insightflows_chatbot2.gif" demo.gif")


## What to Install

#### Install Rasa NLU

`$pip install rasa_nlu`

#### Install Rasa Core

I am installing from Git.

```

$git clone https://github.com/RasaHQ/rasa_core.git
$cd rasa_core
$pip install -r requirements.txt
$pip install -e .
```


#### How to find rasa_core and rasa_nlu version

```
$python -c "import rasa_nlu; print(rasa_nlu.__version__);"
$python -c "import rasa_core; print(rasa_core.__version__);"
```


## Step 1 - Collect conversation data 

sample data was located at data/data.json


## Step 2 - Train NLU model

```
python -m rasa_nlu.train -c config_spacy.json --data data/data.json -o models/nlu
```


## Step 3 - Initiate NLU server 

```
python -m rasa_nlu.server -c config_spacy.json --path ./models/nlu
```

## Step 4 - Run web chatbot UI 

```
python bot-application2/app.py
```


## Step 5 - Start chatting!





## Further Improvements:

to-be-updated