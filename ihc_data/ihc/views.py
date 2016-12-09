from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PredictionForm as p_form


def index(request):
    '''
        Loads the index/home page
    '''
    return render(request, 'index.html')



def dashboard(request):
    '''
        Loads the page with all the Tableau things
    '''
    return render(request, 'dashboard.html')


def vizes(request, viz):
    '''
        Loads the page with all the Tableau things
    '''
    context = {'viz': viz}
    return render(request, 'vizes.html', context)


def project_management(request):
    '''
        Loads the page with the project management form which will project
        aspects about an entered-in project.
    '''
    if request.method == 'POST':
        form = p_form(request.POST)
        if form.is_valid():
            import urllib.request
            import json
            lead = form.cleaned_data['lead']
            service_line = form.cleaned_data['service_line']
            difficulty = form.cleaned_data['difficulty']
            priority = form.cleaned_data['priority']
            projected_annual_savings = form.cleaned_data['projected_annual_savings']
            year = form.cleaned_data['year']
            region = form.cleaned_data['region']
            facility = form.cleaned_data['facility']
            ops_officer = form.cleaned_data['ops_officer']
            director = form.cleaned_data['director']
            month = form.cleaned_data['month']
            physician_involvement = form.cleaned_data['physician_involvement']
            physician_led = form.cleaned_data['physician_led']
            safety_flag = form.cleaned_data['safety_flag']
            project_type = form.cleaned_data['project_type']

            data = {
                    "Inputs": {
                            "input1":
                            [
                                {
                                    'LEAD': str(lead),
                                    'SERVICE LINE': str(service_line),
                                    'REGION': str(region),
                                    'FACILITY': str(facility),
                                    'OPS_OFFICER': str(ops_officer),
                                    'DIRECTOR': str(director),
                                    'DIFFICULTY': str(difficulty),
                                    'TYPE': str(project_type),
                                    'PRIORITY': str(priority),
                                    'PROJECTED_ANNUAL_SAVINGS': str(projected_annual_savings),
                                    'YEAR': str(year),
                                    'MONTH': str(month),
                                    'PHYSICIAN_INVOLVEMENT_FLAG': str(physician_involvement),
                                    'PHYSICIAN_LED_FLAG': str(physician_led),
                                    'SAFETY_FLAG': str(safety_flag),
                                    'DAYS_LATE_NUM': "1",
                                }
                            ],
                    },
                "GlobalParameters":  {
                }
            }

            body = str.encode(json.dumps(data))

            url = 'https://ussouthcentral.services.azureml.net/workspaces/97ac4e49472e428c94edbac1a06de9c0/services/2d125c2d708848038ae1920274db74b8/execute?api-version=2.0&format=swagger'
            api_key = '/ufpVl9FmhIeZnANA1GmMEEVfhUQjIx1UfD7KYMoSvoIUKn2bRK/EZRXy4kCjKgu7eiV8zTwsJFptRvm8GNhjg==' # Replace this with the API key for the web service
            headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

            req = urllib.request.Request(url, body, headers)

            try:
                response = urllib.request.urlopen(req)
                result = response.read().decode('utf-8')
                result = json.loads(result)
                result = result['Results']['output1']
                scored_label = result[0]['Scored Labels']
                # scored_probability = result[0]['Scored Probabilities']
                # scored_probability = float(scored_probability)*100
                print(result)
            except urllib.error.HTTPError as error:
                print("The request failed with status code: " + str(error.code))

                # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
                print(error.info())
                print(json.loads(error.read().decode("utf8", 'ignore')))

            context = {'scored_label': scored_label,
                    #    'scored_probability': scored_probability,
                       'form': form,}
            return HttpResponseRedirect('/response/%s' % scored_label)
        else:
            print(form.errors)
    else:
        form = p_form()
    context = {'form': form,}

    return render(request, 'project_management.html', context)

def response(request, val):
    context = {'result': val}
    print(val)
    # print(val2)
    return render(request, 'response.html', context)
