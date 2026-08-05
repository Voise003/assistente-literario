def gerar_analise(livro, prompt):

    if "Resumo" in prompt:
        return f"""
# 📖 Resumo de {livro}

Esta é uma simulação de um resumo da obra.
"""

    elif "Personagens" in prompt:
        return f"""
# 👥 Personagens de {livro}

Aqui aparecerão os principais personagens da obra.
"""

    elif "Temas" in prompt:
        return f"""
# 🎭 Temas de {livro}

Aqui aparecerão os principais temas da obra.
"""

    elif "Simbolismos" in prompt:
        return f"""
# 🔎 Simbolismos de {livro}

Aqui aparecerão os simbolismos presentes na obra.
"""

    else:
        return f"""
# 📚 Análise completa de {livro}

## Contexto histórico

Em breve será substituído pela IA.

## Temas

...

## Personagens

...

## Simbolismos

...
"""