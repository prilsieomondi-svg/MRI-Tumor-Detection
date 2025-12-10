import sys
import os

# Add application directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Set the virtual environment interpreter
INTERP = os.path.join(os.environ['HOME'], 'virtualenv', 'public_html', 'mri', '3.11', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Import the Flask app
from app import app as application

# WSGI application
if __name__ == '__main__':
    application.run()

