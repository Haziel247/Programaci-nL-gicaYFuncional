% Síntomas del dengue
sintoma(fiebre).
sintoma(dolor_muscular).
sintoma(sarpullido).
sintoma(sangrado).
sintoma(dificultad_respiratoria).


% Prevención
prevencion(uso_de_repelente).
prevencion(eliminacion_de_criaderos).

% Diagnósticos posibles
diagnostico(dengue_clasico).
diagnostico(dengue_grave).

% Tratamientos
tratamiento(dengue_clasico, [hidratacion, reposo, paracetamol]).
tratamiento(dengue_grave, [hospitalizacion, suero_intravenoso]).

% Recomendaciones según diagnóstico

recomendacion(dengue_clasico, 'Mantener reposo, buena hidratacion y monitorear sintomas.').
recomendacion(dengue_grave, 'Acudir inmediatamente al hospital para atencin medica especializada.').

% Síntomas presentados por el paciente
presenta(fiebre).
presenta(dolor_muscular).
presenta(sarpullido).
presenta(sangrado).
presenta(dificultad_respiratoria).

% Reglas de diagnóstico
diagnosticar(dengue_clasico) :-
    presenta(fiebre),
    presenta(dolor_muscular),
    presenta(sarpullido).

diagnosticar(dengue_grave) :-
    presenta(fiebre),
    presenta(dolor_muscular),
    presenta(sarpullido),
    presenta(sangrado),
    presenta(dificultad_respiratoria).

% Consulta combinada: diagnóstico, tratamiento y recomendación

atencion(Diagnostico, Tratamiento, Recomendacion) :-
    diagnosticar(Diagnostico),
    tratamiento(Diagnostico, Tratamiento),
    recomendacion(Diagnostico, Recomendacion).
