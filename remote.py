import json

from http.client import HTTPConnection

class RemoteIntegrate:
    ''' Camada de integração com o servidor REST/API '''

    # Constantes
    __URL__ = "localhost"
    __PORT__ = 3000


    # Métodos
    def get_pending(self):
        ''' Retornar um array com a informação de todas a queries pendentes de execução '''
        r = []
        hc = HTTPConnection(self.__URL__, port=self.__PORT__)

        try:

            hc.request("GET", "/api/pendingQuery", headers={ 'Accept' : 'application/json'})

            resp = hc.getresponse()

            if not resp is None:
                while not resp.isclosed():
                    b = resp.read()
                    data = b.decode("utf-8")
            
            if not data is None and len(data) > 0:
                try:
                    r = json.loads(data)
                except:
                    r = []

        except Exception as e:
            r = []
            raise e
        
        finally:
            hc.close()
            
        return r


    def send_data(self, data : list):
        ''' Enviar os dados para o servidor REST/API e retorna verdadeiro caso consiga '''
        r = False
        hc = HTTPConnection(self.__URL__, port=self.__PORT__)

        try:
            body = json.dumps(data)
            print(body)
            hc.request(
                "POST", "/api/pendingQuery", 
                body=body, 
                headers={ 'Accept' : 'application/json', 
                          'Content-Type' : 'application/json' })
            resp = hc.getresponse()

            print(resp.status)

            r = resp.status == 201
            
        except:
            r = False

        finally:
            hc.close()

        return r


