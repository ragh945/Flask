from flask import Flask,render_template,request,redirect,url_for,flash,session


""" 
It creates a instance for the flask class,
which will be your WSGI(Web Server Gateway Interface) application."""

## Jinja 2 template engine
"""
{{ }} is used to display variables in the template.
{% for %} is used for loops.
{% if %} is used for conditional statements.
{% endif %} is used to end the if statement.
{% endfor %} is used to end the for loop.
{% block %} is used to define a block of code that can be overridden in child templates.
{#.....#} is used for comments in Jinja2 templates."""

###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the Flask Application!"

@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/goodbye")
def goodbye():
    return render_template("goodbye.html")

@app.route("/about")
def about():
    return """
<h1>
This is Flask about page.</h1>"""

@app.route("/contact",methods=["GET","POST"])
def contact():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        message=request.form["message"]
        return f"Thank you {name}, we have received your message: {message}. We will contact you at {email}."
    return render_template("contact.html")

@app.route("/success/<int:score>")
def success(score):
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    return render_template("success.html",result=res,score=score)


@app.route("/successscore/<int:score>")
def successscore(score):
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    exp={
        "score":score,
        "result":res
    }
    return render_template("successscore.html",result=exp)


#if condition
@app.route("/successif/<int:score>")
def successif(score):
    return render_template("successif.html",result=score)


#Dynamic URL
@app.route("/submit",methods=["GET","POST"])
def submit():
    total_score=0
    if request.method=="POST":
       data_analyst_score=float(request.form["data_analyst_score"])
       data_scientist_score=float(request.form["data_scientist_score"])
       data_engineer_score=float(request.form["data_engineer_score"])
       total_score=(data_analyst_score+data_scientist_score+data_engineer_score)/3
       return redirect(url_for("successif",score=total_score))
    return render_template("submit.html")
if __name__=="__main__":
    app.run(debug=True) #debug=True will reload the server when you make changes to the code.

# The app.run() method is used to run the application on the local development server.
# The debug=True flag enables the debugger, which provides detailed error messages and automatically reloads the server when code changes are made.
# This is useful during development, but should be turned off in production for security reasons.