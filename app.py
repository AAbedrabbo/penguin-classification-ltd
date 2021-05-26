import flask
import pickle
import pandas as pd

with open("model/penguin_model_rf.pkl", "rb") as f:
    model = pickle.load(f)


app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods = ["GET", "POST"])
def main():

    if flask.request.method == "GET":
        return(flask.render_template('main.html'))

    elif flask.request.method == "POST":

        island = flask.request.form['island']
        cullen = flask.request.form['cullen']
        culdep = flask.request.form['culdep']
        flen = flask.request.form['flen']
        bmas = flask.request.form['bmas']
        sex = flask.request.form['sex']

        # Make dataframe out of input variables
        input_variables = pd.DataFrame([[island, cullen, culdep, flen, bmas, sex]],
                              columns=['island',
                                            'culmen_length_mm',
                                            'culmen_depth_mm',
                                            'flipper_length_mm',
                                            'body_mass_g',
                                            'sex'],
                              index = ['input'])


        prediction = model.predict(input_variables)[0]

        return (flask.render_template('main.html',
                                     original_input =
                                     {'Island': island,
                                     'Culmen Length (mm)': cullen,
                                      'Culmen Depth (mm)': culdep,
                                      'Flipper Length (mm)': flen,
                                      'Body Mass (g)': bmas,
                                      'Sex': sex},
                                     result = prediction))

if __name__ == '__main__':
    app.run()
