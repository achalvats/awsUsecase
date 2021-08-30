 
import json

def lambda_handler(event, context):
    # TODO implement
    message = "Hi,How may I help you?"
    intent_name = event['currentIntent']['name']
    if intent_name == 'Greeting':
        return {
            'dialogAction': {
                'type': 'Close',
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": message
                    },
                "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                            "title":"Login",
                            "subTitle":"login as Employee or User",
                            "buttons":[ 
                                {
                                    "text":"Employee",
                                    "value":"employee"
                                },
                                {
                                    "text":"User",
                                    "value":"user"
                                }
                            ]
                        } 
                    ] 
                }
            }
        }
        # elif (add more intents here)
    elif intent_name == 'Employee':
        return {
            'dialogAction': {
                'type': 'Close',
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Welcome!! Let's begin."
                    },
                "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                            "title":"Avaliable Services",
                            "subTitle":"Select from the following:",
                            "buttons":[ 
                                {
                                    "text":"Trends & Analysis",
                                    "value":"trends"
                                },
                               
                                {
                                    "text":"Mask check",
                                    "value":"mask check"
                                },
                                
                                
                            ]
                        } 
                    ] 
                }
            }
        }
    elif intent_name == 'CustomerView':
        return {
            'dialogAction': {
                'type': 'Close',
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Trends & Analysis"
                    },
                "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                            
                            "subTitle":"Select from the following:",
                            "buttons":[ 
                                {
                                    "text":"Customer Clusters",
                                    "value":"customer clusters"
                                },
                                {
                                    "text":"Show Trends",
                                    "value":"show trends"
                                },
                                {
                                    "text":"Top 5 Products ",
                                    "value":"top five products"
                                },
                                {
                                    "text":"Most Searched",
                                    "value":"most searched"
                                },
                                {
                                    "text":"Most Bought",
                                    "value":"most bought"
                                }
                                
                            ]
                        } 
                    ] 
                }
            }
        }
    elif intent_name == 'User':
        return {
            'dialogAction': {
                'type': 'Close',
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Welcome!! Let's begin the shopping."
                    },
                "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                           
                            "subTitle":"Select from the following:",
                            
                            "buttons":[ 
                                {
                                    "text":"Dairy Products",
                                    "value":"dairy products"
                                },
                                 {
                                    "text":"Safety Essentials",
                                    "value":"safety essentials"
                                },
                                {
                                    "text":"Cleansers",
                                    "value":"cleansers"
                                }
                               
                            ]
                        } 
                    ] 
                }
            }
        }
    elif intent_name == 'MaskCheck':
        return {
            'dialogAction': {
                'type': 'Close',
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Proceed for Mask Check"
                    },
                "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                            "title":"Live Images",
                            "subTitle":"Choose camera",
                            
                            "buttons":[ 
                                {
                                    "text":"Cam 1",
                                    "value":"camera one"
                                },
                                {
                                    "text":"Cam 2",
                                    "value":"camera two"
                                },
                                {
                                    "text":"Cam 3",
                                    "value":"camera three"
                                },
                                {
                                    "text":"Cam 4",
                                    "value":"camera four"
                                }
                                
                            ]
                        } 
                    ] 
                }
            }
        }
    elif intent_name == 'CameraOne':
        return {
            'dialogAction': {
                'type': 'Close',
                "fulfillmentState": "Fulfilled",
               "message": {
                    "contentType": "PlainText",
                    "content": "Cam 1 feed"
                    },
                "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                            "title":"Cam 1 feed",
                            "imageUrl":"https://dl-images-arpit.s3.amazonaws.com/11.png"
                         
                        } 
                    ] 
                }
            }
        }
    elif intent_name == 'CameraTwo':
        return {
            'dialogAction': {
                'type': 'Close',
                "fulfillmentState": "Fulfilled",
               "message": {
                    "contentType": "PlainText",
                    "content": "Cam 2 feed"
                    },
                "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                            "title":"Cam 2 feed ",
                            "imageUrl":"https://dl-images-arpit.s3.amazonaws.com/13.png"
                            
                           
                        } 
                    ] 
                }
            }
        }
    elif intent_name == 'CameraThree':
        return {
            'dialogAction': {
                'type': 'Close',
                "fulfillmentState": "Fulfilled",
               "message": {
                    "contentType": "PlainText",
                    "content": "Cam 3 feed"
                    },
                "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                            "title":"Cam 3 feed ",
                            "imageUrl":"https://dl-images-arpit.s3.amazonaws.com/12.png"
                            
                           
                        } 
                    ] 
                }
            }
        }
    elif intent_name == 'CameraFour':
        return {
            'dialogAction': {
                'type': 'Close',
                "fulfillmentState": "Fulfilled",
               "message": {
                    "contentType": "PlainText",
                    "content": "Cam 4 feed"
                    },
                "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                            "title":"Cam 4 feed ",
                            "imageUrl":"https://dl-images-arpit.s3.amazonaws.com/cam4.png"
                            
                           
                        } 
                    ] 
                }
            }
        }
    elif intent_name == 'ShowTrends':
        return {
            'dialogAction': {
                'type': 'Close',
                "fulfillmentState": "Fulfilled",
                "message": {
                    "contentType": "PlainText",
                    "content": "Details"
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
                                    "text":"Dataset",
                                    "value":"dataset"
                                }
                            ]
                        } 
                    ] 
                }
            }
        }
    
    elif intent_name == 'CustomerClusters':
        return customer_cluster(event)
    elif intent_name == 'dairyproducts':
        return init_or_load_session(event)
    
        
def init_or_load_session(event):

    current = event['currentIntent']
    product = current['slots'].get('product')
    quantity = current['slots'].get('quantity')
    unit = current['slots'].get('unit')
   

    # serialize new session data
    Order = {
        'Order': 'dairyproducts',
        'Product': product,
        'Quantity': quantity,
        'Units': unit,
       
    }

    # fetch or initialize session
    session_attributes = event.get('sessionAttributes') or {}

    # update session data
    session_attributes['currentOrder'] = json.dumps(Order)
    bill_amt = generate_bill(product, quantity, unit)
    message1 = "you ordered " +quantity+ " " +unit+ " of " +product+ "."  " \n Total bill amount is {price} Rupees".format(price=bill_amt)
    return{
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": message1
            },
             "responseCard": {
                    "version": 1,
                    "contentType": "application/vnd.amazonaws.card.generic",
                    "genericAttachments": [
                        {
                            "title":"Payment",
                            
                            
                            "buttons":[ 
                                {
                                    "text":"Payment",
                                    "value":"payment"
                                }
                            ]
                        } 
                    ] 
                }
            }
        }
        
def generate_bill(product, quantity, unit):
    if str(product) == "Milk":
        amt = 60*int(quantity)
        return amt
    elif str(product) == "butter":
        amt = 300*int(quantity)
        return amt
    else:
        amt = 45*int(quantity)
        return amt  
        
def customer_cluster(event):

    current = event['currentIntent']
    slotChannel = current['slots'].get('Channel')
    slotRegion = current['slots'].get('Region')
    slotFresh = current['slots'].get('Fresh')
    slotMilk = current['slots'].get('Milk')
    slotGrocery = current['slots'].get('Grocery')
    slotFrozen = current['slots'].get('Frozen')
    slotDetPap = current['slots'].get('DetPap')
    slotDeli = current['slots'].get('Deli')
   

    # serialize new session data
    cluster_input = {
        'slotChannel':slotChannel,
        'slotRegion' :slotRegion,
        'slotFresh':slotFresh,
        'slotMilk': slotMilk,
        'slotGrocery': slotGrocery,
        'slotFrozen': slotFrozen,
        'slotDetPap':slotDetPap,
        'slotDeli':slotDeli
       
    }

    # fetch or initialize session
    session_attributes = event.get('sessionAttributes') or {}

    # update session data
    session_attributes['cluster_input'] = json.dumps(cluster_input)
    message1 = "your given cluster values " +slotChannel+ " " +slotRegion+ " of " +slotDetPap+ "."
    return{
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'Close',
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": message1
                }
                }
                }
   