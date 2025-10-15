import os, sys, subprocess
w=sys.argv[1]; src=sys.argv[2]; proj=sys.argv[3] if len(sys.argv)>3 else os.path.join(os.getcwd(),'runs'); name=sys.argv[4] if len(sys.argv)>4 else 'predictions'
subprocess.run(['python','detect.py','--weights',w,'--img','640','--conf','0.25','--source',src,'--project',proj,'--name',name,'--exist-ok'], check=True)
