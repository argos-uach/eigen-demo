from alerce.core import Alerce
import pandas

client = Alerce()
cols = ['mjd', 'fid', 'magpsf', 'sigmapsf']
oids = client.query_objects(class_name='RRL', page_size=2)['oid']
lcs = {oid: client.query_detections(oid, format='pandas')[cols] for oid in oids}

df = pandas.DataFrame(lcs[list(lcs.keys())[0]])
dg = pandas.DataFrame(lcs[list(lcs.keys())[1]])

print(df.columns)
#columns=['mjd','fid','magpsf','sigmapsf]
#detalles: key de lcs(estrella)
#          sacar indice de df (no funciona el index xd)
print(df)
df.to_csv("out1.csv", index=False)
dg.to_csv("out2.csv", index=False)

#print(oids)

