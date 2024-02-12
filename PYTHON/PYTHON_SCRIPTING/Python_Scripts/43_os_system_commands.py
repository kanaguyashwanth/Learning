import os
cmd = "date"
rt = os.system(cmd)    # Return Code: 0 - Successful , non-zero - Failed

if rt==0:
    print("Your cmd was successfully executed")
else:
    print("Your cmd failed to execute")