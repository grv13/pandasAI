import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from pandasai import SmartDataframe
import os
os.environ["OPENAI_API_KEY"] = "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"

OPENAI_API_KEY = "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"
llm = OpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo-16k")
# pandas_ai = PandasAI(llm=llm)
pandas_ai = SmartDataframe("airdata.csv", config={"llm": llm})

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        user_input = request.form["user_input"]
        result = pandas_ai.chat(user_input)
        return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
