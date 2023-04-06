"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    datos=pd.read_csv('solicitudes_credito.csv',sep=';',index_col='Unnamed: 0')
    def may_min(datos):
        columnas=datos.select_dtypes(object).columns
        for i in columnas:
            datos[i]=datos[i].str.lower()
            datos[i]=datos[i].str.replace('_',' ',regex=True)
            datos[i]=datos[i].str.replace('-',' ',regex=True)
        datos=datos.dropna()  
        return datos
    datos=may_min(datos)
    datos['monto_del_credito']=datos['monto_del_credito'].str.replace('$','')
    datos['monto_del_credito']=datos['monto_del_credito'].str.replace('.','d')
    datos['monto_del_credito']=datos['monto_del_credito'].str.replace(' ','')
    datos['monto_del_credito']=datos['monto_del_credito'].str.replace('d00','')
    datos['monto_del_credito']=datos['monto_del_credito'].str.replace(',','',regex=True)
    datos['monto_del_credito']=datos['monto_del_credito'].astype(int)
    datos['comuna_ciudadano']=datos['comuna_ciudadano'].astype(int)
    datos['comuna_ciudadano']=datos['comuna_ciudadano'].astype(int)
    datos['línea_credito']=datos['línea_credito'].str.replace(' ','',regex=True)
    formatos_fecha = ['%Y/%m/%d', '%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y', '%m/%d/%Y', '%Y/%d/%m']
    def convertir_fecha(cadena):
        for formato in formatos_fecha:
            try:
                return pd.to_datetime(cadena, format=formato)
            except:
                pass
        return np.nan
    datos['fecha_de_beneficio'] = datos['fecha_de_beneficio'].apply(convertir_fecha)
    df=datos.drop_duplicates()
    return df
