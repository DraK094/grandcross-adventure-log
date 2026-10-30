import json,hashlib
from pathlib import Path
root=Path('/mnt/data')
src=json.loads((root/'GrandCross_PASSOS_1165_1169_RMI_Evidencias.json').read_text())
assert src['metadataSHA256']==hashlib.sha256((root/'global-metadata(2).dat').read_bytes()).hexdigest()
classes=src['classes']
marshal=next(c for c in classes if c['namespace']=='CommonPacket' and c['class']=='Marshaler')
handler=next(c for c in classes if c['class']=='Auth_PacketHandler')
methods=marshal['methods']
assert len(methods)==3185 and all(methods[j]['name']=='Write' and methods[j+1]['name']=='Read' for j in range(0,3184,2))
targets=['CG_RequestLoginOK','CG_RequestLoginInstantlyOK','CG_RequestNetmarbleAuthOK','CG_RequestAuthenticateCreateOK']
rows=[]
for name in targets:
 for h in [m for m in handler['methods'] if m['name']==name]:
  for p in h['params']:
   matches=[]
   for i,m in enumerate(methods):
    if m['name']=='Write' and len(m['params'])>=2 and m['params'][-1]['typeIndex']==p['typeIndex']:
     r=methods[i+1] if i+1<len(methods) else None
     matches.append({'writeToken':m['token'],'readToken':r['token'] if r and r['name']=='Read' else None,'writeTypeIndex':p['typeIndex'],'readTypeIndex':r['params'][-1]['typeIndex'] if r and r['name']=='Read' else None,'pairOrdinalZeroBased':i//2})
   rows.append({'handler':name,'parameter':p['name'],'typeIndex':p['typeIndex'],'marshalWriteMatches':matches})
assert any(x['parameter']=='userInfo' and x['marshalWriteMatches'] for x in rows)
assert any(x['parameter']=='loginServiceInfo' and x['marshalWriteMatches'] for x in rows)
result={'metadataSHA256':src['metadataSHA256'],'steps':{'1170':'Correlacionar tipos de parâmetros de handlers com overloads Write','1171':'Confirmar Write para userInfo e loginServiceInfo','1172':'Verificar pares Read adjacentes e tokens','1173':'Verificar parâmetros auxiliares e limites de correspondência','1174':'Auditoria e separação entre metadata e wire format'},'matches':rows,'limits':['Tokens de métodos IL2CPP não são IDs RMI','TypeIndex não especifica layout serializado','Adjacência Write/Read não comprova chamada em runtime','Não foi produzido byte stream real do jogo']}
p=root/'GrandCross_PASSOS_1170_1174_Evidencias.json';p.write_text(json.dumps(result,indent=2,ensure_ascii=False))
for x in rows:
 print(x['handler'],x['parameter'],x['typeIndex'], x['marshalWriteMatches'])
print('VALIDATED',p)
