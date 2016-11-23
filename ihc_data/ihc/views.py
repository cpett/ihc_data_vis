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
            project_title = form.cleaned_data['project_title']
            lead = form.cleaned_data['lead']
            service_line = form.cleaned_data['service_line']
            difficulty = form.cleaned_data['difficulty']
            project_type = form.cleaned_data['project_type']
            priority = form.cleaned_data['priority']
            priority_num = form.cleaned_data['priority_num']
            status = form.cleaned_data['status']
            status_num = form.cleaned_data['status_num']
            identifier = form.cleaned_data['identifier']
            date_entered = str(form.cleaned_data['date_entered'])
            actual_start = str(form.cleaned_data['actual_start'])
            target_finish = str(form.cleaned_data['target_finish'])
            actual_finish = str(form.cleaned_data['actual_finish'])
            late_finsih = str(form.cleaned_data['late_finsih'])
            projected_annual_savings = form.cleaned_data['projected_annual_savings']
            savings_year = form.cleaned_data['savings_year']
            year = form.cleaned_data['year']
            region = form.cleaned_data['region']
            facility = form.cleaned_data['facility']
            ops_officer = form.cleaned_data['ops_officer']
            director = form.cleaned_data['director']
            system = form.cleaned_data['system']
            month = form.cleaned_data['month']
            week = form.cleaned_data['week']
            active_queue_flag = form.cleaned_data['active_queue_flag']
            active_flag = form.cleaned_data['active_flag']
            active_complete_flag = form.cleaned_data['active_complete_flag']
            queue_time = form.cleaned_data['queue_time']
            duration = form.cleaned_data['duration']
            tally_c = form.cleaned_data['tally_c']
            physician_involvement = form.cleaned_data['physician_involvement']
            physician_led = form.cleaned_data['physician_led']
            safety_flag = form.cleaned_data['safety_flag']
            cost_savings = form.cleaned_data['cost_savings']
            validated_flag = form.cleaned_data['validated_flag']
            status_flag = form.cleaned_data['status_flag']
            cancel_flag = form.cleaned_data['cancel_flag']

            data = {
                    "Inputs": {
                            "input1":
                            [
                                {
                                        'PROJECT TITLE': project_title,
                                        'LEAD': lead,
                                        'SERVICE LINE': service_line,
                                        'DIFFICULTY': difficulty,
                                        'TYPE': project_type,
                                        'PRIORITY': priority,
                                        'PRIORITY_NUM': priority_num,
                                        'STATUS': status,
                                        'STATUS_NUM': status_num,
                                        'IDENTIFIER': identifier,
                                        'DATE ENTERED': date_entered,
                                        'ACTUAL START DATE': actual_start,
                                        'TARGET FINISH DATE': target_finish,
                                        'ACTUAL FINISH DATE': actual_finish,
                                        'LATE_FINISH': late_finsih,
                                        'PROJECTED_ANNUAL_SAVINGS': projected_annual_savings,
                                        'SAVINGS YEAR': savings_year,
                                        'YEAR': year,
                                        'REGION': region,
                                        'FACILITY': facility,
                                        'OPS_OFFICER': ops_officer,
                                        'DIRECTOR': director,
                                        'SYSTEM': system,
                                        'MONTH': month,
                                        'WEEK': week,
                                        'ACTIVE_QUEUE_FLAG': active_queue_flag,
                                        'ACTIVE_FLAG': active_flag,
                                        'ACTIVE_COMPLETE_FLAG': active_complete_flag,
                                        'QUEUE_TIME_(WEEKS)': queue_time,
                                        'DURATION_(WEEKS)': duration,
                                        'YEAR_END': "0",
                                        'YEAR_TODAY': "0",
                                        'TALLY': "1",
                                        'TALLY_C': tally_c,
                                        'PHYSICIAN_INVOLVEMENT_FLAG': physician_involvement,
                                        'PHYSICIAN_LED_FLAG': physician_led,
                                        'SAFETY_FLAG': safety_flag,
                                        'COST_SAVINGS_FLAG': cost_savings,
                                        'VALIDATED_FLAG': validated_flag,
                                        'STATUS_FLAG': status_flag,
                                        'CANCEL_FLAG': cancel_flag,
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
                scored_probability = result[0]['Scored Probabilities']
                scored_probability = float(scored_probability)*100
                print(result)
            except urllib.error.HTTPError as error:
                print("The request failed with status code: " + str(error.code))

                # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
                print(error.info())
                print(json.loads(error.read().decode("utf8", 'ignore')))

            context = {'scored_label': scored_label,
                       'scored_probability': scored_probability,
                       'form': form,}
            return HttpResponseRedirect('/response/%s/%s' % (scored_label, scored_probability))
        else:
            print(form.errors)
    else:
        form = p_form()
    context = {'form': form,}

    return render(request, 'project_management.html', context)

def response(request, val, val2):
    if val == '1':
        result = "Late"
    else:
        result = "On Time"
    context = {'result': result, 'probability':val2}
    print(val)
    print(val2)
    return render(request, 'response.html', context)
