import os
import requests

print("LOADING DEFAULTS")

ADDRESS = os.environ.get("ADDRESS", requests.get(
    "http://checkip.amazonaws.com").text.strip())
PORT = os.environ.get("PORT", 27015)

STEAM_APP = os.environ.get("STEAM_APP", "tf2")
STEAM_APP_ID = os.environ.get("STEAM_APP_ID", 440)

STEAM_APP_DIR = os.environ.get("STEAM_APP_DIR", "/home/steam/ns2-server")
STEAM_DIR = os.environ.get("STEAM_DIR", "/home/steam/steamcmd")

APPLICATION_ID = os.environ.get("APPLICATION_ID")
INTERACTION_TOKEN = os.environ.get("INTERACTION_TOKEN")
EXECUTION_NAME = os.environ.get("EXECUTION_NAME")

WORKFLOW_ENDPOINT = os.environ.get("WORKFLOW_ENDPOINT")

# Server start variables
# https://wiki.naturalselection2.com/view/Dedicated_Server#Server_Configuration
FPS_MAX = os.environ.get("FPS_MAX", 300)
TICKRATE = os.environ.get("TICKRATE", 66)
TV_PORT = os.environ.get("TV_PORT", 27020)
CLIENT_PORT = os.environ.get("CLIENT_PORT", 27005)
MAX_PLAYERS = os.environ.get("MAX_PLAYERS", 16)
GSL_TOKEN = os.environ.get("GSL_TOKEN", "")
RCON_PASSWORD = os.environ.get("RCON_PASSWORD", "")
PASSWORD = os.environ.get("PASSWORD", "")
START_MAP = os.environ.get("START_MAP", "ctf_2fort")
SV_REGION = os.environ.get("SV_REGION", 3)
SERVER_NAME = os.environ.get("SERVER_NAME", f"ServerBoi-{STEAM_APP.upper()}")
WORKSHOP_START_MAP = os.environ.get("WORKSHOP_START_MAP", 0)
HOST_WORKSHOP_COLLECTION = os.environ.get("HOST_WORKSHOP_COLLECTION", 0)
WORKSHOP_AUTHKEY = os.environ.get("WORKSHOP_AUTHKEY", "")

DOWNLOAD_CLIENT = f"{STEAM_DIR}/steamcmd.sh +login anonymous \
        +force_install_dir {STEAM_APP_DIR} \
        +app_update {STEAM_APP_ID} \
        +quit"

RUN_CLIENT = f"{STEAM_APP_DIR}/srcds_run -game {STEAM_APP} -console -autoupdate \
    -steam_dir {STEAM_DIR} \
    -usercon \
    +fps_max {FPS_MAX} \
    -tickrate {TICKRATE} \
    -port {PORT} \
    +tv_port {TV_PORT} \
    +clientport {CLIENT_PORT} \
    +maxplayers {MAX_PLAYERS} \
    +map {START_MAP} \
    +sv_setsteamaccount {GSL_TOKEN} \
    +rcon_password {RCON_PASSWORD} \
    +sv_password {PASSWORD} \
    +sv_region {SV_REGION} \
    -ip {ADDRESS} \
    -authkey {WORKSHOP_AUTHKEY}"
