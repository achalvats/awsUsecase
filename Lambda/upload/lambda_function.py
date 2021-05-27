import json
import pickle
import boto3
from kmodes.kmodes import KModes
import pandas
from io import BytesIO

s3 = boto3.client('s3')
bucket="achal-lambda"
key='New.txt'
pickleKey='cluster.pkl'



# slotChannel = 1
# slotRegion = 2
# slotFresh = 2344
# slotMilk = 3456
# slotGrocery = 1345
# slotFrozen = 1245
# slotDetPap = 9765
# slotDeli = 2334


 
def lambda_handler(event, context):
    #getting slot values
    current = event['currentIntent']
    slotChannel = current['slots'].get('Channel')
    slotRegion = current['slots'].get('Region')
    slotFresh = current['slots'].get('Fresh')
    slotMilk = current['slots'].get('Milk')
    slotGrocery = current['slots'].get('Grocery')
    slotFrozen = current['slots'].get('Frozen')
    slotDetPap = current['slots'].get('DetPap')
    slotDeli = current['slots'].get('Deli')

    #getting pickle file from s3 bucket
    response = s3.get_object(Bucket=bucket, Key=pickleKey)
    pickled_list = response['Body'].read()
    #print(response)
    #print(pickled_list)
    
    #creating dataframe from slot values
    user_point = [slotChannel, slotRegion, slotFresh, slotMilk, slotGrocery, slotFrozen, slotDetPap, slotDeli]
    good_data_point = pandas.DataFrame(user_point).T
    print(good_data_point)

    #sample dataframe
    #sample_point = [1,2,2541.0,4737.0,6089.0,2946.0,5316.0,120.0]
    #sample_good_data_point = pandas.DataFrame(sample_point).T
    
    #loading model and prdicting
    model = pickle.loads(pickled_list)
    print('model_loaded')
    pred = model.predict(good_data_point)
    print("prediction done")
    print(pred)
    result =int(pred[0])

    
    #doing if else and adding string concat
    if result == 0:
        clusterSM = "This user is may be a a megamart or supermarket owner, every feature excluding Frozen and Fresh are above the median."
        clusterSM1= " You can increase the sale of this segement by provide mass disconts and combo on the products like 'GROCERY', 'DETERGENTS_PAPER' and 'DELICATESSEN'."
        result = "This is from Supermaket cluster. "+clusterSM+clusterSM1
    elif result == 1:
        clusterFM = "This user is may be a freshfood or a open market owner, every feature excluding Frozen and Fresh are below the median."
        clusterFM1= " You can increase the sale of this segement by provide early and fresh delivery on the products like 'FRESH'and 'FROZEN'."
        result = "This is from Freshfood cluster. "+clusterFM+clusterFM1    
    else:
        result = "Something went wrong. not a correct option"


    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": result
            },
        }
    }
    print('result = ' + str(response))
    return response
