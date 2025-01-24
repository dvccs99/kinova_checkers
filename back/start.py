import servidor.server as sv
import os

if not os.path.exists('uploads'):
    os.makedirs('uploads')
sv.app.run(debug=True)