import os, glob, sys
base = sys.argv[1] if len(sys.argv)>1 else 'data'
for s in ['train','val','test']:
    print(s, len(glob.glob(os.path.join(base,s,'images','*'))),'imagens')
print('Esperado por classe: treino=32, val=4, test=4 (total A+B: 64/8/8)')
