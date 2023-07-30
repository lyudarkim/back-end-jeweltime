import os
from application import create_app


# If the value of 'FLASK_DEBUG' isn't set, use '0' as a default value
if os.environ.get('FLASK_DEBUG', default='0') == '1':
    debug_mode = True
else:
    debug_mode = False

app = create_app()

if __name__ == "__main__":
    app.run(debug=debug_mode)
