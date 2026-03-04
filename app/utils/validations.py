from app.config.constants import MIN , MAX

def validate_prompt(text):
    if not text:
        return "Prompt inválido."

    if len(text) < MIN:
        return "Prompt muito curto."

    if len(text) > MAX:
        return "Prompt muito longo."

    return None