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

    # Get the PORT from environment variables, defaulting to 5000 for local development
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, host='0.0.0.0', port=port)



