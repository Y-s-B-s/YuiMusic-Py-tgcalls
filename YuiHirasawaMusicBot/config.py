from os import getenv
import os
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAarPlu8aVLQvZvAmR6rqEian6nW4T9n7ikGaL3vpVEs9Tg382px2t20eLz4fjSic5qFE8ICf5nF6H6PUN9Ibnrn8kNH7ZSuzjw19RUwsxDZnHz1qN68txcZNbb6_OB9KGHfPDDOq6wavVSIt0q69e4MSNMdldWKqjfHX1zJ3DZBuqXC_8ttBFRfDJIGPl_B9_77lrlOtVxuv1prU8B0DGCdORcM39u65obPu2DRAHtvdUKgVd97MgoAFH2CVkyiWJls7WBWQvxFZP71m8VS7hozVFz0VQjP-W5ln7moU2azNb68noDb3O9PzMsU8AlCgcCGMElGzMDTOUBwPMIq101bAcJiQA")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsmSafone")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/dcfdf612e499eef0e0b1f.png")
admins = {}
API_ID = int(getenv("API_ID", "3148913"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Rengoku_Kyujoro_Helper")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "CapitalLondonRadio")
PROJECT_NAME = getenv("PROJECT_NAME", "Yui v5")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Achu2234/YuiMusic-Py-tgcalls")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
