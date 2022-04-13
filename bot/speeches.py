#insert ubs name
greetings_speech = "Olá! Eu sou o atendente virtual da UBS {}! Para poder te atender, eu preciso do seu número de cadastro do SUS. Informe apenas o número logo após essa mensagem!"
register_speech = dict()
users_speech = dict()
appointment_speech = dict()
denial_speech = dict()
check_appointment_speech = dict()
reschedule_speech = dict()
cancel_speech = dict()

#Registering a new user
register_speech['hello'] = "Parece que é a primeira vez que você usa os serviços do atendente virtual, então vamos precisar fazer um rápido cadastro para que eu possa te conhecer melhor! Primeiro, qual o seu nome completo?"
register_speech['gender'] = "Qual o seu sexo? \n1) Masculino.\n2) Feminino."
register_speech['phone'] = "Qual o seu telefone para contato?"
register_speech['success'] = "Pronto, seu cadastro foi realizado para os serviços do atendente virtual!"
register_speech['failure'] = "Infelizmente não foi possível realizar o seu cadastro nesse momento. Tente novamente mais tarde."

#Registered useres
users_speech['hello'] = "Olá %s! Em que posso ajudar?\n1) Solicitar agendamento.\n2) Solicitar reagendamento.\n3) Solicitar cancelamento.\n4) Consultar agendamentos. \n5) Conversar com o meu ACS. \n6) Nada."
users_speech['acs_notified'] = "O ACS responsável foi notificado e entrará em contato com você em breve!"
users_speech['end'] = "Então até a próxima!"
users_speech['invalid'] = "Opção inválida."


#Make an appointment
appointment_speech['specialty'] = "Para qual especialidade você gostaria de marcar consulta? <especialidades>"
#<especialidade>, <nome_ubs>, <horarios>
appointment_speech['date_time'] = "Esses são os próximos 10 horários disponíveis para {} em {}. Escolha o que mais lhe agrada: {}"
#<especialidade>, <nome ubs>, <horário escolhido>
appointment_speech['user_confirmation'] = "Você confirma que deseja marcar uma consulta para {}, na {}, no seguinte horário: {}? \n1) Sim. \n2) Não."
appointment_speech['apointment_ending'] = "Seu pedido de agendamento de consulta foi encaminhado para o ACS responsável. Assim que ele processar seu pedido, eu te avisarei!"
#<link do calendar>
appointment_speech['acs_confirmation'] = "O ACS responsável confirmou o seu agendamento. Fique atento para as datas e não se esqueça de solicitar o reagendamento caso não seja possível comparecer no dia. Use esse link para adicionar a consulta como evento ao seu calendário: {}"

#Appointment denial
#<especialidade>, <nome_ubs>, <horário>
denial_speech['acs_denial'] = "O ACS responsável não foi capaz de confirmar o seu agendamento para {} em {} no horário {}. "
denial_speech['talk_to_acs'] = "Gostaria de falar diretamente com ele ou quer tentar novamente?\n1)  Solicitar um contato com o ACS. Ele entrará em contato com você assim que estiver disponível. \n2) Tentar novamente"
denial_speech['acs_notified'] = "O ACS responsável foi notificado e entrará em contato com você em breve!"

#Check appointments
#<agendamentos já confirmados que o usuário solicitou, no formato:especialidade: dd/mm/aaaa.
check_appointment_speech['confirmed'] = "Esses são os seus agendamentos confirmados: {}"
#<agendamentos ainda pendentes que o usuário solicitou, no formato:especialidade: dd/mm/aaaa
check_appointment_speech['pending']= "Esses são os seus agendamentos ainda pendentes:{}"

#Reschedule appointment
#<especialidades com agendamento>
reschedule_speech['specialty'] = "Para qual especialidade você gostaria de reagendar a consulta? {}"
#<especialidade>, <nome_UBS>,<horarios>
reschedule_speech['date_time'] = "Esses são os próximos 10 horários disponíveis para {} em {}: {}"
#<especialidade>, <nome_UBS>,<horario_selecionado>
reschedule_speech['user_confirmation']= "Você confirma que deseja solicitar remarcação de consulta para {}, na {}, no seguinte horário: {} ? \n1) Sim \n2) Não"
reschedule_speech['request_sent'] = "Seu pedido de agendamento de consulta foi encaminhado para o ACS responsável. Assim que ele processar seu pedido, eu te avisarei!"
#<link google calendar>
reschedule_speech['acs_confirmation'] = "O ACS responsável confirmou o seu reagendamento. Fique atento para as datas e não se esqueça de solicitar o reagendamento caso não seja possível comparecer no dia. Use esse link para adicionar a consulta como evento ao seu calendário: {}"

#Cancel appointment
#<especialidades com agendamento>
cancel_speech['specialty'] = "Para qual especialidade você gostaria de reagendar a consulta? {}"
#<especialidade_escolhida>, <nome_UBS>, <especialidade_escolhida>, <dia_escolhido>
cancel_speech['user_confirmation'] = "Você confirma que deseja cancelar uma consulta para {}, na {}, no seguinte horário: {} do dia: {}? \n 1) Sim 2) Não "
cancel_speech['acs_notified']  = "Seu pedido de cancelamento de consulta foi encaminhado para ACS responsável."
