from flask import Flask, render_template,request
import mysql.connector

is_authorized=False

app = Flask(__name__)
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'kk@12345/',
    'database': 'ORG;'
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.form.get('data')
    if data=="correct":
        is_authorized=True
    else:
        if data=="logout":
            is_authorized=False
        else:
            return "incorrect password"
    
    if(is_authorized==False):
        return "You are not logged in"
    else:
        return "You have been authorized"

@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    result = execute_query(query)
    return render_template('index.html', result=result)

def execute_query(query):
    try:
        connection = mysql.connector.connect(**mysql_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
    except mysql.connector.Error as error:
        print("Error executing query:", error)
        result = None
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
    return result


    
if __name__ == "__main__":
    app.run(debug=True)