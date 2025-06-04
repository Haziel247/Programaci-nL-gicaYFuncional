% Sensores principales
humedad_suelo(baja).  % Puede ser: baja, media, critica
temperatura_area1(29). % Temperatura en área principal (grados)
hora_actual(9).       % Hora actual (formato 24h)
pronostico_lluvia(false).

% Sensor de humedad para área secundaria
humedad_area2(media).  % Puede ser: baja, media, critica
temperatura_area2(20). % Temperatura en área secundaria

% --------------------------------------------
% REGLAS PRINCIPALES
% --------------------------------------------

% Determina si es hora adecuada para regar
hora_adecuada :-
    hora_actual(H),
    temperatura_area1(Temp),
    ((Temp > 30, (H =< 8 ; H >= 19)) ;  % Horas frescas si hace mucho calor
    (Temp =< 30, (H =< 10 ; H >= 18))).  % Horario normal

% Control de riego para área principal
activar_riego_principal :-
    humedad_suelo(Humedad),
    necesita_riego_principal(Humedad),
    pronostico_lluvia(false),
    hora_adecuada.

necesita_riego_principal(critica) :- !.
necesita_riego_principal(baja) :- !.
necesita_riego_principal(media) :-
    temperatura_area1(Temp),
    Temp > 28.  % Solo regar si temperatura es alta

% Control de riego para área secundaria
activar_riego_secundario :-
    humedad_area2(Humedad),
    necesita_riego_secundario(Humedad),
    pronostico_lluvia(false),
    hora_adecuada.

necesita_riego_secundario(critica) :- !.
necesita_riego_secundario(baja) :- !.
necesita_riego_secundario(media) :-
    temperatura_area2(Temp),
    Temp > 25,
    humedad_suelo(HPrincipal),
    HPrincipal \= critica.

% --------------------------------------------
% SISTEMA DE RECOMENDACIONES
% --------------------------------------------

% Recomendaciones generales
recomendacion_riego :-
    (activar_riego_principal ; activar_riego_secundario),
    temperatura_area2(Temp),
    (Temp > 30 ->
        writeln('Recomendación: Regar por la noche o temprano en la mañana');
        writeln('Recomendación: Puede regar en el horario establecido')).

recomendacion_riego :-
    writeln('No se requiere riego en este momento').

% Recomendaciones específicas para humedad media
recomendacion_humedad_media :-
    humedad_suelo(media),
    not(activar_riego_principal),
    writeln('Recomendación: Monitorear área principal - Humedad media detectada').

recomendacion_humedad_media :-
    humedad_area2(media),
    not(activar_riego_secundario),
    writeln('Recomendación: Monitorear área secundaria - Humedad media detectada').

% --------------------------------------------
% INTERFAZ DE USUARIO
% --------------------------------------------

% Estado del sistema
estado_riego :-
    (activar_riego_principal -> 
        writeln('Área principal: Riego ACTIVADO') ;
        writeln('Área principal: Riego desactivado')),
    
    (activar_riego_secundario -> 
        writeln('Área secundaria: Riego ACTIVADO') ;
        writeln('Área secundaria: Riego desactivado')).

% Sistema de alertas
ver_alertas :-
    (temperatura_area1(T1), T1 > 32 -> 
        writeln('Alerta: Temperatura alta en área principal') ; true),
    (temperatura_area2(T2), T2 > 32 -> 
        writeln('Alerta: Temperatura alta en área secundaria') ; true),
    (temperatura_area1(T1), T1 < 32 -> 
        writeln('Alerta: Temperatura normal en área principal') ; true),
    (temperatura_area2(T2), T2 < 32 -> 
        writeln('Alerta: Temperatura normal en área secundaria') ; true),
    (humedad_suelo(critica) -> 
        writeln('Alerta: Humedad CRÍTICA en área principal') ; true),
    (humedad_area2(critica) -> 
        writeln('Alerta: Humedad CRÍTICA en área secundaria') ; true).
