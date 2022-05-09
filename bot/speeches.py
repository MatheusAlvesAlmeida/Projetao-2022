register_speech = dict()
users_speech = dict()
appointment_speech = dict()
denial_speech = dict()
check_appointment_speech = dict()
reschedule_speech = dict()
contact_order_speech = dict()
error_speech = dict()
 
# Greeting user
greetings_speech = "Olá! Eu sou Biu, o atendente virtual da UBS {}! Para poder te atender, eu preciso do seu *número de cadastro do SUS*. Informe apenas o número logo após essa mensagem!"
 
# Asking user to wait
wait_speech = "Estou muito ocupado nesse momento! Aguarde alguns minutos!"
 
# Asking user to send only messages with text
no_text_speech = "No momento, eu só consigo entender texto! Tente enviar uma mensagem contendo palavras da próxima vez!"
 
#Registering a new user
           #nome, cpf, rg, sus, data n, end, tel
 
register_speech['hello'] = "Parece que é a primeira vez que você usa os serviços do atendente virtual, então vamos precisar fazer um rápido cadastro para que eu possa te conhecer melhor! Primeiro, *qual o seu nome completo?*"
register_speech['gender'] = "Qual o seu sexo? \n1) Masculino.\n2) Feminino."
register_speech['CPF'] = "Digite o seu *CPF*"
register_speech['RG'] = "Digite o seu *RG*"
register_speech['birth'] = "Digite a sua *data de nascimento* dd/mm/aa"
register_speech['address_cep'] = "Qual o seu *CEP*?"
register_speech['address_street_number'] = "Agora digite o *número de sua residência*"
register_speech['phone'] = "Qual o seu *telefone* para contato?"
register_speech['success'] = "Pronto, seu cadastro foi realizado para os serviços do atendente virtual!"
register_speech['failure'] = "Infelizmente não foi possível realizar o seu cadastro nesse momento. Tente novamente mais tarde."
 
#Registered users
users_speech['hello'] = "Olá {}! Em que posso ajudar?\n1) Solicitar agendamento.\n2) Consultar agendamentos. \n3) Conversar com o meu ACS. \n4) Nada."
users_speech['acs_notified'] = "O ACS responsável foi notificado e entrará em contato com você em breve!"
users_speech['end'] = "Então até a próxima!"
users_speech['invalid'] = "Opção inválida."
 
 
#Make an appointment
appointment_speech['specialty'] = "Para qual *especialidade* você gostaria de marcar consulta?"
#<especialidade>
appointment_speech['date_time'] = "Esses são os próximos 10 horários disponíveis para {}. Escolha o que mais lhe agrada:"
#<especialidade>, <nome ubs>
appointment_speech['user_confirmation'] = "Você confirma que deseja marcar uma consulta para {}, na UBS {}? \n1) Sim. \n2) Não."
appointment_speech['apointment_ending'] = "Seu pedido de agendamento de consulta foi encaminhado para o ACS responsável. Assim que ele processar seu pedido, eu te avisarei!"
#<link do calendar>
appointment_speech['acs_confirmation'] = "O ACS responsável confirmou o seu agendamento. Fique atento para a data e caso não seja possível comparecer no dia, solicite um cancelamento e depois agende novamente! Use esse link para adicionar a consulta como evento ao seu calendário: {}"
 
#Appointment denial
#<especialidade>, <nome_ubs>, <horário>
denial_speech['acs_denial'] = "O ACS responsável não foi capaz de confirmar o seu agendamento para {} em {} no horário {}. "
denial_speech['talk_to_acs'] = "Gostaria de falar diretamente com ele ou quer tentar novamente?\n1)  Solicitar um contato com o ACS. Ele entrará em contato com você assim que estiver disponível. \n2) Tentar novamente"
denial_speech['acs_notified'] = "O ACS responsável foi notificado e entrará em contato com você em breve!"
 
#Check appointments
check_appointment_speech['confirmed'] = "Esses são os seus *agendamentos confirmados*:"
check_appointment_speech['pending']= "Esses são os seus *agendamentos ainda pendentes*:"
 
#Contact Order
contact_order_speech['contact_type'] = "Qual dessas opções melhor classifica o motivo do seu contato?\n1) Cancelar ou reagendar consulta.\n2) Dúvida acerca dos horários e funcionamento da UBS.\n3) A especialidade que quero marcar não está listada na seção de solicitação de agendamentos.\n4) Motivos pessoais.\n5) Outros.\n6) Não preciso falar com a ACS."
contact_order_speech['contact_description'] = "Em poucas palavras e em apenas uma mensagem, descreva o motivo do seu pedido de contato para que possamos agilizar o processo!"
contact_order_speech['acs_notified'] = "O ACS responsável será notificado e entrará em contato com você em breve!"
 
error_speech['invalid_number'] = "Inválido. Pode repetir? Dessa vez, escolha apenas um número das opções listadas anteriormente."
error_speech['only_numbers'] = "Pode repetir? Dessa vez, *apenas o número*, por favor!"