import json
from watson_developer_cloud import ToneAnalyzerV3
from pandas.io.json import json_normalize
import pandas as pd
text = open('mytext.txt','r')
text = text.read()


tone_analyzer = ToneAnalyzerV3(
   username='881f59aa-4e34-4337-9852-62bdf34b9773',
   password='5Y7H2cCb6BQn',
   version='2016-05-19 ')

response = json.dumps(tone_analyzer.tone(text=text), indent=2)
response = json.loads(response)
data = response['document_tone']['tone_categories'][0]['tones']
df = pd.DataFrame(pd.DataFrame.from_records(
        data, 
        columns=["score", "tone_name", "tone_id"]))

df = df.sort_values(['score'], ascending=[False])
df = df.reset_index(drop=True)


tone1 = df.ix[0,1]
tone2 = df.ix[1,1]
tone3 = df.ix[2,1]


