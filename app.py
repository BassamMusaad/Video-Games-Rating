from flask import Flask, request ,render_template,abort
import pickle,numpy as np


# initiate the app
app=Flask(__name__)

# load the train model
model = pickle.load(open('model.pkl', 'rb'))

# Endpoint
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
   # if the any input string or have NaN value report error
   try:
      example = take_values(request)
      # convert the input into float.
      example = [float(x) for x in example]
      # convert into vector
      format_example = [np.array(example)]
   except:
       abort(404)

   prediction = model.predict(format_example)
   # the result of the model
   output=prediction[0]
   description=rating_description(output)

   return render_template('result.html',rating =output,description=description)



# Helper function

# use to take the value from the form in order...
def take_values(request):
    example = list()
    example.append(request.form.get('console'))
    example.append(request.form.get('Alcohol_Reference'))
    example.append(request.form.get('Animated_Blood'))
    example.append(request.form.get('Blood'))
    example.append(request.form.get('BloodandGore'))
    example.append(request.form.get('Cartoon_Violence'))
    example.append(request.form.get('DrugRe_ference'))
    example.append(request.form.get('Fantasy_Violence'))
    example.append(request.form.get('Intense_Violence'))
    example.append(request.form.get('Language'))
    example.append(request.form.get('Lyrics'))
    example.append(request.form.get('Mature_Humor'))
    example.append(request.form.get('Mild_Blood'))
    example.append(request.form.get('MildCartoonViolence'))
    example.append(request.form.get('MildFantasyViolence'))
    example.append(request.form.get('Mild_Language'))
    example.append(request.form.get('Mild_Lyrics'))
    example.append(request.form.get('MildSuggestiveThemes'))
    example.append(request.form.get('MildCartoonViolence'))
    example.append(request.form.get('Mild_Violence'))
    example.append(request.form.get('No_Descriptors'))
    example.append(request.form.get('Nudity'))
    example.append(request.form.get('Partial_Nudity'))
    example.append(request.form.get('Sexual_Content'))
    example.append(request.form.get('Sexual_Themes'))
    example.append(request.form.get('Simulated_Gambling'))
    example.append(request.form.get('Strong_Language'))
    example.append(request.form.get('StrongSexualContent'))
    example.append(request.form.get('Suggestive_Themes'))
    example.append(request.form.get('UseofAlcohol'))
    example.append(request.form.get('UseofDrugsandAlcohol'))
    example.append(request.form.get('Violence'))
    return example

# add rating description.
def rating_description(rating):
    switcher = {
        'RP':'Rating Pending',
        'EC':'Early Childhood',
        'E':'Everyone',
        'E 10+':'Everyone 10+',
        'T':'Teen',
        'M':'Mature',
        'A':'Adult',
    }
    return switcher.get(rating)



# Error Handle

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500




# Launch

# Default port:
if __name__ == '__main__':
    app.run()