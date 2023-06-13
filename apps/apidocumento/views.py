from django.http import JsonResponse
from django.views import View
import requests
import base64

class DataAPI(View):
    def __init__(self):
        pass

    @staticmethod
    def api_documentos(request, tipo_documento, numero_documento):
        try:
            result = {}
            
            if tipo_documento == '03':
                # Consultar la API de la RENIEC
                url_reniec = f'https://ws.trabajo.gob.pe/siscoweb/client/api/reniec/consolidada/128/{numero_documento}'
    
                headers = {
                    'Authorization': 'Basic TVRQRVdTOlY0R01SWFFP'
                }
                
                response_reniec = requests.get(url_reniec, headers=headers)
                data_reniec = response_reniec.json()
    
                result['nombres'] = data_reniec.get('nombres')
                result['apellidoMaterno'] = data_reniec.get('apellidoMaterno')
                result['apellidoPaterno'] = data_reniec.get('apellidoPaterno')
    
            elif tipo_documento =='26':
                #NOTE Consultar la de migraciones API
                url_migraciones = f'https://ws.trabajo.gob.pe/migraciones-rest/consulta/cpp/{numero_documento}'
                response_migraciones = requests.get(url_migraciones)
                data_migraciones = response_migraciones.json()
    
                result['nombres'] = data_migraciones['datosPersonales'].get('nombres')
                result['apellidoMaterno'] = data_migraciones['datosPersonales'].get('apematerno')
                result['apellidoPaterno'] = data_migraciones['datosPersonales'].get('apepaterno')
    
            elif tipo_documento == '06':
                #NOTE Consultar a la API de migraciones Carnet de extranjería
                url_migraciones = f'https://ws.trabajo.gob.pe/migraciones-rest/consulta/ce/{numero_documento}'
                response_migraciones = requests.get(url_migraciones)
                data_migraciones = response_migraciones.json()
    
                result['nombres'] = data_migraciones['datosPersonales'].get('nombres')
                result['apellidoMaterno'] = data_migraciones['datosPersonales'].get('apematerno')
                result['apellidoPaterno'] = data_migraciones['datosPersonales'].get('apepaterno')
    
            elif tipo_documento == '18':
                #NOTE Consultar a la API de migraciones Carnet de extranjería
                url_migraciones = f'https://ws.trabajo.gob.pe/migraciones-rest/consulta/ce/{numero_documento}'
                response_migraciones = requests.get(url_migraciones)
                data_migraciones = response_migraciones.json()
    
                result['nombres'] = data_migraciones['datosPersonales']
                result['apellidoMaterno'] = data_migraciones['datosPersonales']
                result['apellidoPaterno'] = data_migraciones['datosPersonales']
             
            #NOTE Acceder a información del request
            ip_address = request.META.get('REMOTE_ADDR')
            request_method = request.META.get('REQUEST_METHOD')

            #NOTE Agregar información adicional al resultado
            result['ip_address'] = ip_address
            result['request_method'] = request_method
    
            return JsonResponse(result)
    
        except Exception as e:
            error_message = str(e)
            return JsonResponse({'error': error_message})
        
    @staticmethod
    def api_sunat(request, nruc):
        try:
            result = {}

            url_ruc = f'https://ws.trabajo.gob.pe/siscoweb/client/api/sunat/pide/datosPrincipales/128/{nruc}/'
            

            username = 'MTPEWS'
            password = 'V4GMRXQO'
            credentials = f'{username}:{password}'
            encoded_credentials = base64.b64encode(credentials.encode()).decode('utf-8')
        
            headers = {
                    'Authorization': f'Basic {encoded_credentials}'
                }

            response_ruc = requests.get(url_ruc, headers=headers)
            data_ruc = response_ruc.json()

                       
            ip_address = request.META.get('REMOTE_ADDR')
            request_method = request.META.get('REQUEST_METHOD')

            
            result = {
                'ip_address': ip_address,
                'request_method': request_method,
               
            }

            response_data = {
                'desc_dep': data_ruc.get('desc_dep'),
                'desc_dist': data_ruc.get('desc_dist'),
                'desc_prov': data_ruc.get('desc_prov'),
                'ddp_nomvia': data_ruc.get('ddp_nomvia'),
                'ddp_nombre': data_ruc.get('ddp_nombre'),
                 **result
            }  

            return JsonResponse(response_data)

        except Exception as e:
            error_message = str(e)
            return JsonResponse({'error ': error_message})
        