def diagnose(symptom):
    symptom=symptom.lower()
    if symptom=="fever":
        return "You may have Viral Infection."
    elif symptom=="cough":
        return "You may have Cold or Flu."
    elif symptom=="headache":
        return "You may be stressed or dehydrated."
    elif symptom=="stomach pain":
        return "You may have Gastric Problem."
    elif symptom=="chest pain":
        return "Please consult a doctor immediately."
    else:
        return "Sorry, symptom not found."

print("=== Medical Expert System ===")

while True:
    symp=input("\nEnter your symptoms (or exit):")
    if symp.lower()=='exit':
        print(f'Thank you!')
        break
    result=diagnose(symp)
    print('Diagnosis: ',result)
