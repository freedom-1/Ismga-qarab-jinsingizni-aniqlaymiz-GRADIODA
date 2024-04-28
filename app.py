import requests
import gradio as gr
from countries_code import a

def binary_search(list,item):
    low=0
    high = len(list)-1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

list1 = [a[j]['code'] for j in range(len(a))]
list2 = [a[i]['name'] for i in range(len(a))]

def name_gender(name,country):
    try:
        if name!='' and country!='':
            country = list1[binary_search(list2,country)]
            url = f"https://api.genderize.io/?name={name.title()}&country_id={country}"
            response = requests.get(url)
            if response.status_code==200:
                return response.json()
            else:
                return f"Serverdan so'rov kelmadi: {response.status_code}"
            
    except Exception as e:
        return f"Xatolik: {e}"

demo = gr.Interface(
    fn=name_gender,
    description=
    """
    <h1 align="center">Name to Gender</h1>
    O'z ismingizni kiriting va qaysi millat fuqarosi ekanligini taxmin qilib ko'ring<br>
    Creator: <a href="https://t.me/shohabbosdev">Shoh Abbos</a>
    """,
    inputs=[
        gr.Textbox(placeholder="Ismingizni kiriting...", label="Ism", autofocus=True),
        gr.Dropdown(choices=list2, value="Uzbekistan", allow_custom_value=True)
    ],
    submit_btn = gr.Button("Aniqlash", variant="primary"),
    clear_btn = gr.Button("Tozalash", variant="secondary"),
    outputs = gr.JSON(label="Natija oynasi")
)
if __name__ == "__main__":
    demo.launch(share=False)