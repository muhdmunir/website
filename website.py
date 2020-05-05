from flask import Flask, render_template #access html files

app=Flask(__name__) #create variable to store flask object instance.(flask Application)

@app.route('/') #add decorator route. URL to view website. / is for homepage
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
