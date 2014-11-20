# Initialize virtualenv
source env/bin/activate
pip install -r requirements.txt

# Export local environment variables

# For use with config.py
export APP_SETTINGS="config.DevelopmentConfig"