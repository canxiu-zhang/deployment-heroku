from flask import Flask,request,render_template
import openai

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict():
    question = [x for x in request.form.values()]
    openai.api_key = "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"
    answer = openai.Completion.create(
    model="text-davinci-003",
    prompt=question[0],
    max_tokens=100,
    temperature=0
    )
    
    return render_template('home.html',pred='Answer: {}'.format(answer["choices"][0]["text"]))

if __name__ == '__main__':
    app.run(debug=True)
    