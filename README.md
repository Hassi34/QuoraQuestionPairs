
# Duplicate Questions Predictor

This was the challenge provided by Quora to classify whether question pairs are duplicates or not. Doing so will make it easier to find high quality answers to questions resulting in an improved experience for Quora writers, seekers, and readers.




## 🔗 Project Links
Check out the deployed app [here](https://duplicate-question-pair.herokuapp.com/)
while Kaggle Competition link [here](https://www.kaggle.com/c/quora-question-pairs)

## Run Locally

Clone the project

```bash
  git clone https://github.com/Hassi34/QuoraQuestionPairs.git
```

Go to the project directory

```bash
  cd QuoraQuestionPairs
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```


## Usage/Examples 
## REST API
```javascript
import requests
res = requests.post('https://duplicate-question-pair.herokuapp.com/predict_duplicates', json={"question1" : ["Will AI be in demand in future ?"], "question2" : ["What is going to be the demand for AI practioner in future?"]})
if res.ok:
    print(res.text)
else :
    print(res)
```

