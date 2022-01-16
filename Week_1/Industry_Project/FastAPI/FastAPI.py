from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/Q1')
def question1 ():
    return {"What was the best month for sales?" : "From the bar chart we can conclude that the best month for sales was December."}

@app.get('/Q2')
def question2 ():
    return {"What city sold the most product?" : "It is evident from the bar chart that most no. of products were sold in San Francisco."}

@app.get('/Q3')
def question3 ():
    return {"What time should we display advertisements to maximize likelihood of customer's buying product?" : "My recommendation is to display advertisments slightly before 11 AM or 7 PM."}

@app.get('/Q4')
def question4 ():
    return {"What products are most often sold together and what can we do with that data?" : "We can offer smart deals on (Iphone, Lightning Charging Cable) and so-on."}

@app.get('/Q5')
def question5 ():
    return {"What product sold the most? Why do you think it sold the most?" : "From the above two graphs we can prove the hypothesis that the product whose price is high was sold the least and vice versa."}