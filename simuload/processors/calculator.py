from simuload.arch.service import Service
import numpy as np

class Calculator: 
     
    
    def carga_consumo(self, carga_id: int):
        consumo = np.zeros((24))
        equipamentos = Service().consultar_equip_na_carga(carga_id)
        for equip in equipamentos:
            equip_id = equip[0]
            equip_qtd = equip[2]
            equip_info = Service().consultar_equipamento_id(equip_id,
                                                            structured=True)
            consumo += equip_qtd*equip_info["Uso"]*equip_info["Potencia"]
        return consumo
    
    def curva_consumo(self,curva_id:int):
        consumo = np.zeros((24))
        cargas = Service().consultar_curva_carga(curva_id)
        for carga in cargas:
            carga_qtd = carga[2]
            consumo_carga = self.carga_consumo(carga[0])
            consumo += consumo_carga*carga_qtd
        return consumo

    def transformador_consumo(self, transformador_id: int):
        consumo = np.zeros((24))
        transformador = Service().consultar_transformador_id(transformador_id,
                                                             structured=True)
        # for equip in equipamentos:
        #     equip_id = equip[0]
        #     equip_qtd = equip[2]
        #     equip_info = Service().consultar_equipamento_id(equip_id,
        #                                                     structured=True)
        consumo += transformador["Fornecimento"]*transformador["Demanda"]
        return consumo
              
    def interpolador_transf(self, consumo_curva, intervalo = 1):
        # :param: intervalo - números de pontos na interpolação
        # Tal que num_pontos = np.ceil(24/intervalo)
        # Exemplo intervalo = 1 num_pontos = 24
        # Exemplo intervalo = 0.25 (15 min) num_pontos = 96
        values = int(24 * (60/intervalo))
        intervalo_horas = np.linspace(0, 23, 24)
        intervalo_interp = np.linspace(0, 23, values)
        consumo_curva_interp = np.interp(intervalo_interp, intervalo_horas, consumo_curva)
        return intervalo_interp, consumo_curva_interp/1000

    def interpolador_curva(self, consumo_curva, intervalo = 1):
        # :param: intervalo - números de pontos na interpolação
        # Tal que num_pontos = np.ceil(24/intervalo)
        # Exemplo intervalo = 1 num_pontos = 24
        # Exemplo intervalo = 0.25 (15 min) num_pontos = 96
        values = int(24 * (60/intervalo))
        intervalo_interp = np.linspace(0, 23, values)
        # consumo_curva_interp = np.interp(intervalo_interp, intervalo_horas, consumo_curva)
        consumo_curva_interp = [None] * values

        sum = int(values/24)
        count = 0
        np.random.seed(int(np.sum(consumo_curva)))        

        while (count < values):
            consumo_curva_interp[count] = consumo_curva[int(count/sum)]

            val = consumo_curva_interp[count]

            if(values > 24):
                i = 0
                while i < sum:
                    rgen = np.random.randint(0, 10)
                    rinv = 10 - rgen
                    consumo_curva_interp[count+i] = val*(1+rgen*0.01)
                    consumo_curva_interp[count+i+1] = val*(1-rinv*0.01)
                    i += 2

            count += sum        
        return intervalo_interp, np.array(consumo_curva_interp)/1000

    @classmethod
    def simulate_curva(cls, curva_id, curva_config):
        
        consumo_curva = Calculator().curva_consumo(curva_id)
        intervalo_config ={'5 min': 5,
                           '15 min': 15,
                           '30 min': 30,
                           '1 hora': 60                          
                        }
        return Calculator().interpolador_curva(consumo_curva,
                                         intervalo_config[curva_config])

    @classmethod
    def simulate_transf(cls, transformador_id, curva_config):
        
        consumo_transf = Calculator().transformador_consumo(transformador_id)
        intervalo_config ={'5 min': 5,
                           '15 min': 15,
                           '30 min': 30,
                           '1 hora': 60                           
                        }
        return Calculator().interpolador_transf(consumo_transf,
                                         intervalo_config[curva_config])
   
if __name__=='__main__':
    import matplotlib.pyplot as plt
    curva_id = 1
    consumo = Calculator().curva_consumo(curva_id)
    
    intervalo = 15
    intervalo_horas = np.linspace(0, 23, 24)
    intervalo_interp = np.linspace(0, 23, int(24 * (60/intervalo)))
    
    
    a = Calculator().interpolador_curva(consumo, intervalo=intervalo)
    
    plt.plot(intervalo_horas,consumo,'o')
    plt.plot(intervalo_interp, a, '-x')
    plt.show()