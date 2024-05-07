import logging
import azure.functions as func
import requests

def main(timer: func.TimerRequest) -> None:
    if timer.past_due:
        logging.info('The timer is past due!')

    logging.info('Starting the function to initialize small group rooms in Zoom.')

    # Suponemos que tienes almacenado el token de acceso en una variable de entorno o de configuración segura
    access_token = '<your_zoom_access_token>'
    meeting_id = '85866367995'  # ID de la reunión

    url = f'https://api.zoom.us/v2/meetings/{meeting_id}/meetings'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'settings': {
            'breakout_room': {
                'enable': True,
                'rooms': [
                    # Añade aquí la configuración de tus salas de grupos pequeños
                ]
            }
        }
    }

    response = requests.patch(url, headers=headers, json=payload)
    if response.status_code == 204:
        logging.info('Successfully configured breakout rooms in Zoom.')
    else:
        logging.error(f'Failed to configure breakout rooms: {response.text}')

