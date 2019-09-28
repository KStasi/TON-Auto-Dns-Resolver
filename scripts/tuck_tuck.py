import os
with open('../test/smart_contracts_test/hardscreen') as f:
    if 'nanograms' in f.read():
        print("true")
    else:
        cmd = 'screen -S iced -p 0 -X stuff "sendfile wallet-query.boc\n"'
        os.system(cmd)
