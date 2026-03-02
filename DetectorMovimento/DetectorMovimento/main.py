from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__, template_folder="template")

s = {
    "armed": True,
    "alarm": False,
    "last": "-"
}

def now():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/state")
def state():
    return jsonify(s)

@app.post("/arm")
def arm():
    s["armed"] = True
    return jsonify(msg="Sistema ARMADO", **s)

@app.post("/disarm")
def disarm():
    s["armed"] = False
    s["alarm"] = False
    return jsonify(msg="Sistema DESARMADO", **s)

@app.post("/motion")
def motion():
    if not s["armed"]:
        return jsonify(msg="Mensagem via Wi-Fi: Movimento ignorado", popup=False, **s)

    s["alarm"] = True
    s["last"] = now()

    return jsonify(
        msg="Mensagem via Wi-Fi: Movimento detectado",
        popup=True,
        **s
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)