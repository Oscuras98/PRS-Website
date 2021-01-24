from flask import Flask, render_template, redirect, url_for
import webbrowser
app = Flask(__name__)



#   Main Menu
# 1  Home
@app.route('/')
def home():
    return render_template('ENG/1_Home/1_home_ENG.html');

@app.route('/inicio')
def inicio():
    return render_template('ESP/1_Inicio/1_inicio_ESP.html');

@app.route('/index')
def index():
    return render_template('HUN/1_Index/1_index_HUN.html');
#-------------------------------------------------------

# 2	Gaming
@app.route('/Gaming_ENG')
def Gaming_ENG():
    return render_template('ENG/2_Gaming/Gaming_ENG.html');

@app.route('/Gaming_ESP')
def Gaming_ESP():
    return render_template('ESP/2_Gaming/Gaming_ESP.html');

@app.route('/Gaming_HUN')
def Gaming_HUN():
    return render_template('HUN/2_Gaming/Gaming_HUN.html');
# -------------------------------------
# 				GAMING SUB MENU ENGLISH
@app.route('/Gaming_NEWS_ENG')
def Gaming_NEWS_ENG():
    return render_template('ENG/2_Gaming/1_GAMING_NEWS/1_GAMING_NEWS_ENG.html');
@app.route('/Gameplays_ENG')
def Gameplays_ENG():
    return render_template('ENG/2_Gaming/2_Gameplays/2_GAMEPLAYS_ENG.html');
@app.route('/Retro_PC_Games_ENG')
def Retro_PC_Games_ENG():
    return render_template('ENG/2_Gaming/3_RETRO_PC_GAMES/3_RETRO_PC_GAMES_ENG.html');

#----------------------------------------
#				Gaming sub menu spanish



# 5 Community
@app.route('/Community_ENG')
def Community_ENG():
    return render_template('ENG/3_Community/Community_ENG.html');

# 3 Learn To Code
@app.route('/Learn_ENG')
def Learn_ENG():
	return render_template('ENG/4_Learn/Learn_ENG.html');
# Learn JAVA Bellow
@app.route('/Learn_JAVA_1')
def Learn_JAVA_1():
	return render_template('ENG/4_Learn/1 Java/java_1.html');
	
@app.route('/Downloads_ENG')
def Uploads_ENG():
    return render_template('ENG/8_Downloads/8_Downloads_ENG.html');
if __name__ == '__main__':
    app.run(debug=True)
