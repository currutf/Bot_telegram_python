import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('¡Hola! Soy un bot de respuestas automáticas. ¿En qué puedo ayudarte?')

def get_rut(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('RUT Damián: 27.350.750-2')

def get_values(update: Update, context: CallbackContext) -> None:
    # Obtener información actualizada de UF, UTM y Dólar
    sii_api_url = "https://api.sii.cl/recursos/v1.0/uf/2023-01-01"
    response = requests.get(sii_api_url)
    data = response.json()

    uf_value = data.get('UF', 'No disponible')
    utm_value = data.get('UTM', 'No disponible')

    # Puedes usar otra API para obtener el valor del dólar
    # dólar_api_url = "URL de la API del dólar"
    # response_dolar = requests.get(dólar_api_url)
    # dolar_value = response_dolar.json().get('dolar', 'No disponible')
    dolar_value = 'No disponible'

    # Responder al usuario con los valores
    update.message.reply_text(f'UF - {uf_value}\nUTM - {utm_value}\nDólar - {dolar_value}')

def calculate_pension(update: Update, context: CallbackContext) -> None:
    # Obtener valor de la UTM
    sii_api_url = "https://api.sii.cl/recursos/v1.0/utm/2023-01-01"
    response = requests.get(sii_api_url)
    data = response.json()
    utm_value = data.get('UTM', 1)  # Valor por defecto si no está disponible

    # Calcular pensión
    pension = utm_value * 2.18591

    update.message.reply_text(f'El cálculo de la pensión es: {pension}')

def main() -> None:
    updater = Updater("TOKEN")
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rut_damian", get_rut))
    dp.add_handler(CommandHandler("valores", get_values))
    dp.add_handler(CommandHandler("pension", calculate_pension))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
