import requests
import pandas as pd 

def instagram_extract(data):

    def getCreds(data) :

        creds = dict() # dictionary to hold everything
        creds['access_token'] = data.fb_access_token # access token for use with all api calls
        creds['client_id'] = data.fb_client_id, # client id from facebook app IG Graph API Test
        creds['client_secret'] = data.fb_client_secret # client secret from facebook app
        creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
        creds['graph_version'] = 'v12.0' # version of the api we are hitting
        creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
        creds['page_id'] = data.fb_page_id # users page id
        creds['instagram_account_id'] = data.fb_instagram_account_id # users instagram account id
        creds['ig_username'] = data.fb_ig_username # ig username
        creds['intagram_business_id'] = data.instagram_business_id

        return creds

    def makeApiCall( url, endpointParams = '') :

        req = url + endpointParams
        data = requests.get( req ) # make get request

        response = dict() # hold response info
        response['url'] = url # url we are hitting
        print(data.json())
        if data.ok:
            return (data.json())
        else:
            print('error')
            return ('error',data.status_code)
            

    def displayApiCallData( response ) :
        """ Print out to cli response from api call """


        print (response['endpoint_params_pretty']) # display params passed to the endpoint
        print ("\nResponse: ") # title
        print (response['json_data_pretty']) # make look pretty for cli


    def getAccountInfo( params ) :

        endpointParams = dict() # parameter to send to the endpoint
        endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}' # string of fields to get back with the request for the account
        endpointParams['access_token'] = params['access_token'] # access token

        url = params['endpoint_base'] + params['intagram_business_id'] +'?' # endpoint url
        call = list(endpointParams.keys())[0] + '=' + endpointParams['fields'] +'&'+ list(endpointParams.keys())[1] + '=' + endpointParams['access_token']
        return makeApiCall( url, call) # make the api call


    #BUSINESS ACCOUNT MEDIA
    def get_Media(params):
        
        endpointParams = dict() # parameter to send to the endpoint
        endpointParams['fields'] = 'media'
        endpointParams['access_token'] = params['access_token'] # access token
        url = params['endpoint_base'] + params['intagram_business_id'] +'?' # endpoint url
        call = list(endpointParams.keys())[0] + '=' + endpointParams['fields'] +'&'+ list(endpointParams.keys())[1] + '=' + endpointParams['access_token']
        response = makeApiCall( url, call) 
        media_Id = []
        media_Id.extend(response['media']['data'])
        media_next = response['media']['paging']['next']
        print('filled or not',media_next)
        while media_next :
            response = makeApiCall(media_next)
            media_Id.extend(response['data'])
            try:
                media_next = response['paging']['next']
            except:
                return media_Id# make the api call



    def get_media_data(params,m_id):

        endpointParams = dict()
        endpointParams['fields'] = 'caption,like_count,media_type,media_url,comments_count,timestamp'
        endpointParams['access_token'] = params['access_token'] # access token
        url = params['endpoint_base'] + m_id +'?' # endpoint url
        call = list(endpointParams.keys())[0] + '=' + endpointParams['fields'] +'&'+ list(endpointParams.keys())[1] + '=' + endpointParams['access_token']
        return makeApiCall( url, call)





    def get_media_comments(params,m_id):
        endpointParams = dict()
        endpointParams['fields'] = 'comments{id,user,username,text}'
        endpointParams['access_token'] = params['access_token'] # access token
        url = params['endpoint_base'] + m_id +'?' # endpoint url
        call = list(endpointParams.keys())[0] + '=' + endpointParams['fields'] +'&'+ list(endpointParams.keys())[1] + '=' + endpointParams['access_token']
        return makeApiCall( url, call)


    def get_media_insights(params , m_id):

        endpointParams = dict() # parameter to send to the endpoint
        #endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}' # string of fields to get back with the request for the account
        endpointParams['metric'] = 'impressions,reach,engagement'
        endpointParams['access_token'] = params['access_token'] # access token
        url = params['endpoint_base'] + m_id +'/' + 'insights' + '?'# endpoint url
        call = list(endpointParams.keys())[0] + '=' + endpointParams['metric'] +'&'+ list(endpointParams.keys())[1] + '=' + endpointParams['access_token']
        return makeApiCall( url, call)


    # facebook

    def get_fb_data(params):
        #17858983892303896?fields=caption,like_count,media_product_type,media_type,media_url,owner,permalink,shortcode,thumbnail_url,timestamp,username,comments{user},comments_count
        endpointParams = dict() # parameter to send to the endpoint
        #endpointParams['fields'] = 'business_discovery.username(' + params['ig_username'] + '){username,website,name,ig_id,id,profile_picture_url,biography,follows_count,followers_count,media_count}' # string of fields to get back with the request for the account
        endpointParams['fields'] = 'feed{created_time,actions,likes{id}},followers_count,likes'
        endpointParams['access_token'] = params['access_token'] # access token
        url = params['endpoint_base'] + params['page_id'] +'?' # endpoint url
        call = list(endpointParams.keys())[0] + '=' + endpointParams['fields'] +'&'+ list(endpointParams.keys())[1] + '=' + endpointParams['access_token']

        return makeApiCall( url, call)

    #here is where we call every thing from start to end

    params = getCreds(data)
    # all info get function
    response = getAccountInfo( params ) # hit the api for some data!
    print(response)

    info = {'username':[response['business_discovery']['username']],'media_count':[response['business_discovery']['media_count']],'followers':[response['business_discovery']['followers_count']],'following':[response['business_discovery']['follows_count'] ] }
    info
    df_info = pd.DataFrame(info)
    print('df_info: ', df_info)
    df_info.to_csv('ig_info.csv')


    #all media get function
    media = get_Media(params)
    print('media: ', media)

    current_media = media[0]['id']

    # amount of data to gather on a current media
    media_data_count = 10

    d = [get_media_data(params,current_media) for i in range(media_data_count)]
    
    df = pd.DataFrame(d)
    print('df: ', df)


    df.to_csv('ig_media.csv')

    comments_ = [get_media_comments(params,current_media) for i in range(media_data_count)]
    print('asdfkjh',comments_[1])


    c_df = pd.DataFrame(comments_)
    print('c_df: ', c_df)

    comm = pd.DataFrame(c_df.iloc[1]['comments']['data'])

    comm.to_csv('ig_comments.csv')

    
    insights_ = [get_media_insights(params,current_media) for i in range(media_data_count)]
    print('asdfkjh',insights_[1])

    insights_df = pd.DataFrame(insights_[1]['data'])
    print('insights_df: ', insights_df)



    insights_df.to_csv('ig_insights.csv')




    t = get_fb_data(params)

def instagram_extractor(data):

    instagram_extract(data)









