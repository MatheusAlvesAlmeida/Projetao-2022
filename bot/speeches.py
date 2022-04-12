greetings_speech = "Olá! Eu sou o atendente virtual da UBS <nome_UBS>! Para poder te atender, eu preciso do seu número de cadastro do SUS. Informe apenas o número logo após essa mensagem!"
register_speech = dict()
users_speech = dict()
appointment_speech = dict()
denial_speech = dict()
check_appointment_speech = dict()
reschedule_speech = dict()
cancel_speech = dict()
error_speech = dict()

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
appointment_speech['specialty'] = "Para qual especialidade você gostaria de marcar consulta?"
appointment_speech['date_time'] = "Esses são os próximos 10 horários disponíveis para <especialidade_escolhida> em <nome_UBS>. Escolha o que mais lhe agrada: <Horários>"
appointment_speech['user_confirmation'] = "Você confirma que deseja marcar uma consulta para <especialidade_escolhida>, na <nome_UBS>, no seguinte horário: <horário_escolhido>? \n1) Sim. \n2) Não."
appointment_speech['apointment_ending'] = "Seu pedido de agendamento de consulta foi encaminhado para o ACS responsável. Assim que ele processar seu pedido, eu te avisarei!"
appointment_speech['acs_confirmation'] = "O ACS responsável confirmou o seu agendamento. Fique atento para as datas e não se esqueça de solicitar o reagendamento caso não seja possível comparecer no dia. Use esse link para adicionar a consulta como evento ao seu calendário: <link google calendar> "

#Appointment denial
denial_speech['acs_denial'] = "O ACS responsável não foi capaz de confirmar o seu agendamento."
denial_speech['talk_to_acs'] = "Gostaria de falar diretamente com ele ou quer tentar novamente?\n1)  Solicitar um contato com o ACS. Ele entrará em contato com você assim que estiver disponível. \n2) Tentar novamente"
denial_speech['acs_notified'] = "O ACS responsável foi notificado e entrará em contato com você em breve!"

#Check appointments
check_appointment_speech['confirmed'] = "Esses são os seus agendamentos confirmados:<agendamentos já confirmados que o usuário solicitou, no formato:especialidade: dd/mm/aaaa."
check_appointment_speech['pending']= "Esses são os seus agendamentos ainda pendentes:<agendamentos ainda pendentes que o usuário solicitou, no formato:especialidade: dd/mm/aaaa."

#Reschedule appointment
reschedule_speech['specialty'] = "Para qual especialidade você gostaria de reagendar a consulta? <especialidades com agendamento>"
reschedule_speech['date_time'] = "Esses são os próximos 10 horários disponíveis para <especialidade> em <UBS>: <horarios>"
reschedule_speech['user_confirmation']= "Você confirma que deseja solicitar remarcação de consulta para <especialidade>, na <nome_UBS>, no seguinte horário: <horário_escolhido>? \n1) Sim \n2) Não"
reschedule_speech['request_sent'] = "Seu pedido de agendamento de consulta foi encaminhado para o ACS responsável. Assim que ele processar seu pedido, eu te avisarei!"
reschedule_speech['acs_confirmation'] = "O ACS responsável confirmou o seu reagendamento. Fique atento para as datas e não se esqueça de solicitar o reagendamento caso não seja possível comparecer no dia. Use esse link para adicionar a consulta como evento ao seu calendário: <link google calendar> "

#Cancel appointment
cancel_speech['specialty'] = "Para qual especialidade você gostaria de reagendar a consulta? <especialidades com agendamento>"
cancel_speech['user_confirmation'] = "Você confirma que deseja cancelar uma consulta para <especialidade_escolhida>, na <nome_UBS>, no seguinte horário: <horário_escolhido> do dia: <dia_escolhido>? \n 1) Sim 2) Não "
cancel_speech['acs_notified']  = "Seu pedido de cancelamento de consulta foi encaminhado para ACS responsável."

error_speech['invalid_number'] = "Inválido. Pode repetir? Dessa vez, escolha apenas um número das opções listadas anteriormente."
error_speech['only_numbers'] = "Pode repetir? Dessa vez, apenas o número, por favor!"