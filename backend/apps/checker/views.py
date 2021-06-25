import pickle
from pprint import PrettyPrinter

from django.shortcuts import render
from .models import *
from .strainer import *
from .util import *


def news_checker(request):
    url = request.POST.get('enteredURL')
    print('REQUEST WAS HERE', url)
    if((url is not None) and (len(url) > 5)):
        # 1. Load the model from disk
        print("Setting up")
        svc_model = pickle.load(
            open('E:/Highway/prototype-hackathon/backend/apps/checker/svc_model.sav', 'rb'))
        mlp_model = pickle.load(open(
            'E:/Highway/prototype-hackathon/backend/apps/checker/MLPC_model.sav', 'rb'))
        log_model = pickle.load(
            open('E:/Highway/prototype-hackathon/backend/apps/checker/log_model.sav', 'rb'))
        cDict = loadCanonDict()
        ss = SoupStrainer()
        ss.init()
        print("Setup complete")
        print("Attempting URL: " + url)
        if(ss.loadAddress(url)):
            articleX = buildExampleRow(ss.extractText, cDict)
        else:
            print("Error on URL, exiting")
            return render(request, 'urlFail.html', {'URL', url})

        articleX = articleX.reshape(1, -1)

        print('NOW IT IS BELOW articleX')

        # 5. Send the X row to the model to produce a prediction
        svc_prediction = svc_model.predict(articleX)
        svc_probabilities = svc_model.predict_proba(articleX)

        mlp_prediction = mlp_model.predict(articleX)
        mlp_probabilities = mlp_model.predict_proba(articleX)

        log_prediction = log_model.predict(articleX)
        log_probabilities = log_model.predict_proba(articleX)

        # The classifications produced as predictions, espcially by the SVC, are sometimes different
        # than the highest probability. So, we'll calculate fake + dodgy and seems legit + true to come up
        # with a ruling of yes or no, is it real or not. Then we'll give the probabiilties to allow
        # the user to make up their mind.

        svc_prb = (svc_probabilities[0][0]*100, svc_probabilities[0][1]
                   * 100, svc_probabilities[0][2]*100, svc_probabilities[0][3]*100)
        svc_totFake = (svc_probabilities[0][0]
                       * 100) + (svc_probabilities[0][1]*100)
        svc_totReal = (svc_probabilities[0][2]
                       * 100) + (svc_probabilities[0][3]*100)

        mlp_prb = (mlp_probabilities[0][0]*100, mlp_probabilities[0][1]
                   * 100, mlp_probabilities[0][2]*100, mlp_probabilities[0][3]*100)
        mlp_totFake = (mlp_probabilities[0][0]
                       * 100) + (mlp_probabilities[0][1]*100)
        mlp_totReal = (mlp_probabilities[0][2]
                       * 100) + (mlp_probabilities[0][3]*100)

        log_prb = (log_probabilities[0][0]*100, log_probabilities[0][1]
                   * 100, log_probabilities[0][2]*100, log_probabilities[0][3]*100)
        log_totFake = (log_probabilities[0][0]
                       * 100) + (log_probabilities[0][1]*100)
        log_totReal = (log_probabilities[0][2]
                       * 100) + (log_probabilities[0][3]*100)

        fin_prb = ((((svc_probabilities[0][0]*100)+(mlp_probabilities[0][0]*100)+(log_probabilities[0][0]*100))/3),
                   (((svc_probabilities[0][1]*100)+(mlp_probabilities[0]
                                                    [1]*100)+(log_probabilities[0][1]*100))/3),
                   (((svc_probabilities[0][2]*100)+(mlp_probabilities[0]
                                                    [2]*100)+(log_probabilities[0][2]*100))/3),
                   (((svc_probabilities[0][3]*100)+(mlp_probabilities[0][3]*100)+(log_probabilities[0][3]*100))/3))
        fin_totFake = (svc_totFake + mlp_totFake + log_totFake)/3
        fin_totReal = (svc_totReal + mlp_totReal + log_totReal)/3

        print('NOW IT IS BELOW fin')

        # 6. Display the processed text and the results

        context = {'headline': ss.recHeadline, 'words': ss.extractText, 'url': url,
                   'svc_totFake': svc_totFake,
                   'svc_totReal': svc_totReal,
                   'svc_prediction': svc_prediction.tolist(),
                   'svc_probabilities': svc_prb,
                   'mlp_totFake': mlp_totFake,
                   'mlp_totReal': mlp_totReal,
                   'mlp_prediction': mlp_prediction.tolist(),
                   'mlp_probabilities': mlp_prb,
                   'log_totFake': log_totFake,
                   'log_totReal': log_totReal,
                   'log_prediction': log_prediction.tolist(),
                   'log_probabilities': log_prb,
                   'fin_totFake': fin_totFake,
                   'fin_totReal': fin_totReal,
                   'fin_probabilities': fin_prb
                   }

        print('SENT ALL DATA!')
        printer = PrettyPrinter(indent=4, depth=4)
        printer.pprint(context)

        return render(request, 'checker/results.html', context)
        # return JsonResponse(data=context)
    else:
        # return JsonResponse({'ERROR': "didn't receive the url"})
        return render(request, 'checker/urlform.html')
        # return render(request, 'index.html')
