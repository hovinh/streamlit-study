# streamlit-study

## Environment setup

```bash
conda create -n py39_streamlit python=3.9
pip install streamlit
streamlit hello
```

## Study note:

- Can quickly use streamlit to run a script:

```bash
streamlit run scripts\write_text.py
streamlit run scripts\plot_line_chart.py
```

- Streamlit auto detects if there is a change and ask to rerun your app. Choose "Always rerun".

- Data flow: any time something must be updated on the screen, Streamlit reruns your entire python script from top to bottom.
  - When you modify app code.
  - When a user interacts with widgets.
- When a callback is passed to a widget via `on_change` or `on_click` parameter, it will run before the rest of the script.

- Magic command: do not need to explicitly use streamlit commands by putting a variable or literal value on its own line, streamlit writes that to your app with `st.write()`. Turn magic off in ~/streamlit/config.toml (magicEnabled=false). Only work in main python app file.

- Widget: treat widgets as variables

```python
import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
```

- UI Layout: side bar, columns (with command to customize inside).

- Session: single instance of viewing an app. If you open 2 tabs, there are 2 sessions. If refresh, Session State resets. Makes use of Session State as dictionary to have a progressive process if you want to build upon from one rerun to the next, but exist for the existing session..
- Caching: avoid repeated execution of a function with the same input values, available for all users across different sessions. Use decorators:

  - @st.cache_data: serializable object, should work on most cases.
  - @st.cache_resource: global resources like ML models or database connection.

- Page routing: create `pages` folder. Those scripts within will show up in side bar.

- Static file serving: typically st.image<path to image> handle for you, but if you want a direct URL to a file, you need to host it in static folder.

- Secret management: in secrets.toml file, then it's accessible via st.secrets.

- Deploy: Streamlit Community Cloud launches app directly from Github repo, so app code and dependencies need to be on Github before deploying.

```
your-repo/
|-- your_app.py
|-- requirements.txt
|-- .streamlit/
    |-- config.toml
```

Have an account in https://share.streamlit.io/ and click "New app". Advanced option allows to pick python version. You can change to a custom subdomain. I tried to deploy `layout_test.py`. If there error during setup, the build process auto hook and rebuild. Check `Manage App` on bottom left for build progress. If deployed and no progress, do reboot.

## Note:

- Linux: streamlit apps cannot run from root directory. It will throw the error FileNotFoundError.
