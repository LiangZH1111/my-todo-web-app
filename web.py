import streamlit as st
import functions
todos = functions.get_todo()

def add_todo():
    todo = st.session_state["new_todo"]
    functions.append_todo(todo)
    st.session_state["new_todo"] = ""

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for todo in todos:
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.remove(todo)
        functions.set_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo")
