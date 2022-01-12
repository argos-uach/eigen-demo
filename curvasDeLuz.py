from alerce.core import Alerce
import pandas

client = Alerce()
cols = ['mjd', 'fid', 'magpsf', 'sigmapsf']
oids = client.query_objects(class_name='RRL', page_size=1)['oid']
lcs = {oid: client.query_detections(oid, format='pandas')[cols] for oid in oids}

df = pandas.DataFrame(lcs['ZTF19aawfyoh'],index=False, columns=['mjd','fid','magpsf','sigmapsf'])
#detalles: key de lcs(estrella)
#          sacar indice de df (no funciona el index xd)
print(df)
df.to_csv("out.csv")

#print(oids)