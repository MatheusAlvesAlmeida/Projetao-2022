from sympy import re


register_speech = dict()
users_speech = dict()
appointment_speech = dict()
denial_speech = dict()
check_appointment_speech = dict()
reschedule_speech = dict()
cancel_speech = dict()
error_speech = dict()

# Greeting user
greetings_speech = "Olá! Eu sou o atendente virtual da UBS {}! Para poder te atender, eu preciso do seu número de cadastro do SUS. Informe apenas o número logo após essa mensagem!"

# Asking user to wait
wait_speech = "Estou muito ocupado nesse momento! Aguarde alguns minutos!"

#Registering a new user
            #nome, cpf, rg, sus, data n, end, tel

register_speech['hello'] = "Parece que é a primeira vez que você usa os serviços do atendente virtual, então vamos precisar fazer um rápido cadastro para que eu possa te conhecer melhor! Primeiro, qual o seu nome completo?"
register_speech['gender'] = "Qual o seu sexo? \n1) Masculino.\n2) Feminino."
register_speech['CPF'] = "Digite o seu CPF"
register_speech['RG'] = "Digite o seu RG"
register_speech['birth'] = "Digite a sua data de nascimento dd/mm/aa"
register_speech['address_cep'] = "Qual o seu cep?"
register_speech['address_street_number'] = "Agora digite o número de sua residência"
register_speech['phone'] = "Qual o seu telefone para contato?"
register_speech['success'] = "Pronto, seu cadastro foi realizado para os serviços do atendente virtual!"
register_speech['failure'] = "Infelizmente não foi possível realizar o seu cadastro nesse momento. Tente novamente mais tarde."

#Registered users
users_speech['hello'] = "Olá {}! Em que posso ajudar?\n1) Solicitar agendamento.\n2) Solicitar cancelamento.\n3) Consultar agendamentos. \n4) Conversar com o meu ACS. \n5) Nada."
users_speech['acs_notified'] = "O ACS responsável foi notificado e entrará em contato com você em breve!"
users_speech['end'] = "Então até a próxima!"
users_speech['invalid'] = "Opção inválida."


#Make an appointment
appointment_speech['specialty'] = "Para qual especialidade você gostaria de marcar consulta?"
#<especialidade>
appointment_speech['date_time'] = "Esses são os próximos 10 horários disponíveis para {}. Escolha o que mais lhe agrada:"
#<especialidade>, <nome ubs>, <horário escolhido>
appointment_speech['user_confirmation'] = "Você confirma que deseja marcar uma consulta para {}, na UBS {}, no seguinte horário: {}? \n1) Sim. \n2) Não."
appointment_speech['apointment_ending'] = "Seu pedido de agendamento de consulta foi encaminhado para o ACS responsável. Assim que ele processar seu pedido, eu te avisarei!"
#<link do calendar>
appointment_speech['acs_confirmation'] = "O ACS responsável confirmou o seu agendamento. Fique atento para a data e caso não seja possível comparecer no dia, solicite um cancelamento e depois agende novamente! Use esse link para adicionar a consulta como evento ao seu calendário: {}"

#Appointment denial
#<especialidade>, <nome_ubs>, <horário>
denial_speech['acs_denial'] = "O ACS responsável não foi capaz de confirmar o seu agendamento para {} em {} no horário {}. "
denial_speech['talk_to_acs'] = "Gostaria de falar diretamente com ele ou quer tentar novamente?\n1)  Solicitar um contato com o ACS. Ele entrará em contato com você assim que estiver disponível. \n2) Tentar novamente"
denial_speech['acs_notified'] = "O ACS responsável foi notificado e entrará em contato com você em breve!"

#Check appointments
check_appointment_speech['confirmed'] = "Esses são os seus agendamentos confirmados:"
check_appointment_speech['pending']= "Esses são os seus agendamentos ainda pendentes:"

#Cancel appointment
#<especialidade_escolhida>, <nome_UBS>, <data_hora_escolhida>
cancel_speech['user_confirmation'] = "Você confirma que deseja cancelar uma consulta para {}, na UBS {}, na data {}? \n 1) Sim 2) Não "
cancel_speech['appointment'] = "Qual agendamento você gostaria de cancelar?"
cancel_speech['acs_notified']  = "Seu pedido de cancelamento de consulta foi encaminhado para ACS responsável."

error_speech['invalid_number'] = "Inválido. Pode repetir? Dessa vez, escolha apenas um número das opções listadas anteriormente."
error_speech['only_numbers'] = "Pode repetir? Dessa vez, apenas o número, por favor!"