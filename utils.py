from docx import Document

def analyze_docx(path):
    try:
        doc = Document(path)
        full_text = "\n".join([para.text for para in doc.paragraphs if para.text.strip()])

        issues = []
        if "цель" not in full_text.lower():
            issues.append("- Не указана цель исследования.")
        if "метод" not in full_text.lower():
            issues.append("- Не описана методология.")
        if "согласие" not in full_text.lower():
            issues.append("- Нет информации о процессе информированного согласия.")

        recommended_forms = []
        if "опрос" in full_text.lower():
            recommended_forms.append("Appendix C: Internet Survey Consent Form")
        if "студент" in full_text.lower():
            recommended_forms.append("Appendix B: Written Consent Form")

        report = "## Анализ заявки\n"
        report += "\n### Проблемы:\n" + ("\n".join(issues) if issues else "Нет критичных проблем.") + "\n"
        report += "\n### Рекомендуемые формы:\n" + ("\n".join(recommended_forms) if recommended_forms else "Формы не требуются.") + "\n"
        return report
    except Exception as e:
        return f"Ошибка при обработке файла: {e}"
