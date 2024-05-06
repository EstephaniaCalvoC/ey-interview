# ey-interview

Basic chatbot API base on RAG

- **Status**:

    - [Backend code](back/README.md): Done
    - Front: Done
    - Deploy: In progress

## How to run

1. **Run back** <a id="env-vars"></a>

    Following the instructions [here](back/README.md) to start the back server

2. **Install front requirements** <a id="venv"></a>

    ~~~bash
    pip install -r requirements.txt
    ~~~

    **Note**: Make sure the virtual enviroment is activated

3. **Run front**
    ~~~bash
    streamlit run front.py
    ~~~

    Finally open http://localhost:8501/ in the browser

## Demo

**Knowlagebase**

EY report PDF: [How can AI unlock value for industrials?](https://www.ey.com/en_us/insights/advanced-manufacturing/how-can-ai-unlock-value-for-industrials)

**Results**

    **Note:** Please read from bottom to top

   ![Alt text](/demo_chat.jpg "Demochat image")
