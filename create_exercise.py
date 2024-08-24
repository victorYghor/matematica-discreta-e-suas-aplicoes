from pypdf import PdfWriter


def create_exercise(base_name, question_number):
    start_pattern = """\\documentclass{minimal}
\\usepackage{amsmath}

\\begin{document}"""
    end_pattern = """\\end{document}"""
    directory = base_name.split('_')[1]
    enumciado = directory + '/' + base_name + f"_enumciado{question_number}.tex"
    solucao = directory + '/' + base_name + f"_solucao{question_number}.tex"
    result_question = f"{directory}/{base_name}_exercicio{question_number}.tex"

    solucao_text = ''
    with open(enumciado, 'r') as enumciado_file:
        solucao_text += enumciado_file.read().replace(end_pattern, '')

        with open(solucao, 'r') as solucao_file:
            solucao_text += solucao_file.read().replace(start_pattern, '')

    with open(result_question, 'w') as result_question_file:
        result_question_file.write(solucao_text)

