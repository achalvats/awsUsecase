import json

def lambda_handler(event, context):
    # TODO implement
    
    clusterSM = "A Megamart/Supermaket user"
    clusterSM1= " Provide mass discounts on products like 'GROCERY', 'DETERGENTS_PAPER' and 'DELICATESSEN' improve sale"  
    resultSM = "This is from Supermaket cluster. "+clusterSM+clusterSM1
        
    clusterFM = "A Freshfood/Openmarket user"
    clusterFM1= " Provide early and fresh delivery on the products like 'FRESH'and 'FROZEN'. to improve sales"
    resultFM = "This is from Freshfood cluster. "+clusterFM+clusterFM1
    
    result1 ="Found 2 clusters in the dataset"
    result= result1+"\n 1. Supermaket Cluster: "+clusterSM+clusterSM1+"\n 2. Freshfood Cluster: "+clusterFM+clusterFM1
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
              "contentType": "SSML",
              "content": result
            },
            "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                            "title":"Trends",
                            "subTitle":"Two clusters in dataset",
                            "buttons":[ 
                                {
                                    "text":"Megamart",
                                    "value":"mega mart"
                                },
                                {
                                    "text":"Freshfood",
                                    "value":"fresh food"
                                },
                                {
                                    "text":"DataSet",
                                    "value":"dataset"
                                }
                            ]
                        } 
                    ] 
                }
            }
        }
    
    print('result = ' + str(response))
    return response
    