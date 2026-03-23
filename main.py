from breeze_connect import BreezeConnect #type: ignore
import eel # type: ignore
import os

eel.init('web')

apikey = os.getenv('BREEZE_API_KEY')
apisecret = os.getenv('BREEZE_API_SECRET')


@eel.expose
def connectBreeze(sessionToken):

    if not sessionToken or not sessionToken.strip():
        return {'success': False, 'message': 'Session token is required'}

    sessionToken = sessionToken.strip()

    try:
        breeze = BreezeConnect(api_key=apikey)
        breeze.generate_session(api_secret=apisecret, session_token=sessionToken)
        return {'success': True, 'message': 'Connected successfully'}
    
    except ValueError as e:
        return {'success': False, 'message': 'Invalid API key, secret or session token: '}
    
    except Exception as e:
        return {'success': False, 'message': 'Connection failed - check logs/connect.log'}

eel.start('index.html', size=(800, 600), mode="default")
