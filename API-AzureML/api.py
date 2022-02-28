def predict(a,b,c,d,e,f,g,h,i,j,k,l,m,n=0):
  
  import urllib.request
  import json
  import os
  import ssl

  def allowSelfSignedHttps(allowed):
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
      ssl._create_default_https_context=ssl._create_unverified_context

  allowSelfSignedHttps(True)

  data = {
      "Inputs": {
          "WebServiceInput0":
          [
              {
                  "age": a,
                  "sex": b,
                  "cp": c,
                  "trestbps": d,
                  "chol": e,
                  "fbs": f,
                  "restecg": g,
                  "thalach": h,
                  "exang": i,
                  "oldpeak": j,
                  "slope": k,
                  "ca": l,
                  "thal": m,
                  "target": n
              },
          ]
      },
      "GlobalParameters": {
      }
  }

  body = str.encode(json.dumps(data))

  url = 'http://52.226.243.118:80/api/v1/service/htatk/score'
  api_key = 'SexFGCGjcSzYFoI2aEOrFatQGH709CxQ'
  headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

  req = urllib.request.Request(url, body, headers)

  try:
      response = urllib.request.urlopen(req)
      result = response.read()
      result = json.loads(result)
      print("YOUR PROBABILITY OF HAVING A HEART ATTACK IS",end=' : ')
      print(float(result["Results"]["WebServiceOutput0"][0]["Scored Probabilities"]))
  except urllib.error.HTTPError as error:
      print("ERROR in entered values.Please enter values as described")
      """print("The request failed with status code:"+str(error.code))
      print(error.info())
      print(json.loads(error.read().decode("utf8", 'ignore')))"""