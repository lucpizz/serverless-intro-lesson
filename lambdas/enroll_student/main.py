# handler.py
 
import numpy as np
 
def handler(event, context):
    a = np.arange(15).reshape(3, 5)
 
    print("Your numpy array:")
    print(a)
    return {
        'statusCode': 200,
        'body': a.tolist()
    }
