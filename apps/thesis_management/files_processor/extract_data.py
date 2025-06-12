from .pdf_processor import handle_uploaded_pdf, get_pdf_pages, create_pdf_buffer
from django.http import JsonResponse
from openai import OpenAI
import json
import os


def request_thesis_data(request):
    try:
        thesis = request.FILES["file"]

        buffer = create_pdf_buffer(thesis)

        num_pages = get_pdf_pages(buffer)

        client = OpenAI(
            api_key=os.environ.get('API_KEY'),
            base_url=os.environ.get("API_PROVIDER"),
        )
        chat = client.chat.completions.create(
            model=os.environ.get("AI_MODEL"),
            messages=[
                {
                    "role": "system",
                    "content": """
                    The user will provide some text of a thesis in spanish. Please parse the "resumen", "palabras clave" (capitalized), "autor" (capitalized) and "titulo" and output them in JSON format. 

                    EXAMPLE INPUT: 
                    *.pdf content*

                    EXAMPLE JSON OUTPUT:
                    {
                        "titulo" : "Propuesta para el desarrollo de sistema de gestión de currículum en la UNEFA, Falcón, Punto Fijo",
                        "autor" : [{"Nombre" :"Juan", "Apellido" : "Medina"},{"Nombre" :"Luis", "Apellido" : "Medina"}],
                        "palabras clave" : ["sistema", "currículim", "gestión"],
                        "resumen" : "El presente trabajo se realizó en......",
                        "sucess" : "true"
                    }

                    You can only read the index of the content for get the pages of the contents. And make sure that each word has an empty space between them, giving it a natural appearance.

                    EXCEPTION:
                    You will return a error if you didn't find an explicit "resumen" neither "Palabras clave" neither "autores" neither "titulo". By using the following json format:

                    {
                        "sucess" : "false"
                    }

                    You will return this error if:
                        - The file isn't thesis.
                        - Don't find any of the attributes for the json.

                    NOTE: 
                    You won't to create text by yourself. Only use the content of the file you received. Only you can to touch it if isn't coorect formatted or writed.
                """
                ,
                },
                {"role": "user",
                 "content": handle_uploaded_pdf(buffer)
                },
            ],
            response_format={"type": "json_object"},
        )
        json_response = chat.choices[0].message.content
        data = json.loads(json_response)

        data["paginas"] = num_pages
        return JsonResponse(data, json_dumps_params={'ensure_ascii':False})
        """
        return JsonResponse(
                {
                    "titulo": "Jaja se te acabó la API",
                    "autor": [
                        {"Nombre": "Hernan", "Apellido": "Gonzalez"},
                        {"Nombre": "Lionel", "Apellido": "Messi"},
                    ],
                    "palabras clave": ["Ludwing", "traga", "trabas"],
                    "resumen": "no weno  pues, me jodí",
                    "success": "true",
                    "paginas": 10,
                }
            )
        """
    except Exception as e:
        return JsonResponse({"sucess": False,"message": str(e)})