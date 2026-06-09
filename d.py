import threading
import jwt
import random
from threading import Thread
import json
import requests 
import google.protobuf
from protobuf_decoder.protobuf_decoder import Parser
import json
import datetime
from google.protobuf.json_format import MessageToJson
import my_message_pb2
import data_pb2
import base64
import logging
import re
import socket
from google.protobuf.timestamp_pb2 import Timestamp
import jwt_generator_pb2
import os
import binascii
import sys
import MajorLoginRes_pb2
from time import sleep
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time
import urllib3
from important_zitado import*
from byte import*
from datetime import datetime, timedelta
import queue
import hashlib
import html
import io
import psutil
import platform
import asyncio

# ==================== GHOST NEW IMPORTS ====================
from black9 import (
    EnC_AEs, EnC_PacKeT, DeCode_PackEt, EnC_Uid, EnC_Vr,
    CrEaTe_ProTo, CrEaTe_VarianT, CrEaTe_LenGTh, DecodE_HeX,
    ArA_CoLor, xBunnEr, ghost_pakcet, GenJoinSquadsPacket, ExiT,
    ChEck_Commande
)
try:
    from bite import xKEys
except ImportError:
    try:
        import xKEys
    except ImportError:
        class xKEys:
            class MyMessage:
                def ParseFromString(self, data):
                    self.field21 = 0
                    self.field22 = b''
                    self.field23 = b''

# ==================== MASRY SYSTEM IMPORTS ====================
from KEys import MyMessage as MasryKEys
from bate import Encrypt_ID, encrypt_api as bate_encrypt_api
from xH import gJwt

# ==================== LOGGING ====================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot_logs.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


TELEGRAM_BOT_TOKEN = "8661716124:AAGvWPm8jACf5b49TPYPZvGlKc4bbuKSfl0"
TELEGRAM_CHAT_ID = "-1003925048342"


GROUPS_FILE = "groups_data.json"
ACCOUNTS_FILE = "accounts.json"
ADMIN_ID = "7153983789"

USERS_FILE = "users2.json"
MAINTENANCE_FILE = "maintenance2.json"

RESTART_ON_DISCONNECT = True
MAX_RESTART_ATTEMPTS = 10
RESTART_DELAY = 5


MAX_CONCURRENT_REQUESTS = 10
MAX_ACCOUNTS = 20

ACCOUNT_RESTART_INTERVAL = 180

JWT_TOKEN = None
users = {}
maintenance_mode = False
restart_count = 0

# ==================== MASRY SYSTEM VARIABLES ====================
MaSrY_ToK = []
JWT_ToKeNs = {}
Visit_Running = {}
SpamReq_Running = {}

# ==================== MASRY KEYS ====================
MASRY_KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
MASRY_IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])

# ==================== NEW ADMIN SYSTEM VARIABLES ====================
shadowbanned_users: set = set()


def restart_bot():
    """Restart the bot"""
    print("🔄 Restarting bot...")
    p = psutil.Process(os.getpid())
    for handler in p.open_files():
        try:
            os.close(handler.fd)
        except:
            pass
    for conn in p.net_connections():
        try:
            if hasattr(conn, 'fd'):
                os.close(conn.fd)
        except:
            pass
    os.execv(sys.executable, ['python'] + sys.argv)


tempid = None
sent_inv = False
start_par = False
pleaseaccept = False
nameinv = "none"
idinv = 0
senthi = False
statusinfo = False
tempdata1 = None
tempdata = None
leaveee = False
leaveee1 = False
data22 = None
isroom = False
isroom2 = False
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


current_clients = []
command_queue = queue.Queue()
command_lock = threading.Lock()
command_processing = False
pending_messages = {}
threads = []


account_index = 0
accounts_loaded = []


last_connection_time = time.time()
CONNECTION_TIMEOUT = 300


bot_connected = False
telegram_ready = False
game_ready = False


active_requests_per_account = {}

# ==================== SPAM SYSTEM VARIABLES ====================
_target_owners = {}
_target_owners_lock = threading.Lock()
_spam_tasks = {}
_spam_active_semaphore = threading.BoundedSemaphore(15)

# ==================== GHOST SYSTEM VARIABLES ====================
account_busy_for_commands = {}
account_busy_lock = threading.Lock()
account_queue = []
account_queue_lock = threading.Lock()

# ==================== MASRY SPAM SYSTEM VARIABLES ====================
_visit_tasks = {}
_visit_tasks_lock = threading.Lock()
_friend_spam_tasks = {}
_friend_spam_tasks_lock = threading.Lock()

# ==================== ENCRYPTION CONSTANTS ====================
ENCRYPTION_KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
ENCRYPTION_IV = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])

# ==================== LIKE API CONFIG ====================
LIKE_API_URL = "https://xct-like-x-team.up.railway.app/like"


# ==================== NEW ADMIN FUNCTIONS ====================

def add_shadowban(user_id):
    """Add user to shadowban list"""
    global shadowbanned_users
    shadowbanned_users.add(int(user_id))
    logger.info(f"👻 Shadowbanned user: {user_id}")

def remove_shadowban(user_id):
    """Remove user from shadowban list"""
    global shadowbanned_users
    shadowbanned_users.discard(int(user_id))
    logger.info(f"👻 Unshadowbanned user: {user_id}")

def is_shadowbanned(user_id):
    """Check if user is shadowbanned"""
    return int(user_id) in shadowbanned_users

def delete_message(chat_id, message_id):
    """Delete a single message"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/deleteMessage"
        data = {"chat_id": chat_id, "message_id": message_id}
        response = requests.post(url, data=data, timeout=10)
        return response.json().get("ok", False)
    except:
        return False

def delete_messages_bulk(chat_id, message_ids):
    """Delete multiple messages from a group"""
    deleted = 0
    for msg_id in message_ids:
        try:
            if delete_message(chat_id, msg_id):
                deleted += 1
        except:
            pass
    return deleted

def set_group_permissions(chat_id, locked=True):
    """Lock or unlock a group"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setChatPermissions"
        
        if locked:
            permissions = {
                "can_send_messages": False,
                "can_send_media_messages": False,
                "can_send_polls": False,
                "can_send_other_messages": False,
                "can_add_web_page_previews": False,
                "can_change_info": False,
                "can_invite_users": False,
                "can_pin_messages": False
            }
        else:
            permissions = {
                "can_send_messages": True,
                "can_send_media_messages": True,
                "can_send_polls": True,
                "can_send_other_messages": True,
                "can_add_web_page_previews": True,
                "can_change_info": False,
                "can_invite_users": True,
                "can_pin_messages": False
            }
        
        data = {"chat_id": chat_id, "permissions": json.dumps(permissions)}
        response = requests.post(url, data=data, timeout=10)
        return response.json().get("ok", False)
    except Exception as e:
        logger.error(f"Lockdown error: {e}")
        return False

def ban_chat_member(chat_id, user_id):
    """Ban a member from the group"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/banChatMember"
        data = {"chat_id": chat_id, "user_id": user_id}
        response = requests.post(url, data=data, timeout=10)
        return response.json().get("ok", False)
    except Exception as e:
        logger.error(f"Ban error: {e}")
        return False

def unban_chat_member(chat_id, user_id):
    """Unban a member"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/unbanChatMember"
        data = {"chat_id": chat_id, "user_id": user_id, "only_if_banned": True}
        response = requests.post(url, data=data, timeout=10)
        return response.json().get("ok", False)
    except Exception as e:
        logger.error(f"Unban error: {e}")
        return False

def restrict_chat_member(chat_id, user_id, can_send_messages=True):
    """Restrict a member (mute/unmute)"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/restrictChatMember"
        permissions = {
            "can_send_messages": can_send_messages,
            "can_send_media_messages": can_send_messages,
            "can_send_polls": can_send_messages,
            "can_send_other_messages": can_send_messages,
            "can_add_web_page_previews": can_send_messages,
            "can_change_info": False,
            "can_invite_users": True,
            "can_pin_messages": False
        }
        data = {"chat_id": chat_id, "user_id": user_id, "permissions": json.dumps(permissions)}
        response = requests.post(url, data=data, timeout=10)
        return response.json().get("ok", False)
    except Exception as e:
        logger.error(f"Restrict error: {e}")
        return False

def get_server_stats():
    """Get server statistics"""
    stats = {}
    
    stats['os'] = f"{platform.system()} {platform.release()}"
    stats['python'] = platform.python_version()
    stats['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        import psutil
        stats['cpu_percent'] = psutil.cpu_percent(interval=0.5)
        stats['ram_percent'] = psutil.virtual_memory().percent
        stats['ram_used'] = psutil.virtual_memory().used // (1024**2)
        stats['ram_total'] = psutil.virtual_memory().total // (1024**2)
        stats['disk_percent'] = psutil.disk_usage('/').percent
        stats['disk_used'] = psutil.disk_usage('/').used // (1024**2)
        stats['disk_total'] = psutil.disk_usage('/').total // (1024**2)
    except:
        stats['cpu_percent'] = 0
        stats['ram_percent'] = 0
        stats['ram_used'] = 0
        stats['ram_total'] = 0
        stats['disk_percent'] = 0
        stats['disk_used'] = 0
        stats['disk_total'] = 0
    
    return stats

def format_server_stats(stats):
    """Format server statistics in bot style"""
    def progress_bar(value, width=10):
        filled = int((value / 100) * width)
        return f"[{'█' * filled}{'░' * (width - filled)}] {value:.1f}%"
    
    return (
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "💻 <b>SERVER STATUS</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"🖥️ <b>OS:</b> {stats['os']}\n"
        f"🐍 <b>Python:</b> {stats['python']}\n"
        f"⏰ <b>Time:</b> {stats['time']}\n\n"
        f"⚡ <b>CPU:</b> {progress_bar(stats['cpu_percent'])}\n"
        f"💾 <b>RAM:</b> {progress_bar(stats['ram_percent'])}\n"
        f"   └─ {stats['ram_used']} MB / {stats['ram_total']} MB\n"
        f"💿 <b>DISK:</b> {progress_bar(stats['disk_percent'])}\n"
        f"   └─ {stats['disk_used']} MB / {stats['disk_total']} MB\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━"
    )

def send_admin_message(message, chat_id=None, reply_to_message_id=None, parse_mode="HTML"):
    """Send a message to admin without signature"""
    try:
        if chat_id is None:
            chat_id = TELEGRAM_CHAT_ID
        
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": parse_mode
        }
        
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
            
        response = requests.post(url, data=data, timeout=10)
        return response.json()
    except Exception as e:
        logger.error(f"Error sending admin message: {e}")
        return None

def show_admin_menu(chat_id, user_id):
    """Admin commands menu (only shown to admin in private chat)"""
    if str(user_id) != ADMIN_ID:
        return None
    
    if str(chat_id).startswith('-'):
        return None
    
    return (
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "👑 <b>ADMIN COMMANDS</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "👥 <b>User Management</b> (Reply to message)\n"
        "├─ <code>/ban</code> - Ban user permanently\n"
        "├─ <code>/kick</code> - Kick user (can rejoin)\n"
        "├─ <code>/mute</code> - Mute user\n"
        "├─ <code>/unmute</code> - Unmute user\n"
        "├─ <code>/shadowban</code> - Ghost ban (messages deleted silently)\n"
        "└─ <code>/unshadowban</code> - Remove ghost ban\n\n"
        "⚡ <b>Group Control</b>\n"
        "├─ <code>/purge</code> - Delete 35 recent messages\n"
        "├─ <code>/purge 50</code> - Delete 50 messages\n"
        "├─ <code>/lockdown</code> - Freeze entire group\n"
        "└─ <code>/unlock</code> - Unfreeze group\n\n"
        "💻 <b>System</b>\n"
        "├─ <code>/server</code> - Show server statistics\n"
        "└─ <code>/start</code> - Show this menu\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━"
    )

# ==================== MASRY ENCRYPTION FUNCTIONS ====================

def EnC_AEs(HeX):
    """AES encryption for data"""
    cipher = AES.new(MASRY_KEY, AES.MODE_CBC, MASRY_IV)
    return cipher.encrypt(pad(bytes.fromhex(HeX), AES.block_size)).hex()

def encrypt_api(plain_text):
    """Encrypt API using AES-CBC"""
    plain_text = bytes.fromhex(plain_text)
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, ENCRYPTION_IV)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()

def encrypt_id(number):
    """Encrypt ID to Varint hex format"""
    number = int(number)
    encoded_bytes = []
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    return bytes(encoded_bytes).hex()

# ==================== MASRY LOAD FUNCTIONS ====================

def load_masry_tokens(filepath="MaSrY.txt"):
    """Load accounts from MaSrY.txt file"""
    global MaSrY_ToK
    if not os.path.exists(filepath):
        logger.error(f"⚠️ File {filepath} not found! No accounts loaded.")
        return False
    
    loaded = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ':' in line:
                uid, pwd = line.split(':', 1)
                loaded.append((uid.strip(), pwd.strip()))
            else:
                loaded.append((line.strip(), ''))
    
    MaSrY_ToK = loaded
    logger.info(f"✅ Loaded {len(MaSrY_ToK)} accounts from {filepath}")
    return True

def masry_update_jwt():
    """Periodically update JWT for all accounts"""
    global JWT_ToKeNs
    while True:
        for uId, PaSs in MaSrY_ToK:
            try:
                token = gJwt(uId, PaSs)
                if token:
                    JWT_ToKeNs[uId] = token
                    logger.info(f"🎫 Updated JWT for account {uId}")
            except Exception as e:
                logger.error(f"❌ Failed to update JWT for account {uId}: {e}")
        time.sleep(3600)

# ==================== MASRY SPAM FUNCTIONS ====================

def masry_send_visit(target_uid, token):
    """Send one visit request via HTTP using token"""
    try:
        enc_target = encrypt_id(target_uid)
        payload = f"08{enc_target}1801"
        enc_payload = encrypt_api(payload)
        headers = {
            "Authorization": f"Bearer {token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB53",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; Android 9)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        response = requests.post(
            "https://clientbp.ggpolarbear.com/GetPlayerPersonalShow",
            headers=headers,
            data=bytes.fromhex(enc_payload),
            timeout=10,
            verify=False
        )
        return response
    except Exception as e:
        return None

def masry_send_friend_spam(target_uid, token):
    """Send one friend request via HTTP using token"""
    try:
        enc_target = encrypt_id(target_uid)
        payload = f"08a7c4839f1e10{enc_target}1801"
        enc_payload = encrypt_api(payload)
        headers = {
            "Authorization": f"Bearer {token}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB53",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; Android 9)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        response = requests.post(
            "https://clientbp.ggpolarbear.com/RequestAddingFriend",
            headers=headers,
            data=bytes.fromhex(enc_payload),
            timeout=10,
            verify=False
        )
        return response
    except Exception as e:
        return None

# ==================== VISIT SPAM FUNCTIONS ====================

def run_visit_spam(target_uid, stop_event, chat_id, user_message_id):
    """Run visit spam loop"""
    while not stop_event.is_set():
        for uid, _ in MaSrY_ToK:
            if stop_event.is_set():
                break
            
            token = JWT_ToKeNs.get(uid)
            if not token:
                continue
            
            try:
                resp = masry_send_visit(target_uid, token)
            except Exception:
                pass
            
            time.sleep(0.05)
    
    with _visit_tasks_lock:
        if target_uid in _visit_tasks:
            del _visit_tasks[target_uid]

def start_visit_spam(target_uid, chat_id=None, user_message_id=None):
    """Start visit spam"""
    global _visit_tasks
    target_uid_str = str(target_uid)
    
    if not MaSrY_ToK:
        if chat_id and user_message_id:
            send_telegram_message(
                f"━━━━━━━━━━━━━━━━━━━━━━\n"
                f"⚠️ <b>NO ACCOUNTS</b>\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"Please add accounts to <code>accounts.txt</code> file\n"
                f"━━━━━━━━━━━━━━━━━━━━━━",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
        return False
    
    with _visit_tasks_lock:
        if target_uid_str in _visit_tasks:
            if chat_id and user_message_id:
                send_telegram_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚠️ <b>SPAM ACTIVE</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"Visit spam already running on: <code>{target_uid_str}</code>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
            return False
        
        stop_event = threading.Event()
        spam_thread = threading.Thread(
            target=run_visit_spam,
            args=(target_uid_str, stop_event, chat_id, user_message_id),
            daemon=True
        )
        _visit_tasks[target_uid_str] = (spam_thread, stop_event)
        spam_thread.start()
    
    if chat_id and user_message_id:
        send_telegram_message(
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"👁️ <b>VISIT SPAM STARTED</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🎯 <b>Target:</b> <code>{target_uid_str}</code>\n"
            f"👥 <b>Accounts:</b> {len(MaSrY_ToK)}\n"
            f"📊 <b>Status:</b> 🚀 Running\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )
    
    logger.info(f"👁️ Visit spam started on {target_uid_str}")
    return True

def stop_visit_spam(target_uid, chat_id=None, user_message_id=None):
    """Stop visit spam"""
    global _visit_tasks
    target_uid_str = str(target_uid)
    
    with _visit_tasks_lock:
        if target_uid_str not in _visit_tasks:
            if chat_id and user_message_id:
                send_telegram_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚠️ <b>NO SPAM FOUND</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"No active visit spam on: <code>{target_uid_str}</code>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
            return False
        
        thread, stop_event = _visit_tasks.pop(target_uid_str)
        stop_event.set()
    
    if chat_id and user_message_id:
        send_telegram_message(
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"⏹️ <b>VISIT SPAM STOPPED</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🎯 <b>Target:</b> <code>{target_uid_str}</code>\n"
            f"📊 <b>Status:</b> ⏹️ Stopped\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )
    
    logger.info(f"👁️ Visit spam stopped on {target_uid_str}")
    return True

# ==================== FRIEND SPAM FUNCTIONS ====================

def run_friend_spam(target_uid, stop_event, chat_id, user_message_id):
    """Run friend request spam loop"""
    while not stop_event.is_set():
        for uid, _ in MaSrY_ToK:
            if stop_event.is_set():
                break
            
            token = JWT_ToKeNs.get(uid)
            if not token:
                continue
            
            try:
                resp = masry_send_friend_spam(target_uid, token)
            except Exception:
                pass
            
            time.sleep(0.05)
    
    with _friend_spam_tasks_lock:
        if target_uid in _friend_spam_tasks:
            del _friend_spam_tasks[target_uid]

def start_friend_spam(target_uid, chat_id=None, user_message_id=None):
    """Start friend request spam"""
    global _friend_spam_tasks
    target_uid_str = str(target_uid)
    
    if not MaSrY_ToK:
        if chat_id and user_message_id:
            send_telegram_message(
                f"━━━━━━━━━━━━━━━━━━━━━━\n"
                f"⚠️ <b>NO ACCOUNTS</b>\n"
                f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                f"Please add accounts to <code>accounts.txt</code> file\n"
                f"━━━━━━━━━━━━━━━━━━━━━━",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
        return False
    
    with _friend_spam_tasks_lock:
        if target_uid_str in _friend_spam_tasks:
            if chat_id and user_message_id:
                send_telegram_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚠️ <b>SPAM ACTIVE</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"Friend spam already running on: <code>{target_uid_str}</code>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
            return False
        
        stop_event = threading.Event()
        spam_thread = threading.Thread(
            target=run_friend_spam,
            args=(target_uid_str, stop_event, chat_id, user_message_id),
            daemon=True
        )
        _friend_spam_tasks[target_uid_str] = (spam_thread, stop_event)
        spam_thread.start()
    
    if chat_id and user_message_id:
        send_telegram_message(
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"👥 <b>FRIEND SPAM STARTED</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🎯 <b>Target:</b> <code>{target_uid_str}</code>\n"
            f"👥 <b>Accounts:</b> {len(MaSrY_ToK)}\n"
            f"📊 <b>Status:</b> 🚀 Running\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )
    
    logger.info(f"👥 Friend spam started on {target_uid_str}")
    return True

def stop_friend_spam(target_uid, chat_id=None, user_message_id=None):
    """Stop friend request spam"""
    global _friend_spam_tasks
    target_uid_str = str(target_uid)
    
    with _friend_spam_tasks_lock:
        if target_uid_str not in _friend_spam_tasks:
            if chat_id and user_message_id:
                send_telegram_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚠️ <b>NO SPAM FOUND</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"No active friend spam on: <code>{target_uid_str}</code>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
            return False
        
        thread, stop_event = _friend_spam_tasks.pop(target_uid_str)
        stop_event.set()
    
    if chat_id and user_message_id:
        send_telegram_message(
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"⏹️ <b>FRIEND SPAM STOPPED</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🎯 <b>Target:</b> <code>{target_uid_str}</code>\n"
            f"📊 <b>Status:</b> ⏹️ Stopped\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )
    
    logger.info(f"👥 Friend spam stopped on {target_uid_str}")
    return True

def get_masry_spam_status():
    """Get status of all active Masry spams"""
    with _visit_tasks_lock:
        visit_count = len(_visit_tasks)
        visit_targets = list(_visit_tasks.keys())
    
    with _friend_spam_tasks_lock:
        friend_count = len(_friend_spam_tasks)
        friend_targets = list(_friend_spam_tasks.keys())
    
    return {
        'visit_count': visit_count,
        'visit_targets': visit_targets,
        'friend_count': friend_count,
        'friend_targets': friend_targets,
        'masry_accounts': len(MaSrY_ToK),
        'jwt_tokens': len(JWT_ToKeNs)
    }

def stop_all_visit_spam(chat_id=None, user_message_id=None):
    """Stop all visit spams"""
    global _visit_tasks
    with _visit_tasks_lock:
        if not _visit_tasks:
            if chat_id and user_message_id:
                send_telegram_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚠️ <b>NO ACTIVE SPAMS</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"No active visit spams to stop.",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
            return 0
        
        count = len(_visit_tasks)
        for uid, (thread, stop_event) in list(_visit_tasks.items()):
            stop_event.set()
        _visit_tasks.clear()
    
    if chat_id and user_message_id:
        send_telegram_message(
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"⏹️ <b>ALL VISITS STOPPED</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"📊 <b>Stopped:</b> {count} visit spam(s)\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )
    return count

def stop_all_friend_spam(chat_id=None, user_message_id=None):
    """Stop all friend request spams"""
    global _friend_spam_tasks
    with _friend_spam_tasks_lock:
        if not _friend_spam_tasks:
            if chat_id and user_message_id:
                send_telegram_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚠️ <b>NO ACTIVE SPAMS</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"No active friend spams to stop.",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
            return 0
        
        count = len(_friend_spam_tasks)
        for uid, (thread, stop_event) in list(_friend_spam_tasks.items()):
            stop_event.set()
        _friend_spam_tasks.clear()
    
    if chat_id and user_message_id:
        send_telegram_message(
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"⏹️ <b>ALL FRIEND SPAMS STOPPED</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"📊 <b>Stopped:</b> {count} friend spam(s)\n\n"
            f"━━━━━━━━━━━━━━━━━━━━━━",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )
    return count

# ==================== GHOST SYSTEM FUNCTIONS ====================

def init_account_queue():
    """Initialize available accounts queue for Ghost"""
    global account_queue
    with account_queue_lock:
        with command_lock:
            account_queue = []
            for client in current_clients:
                if client.is_connected and hasattr(client, 'socket_client') and client.socket_client:
                    account_queue.append(client)
            logger.info(f"👻 Ghost Queue: {len(account_queue)} clients available")

def get_next_available_ghost_client():
    """Get an available account for Ghost execution"""
    with account_queue_lock:
        with account_busy_lock:
            available_clients = []
            
            with command_lock:
                for client in current_clients:
                    if (client.is_connected and 
                        hasattr(client, 'socket_client') and 
                        client.socket_client and
                        client.key and client.iv and
                        not account_busy_for_commands.get(client.id, False)):
                        available_clients.append(client)
            
            if not available_clients:
                return None
            
            client = random.choice(available_clients)
            mark_account_busy_for_ghost(client.id)
            return client

def mark_account_busy_for_ghost(account_id):
    """Mark an account as busy for Ghost"""
    with account_busy_lock:
        account_busy_for_commands[account_id] = datetime.now()

def mark_account_free_for_ghost(account_id):
    """Free an account after Ghost execution"""
    with account_busy_lock:
        if account_id in account_busy_for_commands:
            del account_busy_for_commands[account_id]

def execute_ghost_command_new(client, teamcode, name):
    """Execute Ghost command via socket"""
    success = False
    try:
        if client.socket_client and client.key and client.iv:
            join_packet = GenJoinSquadsPacket(teamcode, client.key, client.iv)
            client.socket_client.send(join_packet)
            
            start_time = time.time()
            response_received = False
            idT = None
            sq = None
            
            while time.time() - start_time < 5:
                try:
                    if hasattr(client, 'last_received_data') and client.last_received_data:
                        hex_data = client.last_received_data.hex()
                        if '0500' in hex_data[0:4] and len(hex_data) > 30:
                            try:
                                if "08" in hex_data:
                                    decoded_data = DeCode_PackEt(f'08{hex_data.split("08", 1)[1]}')
                                else:
                                    decoded_data = DeCode_PackEt(hex_data[10:])
                                
                                dT = json.loads(decoded_data)
                                
                                if "5" in dT and "data" in dT["5"]:
                                    team_data = dT["5"]["data"]
                                    
                                    if "31" in team_data and "data" in team_data["31"]:
                                        sq = team_data["31"]["data"]
                                        idT = team_data["1"]["data"]
                                        response_received = True
                                        break
                            except Exception:
                                pass
                    time.sleep(0.1)
                except Exception:
                    time.sleep(0.1)
            
            if response_received and idT and sq:
                for _ in range(3):
                    try:
                        client.socket_client.send(GenJoinSquadsPacket(teamcode, client.key, client.iv))
                        client.socket_client.send(ghost_pakcet(idT, name, sq, client.key, client.iv))
                        time.sleep(0.1)
                        client.socket_client.send(ExiT('000000', client.key, client.iv))
                    except Exception:
                        break
                success = True
            else:
                try:
                    client.socket_client.send(ghost_pakcet(teamcode, name, "1", client.key, client.iv))
                    time.sleep(0.3)
                    success = True
                except Exception:
                    pass
    except Exception as e:
        logger.error(f"Ghost Error for client {client.client_id}: {e}")
    
    return success

def format_ghost_response(team_code, name, success_count, total_clients):
    """Format ghost response message"""
    if success_count > 0:
        message = (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>GHOSTS SENT SUCCESSFULLY</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"📝 <b>Team Code:</b> <code>{team_code}</code>\n"
            f"👤 <b>Name:</b> {name}\n"
            f"👻 <b>Ghosts Sent:</b> {success_count}\n"
            f"📊 <b>Accounts Used:</b> {total_clients}\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━"
        )
    else:
        message = (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "❌ <b>GHOST SEND FAILED</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"📝 <b>Team Code:</b> <code>{team_code}</code>\n"
            f"👤 <b>Name:</b> {name}\n"
            f"❌ <b>Status:</b> Failed to send ghosts\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━"
        )
    return message

def send_ghost_command_new(team_code, name, chat_id, user_message_id=None):
    """Send new Ghost command"""
    try:
        if not ChEck_Commande(team_code):
            send_telegram_message(
                "━━━━━━━━━━━━━━━━━━━━━━\n"
                "❌ <b>ERROR</b>\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "Invalid team code format",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
            return
        
        clients = []
        with command_lock:
            for client in current_clients:
                if (client.is_connected and 
                    hasattr(client, 'socket_client') and 
                    client.socket_client and
                    client.key and client.iv and
                    not account_busy_for_commands.get(client.id, False)):
                    clients.append(client)
                    mark_account_busy_for_ghost(client.id)
                    if len(clients) >= 3:
                        break
        
        if not clients:
            send_telegram_message(
                "━━━━━━━━━━━━━━━━━━━━━━\n"
                "❌ <b>NO ACCOUNTS AVAILABLE</b>\n"
                "━━━━━━━━━━━━━━━━━━━━━━\n\n"
                "All accounts are busy. Please try again.",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
            return
        
        success_count = 0
        threads = []
        
        for client in clients:
            account_id = client.id
            
            def run_ghost(c, acc_id):
                nonlocal success_count
                try:
                    if execute_ghost_command_new(c, team_code, name):
                        with threading.Lock():
                            success_count += 1
                finally:
                    mark_account_free_for_ghost(acc_id)
            
            thread = threading.Thread(target=run_ghost, args=(client, account_id))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join(timeout=20)
        
        result_text = format_ghost_response(team_code, name, success_count, len(clients))
        send_telegram_message(
            result_text,
            chat_id=chat_id,
            reply_to_message_id=user_message_id,
            no_signature=True
        )
        
    except Exception as e:
        logger.error(f"Error in send_ghost_command_new: {e}")
        send_telegram_message(
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"⚠️ <b>UNEXPECTED ERROR</b>\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"{str(e)[:100]}",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )

# ==================== LIKES SYSTEM FUNCTIONS ====================

def format_like_response(data: dict) -> str:
    """Format like API response in bot style"""
    try:
        status = data.get("status")
        if status != 1:
            return "━━━━━━━━━━━━━━━━━━━━━━\n❌ <b>API ERROR</b>\n━━━━━━━━━━━━━━━━━━━━━━\n\nPlease try again later."
        
        likes_added = data.get("LikesAdded", 0)
        total_likes = data.get("LikesafterCommand", 0)
        nickname = data.get("PlayerNickname", "Player")
        uid = data.get("UID", "Unknown")
        tokens_used = data.get("tokens_used", 0)
        
        message = (
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "✅ <b>LIKES ADDED SUCCESSFULLY</b>\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"👤 <b>Player:</b> {nickname}\n"
            f"🆔 <b>UID:</b> <code>{uid}</code>\n"
            f"❤️ <b>Likes Added:</b> +{likes_added}\n"
            f"📊 <b>Total Likes:</b> {total_likes}\n"
            f"⚙️ <b>Tokens Used:</b> {tokens_used}\n\n"
            "🎉 Thank you for using the bot!\n"
            "━━━━━━━━━━━━━━━━━━━━━━"
        )
        return message
    except Exception as e:
        logger.error(f"Error formatting like response: {e}")
        return "━━━━━━━━━━━━━━━━━━━━━━\n⚠️ <b>ERROR</b>\n━━━━━━━━━━━━━━━━━━━━━━\n\nFailed to process server response."

def send_likes(uid: str, chat_id: int, user_message_id: int = None):
    """Send likes request to API"""
    try:
        response = requests.get(LIKE_API_URL, params={"uid": uid}, timeout=30)
        
        if response.status_code != 200:
            send_telegram_message(
                f"━━━━━━━━━━━━━━━━━━━━━━\n❌ <b>API ERROR</b>\n━━━━━━━━━━━━━━━━━━━━━━\n\nConnection error (Code: {response.status_code})",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
            return
        
        data = response.json()
        result_text = format_like_response(data)
        
        send_telegram_message(
            result_text,
            chat_id=chat_id,
            reply_to_message_id=user_message_id,
            no_signature=True
        )
        
    except requests.exceptions.Timeout:
        send_telegram_message(
            "━━━━━━━━━━━━━━━━━━━━━━\n⏰ <b>TIMEOUT</b>\n━━━━━━━━━━━━━━━━━━━━━━\n\nConnection timeout, please try again later.",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )
    except requests.exceptions.ConnectionError:
        send_telegram_message(
            "━━━━━━━━━━━━━━━━━━━━━━\n🌐 <b>CONNECTION ERROR</b>\n━━━━━━━━━━━━━━━━━━━━━━\n\nFailed to connect to server.",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )
    except Exception as e:
        logger.error(f"Error in send_likes: {e}")
        send_telegram_message(
            f"━━━━━━━━━━━━━━━━━━━━━━\n⚠️ <b>UNEXPECTED ERROR</b>\n━━━━━━━━━━━━━━━━━━━━━━\n\n{str(e)[:100]}",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )

# ==================== PROTOBUF FUNCTIONS ====================

def encode_varint(number):
    """Encode number to Varint"""
    if number < 0:
        raise ValueError("Number must be non-negative")
    
    encoded_bytes = []
    while True:
        byte = number & 0x7F
        number >>= 7
        if number:
            byte |= 0x80
        encoded_bytes.append(byte)
        if not number:
            break
    return bytes(encoded_bytes)

def create_varint_field(field_number, value):
    """Create Varint field in Protobuf"""
    field_header = (field_number << 3) | 0
    return encode_varint(field_header) + encode_varint(value)

def create_length_delimited_field(field_number, value):
    """Create Length Delimited field in Protobuf"""
    field_header = (field_number << 3) | 2
    encoded_value = value.encode() if isinstance(value, str) else value
    return encode_varint(field_header) + encode_varint(len(encoded_value)) + encoded_value

def create_protobuf_packet(fields):
    """Create complete Protobuf packet"""
    packet = bytearray()
    
    for field, value in fields.items():
        if isinstance(value, dict):
            nested_packet = create_protobuf_packet(value)
            packet.extend(create_length_delimited_field(field, nested_packet))
        elif isinstance(value, int):
            packet.extend(create_varint_field(field, value))
        elif isinstance(value, str) or isinstance(value, bytes):
            packet.extend(create_length_delimited_field(field, value))
    
    return packet

def decrypt_id(encoded_bytes):
    """Decrypt ID from Varint"""
    encoded_bytes = bytes.fromhex(encoded_bytes)
    number = 0
    shift = 0
    for byte in encoded_bytes:
        value = byte & 0x7F
        number |= value << shift
        shift += 7
        if not byte & 0x80:
            break
    return number

# ==================== JWT FUNCTIONS ====================

def decrypt_api(cipher_text):
    """Decrypt API"""
    cipher_text_bytes = bytes.fromhex(cipher_text)
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_CBC, ENCRYPTION_IV)
    plain_text = unpad(cipher.decrypt(cipher_text_bytes), AES.block_size)
    return plain_text.hex()

def token_maker(old_access_token, new_access_token, old_open_id, new_open_id, uid):
    """Create new JWT Token"""
    now = datetime.now()
    now = str(now)[:len(str(now)) - 7]
    
    data = bytes.fromhex('1a13323032352d31312d32362030313a35313a3238220966726565206669726528013a07312e3132332e314232416e64726f6964204f532039202f204150492d3238202850492f72656c2e636a772e32303232303531382e313134313333294a0848616e6468656c64520c4d544e2f537061636574656c5a045749464960800a68d00572033234307a2d7838362d3634205353453320535345342e3120535345342e32204156582041565832207c2032343030207c20348001e61e8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e329a012b476f6f676c657c36323566373136662d393161372d343935622d396631362d303866653964336336353333a2010e3137362e32382e3133392e313835aa01026172b201203433303632343537393364653836646134323561353263616164663231656564ba010134c2010848616e6468656c64ca010d4f6e65506c7573204135303130ea014063363961653230386661643732373338623637346232383437623530613361316466613235643161313966616537343566633736616334613065343134633934f00101ca020c4d544e2f537061636574656cd2020457494649ca03203161633462383065636630343738613434323033626638666163363132306635e003b5ee02e8039a8002f003af13f80384078004a78f028804b5ee029004a78f029804b5ee02b00404c80401d2043d2f646174612f6170702f636f6d2e6474732e667265656669726574682d66705843537068495636644b43376a4c2d574f7952413d3d2f6c69622f61726de00401ea045f65363261623933353464386662356662303831646233333861636233333439317c2f646174612f6170702f636f6d2e6474732e667265656669726574682d66705843537068495636644b43376a4c2d574f7952413d3d2f626173652e61706bf00406f804018a050233329a050a32303139313139303236a80503b205094f70656e474c455332b805ff01c00504e005be7eea05093372645f7061727479f205704b717348543857393347646347335a6f7a454e6646775648746d377171316552554e6149444e67526f626f7a4942744c4f695943633459367a767670634943787a514632734f453463627974774c7334785a62526e70524d706d5752514b6d654f35766373386e51594268777148374bf805e7e4068806019006019a060134a2060134b2062213521146500e590349510e460900115843395f005b510f685b560a6107576d0f0366')
    
    data = data.replace(old_open_id.encode(), new_open_id.encode())
    data = data.replace(old_access_token.encode(), new_access_token.encode())
    
    d = encrypt_api(data.hex())
    final_payload = bytes.fromhex(d)
    
    headers = {
        "Host": "loginbp.ggpolarbear.com",
        "X-Unity-Version": "2018.4.11f1",
        "Accept": "*/*",
        "Authorization": "Bearer",
        "ReleaseVersion": "OB53",
        "X-GA": "v1 1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": str(len(final_payload)),
        "User-Agent": "Free%20Fire/2019118692 CFNetwork/3826.500.111.2.2 Darwin/24.4.0",
        "Connection": "keep-alive"
    }
    
    URL = "https://loginbp.ggpolarbear.com/MajorLogin"
    
    try:
        response = requests.post(URL, headers=headers, data=final_payload, verify=False)
        
        if response.status_code == 200:
            if len(response.text) < 10:
                return False
            jwt_start = response.text.find("eyJhbGciOiJIUzI1NiIsInN2ciI6IjEiLCJ0eXAiOiJKV1QifQ")
            if jwt_start == -1:
                return False
            BASE64_TOKEN = response.text[jwt_start:-1]
            second_dot_index = BASE64_TOKEN.find(".", BASE64_TOKEN.find(".") + 1)
            if second_dot_index != -1:
                BASE64_TOKEN = BASE64_TOKEN[:second_dot_index + 44]
            return BASE64_TOKEN
        else:
            logger.error(f"MajorLogin failed with status: {response.status_code}")
            return False
    except Exception as e:
        logger.error(f"Error in token_maker: {e}")
        return False

def fetch_jwt_token(max_retries=10, retry_delay=5):
    """Fetch new JWT Token from Garena with multiple attempts"""
    for attempt in range(max_retries):
        try:
            uid = "5007239992"
            password = "7658675B67033388C0BEFF66E21882A21CFEBFE107ECB63B4231892BCEA39FE0"
            
            url = "https://100067.connect.garena.com/oauth/guest/token/grant"
            headers = {
                "Host": "100067.connect.garena.com",
                "User-Agent": "GarenaMSDK/4.0.19P4(G011A ;Android 9;en;US;)",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "close",
            }
            data = {
                "uid": f"{uid}",
                "password": f"{password}",
                "response_type": "token",
                "client_type": "2",
                "client_secret": "",
                "client_id": "100067",
            }
            
            response = requests.post(url, headers=headers, data=data, verify=False)
            response_data = response.json()
            
            if "access_token" in response_data and "open_id" in response_data:
                new_access_token = response_data['access_token']
                new_open_id = response_data['open_id']
                old_access_token = "c69ae208fad72738b674b2847b50a3a1dfa25d1a19fae745fc76ac4a0e414c94"
                old_open_id = "4306245793de86da425a52caadf21eed"
                
                token = token_maker(old_access_token, new_access_token, old_open_id, new_open_id, uid)
                if token:
                    logger.info(f"✅ JWT Token fetched successfully on attempt {attempt + 1}")
                    return token
                else:
                    logger.warning(f"⚠️ token_maker returned None on attempt {attempt + 1}")
            else:
                error_msg = response_data.get('error', 'Unknown error')
                logger.warning(f"⚠️ Attempt {attempt + 1}/{max_retries} failed: {error_msg}")
                
        except Exception as e:
            logger.warning(f"⚠️ Attempt {attempt + 1}/{max_retries} error: {e}")
        
        if attempt < max_retries - 1:
            logger.info(f"⏳ Waiting {retry_delay} seconds before retry...")
            time.sleep(retry_delay)
    
    logger.error(f"❌ Failed to fetch JWT token after {max_retries} attempts")
    return None

def update_jwt_periodically():
    """Update JWT Token every hour"""
    global JWT_TOKEN
    while True:
        time.sleep(3600)
        
        logger.info("🔄 Attempting to refresh JWT token...")
        
        for retry in range(5):
            new_token = fetch_jwt_token(max_retries=3, retry_delay=3)
            if new_token:
                JWT_TOKEN = new_token
                logger.info("✅ JWT Token refreshed successfully")
                break
            else:
                logger.warning(f"⚠️ Refresh attempt {retry + 1}/5 failed, waiting 10 seconds...")
                time.sleep(10)
        else:
            logger.error("❌ Failed to refresh JWT token after multiple attempts, will try again in 1 hour")

# ==================== FRIEND SYSTEM FUNCTIONS ====================

def send_friend_request(player_id):
    """Send friend request"""
    global JWT_TOKEN
    
    if not JWT_TOKEN:
        return "⚠️ Token is currently unavailable"
    
    try:
        enc_id = encrypt_id(player_id)
        payload = f"08a7c4839f1e10{enc_id}1801"
        encrypted_payload = encrypt_api(payload)
        
        url = "https://clientbp.ggpolarbear.com/RequestAddingFriend"
        headers = {
            "Authorization": f"Bearer {JWT_TOKEN}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB53",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; Android 9)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        
        response = requests.post(url, headers=headers, data=bytes.fromhex(encrypted_payload), timeout=15, verify=False)
        
        if response.status_code == 200:
            if "BR_FRIEND_NOT_SAME_REGION" in response.text:
                return "❌ The player cannot be added because he is not in your region."
            return "✅ The friend request was sent successfully."
        elif response.status_code == 401:
            JWT_TOKEN = None
            return "❌ The token is invalid, it will be updated automatically."
        elif response.status_code == 400:
            if "BR_FRIEND_NOT_SAME_REGION" in response.text:
                return "❌ The player cannot be added because he is not in your region."
            return "❌ Request error"
        else:
            return f"❌ Failed to send request (code: {response.status_code})"
            
    except Exception as e:
        logger.error(f"Error in send_friend_request: {e}")
        return f"❌ An error occurred: {str(e)}"

def remove_friend(player_id):
    """Remove friend from list"""
    global JWT_TOKEN
    
    if not JWT_TOKEN:
        return "⚠️ Token is currently unavailable"
    
    try:
        enc_id = encrypt_id(player_id)
        payload = f"08a7c4839f1e10{enc_id}1802"
        encrypted_payload = encrypt_api(payload)
        
        url = "https://clientbp.ggpolarbear.com/RemoveFriend"
        headers = {
            "Authorization": f"Bearer {JWT_TOKEN}",
            "X-Unity-Version": "2018.4.11f1",
            "X-GA": "v1 1",
            "ReleaseVersion": "OB53",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Dalvik/2.1.0 (Linux; Android 9)",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        
        response = requests.post(url, headers=headers, data=bytes.fromhex(encrypted_payload), timeout=15, verify=False)
        
        if response.status_code == 200:
            return "✅ Deleted successfully"
        elif response.status_code == 401:
            JWT_TOKEN = None
            return "❌ Invalid token"
        elif response.status_code == 400:
            return f"❌ Deletion failed (Error 400)"
        elif response.status_code == 404:
            return "❌ Player not on list"
        else:
            return f"❌ Deletion failed (Code: {response.status_code})"
            
    except Exception as e:
        logger.error(f"Error in remove_friend: {e}")
        return f"❌ Error occurred: {str(e)}"

def get_player_info(uid):
    """Get player info from external API"""
    try:
        response = requests.get(f"https://jagwar-info.vercel.app/player-info?uid={uid}", timeout=10)
        data = response.json()
        info = data.get("basicInfo", {})
        name = info.get("nickname", "Unknown")
        region = info.get("region", "N/A")
        level = info.get("level", "N/A")
        return name, region, level
    except Exception as e:
        logger.error(f"Error fetching info for {uid}: {e}")
        return "Unknown", "N/A", "N/A"

# ==================== DETAILED PLAYER INFO FUNCTIONS ====================

def format_player_info_detailed(data: dict) -> str:
    """Format detailed player information in bot style"""
    info = data.get("basicInfo", {})
    clan = data.get("clanBasicInfo", {})
    captain = data.get("captainBasicInfo", {})
    pet = data.get("petInfo", {})
    social = data.get("socialInfo", {})
    credit = data.get("creditScoreInfo", {})
    diamond = data.get("diamondCostRes", {})
    
    formatted_text = (
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "📋 <b>ACCOUNT INFO</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"├─ <b>NAME:</b> {info.get('nickname', 'N/A')}\n"
        f"├─ <b>UID:</b> <code>{info.get('accountId', 'N/A')}</code>\n"
        f"├─ <b>Region:</b> {info.get('region', 'N/A')}\n"
        f"└─ <b>Level:</b> {info.get('level', 'N/A')} | <b>EXP:</b> {info.get('exp', 0):,}\n\n"
        "🎖 <b>RANK INFO</b>\n"
        f"├─ <b>BR Rank:</b> {info.get('rank', 'N/A')} | {info.get('rankingPoints', 0)} pts\n"
        f"├─ <b>Max Rank:</b> {info.get('maxRank', 'N/A')}\n"
        f"└─ <b>CS Rank:</b> {info.get('csRank', 'N/A')} | {info.get('csRankingPoints', 0)} pts\n\n"
        "📊 <b>ACCOUNT DETAILS</b>\n"
        f"├─ <b>Badges:</b> {info.get('badgeCnt', 0)}\n"
        f"├─ <b>Likes:</b> {info.get('liked', 0):,}\n"
        f"├─ <b>Elite Pass:</b> No\n"
        f"├─ <b>Season:</b> {info.get('seasonId', 'N/A')}\n"
        f"└─ <b>Version:</b> {info.get('releaseVersion', 'N/A')}\n\n"
        f"💎 <b>Diamond Cost:</b> {diamond.get('diamondCost', 0)}\n\n"
        "⭐ <b>CREDIT SCORE</b>\n"
        f"├─ <b>Score:</b> {credit.get('creditScore', 0)}\n"
        f"└─ <b>From:</b> N/A\n\n"
        "🏰 <b>CLAN INFO</b>\n"
        f"├─ <b>Name:</b> {clan.get('clanName', 'N/A')}\n"
        f"├─ <b>ID:</b> {clan.get('clanId', 'N/A')}\n"
        f"└─ <b>Level:</b> {clan.get('clanLevel', 'N/A')}\n\n"
        "👑 <b>LEADER INFO</b>\n"
        f"├─ <b>Nickname:</b> {captain.get('nickname', 'N/A')}\n"
        f"├─ <b>Level:</b> {captain.get('level', 'N/A')}\n"
        f"└─ <b>Likes:</b> {captain.get('liked', 0):,}\n\n"
        "🐾 <b>PET INFO</b>\n"
        f"├─ <b>Level:</b> {pet.get('level', 'N/A')}\n"
        f"├─ <b>EXP:</b> {pet.get('exp', 0)}\n"
        f"├─ <b>Pet ID:</b> {pet.get('id', 'N/A')}\n"
        f"└─ <b>Skill ID:</b> {pet.get('selectedSkillId', 'N/A')}\n\n"
        "🌐 <b>SOCIAL INFO</b>\n"
        f"├─ <b>Language:</b> {social.get('language', 'N/A')}\n"
        f"└─ <b>Signature:</b>\n{social.get('signature', 'No signature')}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "👑 <b>Developer: JAGWAR KING</b>\n"
        "━━━━━━━━━━━━━━━━━━━━━━"
    )
    
    return formatted_text

def fetch_player_image(uid: str):
    """Fetch player image from external API"""
    try:
        image_url = f"https://jagwar-outfit.vercel.app/outfit-image?uid={uid}&key=JOT-TEAM"
        response = requests.get(image_url, timeout=20)
        
        if response.status_code == 200:
            return True, response.content
        else:
            return False, None
    except:
        return False, None

def send_player_info_with_image(player_id, chat_id, user_message_id=None):
    """Send player information with image to Telegram"""
    try:
        info_url = f"https://jagwar-info.vercel.app/player-info?uid={player_id}"
        info_response = requests.get(info_url, timeout=15)
        
        if info_response.status_code != 200:
            send_telegram_message(
                f"❌ Error: Player not found\n├─ UID: <code>{player_id}</code>",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
            return
        
        info_data = info_response.json()
        
        if not info_data or "basicInfo" not in info_data:
            send_telegram_message(
                f"❌ Player not found\n├─ UID: <code>{player_id}</code>",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
            return
        
        caption = format_player_info_detailed(info_data)
        
        image_success, image_bytes = fetch_player_image(player_id)
        
        if image_success and image_bytes:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendPhoto"
            files = {
                'photo': (f'{player_id}.png', io.BytesIO(image_bytes), 'image/png')
            }
            data = {
                'chat_id': chat_id,
                'caption': caption,
                'parse_mode': 'HTML'
            }
            if user_message_id:
                data['reply_to_message_id'] = user_message_id
            
            response = requests.post(url, data=data, files=files, timeout=30)
            
            if response.status_code != 200:
                send_telegram_message(
                    caption,
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id,
                    no_signature=True
                )
        else:
            send_telegram_message(
                caption,
                chat_id=chat_id,
                reply_to_message_id=user_message_id,
                no_signature=True
            )
            
    except Exception as e:
        logger.error(f"Error in send_player_info_with_image: {e}")
        send_telegram_message(
            f"❌ Error fetching player info\n└─ {str(e)[:100]}",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )

def load_users():
    """Load user data from JSON file"""
    global users
    if os.path.exists(USERS_FILE):
        try:
            with open(USERS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    users = data
                    return users
        except json.JSONDecodeError:
            pass
    users = {}
    return users

def save_users():
    """Save user data to JSON file"""
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=4)

def load_maintenance_status():
    """Load maintenance status"""
    global maintenance_mode
    if os.path.exists(MAINTENANCE_FILE):
        try:
            with open(MAINTENANCE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                maintenance_mode = data.get("maintenance_mode", False)
                return maintenance_mode
        except json.JSONDecodeError:
            pass
    maintenance_mode = False
    return maintenance_mode

def save_maintenance_status(status):
    """Save maintenance status"""
    global maintenance_mode
    maintenance_mode = status
    with open(MAINTENANCE_FILE, "w", encoding="utf-8") as f:
        json.dump({"maintenance_mode": status}, f)

def get_total_users_count():
    """Get total number of added users"""
    count = 0
    for uid, data in users.items():
        if isinstance(data, dict) and "name" in data and "expiry" in data:
            count += 1
    return count

def format_remaining_time(expiry_time):
    """Format remaining time"""
    remaining = int(expiry_time - time.time())
    if remaining <= 0:
        return "⛔ Expired"
    
    days = remaining // 86400
    hours = (remaining % 86400) // 3600
    minutes = ((remaining % 86400) % 3600) // 60
    seconds = remaining % 60
    
    parts = []
    if days > 0:
        parts.append(f"{days} day")
    if hours > 0:
        parts.append(f"{hours} hour")
    if minutes > 0:
        parts.append(f"{minutes} minute")
    parts.append(f"{seconds} second")
    
    return " ".join(parts)

def remove_expired_users():
    """Automatically remove expired users"""
    global users
    now = time.time()
    expired = [uid for uid, data in users.items() if isinstance(data, dict) and data.get("expiry", 0) <= now]
    
    for uid in expired:
        if uid in users:
            if users[uid].get("added_by_tele_id"):
                remove_friend(uid)
            del users[uid]
    
    if expired:
        save_users()
        logger.info(f"🗑️ Removed {len(expired)} expired users")

def check_expired_users_periodically():
    """Periodically check for expired users"""
    while True:
        remove_expired_users()
        time.sleep(60)

def reset_daily_adds():
    """Reset daily add count"""
    global users
    now = datetime.now()
    for tele_id in list(users.keys()):
        if isinstance(users[tele_id], dict) and 'last_reset_day' in users[tele_id]:
            last_reset = datetime.fromtimestamp(users[tele_id]['last_reset_day'])
            if now.date() > last_reset.date():
                users[tele_id]['adds_today'] = 0
                users[tele_id]['last_reset_day'] = now.timestamp()
    save_users()

def daily_reset_timer():
    """Daily reset timer"""
    while True:
        reset_daily_adds()
        time.sleep(3600)

def send_message_to_all_groups(message_text):
    """Send message to all active groups"""
    groups_data = load_groups_data()
    for chat_id in groups_data.keys():
        try:
            send_telegram_message(message_text, chat_id=int(chat_id), parse_mode="HTML", no_signature=True)
            time.sleep(1)
        except Exception as e:
            logger.error(f"Failed to send message to group {chat_id}: {e}")

# ==================== ORIGINAL FUNCTIONS ====================

def load_accounts():
    """Load accounts from JSON file"""
    global accounts_loaded
    
    try:
        if os.path.exists(ACCOUNTS_FILE):
            with open(ACCOUNTS_FILE, 'r', encoding='utf-8') as f:
                accounts = json.load(f)
                logger.info(f"✅ Loaded {len(accounts)} accounts from {ACCOUNTS_FILE}")
                accounts_loaded = accounts[:MAX_ACCOUNTS]
                for account in accounts_loaded:
                    uid = str(account.get('uid', ''))
                    active_requests_per_account[uid] = 0
                return accounts_loaded
        else:
            logger.error(f"❌ File {ACCOUNTS_FILE} not found")
            return []
    except Exception as e:
        logger.error(f"⚠️ Error loading accounts: {e}")
        return []

def get_next_account():
    """Get next account in rotation"""
    global account_index
    if not accounts_loaded:
        accounts_loaded = load_accounts()
    
    if not accounts_loaded:
        return None
    
    account = accounts_loaded[account_index]
    account_index = (account_index + 1) % len(accounts_loaded)
    return account

def check_connection_health():
    """Check connection health and restart if needed"""
    global last_connection_time, restart_count, bot_connected
    
    if not bot_connected:
        return
        
    current_time = time.time()
    if current_time - last_connection_time > CONNECTION_TIMEOUT:
        logger.warning(f"⚠️ Connection timeout detected. Last activity: {current_time - last_connection_time:.0f} seconds ago")
        
        if RESTART_ON_DISCONNECT and restart_count < MAX_RESTART_ATTEMPTS:
            restart_count += 1
            logger.info(f"🔄 Attempting restart #{restart_count}")
            time.sleep(RESTART_DELAY)
            restart_bot()
    
    if restart_count > 0 and current_time - last_connection_time < 10:
        restart_count = 0

def update_connection_time():
    """Update last connection activity time"""
    global last_connection_time, bot_connected
    last_connection_time = time.time()
    bot_connected = True

def load_groups_data():
    """Load group data from JSON file"""
    try:
        if os.path.exists(GROUPS_FILE):
            with open(GROUPS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    except Exception as e:
        logger.error(f"⚠️ Error loading groups data: {e}")
        return {}

def save_groups_data(groups_data):
    """Save group data to JSON file"""
    try:
        with open(GROUPS_FILE, 'w', encoding='utf-8') as f:
            json.dump(groups_data, f, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        logger.error(f"⚠️ Error saving groups data: {e}")
        return False

def is_group_active(chat_id):
    """Check if group is active and valid"""
    groups_data = load_groups_data()
    chat_id_str = str(chat_id)
    
    if chat_id_str in groups_data:
        group_data = groups_data[chat_id_str]
        expiry_date = datetime.fromisoformat(group_data['expiry_date'])
        
        if datetime.now() < expiry_date:
            return True
        else:
            del groups_data[chat_id_str]
            save_groups_data(groups_data)
            return False
    return False

def activate_group(chat_id, days, admin_id):
    """Activate a new group or renew an existing one"""
    if str(admin_id) != ADMIN_ID:
        return False, "❌ You don't have permission to activate the bot"
    
    groups_data = load_groups_data()
    chat_id_str = str(chat_id)
    
    expiry_date = datetime.now() + timedelta(days=days)
    
    groups_data[chat_id_str] = {
        'activated_by': admin_id,
        'activation_date': datetime.now().isoformat(),
        'expiry_date': expiry_date.isoformat(),
        'days': days
    }
    
    if save_groups_data(groups_data):
        return True, f"✅ Bot activated in group for {days} days\n⏰ Expires: {expiry_date.strftime('%Y-%m-%d %H:%M')}"
    else:
        return False, "❌ Error saving data"

def deactivate_group(chat_id, admin_id):
    """Deactivate a group"""
    if str(admin_id) != ADMIN_ID:
        return False, "❌ You don't have permission to deactivate"
    
    groups_data = load_groups_data()
    chat_id_str = str(chat_id)
    
    if chat_id_str in groups_data:
        del groups_data[chat_id_str]
        if save_groups_data(groups_data):
            return True, "✅ Bot deactivated in this group"
        else:
            return False, "❌ Error saving data"
    else:
        return False, "❌ Group is not activated"

def get_group_info(chat_id):
    """Get group information"""
    groups_data = load_groups_data()
    chat_id_str = str(chat_id)
    
    if chat_id_str in groups_data:
        group_data = groups_data[chat_id_str]
        expiry_date = datetime.fromisoformat(group_data['expiry_date'])
        activation_date = datetime.fromisoformat(group_data['activation_date'])
        days_left = (expiry_date - datetime.now()).days
        
        if days_left > 0:
            return f"📊 Activation Information:\n├─ Activated: {activation_date.strftime('%Y-%m-%d %H:%M')}\n├─ Expires: {expiry_date.strftime('%Y-%m-%d %H:%M')}\n├─ Days left: {days_left} days\n└─ By: {group_data['activated_by']}"
        else:
            return "❌ Activation expired"
    else:
        return "❌ Group not activated"

def get_all_groups():
    """Get list of all active groups"""
    groups_data = load_groups_data()
    if not groups_data:
        return "❌ No active groups"
    
    active_groups = []
    expired_groups = []
    
    for chat_id, group_data in groups_data.items():
        expiry_date = datetime.fromisoformat(group_data['expiry_date'])
        days_left = (expiry_date - datetime.now()).days
        
        group_info = f"• 🆔 `{chat_id}` | 📅 {days_left} days left"
        
        if days_left > 0:
            active_groups.append(group_info)
        else:
            expired_groups.append(group_info)
    
    result = "📊 Active Groups:\n"
    if active_groups:
        result += "\n".join(active_groups)
    else:
        result += "❌ No active groups\n"
    
    if expired_groups:
        result += "\n\n📊 Expired Groups:\n"
        result += "\n".join(expired_groups)
    
    return result

def dec_to_hex(ask):
    """Convert decimal to hex"""
    ask_result = hex(ask)
    final_result = str(ask_result)[2:]
    if len(final_result) == 1:
        final_result = "0" + final_result
        return final_result
    else:
        return final_result

def send_telegram_message(message, parse_mode="HTML", chat_id=None, message_id=None, no_signature=False, reply_to_message_id=None):
    """Send message to Telegram with reply capability"""
    try:
        if chat_id is None:
            chat_id = TELEGRAM_CHAT_ID
        
        if not no_signature:
            signature = "\n\n────────────────────\n"
            signature += "👑 Developer: JAGWAR KING"
            message_with_signature = message + signature
        else:
            message_with_signature = message
            
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": message_with_signature,
            "parse_mode": parse_mode
        }
        
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
            
        response = requests.post(url, data=data, timeout=10)
        return response.json()
    except Exception as e:
        logger.error(f"⚠️ Error sending Telegram message: {e}")

def delete_telegram_message(chat_id, message_id):
    """Delete a Telegram message"""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/deleteMessage"
        data = {
            "chat_id": chat_id,
            "message_id": message_id
        }
        response = requests.post(url, data=data, timeout=10)
        return response.json()
    except Exception as e:
        logger.error(f"⚠️ Error deleting Telegram message: {e}")

def send_private_message(user_id, message, parse_mode="HTML"):
    """Send private message to user"""
    try:
        signature = "\n\n────────────────────\n"
        signature += "👑 Developer: JAGWAR KING"
        
        message_with_signature = message + signature
        
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        data = {
            "chat_id": user_id,
            "text": message_with_signature,
            "parse_mode": parse_mode
        }
        response = requests.post(url, data=data, timeout=10)
        return response.json()
    except Exception as e:
        logger.error(f"⚠️ Error sending private message: {e}")

def encrypt_packet(plain_text, key, iv):
    plain_text = bytes.fromhex(plain_text)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()
    
def gethashteam(hexxx):
    a = zitado_get_proto(hexxx)
    if not a:
        raise ValueError("Invalid hex format or empty response from zitado_get_proto")
    data = json.loads(a)
    return data['5']['7']

def getownteam(hexxx):
    a = zitado_get_proto(hexxx)
    if not a:
        raise ValueError("Invalid hex format or empty response from zitado_get_proto")
    data = json.loads(a)
    return data['5']['1']

def get_player_status(packet):
    json_result = get_available_room(packet)
    parsed_data = json.loads(json_result)

    if "5" not in parsed_data or "data" not in parsed_data["5"]:
        return "OFFLINE"

    json_data = parsed_data["5"]["data"]

    if "1" not in json_data or "data" not in json_data["1"]:
        return "OFFLINE"

    data = json_data["1"]["data"]

    if "3" not in data:
        return "OFFLINE"

    status_data = data["3"]

    if "data" not in status_data:
        return "OFFLINE"

    status = status_data["data"]

    if status == 1:
        return "SOLO"
    
    if status == 2:
        if "9" in data and "data" in data["9"]:
            group_count = data["9"]["data"]
            countmax1 = data["10"]["data"]
            countmax = countmax1 + 1
            return f"INSQUAD ({group_count}/{countmax})"

        return "INSQUAD"
    
    if status in [3, 5]:
        return "INGAME"
    if status == 4:
        return "IN ROOM"
    
    if status in [6, 7]:
        return "IN SOCIAL ISLAND MODE"

def get_random_avatar():
    avatar_list = [
        '902000061', '902000060', '902000064', '902000065', '902000066', 
        '902000074', '902000075', '902000077', '902000078', '902000084', 
        '902000085', '902000087', '902000091', '902000094', '902000306',
        '902000091','902000208','902000209','902000210','902000211',
        '902047016','902047016','902000347'
    ]
    return random.choice(avatar_list)

def convert_to_hex(PAYLOAD):
    hex_payload = ''.join([f'{byte:02x}' for byte in PAYLOAD])
    return hex_payload

def convert_to_bytes(PAYLOAD):
    payload = bytes.fromhex(PAYLOAD)
    return payload

def time_to_seconds(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds

def seconds_to_hex(seconds):
    return format(seconds, '04x')

def extract_time_from_timestamp(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    h = dt.hour
    m = dt.minute
    s = dt.second
    return h, m, s

def extract_jwt_from_hex(hex):
    byte_data = binascii.unhexlify(hex)
    message = jwt_generator_pb2.Garena_420()
    message.ParseFromString(byte_data)
    json_output = MessageToJson(message)
    token_data = json.loads(json_output)
    return token_data

def format_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def get_available_room(input_text):
    try:
        parsed_results = Parser().parse(input_text)
        parsed_results_objects = parsed_results
        parsed_results_dict = parse_results(parsed_results_objects)
        json_data = json.dumps(parsed_results_dict)
        return json_data
    except Exception as e:
        logger.error(f"error {e}")
        return None

def parse_results(parsed_results):
    result_dict = {}
    for result in parsed_results:
        field_data = {}
        field_data["wire_type"] = result.wire_type
        if result.wire_type == "varint":
            field_data["data"] = result.data
        if result.wire_type == "string":
            field_data["data"] = result.data
        if result.wire_type == "bytes":
            field_data["data"] = result.data
        elif result.wire_type == "length_delimited":
            field_data["data"] = parse_results(result.data.results)
        result_dict[result.field] = field_data
    return result_dict

# ==================== SPAM CORE FUNCTIONS ====================

def create_spam_room_packet(key, iv):
    """Create spam room packet"""
    try:
        fields = {
            1: 2,
            2: {
                1: 1,
                2: 15,
                3: 5,
                4: "[FF0000]SPAM",
                5: "1",
                6: 12,
                7: 1,
                8: 1,
                9: 1,
                11: 1,
                12: 2,
                14: 36981056,
                15: {
                    1: "IDC3",
                    2: 126,
                    3: "ME"
                },
                16: "\u0001\u0003\u0004\u0007\t\n\u000b\u0012\u000f\u000e\u0016\u0019\u001a \u001d",
                18: 2368584,
                27: 1,
                34: "\u0000\u0001",
                40: "en",
                48: 1,
                49: {1: 21},
                50: {1: 36981056, 2: 2368584, 5: 2}
            }
        }
        
        packet = create_protobuf_packet(fields)
        packet = packet.hex()
        header_lenth = len(encrypt_packet(packet, key, iv))//2
        header_lenth_final = dec_to_hex(header_lenth)
        
        if len(header_lenth_final) == 2:
            final_packet = "0E15000000" + header_lenth_final + encrypt_packet(packet, key, iv)
        elif len(header_lenth_final) == 3:
            final_packet = "0E1500000" + header_lenth_final + encrypt_packet(packet, key, iv)
        elif len(header_lenth_final) == 4:
            final_packet = "0E150000" + header_lenth_final + encrypt_packet(packet, key, iv)
        elif len(header_lenth_final) == 5:
            final_packet = "0E15000" + header_lenth_final + encrypt_packet(packet, key, iv)
        
        return bytes.fromhex(final_packet)
    except Exception as e:
        logger.error(f"Error creating spam room packet: {e}")
        return None

def create_spam_invite_packet(key, iv, target_uid):
    """Create spam invite packet"""
    try:
        fields = {
            1: 22,
            2: {
                1: int(target_uid)
            }
        }
        
        packet = create_protobuf_packet(fields)
        packet = packet.hex()
        header_lenth = len(encrypt_packet(packet, key, iv))//2
        header_lenth_final = dec_to_hex(header_lenth)
        
        if len(header_lenth_final) == 2:
            final_packet = "0E15000000" + header_lenth_final + encrypt_packet(packet, key, iv)
        elif len(header_lenth_final) == 3:
            final_packet = "0E1500000" + header_lenth_final + encrypt_packet(packet, key, iv)
        elif len(header_lenth_final) == 4:
            final_packet = "0E150000" + header_lenth_final + encrypt_packet(packet, key, iv)
        elif len(header_lenth_final) == 5:
            final_packet = "0E15000" + header_lenth_final + encrypt_packet(packet, key, iv)
        
        return bytes.fromhex(final_packet)
    except Exception as e:
        logger.error(f"Error creating spam invite packet: {e}")
        return None

def spam_attack_loop(target_uid, stop_event, requester_id, requester_name):
    """Main spam attack loop"""
    while not stop_event.is_set():
        try:
            with command_lock:
                active_clients = [c for c in current_clients if c.is_connected and c.socket_client and c.key and c.iv]
            
            if not active_clients:
                stop_event.wait(2)
                continue
            
            for client in active_clients[:5]:
                if stop_event.is_set():
                    break
                    
                try:
                    room_packet = create_spam_room_packet(client.key, client.iv)
                    if room_packet:
                        client.socket_client.send(room_packet)
                        time.sleep(0.2)
                    
                    for _ in range(5):
                        if stop_event.is_set():
                            break
                        invite_packet = create_spam_invite_packet(client.key, client.iv, target_uid)
                        if invite_packet:
                            client.socket_client.send(invite_packet)
                            time.sleep(0.1)
                    
                except Exception as e:
                    logger.error(f"Spam client error: {e}")
                    continue
                    
            stop_event.wait(0.5)
            
        except Exception as e:
            logger.error(f"Spam attack loop error: {e}")
            stop_event.wait(1)

def start_spam(target_uid, requester_id, requester_name, chat_id=None, user_message_id=None):
    """Start spam attack on target"""
    global _spam_tasks
    
    target_uid_str = str(target_uid)
    
    if target_uid_str in _spam_tasks:
        if chat_id and user_message_id:
            send_telegram_message(
                f"❌ Spam already active on ID: `{target_uid_str}`",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
        return False
    
    with _target_owners_lock:
        _target_owners[target_uid_str] = (requester_id, requester_name)
    
    stop_event = threading.Event()
    spam_thread = threading.Thread(
        target=spam_attack_loop,
        args=(target_uid_str, stop_event, requester_id, requester_name),
        daemon=True
    )
    spam_thread.start()
    
    _spam_tasks[target_uid_str] = (spam_thread, stop_event)
    
    logger.info(f"🎯 Spam started on {target_uid_str} by {requester_name}")
    
    if chat_id and user_message_id:
        send_telegram_message(
            f"✅ Spam attack started!\n"
            f"├─ Target ID: {target_uid_str}\n"
            f"├─ Started by: {requester_name}\n"
            f"└─ Status: 🚀 Running",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )
    
    return True

def stop_spam(target_uid, requester_id, chat_id=None, user_message_id=None):
    """Stop spam attack on target"""
    global _spam_tasks
    
    target_uid_str = str(target_uid)
    
    if target_uid_str not in _spam_tasks:
        if chat_id and user_message_id:
            send_telegram_message(
                f"❌ No spam attack found on ID: `{target_uid_str}`",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
        return False
    
    with _target_owners_lock:
        owner_id, owner_name = _target_owners.get(target_uid_str, (None, "unknown"))
    
    if str(requester_id) != str(owner_id) and str(requester_id) != ADMIN_ID:
        if chat_id and user_message_id:
            send_telegram_message(
                f"❌ Permission denied!\n"
                f"├─ This spam was started by: @{owner_name}\n"
                f"└─ Only the owner or admin can stop it.",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
        return False
    
    thread, stop_event = _spam_tasks.pop(target_uid_str)
    stop_event.set()
    
    if thread.is_alive():
        thread.join(timeout=3)
    
    with _target_owners_lock:
        if target_uid_str in _target_owners:
            del _target_owners[target_uid_str]
    
    logger.info(f"🛑 Spam stopped on {target_uid_str} by {requester_id}")
    
    if chat_id and user_message_id:
        send_telegram_message(
            f"✅ Spam attack stopped!\n"
            f"├─ Target ID: {target_uid_str}\n"
            f"└─ Status: ⏹️ Stopped",
            chat_id=chat_id,
            reply_to_message_id=user_message_id
        )
    
    return True

def get_active_spam_targets():
    """Get list of active spam targets"""
    if not _spam_tasks:
        return []
    
    with _target_owners_lock:
        result = []
        for uid, (_, _) in _spam_tasks.items():
            owner_id, owner_name = _target_owners.get(uid, (None, "unknown"))
            result.append({
                'uid': uid,
                'owner_name': owner_name,
                'owner_id': owner_id
            })
    return result

# ==================== HEALTH MANAGER ====================
class HealthManager:
    def __init__(self):
        self.client_status = {}
    
    def check_client_health(self, client):
        """Check client health"""
        client_id = client.client_id
        
        if not client.is_connected and not client.is_connecting:
            if client_id not in self.client_status:
                self.client_status[client_id] = {
                    'last_seen': time.time(),
                    'reconnect_count': 0
                }
            
            last_seen = self.client_status[client_id].get('last_seen', 0)
            if time.time() - last_seen > 60:
                logger.info(f"🔄 Health Manager: Reconnecting client #{client_id}")
                threading.Thread(target=client.reconnect, daemon=True).start()
                self.client_status[client_id]['last_seen'] = time.time()
                self.client_status[client_id]['reconnect_count'] += 1
    
    def monitor_all_clients(self, clients):
        """Monitor all clients"""
        while True:
            try:
                for client in clients:
                    self.check_client_health(client)
                
                time.sleep(10)
                
            except Exception as e:
                logger.error(f"Health Manager error: {e}")
                time.sleep(30)

# ==================== FF_CLIENT CLASS ====================
class FF_CLIENT(threading.Thread):
    def __init__(self, account_data):
        super().__init__()
        self.name = account_data.get('name', 'Unknown')
        self.id = str(account_data.get('uid', ''))
        self.password = account_data.get('password', '')
        self.region = account_data.get('region', 'ME')
        self.key = None
        self.iv = None
        self.socket_client = None
        self.clients = None
        self.is_connected = False
        self.is_connecting = False
        self.client_id = len(current_clients) + 1
        self.last_restart_time = time.time()
        self.active_requests = 0
        self.reconnect_attempts = 0
        self.max_reconnect_attempts = 5
        self.reconnect_delay = 10
        self.session_id = hashlib.md5(f"{self.id}{self.password}{time.time()}".encode()).hexdigest()[:8]
        self.last_received_data = None
        
        current_clients.append(self)
        
        logger.info(f"🕹️ Game bot #{self.client_id} ({self.name}) initialized, waiting for Telegram to be ready...")

    def safe_connect(self, func, *args, **kwargs):
        """Safe connection with retry"""
        for attempt in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Client #{self.client_id}: Attempt {attempt + 1} failed: {e}")
                if attempt < 2:
                    time.sleep(2)
        return None

    def reconnect(self):
        """Automatic reconnection"""
        if self.reconnect_attempts >= self.max_reconnect_attempts:
            logger.error(f"Client #{self.client_id}: Max reconnection attempts reached")
            return False
        
        self.reconnect_attempts += 1
        delay = self.reconnect_delay * self.reconnect_attempts
        logger.info(f"Client #{self.client_id}: Reconnecting in {delay} seconds (attempt {self.reconnect_attempts})")
        
        time.sleep(delay)
        
        try:
            if self.socket_client:
                try:
                    self.socket_client.close()
                except:
                    pass
            
            if self.clients:
                try:
                    self.clients.close()
                except:
                    pass
            
            self.is_connected = False
            time.sleep(2)
            
            success = self.get_tok()
            if success:
                self.reconnect_attempts = 0
                return True
            
        except Exception as e:
            logger.error(f"Client #{self.client_id}: Reconnection error: {e}")
        
        return False

    def create_ping_packet(self):
        """Create ping packet for health check"""
        try:
            fields = {
                1: 100,
                2: {
                    1: 1
                }
            }
            
            packet = create_protobuf_packet(fields)
            packet = packet.hex()
            header_lenth = len(encrypt_packet(packet, self.key, self.iv))//2
            header_lenth_final = dec_to_hex(header_lenth)
            
            if len(header_lenth_final) == 2:
                final_packet = "0515000000" + header_lenth_final + self.nmnmmmmn(packet)
            elif len(header_lenth_final) == 3:
                final_packet = "051500000" + header_lenth_final + self.nmnmmmmn(packet)
            elif len(header_lenth_final) == 4:
                final_packet = "05150000" + header_lenth_final + self.nmnmmmmn(packet)
            elif len(header_lenth_final) == 5:
                final_packet = "0515000" + header_lenth_final + self.nmnmmmmn(packet)
            
            return bytes.fromhex(final_packet)
        except:
            return None

    def health_check_loop(self):
        """Health check loop"""
        while self.is_connected:
            try:
                time.sleep(30)
                
                if self.socket_client:
                    try:
                        ping_packet = self.create_ping_packet()
                        if ping_packet:
                            self.socket_client.send(ping_packet)
                    except:
                        logger.error(f"Client #{self.client_id}: Health check failed, reconnecting...")
                        self.is_connected = False
                        self.reconnect()
                        break
                
            except Exception as e:
                logger.error(f"Client #{self.client_id}: Health check error: {e}")

    def parse_my_message(self, serialized_data):
        MajorLogRes = MajorLoginRes_pb2.MajorLoginRes()
        MajorLogRes.ParseFromString(serialized_data)
        
        timestamp = MajorLogRes.kts
        key = MajorLogRes.ak
        iv = MajorLogRes.aiv
        BASE64_TOKEN = MajorLogRes.token
        timestamp_obj = Timestamp()
        timestamp_obj.FromNanoseconds(timestamp)
        timestamp_seconds = timestamp_obj.seconds
        timestamp_nanos = timestamp_obj.nanos
        combined_timestamp = timestamp_seconds * 1_000_000_000 + timestamp_nanos
        return combined_timestamp, key, iv, BASE64_TOKEN

    def GET_PAYLOAD_BY_DATA(self, JWT_TOKEN, NEW_ACCESS_TOKEN, date):
        token_payload_base64 = JWT_TOKEN.split('.')[1]
        token_payload_base64 += '=' * ((4 - len(token_payload_base64) % 4) % 4)
        decoded_payload = base64.urlsafe_b64decode(token_payload_base64).decode('utf-8')
        decoded_payload = json.loads(decoded_payload)
        NEW_EXTERNAL_ID = decoded_payload['external_id']
        SIGNATURE_MD5 = decoded_payload['signature_md5']
        now = datetime.now()
        now =str(now)[:len(str(now))-7]
        formatted_time = date
        

        payload = bytes.fromhex("1a13323032352d31312d32362030313a35313a3238220966726565206669726528013a07312e3132302e314232416e64726f6964204f532039202f204150492d3238202850492f72656c2e636a772e32303232303531382e313134313333294a0848616e6468656c64520c4d544e2f537061636574656c5a045749464960800a68d00572033234307a2d7838362d3634205353453320535345342e3120535345342e32204156582041565832207c2032343030207c20348001e61e8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e329a012b476f6f676c657c36323566373136662d393161372d343935622d396631362d303866653964336336353333a2010e3137362e32382e3133392e313835aa01026172b201203433303632343537393364653836646134323561353263616164663231656564ba010134c2010848616e6468656c64ca010d4f6e65506c7573204135303130ea014063363961653230386661643732373338623637346232383437623530613361316466613235643161313966616537343566633736616334613065343134633934f00101ca020c4d544e2f537061636574656cd2020457494649ca03203161633462383065636630343738613434323033626638666163363132306635e003b5ee02e8039a8002f003af13f80384078004a78f028804b5ee029004a78f029804b5ee02b00404c80401d2043d2f646174612f6170702f636f6d2e6474732e667265656669726574682d66705843537068495636644b43376a4c2d574f7952413d3d2f6c69622f61726de00401ea045f65363261623933353464386662356662303831646233333861636233333439317c2f646174612f6170702f636f6d2e6474732e667265656669726574682d66705843537068495636644b43376a4c2d574f7952413d3d2f626173652e61706bf00406f804018a050233329a050a32303139313139303236a80503b205094f70656e474c455332b805ff01c00504e005be7eea05093372645f7061727479f205704b717348543857393347646347335a6f7a454e6646775648746d377171316552554e6149444e67526f626f7a4942744c4f695943633459367a767670634943787a514632734f453463627974774c7334785a62526e70524d706d5752514b6d654f35766373386e51594268777148374bf805e7e4068806019006019a060134a2060134b2062213521146500e590349510e460900115843395f005b510f685b560a6107576d0f0366")
        
        payload = payload.replace(b"2026-01-14 12:19:02", str(now).encode())
        payload = payload.replace(b"c69ae208fad72738b674b2847b50a3a1dfa25d1a19fae745fc76ac4a0e414c94", NEW_ACCESS_TOKEN.encode("UTF-8"))
        payload = payload.replace(b"4306245793de86da425a52caadf21eed", NEW_EXTERNAL_ID.encode("UTF-8"))
        payload = payload.replace(b"1ac4b80ecf0478a44203bf8fac6120f5", SIGNATURE_MD5.encode("UTF-8"))
        
        PAYLOAD = payload.hex()
        PAYLOAD = encrypt_api(PAYLOAD)
        PAYLOAD = bytes.fromhex(PAYLOAD)
        whisper_ip, whisper_port, online_ip, online_port = self.GET_LOGIN_DATA(JWT_TOKEN, PAYLOAD)
        return whisper_ip, whisper_port, online_ip, online_port
    
    def GET_LOGIN_DATA(self, JWT_TOKEN, PAYLOAD):
        url = "https://clientbp.ggpolarbear.com/GetLoginData"
        headers = {
            'Expect': '100-continue',
            'Authorization': f'Bearer {JWT_TOKEN}',
            'X-Unity-Version': '2018.4.11f1',
            'X-GA': 'v1 1',
            'ReleaseVersion': 'OB53',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI)',
            'Host': 'clientbp.ggpolarbear.com',
            'Connection': 'close',
            'Accept-Encoding': 'gzip, deflate, br',
        }
        
        max_retries = 3
        attempt = 0

        while attempt < max_retries:
            try:
                response = requests.post(url, headers=headers, data=PAYLOAD, verify=False)
                response.raise_for_status()
                x = response.content.hex()
                json_result = get_available_room(x)
                parsed_data = json.loads(json_result)
                logger.info(f"📡 Client #{self.client_id}: Login data received")
                
                whisper_address = parsed_data['32']['data']
                online_address = parsed_data['14']['data']
                online_ip = online_address[:len(online_address) - 6]
                whisper_ip = whisper_address[:len(whisper_address) - 6]
                online_port = int(online_address[len(online_address) - 5:])
                whisper_port = int(whisper_address[len(whisper_address) - 5:])
                return whisper_ip, whisper_port, online_ip, online_port
            
            except requests.RequestException as e:
                logger.error(f"Client #{self.client_id}: Request failed: {e}. Attempt {attempt + 1} of {max_retries}. Retrying...")
                attempt += 1
                time.sleep(2)

        logger.error(f"Client #{self.client_id}: Failed to get login data after multiple attempts.")
        return None, None, None, None

    def guest_token(self, uid, password):
        url = "https://100067.connect.garena.com/oauth/guest/token/grant"
        headers = {
            "Host": "100067.connect.garena.com",
            "User-Agent": "GarenaMSDK/4.0.19P4(G011A ;Android 10;en;EN;)",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "close",
        }
        data = {
            "uid": f"{uid}",
            "password": f"{password}",
            "response_type": "token",
            "client_type": "2",
            "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
            "client_id": "100067",
        }
        response = requests.post(url, headers=headers, data=data)
        data = response.json()
        NEW_ACCESS_TOKEN = data['access_token']
        NEW_OPEN_ID = data['open_id']
        OLD_ACCESS_TOKEN = "c69ae208fad72738b674b2847b50a3a1dfa25d1a19fae745fc76ac4a0e414c94"
        OLD_OPEN_ID = "4306245793de86da425a52caadf21eed"
        time.sleep(0.2)
        result = self.TOKEN_MAKER(OLD_ACCESS_TOKEN, NEW_ACCESS_TOKEN, OLD_OPEN_ID, NEW_OPEN_ID, uid)
        return result
        
    def TOKEN_MAKER(self, OLD_ACCESS_TOKEN, NEW_ACCESS_TOKEN, OLD_OPEN_ID, NEW_OPEN_ID, id):
        headers = {
            'X-Unity-Version': '2018.4.11f1',
            'ReleaseVersion': 'OB53',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-GA': 'v1 1',
            'Content-Length': '928',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; ASUS_Z01QD Build/QKQ1.190825.002)',
            'Host': 'loginbp.ggwhitehawk.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip'
        }
        
        
        data = bytes.fromhex('1a13323032352d31312d32362030313a35313a3238220966726565206669726528013a07312e3132332e314232416e64726f6964204f532039202f204150492d3238202850492f72656c2e636a772e32303232303531382e313134313333294a0848616e6468656c64520c4d544e2f537061636574656c5a045749464960800a68d00572033234307a2d7838362d3634205353453320535345342e3120535345342e32204156582041565832207c2032343030207c20348001e61e8a010f416472656e6f2028544d292036343092010d4f70656e474c20455320332e329a012b476f6f676c657c36323566373136662d393161372d343935622d396631362d303866653964336336353333a2010e3137362e32382e3133392e313835aa01026172b201203433303632343537393364653836646134323561353263616164663231656564ba010134c2010848616e6468656c64ca010d4f6e65506c7573204135303130ea014063363961653230386661643732373338623637346232383437623530613361316466613235643161313966616537343566633736616334613065343134633934f00101ca020c4d544e2f537061636574656cd2020457494649ca03203161633462383065636630343738613434323033626638666163363132306635e003b5ee02e8039a8002f003af13f80384078004a78f028804b5ee029004a78f029804b5ee02b00404c80401d2043d2f646174612f6170702f636f6d2e6474732e667265656669726574682d66705843537068495636644b43376a4c2d574f7952413d3d2f6c69622f61726de00401ea045f65363261623933353464386662356662303831646233333861636233333439317c2f646174612f6170702f636f6d2e6474732e667265656669726574682d66705843537068495636644b43376a4c2d574f7952413d3d2f626173652e61706bf00406f804018a050233329a050a32303139313139303236a80503b205094f70656e474c455332b805ff01c00504e005be7eea05093372645f7061727479f205704b717348543857393347646347335a6f7a454e6646775648746d377171316552554e6149444e67526f626f7a4942744c4f695943633459367a767670634943787a514632734f453463627974774c7334785a62526e70524d706d5752514b6d654f35766373386e51594268777148374bf805e7e4068806019006019a060134a2060134b2062213521146500e590349510e460900115843395f005b510f685b560a6107576d0f0366')
        
       
        data = data.replace(OLD_OPEN_ID.encode(), NEW_OPEN_ID.encode())
        data = data.replace(OLD_ACCESS_TOKEN.encode(), NEW_ACCESS_TOKEN.encode())
        
        hex = data.hex()
        d = encrypt_api(data.hex())
        Final_Payload = bytes.fromhex(d)
        URL = "https://loginbp.ggpolarbear.com/MajorLogin"

        try:
            RESPONSE = requests.post(URL, headers=headers, data=Final_Payload, verify=False)
            RESPONSE.raise_for_status()
            
            combined_timestamp, key, iv, BASE64_TOKEN = self.parse_my_message(RESPONSE.content)
            if RESPONSE.status_code == 200:
                if len(RESPONSE.content) < 10:
                    logger.error(f"Client #{self.client_id}: Empty response from server")
                    return False
                whisper_ip, whisper_port, online_ip, online_port = self.GET_PAYLOAD_BY_DATA(BASE64_TOKEN, NEW_ACCESS_TOKEN, 1)
                self.key = key
                self.iv = iv
                logger.info(f"✅ Client #{self.client_id}: Token obtained")
                return (BASE64_TOKEN, key, iv, combined_timestamp, whisper_ip, whisper_port, online_ip, online_port)
            else:
                logger.error(f"❌ Client #{self.client_id}: Failed to get token - Error code: {RESPONSE.status_code}")
                return False
        except Exception as e:
            logger.error(f"❌ Client #{self.client_id}: Exception getting token: {str(e)}")
            return False

    def nmnmmmmn(self, data):
        if not self.key or not self.iv:
            return ""
        try:
            key = self.key if isinstance(self.key, bytes) else bytes.fromhex(self.key)
            iv = self.iv if isinstance(self.iv, bytes) else bytes.fromhex(self.iv)
            data = bytes.fromhex(data)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            cipher_text = cipher.encrypt(pad(data, AES.block_size))
            return cipher_text.hex()
        except Exception as e:
            logger.error(f"Client #{self.client_id}: Error in nmnmmmmn: {e}")
            return ""

    def skwad_maker(self):
        fields = {
        1: 1,
        2: {
            2: "\u0001",
            3: 1,
            4: 1,
            5: "en",
            9: 1,
            11: 1,
            13: 1,
            14: {
            2: 5756,
            6: 11,
            8: "1.109.5",
            9: 3,
            10: 2
            },
        }
        }

        packet = create_protobuf_packet(fields)
        packet = packet.hex()
        header_lenth = len(encrypt_packet(packet, self.key, self.iv))//2
        header_lenth_final = dec_to_hex(header_lenth)
        if len(header_lenth_final) == 2:
            final_packet = "0515000000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 3:
            final_packet = "051500000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 4:
            final_packet = "05150000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 5:
            final_packet = "0515000" + header_lenth_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)

    def changes(self, num):
        fields = {
        1: 17,
        2: {
            1: 11371687918,
            2: 1,
            3: int(num),
            4: 62,
            5: "\u001a",
            8: 5,
            13: 329
        }
        }

        packet = create_protobuf_packet(fields)
        packet = packet.hex()
        header_lenth = len(encrypt_packet(packet, self.key, self.iv))//2
        header_lenth_final = dec_to_hex(header_lenth)
        if len(header_lenth_final) == 2:
            final_packet = "0515000000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 3:
            final_packet = "051500000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 4:
            final_packet = "05150000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 5:
            final_packet = "0515000" + header_lenth_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)

    def start_autooo(self):
        fields = {
        1: 9,
        2: {
            1: 11371687918
        }
        }
        packet = create_protobuf_packet(fields)
        packet = packet.hex()
        header_lenth = len(encrypt_packet(packet, self.key, self.iv))//2
        header_lenth_final = dec_to_hex(header_lenth)
        if len(header_lenth_final) == 2:
            final_packet = "0515000000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 3:
            final_packet = "051500000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 4:
            final_packet = "05150000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 5:
            final_packet = "0515000" + header_lenth_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)

    def invite_skwad(self, idplayer):
        fields = {
        1: 2,
        2: {
            1: int(idplayer),
            2: "ME",
            4: 1
        }
        }
        packet = create_protobuf_packet(fields)
        packet = packet.hex()
        header_lenth = len(encrypt_packet(packet, self.key, self.iv))//2
        header_lenth_final = dec_to_hex(header_lenth)
        if len(header_lenth_final) == 2:
            final_packet = "0515000000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 3:
            final_packet = "051500000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 4:
            final_packet = "05150000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 5:
            final_packet = "0515000" + header_lenth_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)

    def leave_s(self):
        fields = {
        1: 7,
        2: {
            1: 11371687918
        }
        }

        packet = create_protobuf_packet(fields)
        packet = packet.hex()
        header_lenth = len(encrypt_packet(packet, self.key, self.iv))//2
        header_lenth_final = dec_to_hex(header_lenth)
        if len(header_lenth_final) == 2:
            final_packet = "0515000000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 3:
            final_packet = "051500000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 4:
            final_packet = "05150000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 5:
            final_packet = "0515000" + header_lenth_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)

    def accept_sq(self, hash, target, owner):
        fields = {
            1: 3,
            2: {
                1: int(owner),
                2: hash,
                3: int(target),
                5: 1,
                6: 0,
                7: 1
            }
        }

        packet = create_protobuf_packet(fields)
        packet = packet.hex()
        header_lenth = len(encrypt_packet(packet, self.key, self.iv))//2
        header_lenth_final = dec_to_hex(header_lenth)
        if len(header_lenth_final) == 2:
            final_packet = "0515000000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 3:
            final_packet = "051500000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 4:
            final_packet = "05150000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 5:
            final_packet = "0515000" + header_lenth_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)

    def GenResponsMsg(self, msg, uid):
        fields = {
            1: 12,
            2: {
                1: int(uid),
                2: msg
            }
        }
        packet = create_protobuf_packet(fields)
        packet = packet.hex()
        header_lenth = len(encrypt_packet(packet, self.key, self.iv))//2
        header_lenth_final = dec_to_hex(header_lenth)
        if len(header_lenth_final) == 2:
            final_packet = "0515000000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 3:
            final_packet = "051500000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 4:
            final_packet = "05150000" + header_lenth_final + self.nmnmmmmn(packet)
        elif len(header_lenth_final) == 5:
            final_packet = "0515000" + header_lenth_final + self.nmnmmmmn(packet)
        return bytes.fromhex(final_packet)

    def check_restart_needed(self):
        """Check if account needs restart (every 3 minutes)"""
        current_time = time.time()
        if current_time - self.last_restart_time > ACCOUNT_RESTART_INTERVAL:
            logger.info(f"🔄 Client #{self.client_id}: Restarting connection after 3 minutes")
            self.last_restart_time = current_time
            self.restart_connection()
            
    def restart_connection(self):
        """Restart game connection"""
        try:
            if self.socket_client:
                self.socket_client.close()
            if self.clients:
                self.clients.close()
            
            self.is_connected = False
            logger.info(f"🔄 Client #{self.client_id}: Restarting connection...")
            self.get_tok()
        except Exception as e:
            logger.error(f"❌ Client #{self.client_id}: Error restarting connection: {e}")

    
    def execute_lag_command(self, team_code, duration=1, chat_id=None, user_message_id=None):
        """Execute lag command - team suspension system"""
        try:
            self.active_requests += 1
            active_requests_per_account[self.id] = active_requests_per_account.get(self.id, 0) + 1
            
            if not self.is_connected or not self.socket_client:
                logger.error(f"Client #{self.client_id}: Not connected, cannot execute lag")
                return False

            
            if duration == 1:
                total_requests = 1000
                repeat_count = 1
            elif duration == 2:
                total_requests = 2000
                repeat_count = 2
            elif duration >= 3:
                total_requests = 3000
                repeat_count = 3
            else:
                total_requests = 1000
                repeat_count = 1
                
            logger.info(f"🚀 Client #{self.client_id}: Starting lag attack on team {team_code}")
            logger.info(f"├─ Duration: {duration}")
            logger.info(f"├─ Batches: {repeat_count}")
            logger.info(f"└─ Total requests: {total_requests}")
            
           
            if chat_id and user_message_id:
                start_msg = send_telegram_message(
                    f"⏸️ Starting team suspension\n"
                    f"├─ Target: {team_code}\n"
                    f"├─ Duration level: {duration}\n"
                    f"├─ Total batches: {repeat_count}\n"
                    f"└─ Total requests: {total_requests}",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                start_msg_id = start_msg.get('result', {}).get('message_id') if start_msg else None
            
           
            request_counter = 0
            for batch in range(repeat_count):
                batch_num = batch + 1
                
               
                if repeat_count > 1 and chat_id and user_message_id:
                    batch_msg = send_telegram_message(
                        f"🔄 Suspension batch {batch_num} of {repeat_count}...",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                    batch_msg_id = batch_msg.get('result', {}).get('message_id') if batch_msg else None
                
                logger.info(f"Client #{self.client_id}: Starting lag batch {batch_num}/{repeat_count}")
                
                
                for request_num in range(1000):
                    try:
                        
                        join_teamcode(self.socket_client, team_code, self.key, self.iv)
                        
                        
                        time.sleep(0.001)
                        
                        
                        leave_packet = self.leave_s()
                        self.socket_client.send(leave_packet)
                        
                        
                        time.sleep(0.0001)
                        
                        request_counter += 1
                        
                    except Exception as e:
                        logger.error(f"Client #{self.client_id}: Error in lag request {request_counter}: {e}")
                        continue
                
                
                if repeat_count > 1 and batch_num < repeat_count:
                    time.sleep(0.1)
                
             
                if repeat_count > 1 and chat_id and batch_msg_id:
                    try:
                        delete_telegram_message(chat_id, batch_msg_id)
                    except:
                        pass
            

            if chat_id and user_message_id:
                send_telegram_message(
                    f"✅ Team suspension completed!\n"
                    f"├─ Target: {team_code}\n"
                    f"├─ Duration level: {duration}\n"
                    f"├─ Total batches: {repeat_count}\n"
                    f"└─ Total requests: {request_counter}",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
            
            logger.info(f"✅ Client #{self.client_id}: Lag attack completed!")
            logger.info(f"├─ Team: {team_code}")
            logger.info(f"├─ Duration: {duration}")
            logger.info(f"└─ Requests sent: {request_counter}")
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Client #{self.client_id}: Error in execute_lag_command: {e}")
            return False
        finally:
            self.active_requests -= 1
            active_requests_per_account[self.id] = max(0, active_requests_per_account.get(self.id, 0) - 1)

    
    def execute_attack_command(self, team_code, chat_id=None, user_message_id=None):
        """Execute attack command (force start)"""
        try:
            self.active_requests += 1
            active_requests_per_account[self.id] = active_requests_per_account.get(self.id, 0) + 1
            
            if not self.is_connected or not self.socket_client:
                logger.error(f"Client #{self.client_id}: Not connected, cannot execute attack")
                return False

            start_packet = self.start_autooo()
            leave_packet = self.leave_s()

            logger.info(f"🚀 Client #{self.client_id}: Starting forced attack on team {team_code}")
            
            attack_start_time = time.time()
            while time.time() - attack_start_time < 45:
                join_teamcode(self.socket_client, team_code, self.key, self.iv)
                self.socket_client.send(start_packet)
                self.socket_client.send(leave_packet)
                time.sleep(0.15)

            logger.info(f"✅ Client #{self.client_id}: Forced attack completed on team {team_code}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Client #{self.client_id}: Error in execute_attack_command: {e}")
            return False
        finally:
            self.active_requests -= 1
            active_requests_per_account[self.id] = max(0, active_requests_per_account.get(self.id, 0) - 1)

    
    def execute_invite_command(self, player_id, squad_type, chat_id=None, user_message_id=None):
        """Execute invite command in game"""
        try:
            self.active_requests += 1
            active_requests_per_account[self.id] = active_requests_per_account.get(self.id, 0) + 1
            
            if not self.is_connected or not self.socket_client:
                logger.error(f"Client #{self.client_id}: Not connected, cannot execute invite")
                return False

            numsc = int(squad_type) - 1
            
            packetmaker = self.skwad_maker()
            self.socket_client.send(packetmaker)
            sleep(0.5)
            
            packetfinal = self.changes(int(numsc))
            self.socket_client.send(packetfinal)
            sleep(0.5)
            
            invite_packet = self.invite_skwad(player_id)
            self.socket_client.send(invite_packet)
            
            sleep(5)
            
            leave_packet = self.leave_s()
            self.socket_client.send(leave_packet)
            sleep(0.5)
            
            solo_packet = self.changes(1)
            self.socket_client.send(solo_packet)
            
            logger.info(f"✅ Client #{self.client_id}: Invite sent to player {player_id} (squad: {squad_type})")
            return True
            
        except Exception as e:
            logger.error(f"❌ Client #{self.client_id}: Error in execute_invite_command: {e}")
            return False
        finally:
            self.active_requests -= 1
            active_requests_per_account[self.id] = max(0, active_requests_per_account.get(self.id, 0) - 1)

    def sockf1(self, tok, online_ip, online_port, packet, key, iv):
        global sent_inv, tempid, start_par, pleaseaccept, tempdata1, nameinv, idinv
        global senthi, statusinfo, tempdata, data22, leaveee, isroom, isroom2, game_ready
        
        try:
            self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            online_port = int(online_port)

            self.socket_client.connect((online_ip, online_port))
            self.is_connected = True
            game_ready = True
            logger.info(f"🎮 Client #{self.client_id}: Connected to game server {online_ip}:{online_port}")
            
            update_connection_time()
            self.socket_client.send(bytes.fromhex(tok))
            
            while True:
                try:
                    self.check_restart_needed()
                    
                    data2 = self.socket_client.recv(9999)
                    if not data2:
                        self.is_connected = False
                        game_ready = False
                        logger.error(f"❌ Client #{self.client_id}: Game connection closed by server")
                        break
                    
                    # Store last received data for Ghost system
                    self.last_received_data = data2
                    
                    update_connection_time()
                    
                    if "0500" in data2.hex()[0:4]:
                        accept_packet = f'08{data2.hex().split("08", 1)[1]}'
                        kk = get_available_room(accept_packet)
                        parsed_data = json.loads(kk)
                        fark = parsed_data.get("4", {}).get("data", None)
                        if fark is not None:
                            if fark == 18:
                                if sent_inv:
                                    accept_packet = f'08{data2.hex().split("08", 1)[1]}'
                                    aa = gethashteam(accept_packet)
                                    ownerid = getownteam(accept_packet)
                                    ss = self.accept_sq(aa, tempid, int(ownerid))
                                    self.socket_client.send(ss)
                                    sleep(1)
                                    startauto = self.start_autooo()
                                    self.socket_client.send(startauto)
                                    start_par = False
                                    sent_inv = False

                    if "0600" in data2.hex()[0:4] and len(data2.hex()) > 700:
                            accept_packet = f'08{data2.hex().split("08", 1)[1]}'
                            kk = get_available_room(accept_packet)
                            parsed_data = json.loads(kk)
                            idinv = parsed_data["5"]["data"]["1"]["data"]
                            nameinv = parsed_data["5"]["data"]["3"]["data"]
                            senthi = True
                            
                except Exception as e:
                    logger.error(f"Client #{self.client_id}: Error in sockf1 recv: {e}")
                    break
                    
        except Exception as e:
            logger.error(f"❌ Client #{self.client_id}: Error connecting to game server: {e}")
            game_ready = False
            self.is_connected = False

    def connect(self, tok, packet, key, iv, whisper_ip, whisper_port, online_ip, online_port):
        global clients, sent_inv, tempid, leaveee, start_par, nameinv, idinv
        global senthi, statusinfo, tempdata, pleaseaccept, tempdata1, data22, game_ready
        
        try:
            self.clients = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clients.connect((whisper_ip, whisper_port))
            self.clients.send(bytes.fromhex(tok))
            logger.info(f"🔗 Client #{self.client_id}: Connected to whisper server {whisper_ip}:{whisper_port}")
            
            thread = threading.Thread(
                target=self.sockf1, args=(tok, online_ip, online_port, "anything", key, iv)
            )
            threads.append(thread)
            thread.start()

            while True:
                try:
                    self.check_restart_needed()
                    
                    data = self.clients.recv(9999)

                    if data == b"":
                        self.is_connected = False
                        game_ready = False
                        logger.error(f"❌ Client #{self.client_id}: Whisper connection closed")
                        break

                    if senthi == True:
                        self.clients.send(
                            self.GenResponsMsg(
                                """[C][B][1E90FF]╔══════════════════════════╗
[FFFFFF]Hello! Thanks for adding me.
[FFFFFF]To see available commands,
[FFFFFF]send any message or emoji.
[1E90FF]╠══════════════════════════╣
[FFFFFF] Auto-restart on disconnect
[FFFFFF] ..............................
[FFD700]Telegram:@JAGWAR_FF1
[1E90FF]╚══════════════════════════╝""", idinv
                            )
                        )
                        senthi = False

                    if "1200" in data.hex()[0:4]:
                        json_result = get_available_room(data.hex()[10:])
                        parsed_data = json.loads(json_result)
                        try:
                            uid = parsed_data["5"]["data"]["1"]["data"]
                        except KeyError:
                            uid = None
                            
                except Exception as e:
                    logger.error(f"Client #{self.client_id}: Error in connect loop: {e}")
                    break
                    
        except Exception as e:
            logger.error(f"❌ Client #{self.client_id}: Error connecting to whisper server: {e}")
            game_ready = False

    def get_tok(self):
        global g_token, game_ready
        
        logger.info(f"🔐 Client #{self.client_id}: Starting connection ({self.name})...")
        self.is_connecting = True
        
        try:
            result = self.safe_connect(self.guest_token, self.id, self.password)
            if not result:
                logger.error(f"❌ Client #{self.client_id}: Complete failure getting token")
                self.is_connecting = False
                return False
                
            token, key, iv, Timestamp, whisper_ip, whisper_port, online_ip, online_port = result
            g_token = token
            
            logger.info(f"✅ Client #{self.client_id}: Game credentials obtained")
            
            try:
                decoded = jwt.decode(token, options={"verify_signature": False})
                account_id = decoded.get('account_id')
                encoded_acc = hex(account_id)[2:]
                hex_value = dec_to_hex(Timestamp)
                time_hex = hex_value
                BASE64_TOKEN_ = token.encode().hex()
            except Exception as e:
                logger.error(f"Client #{self.client_id}: Error processing token: {e}")
                return False

            try:
                head = hex(len(encrypt_packet(BASE64_TOKEN_, key, iv)) // 2)[2:]
                length = len(encoded_acc)
                zeros = '00000000'

                if length == 9:
                    zeros = '0000000'
                elif length == 8:
                    zeros = '00000000'
                elif length == 10:
                    zeros = '000000'
                elif length == 7:
                    zeros = '000000000'
                else:
                    logger.error(f'Client #{self.client_id}: Unexpected length encountered')
                head = f'0115{zeros}{encoded_acc}{time_hex}00000{head}'
                final_token = head + encrypt_packet(BASE64_TOKEN_, key, iv)
            except Exception as e:
                logger.error(f"Client #{self.client_id}: Error constructing final token: {e}")
                return None, None
                
            token = final_token
            self.connect(token, 'anything', key, iv, whisper_ip, whisper_port, online_ip, online_port)
            
            self.is_connected = True
            game_ready = True
            self.is_connecting = False
            self.reconnect_attempts = 0
            
            threading.Thread(target=self.health_check_loop, daemon=True).start()
            
            return True
            
        except Exception as e:
            logger.error(f"❌ Client #{self.client_id}: Final connection error: {str(e)}")
            self.is_connecting = False
            return False
    
    def run(self):
        """Override run function to start game bot"""
        global game_ready
        
        while not telegram_ready:
            logger.info(f"⏳ Client #{self.client_id}: Waiting for Telegram bot to be ready...")
            time.sleep(2)
        
        logger.info(f"🚀 Client #{self.client_id}: Starting connection...")
        self.get_tok()


# ==================== COMMAND PROCESSOR ====================
class CommandProcessor(threading.Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.active_commands = 0
        
    def run(self):
        """Process requests from queue"""
        while True:
            try:
                if self.active_commands < MAX_CONCURRENT_REQUESTS:
                    try:
                        command = command_queue.get(timeout=1)
                        self.active_commands += 1
                        threading.Thread(
                            target=self.process_command,
                            args=(command,),
                            daemon=True
                        ).start()
                        
                    except queue.Empty:
                        pass
                
                time.sleep(0.1)
                
            except Exception as e:
                logger.error(f"❌ Error in command processor: {e}")
                time.sleep(1)
    
    def process_command(self, command):
        """Process a single command"""
        global maintenance_mode
        
        try:
            chat_id = command.get('chat_id')
            user_message_id = command.get('user_message_id')
            
            # ==================== INFO COMMAND HANDLING ====================
            if command['type'] == 'info':
                player_id = command['player_id']
                
                processing_msg = send_telegram_message(
                    "🔍 Searching for player information...",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                
                send_player_info_with_image(player_id, chat_id, user_message_id)
                
                if processing_msg and 'result' in processing_msg:
                    try:
                        delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                    except:
                        pass
                return
            
            # ==================== LIKES COMMAND HANDLING ====================
            if command['type'] == 'like':
                uid = command['player_id']
                
                processing_msg = send_telegram_message(
                    f"❤️ Processing likes request...\n"
                    f"├─ UID: <code>{uid}</code>\n"
                    f"└─ Status: Connecting to API...",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                
                send_likes(uid, chat_id, user_message_id)
                
                if processing_msg and 'result' in processing_msg:
                    try:
                        delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                    except:
                        pass
                return
            
            # ==================== GHOST COMMAND HANDLING ====================
            if command['type'] == 'ghost':
                team_code = command['team_code']
                name = command['name']
                
                processing_msg = send_telegram_message(
                    f"👻 Processing ghost command...\n"
                    f"├─ Team Code: <code>{team_code}</code>\n"
                    f"├─ Name: {name}\n"
                    f"└─ Status: Connecting to game servers...",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                
                send_ghost_command_new(team_code, name, chat_id, user_message_id)
                
                if processing_msg and 'result' in processing_msg:
                    try:
                        delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                    except:
                        pass
                return
            
            # ==================== VISIT SPAM COMMAND HANDLING ====================
            if command['type'] == 'visit_spam':
                target_uid = command['target_uid']
                start_visit_spam(target_uid, chat_id, user_message_id)
                return
            
            # ==================== STOP VISIT SPAM COMMAND HANDLING ====================
            if command['type'] == 'stop_visit_spam':
                target_uid = command['target_uid']
                stop_visit_spam(target_uid, chat_id, user_message_id)
                return
            
            # ==================== FRIEND SPAM COMMAND HANDLING ====================
            if command['type'] == 'friend_spam':
                target_uid = command['target_uid']
                start_friend_spam(target_uid, chat_id, user_message_id)
                return
            
            # ==================== STOP FRIEND SPAM COMMAND HANDLING ====================
            if command['type'] == 'stop_friend_spam':
                target_uid = command['target_uid']
                stop_friend_spam(target_uid, chat_id, user_message_id)
                return
            
            # ==================== SPAM STATUS COMMAND HANDLING ====================
            if command['type'] == 'spam_status':
                status = get_masry_spam_status()
                
                visit_targets = '\n'.join([f"├─ <code>{t}</code>" for t in status['visit_targets']]) if status['visit_targets'] else "├─ None"
                friend_targets = '\n'.join([f"├─ <code>{t}</code>" for t in status['friend_targets']]) if status['friend_targets'] else "├─ None"
                
                send_telegram_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"📊 <b>SPAM STATUS (JAGWR SYSTEM)</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"👁️ <b>Visit Spams:</b> {status['visit_count']}\n"
                    f"{visit_targets}\n\n"
                    f"👥 <b>Friend Spams:</b> {status['friend_count']}\n"
                    f"{friend_targets}\n\n"
                    f"📁 <b>JAGWAR Accounts:</b> {status['masry_accounts']}\n"
                    f"🎫 <b>Active JWT Tokens:</b> {status['jwt_tokens']}\n\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                return
            
            available_client = None
            min_requests = float('inf')
            
            for client in current_clients:
                if client.is_connected:
                    client_requests = active_requests_per_account.get(client.id, 0)
                    if client_requests < min_requests:
                        min_requests = client_requests
                        available_client = client
            
            if not available_client:
                send_telegram_message(
                    "❌ No connected game clients available",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                return
            
            processing_msg = send_telegram_message(
                "🔄 Processing your request...",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
            
            squad_names = {
                "2": "2 Players",
                "3": "3 Players",  
                "4": "4 Players",
                "5": "5 Players",
                "6": "6 Players"
            }
            
            if command['type'] == 'invite':
                player_id = command['player_id']
                squad_type = command['squad_type']
                squad_name = squad_names.get(squad_type, f"{squad_type} Players")
                
                edit_telegram_message(
                    chat_id,
                    processing_msg['result']['message_id'],
                    f"🔄 Processing {squad_name} Squad Invite\n"
                    f"├─ Player ID: `{player_id}`\n"
                    f"└─ Status: Sending invitation..."
                )
                
                success = available_client.execute_invite_command(player_id, squad_type, chat_id, user_message_id)
                
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                
                if success:
                    send_telegram_message(
                        f"✅ Squad Invite Sent Successfully\n"
                        f"├─ Type: {squad_name}\n"
                        f"├─ To Player: <code>{player_id}</code>\n"
                        f"└─ Status: ✅ Delivered",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_telegram_message(
                        f"❌ Failed to Send Invite\n"
                        f"├─ Type: {squad_name}\n"
                        f"├─ To Player: <code>{player_id}</code>\n"
                        f"└─ Status: ❌ Connection error",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
            
            elif command['type'] == 'attack':
                team_code = command['team_code']
                
                edit_telegram_message(
                    chat_id,
                    processing_msg['result']['message_id'],
                    f"⚡ Initiating Attack Protocol\n"
                    f"├─ Target: `{team_code}`\n"
                    f"└─ Status: Loading attack module..."
                )
                
                success = available_client.execute_attack_command(team_code, chat_id, user_message_id)
                
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                
                if success:
                    send_telegram_message(
                        f"🎯 Attack Completed Successfully\n"
                        f"├─ Target: <code>{team_code}</code>\n"
                        f"├─ Duration: 45 seconds\n"
                        f"└─ Status: ✅ Forced start executed",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_telegram_message(
                        f"❌ Attack Failed\n"
                        f"├─ Target: <code>{team_code}</code>\n"
                        f"└─ Status: ❌ System error",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
            
            elif command['type'] == 'lag':
                team_code = command['team_code']
                duration = command.get('duration', 1)
                
                edit_telegram_message(
                    chat_id,
                    processing_msg['result']['message_id'],
                    f"⏸️ Initializing Team Suspension\n"
                    f"├─ Team Code: `{team_code}`\n"
                    f"├─ Duration: {duration} minute(s)\n"
                    f"└─ Status: Loading suspension module..."
                )
                
                success = available_client.execute_lag_command(team_code, duration, chat_id, user_message_id)
                
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                
                if success:
                    send_telegram_message(
                        f"⏸️ Team Suspended Successfully\n"
                        f"├─ Target: <code>{team_code}</code>\n"
                        f"├─ Duration: {duration} minute(s)\n"
                        f"└─ Status: ✅ Team suspended",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_telegram_message(
                        f"❌ Team Suspension Failed\n"
                        f"├─ Target: <code>{team_code}</code>\n"
                        f"└─ Status: ❌ System error",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
            
            # ==================== SPAM COMMAND HANDLING ====================
            elif command['type'] == 'spam':
                target_uid = command['target_uid']
                
                edit_telegram_message(
                    chat_id,
                    processing_msg['result']['message_id'],
                    f"🎯 Initializing Spam Attack\n"
                    f"├─ Target ID: {target_uid}\n"
                    f"├─ Status: Loading spam module..."
                )
                
                requester_name = command.get('requester_name', 'user')
                success = start_spam(target_uid, command['user_id'], requester_name, chat_id, user_message_id)
                
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                
                if not success and command.get('chat_id'):
                    pass
                    
            elif command['type'] == 'stop_spam':
                target_uid = command['target_uid']
                
                edit_telegram_message(
                    chat_id,
                    processing_msg['result']['message_id'],
                    f"⏹️ Stopping Spam Attack\n"
                    f"├─ Target ID: {target_uid}\n"
                    f"└─ Status: Stopping..."
                )
                
                success = stop_spam(target_uid, command['user_id'], chat_id, user_message_id)
                
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                    
            elif command['type'] == 'spam_list':
                active_targets = get_active_spam_targets()
                
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                
                if active_targets:
                    lines = [f"🎯 Active Spam Targets:"]
                    for target in active_targets:
                        lines.append(f"├─ `{target['uid']}` (by @{target['owner_name']})")
                    send_telegram_message(
                        "\n".join(lines),
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_telegram_message(
                        "⚠️ No active spam targets",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
            
            # ==================== FRIEND SYSTEM ====================
            elif command['type'] == 'add_friend':
                player_id = command['player_id']
                days = command.get('days', 0.1667)
                
                if days is None:
                    days = 0.1667
                
                hours = days * 24 if isinstance(days, (int, float)) else 4
                
                edit_telegram_message(
                    chat_id,
                    processing_msg['result']['message_id'],
                    f"👤 Adding Friend\n"
                    f"├─ Player ID: `{player_id}`\n"
                    f"├─ Duration: {hours:.1f} hours\n"
                    f"└─ Status: Sending request..."
                )
                
                name, region, level = get_player_info(player_id)
                response = send_friend_request(player_id)
                
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                
                if "✅" in response:
                    expiry_seconds = days * 86400 if isinstance(days, (int, float)) else 14400
                    
                    users[player_id] = {
                        "name": name,
                        "expiry": time.time() + expiry_seconds,
                        "added_by_tele_id": str(command['user_id']),
                        "added_by_tele_username": command.get('requester_name', 'unknown'),
                        "added_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "region": region,
                        "level": level
                    }
                    save_users()
                    
                    duration_text = f"{days} days" if isinstance(days, (int, float)) and days >= 1 else f"{int(hours)} hours"
                    
                    send_telegram_message(
                        f"✅ Friend request sent successfully!\n"
                        f"├─ Name: {name}\n"
                        f"├─ ID: `{player_id}`\n"
                        f"├─ Region: {region}\n"
                        f"├─ Level: {level}\n"
                        f"└─ Duration: {duration_text}",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_telegram_message(
                        f"❌ Failed to send friend request\n"
                        f"├─ ID: `{player_id}`\n"
                        f"└─ Error: {response}",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                    
            elif command['type'] == 'remove_friend':
                player_id = command['player_id']
                
                edit_telegram_message(
                    chat_id,
                    processing_msg['result']['message_id'],
                    f"🗑️ Removing Friend\n"
                    f"├─ Player ID: `{player_id}`\n"
                    f"└─ Status: Processing..."
                )
                
                if player_id not in users:
                    if processing_msg and 'result' in processing_msg:
                        delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                    send_telegram_message(
                        f"❌ Player not found in list\n"
                        f"├─ ID: `{player_id}`\n"
                        f"└─ Try `/add {player_id}` first",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                    return
                
                name = users[player_id].get('name', 'Unknown')
                response = remove_friend(player_id)
                
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                
                if "✅" in response:
                    del users[player_id]
                    save_users()
                    send_telegram_message(
                        f"✅ Friend removed successfully!\n"
                        f"├─ Name: {name}\n"
                        f"└─ ID: `{player_id}`",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_telegram_message(
                        f"❌ Failed to remove friend\n"
                        f"├─ Name: {name}\n"
                        f"├─ ID: `{player_id}`\n"
                        f"└─ Error: {response}",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                    
            elif command['type'] == 'list_friends':
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                
                game_friends = {uid: data for uid, data in users.items() if isinstance(data, dict) and "name" in data and "expiry" in data}
                
                if not game_friends:
                    send_telegram_message(
                        "📭 No friends added yet.\nUse `/add [ID]` to add friends.",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                    return
                
                total_count = get_total_users_count()
                text = f"📋 Friends List ({total_count}/100):\n\n"
                
                for uid, data in game_friends.items():
                    name = html.unescape(data.get('name', 'Unknown'))
                    remaining = format_remaining_time(data.get('expiry', 0))
                    added_by = data.get('added_by_tele_username', 'unknown')
                    added_date = data.get('added_date', 'unknown')
                    
                    text += f"👤 {name}\n🆔 `{uid}`\n⏳ {remaining}\n👤 By: @{added_by}\n📅 {added_date}\n───────────────────\n"
                
                if len(text) > 4000:
                    chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]
                    for chunk in chunks:
                        send_telegram_message(chunk, chat_id=chat_id, reply_to_message_id=user_message_id)
                        time.sleep(1)
                else:
                    send_telegram_message(text, chat_id=chat_id, reply_to_message_id=user_message_id)
                    
            # ==================== MAINTENANCE COMMANDS ====================
            elif command['type'] == 'maintenance_on':
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                
                if maintenance_mode:
                    send_telegram_message(
                        "⚠️ Bot is already in maintenance mode",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                    return
                
                maintenance_mode = True
                save_maintenance_status(True)
                
                maintenance_message = "⚙️ MAINTENANCE MODE ⚙️\n\n⚠️ Bot is under maintenance. Will be back soon.\n\nThank you for your patience ❤"
                send_telegram_message(
                    "✅ Maintenance mode enabled. Notification sent to all groups.",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                
                groups_data = load_groups_data()
                for group_id in groups_data.keys():
                    try:
                        send_telegram_message(maintenance_message, chat_id=int(group_id), parse_mode="HTML", no_signature=True)
                        time.sleep(0.5)
                    except:
                        pass
                        
            elif command['type'] == 'maintenance_off':
                if processing_msg and 'result' in processing_msg:
                    delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                
                if not maintenance_mode:
                    send_telegram_message(
                        "⚠️ Bot is not in maintenance mode",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                    return
                
                maintenance_mode = False
                save_maintenance_status(False)
                
                unmaintenance_message = "🎉 BOT IS BACK ONLINE 🎉\n\n✅ Bot is now fully operational!\n\nThank you for your patience ❤"
                send_telegram_message(
                    "✅ Maintenance mode disabled. Notification sent to all groups.",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                
                groups_data = load_groups_data()
                for group_id in groups_data.keys():
                    try:
                        send_telegram_message(unmaintenance_message, chat_id=int(group_id), parse_mode="HTML", no_signature=True)
                        time.sleep(0.5)
                    except:
                        pass
                        
            # ==================== LEAVE GROUP COMMAND ====================
            elif command['type'] == 'leave_group':
                target_group_id = command['target_group_id']
                
                edit_telegram_message(
                    chat_id,
                    processing_msg['result']['message_id'],
                    f"🚪 Leaving group {target_group_id}..."
                )
                
                try:
                    bye_message = "👋 Bot is leaving this group. Goodbye!"
                    send_telegram_message(bye_message, chat_id=int(target_group_id), parse_mode="HTML", no_signature=True)
                    time.sleep(1)
                    
                    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/leaveChat"
                    response = requests.post(url, data={"chat_id": target_group_id}, timeout=10)
                    
                    if processing_msg and 'result' in processing_msg:
                        delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                    
                    if response.status_code == 200:
                        send_telegram_message(
                            f"✅ Left group successfully!\n├─ Group ID: `{target_group_id}`",
                            chat_id=chat_id,
                            reply_to_message_id=user_message_id
                        )
                        groups_data = load_groups_data()
                        if str(target_group_id) in groups_data:
                            del groups_data[str(target_group_id)]
                            save_groups_data(groups_data)
                    else:
                        send_telegram_message(
                            f"❌ Failed to leave group\n├─ Group ID: `{target_group_id}`\n└─ Error: {response.text}",
                            chat_id=chat_id,
                            reply_to_message_id=user_message_id
                        )
                except Exception as e:
                    if processing_msg and 'result' in processing_msg:
                        delete_telegram_message(chat_id, processing_msg['result']['message_id'])
                    send_telegram_message(
                        f"❌ Error leaving group: {str(e)}",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
            
            # ==================== NEW ADMIN COMMANDS ====================
            elif command['type'] == 'ban':
                target_id = command['target_id']
                target_name = command['target_name']
                
                success = ban_chat_member(chat_id, target_id)
                if success:
                    send_admin_message(
                        f"━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"💀 <b>USER BANNED</b>\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                        f"User: <b>{target_name}</b>\n"
                        f"ID: <code>{target_id}</code>\n\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_admin_message("❌ Failed to ban user.\nMake sure I am an admin.", chat_id=chat_id, reply_to_message_id=user_message_id)
                return
            
            elif command['type'] == 'kick':
                target_id = command['target_id']
                target_name = command['target_name']
                
                success = ban_chat_member(chat_id, target_id)
                if success:
                    unban_chat_member(chat_id, target_id)
                    send_admin_message(
                        f"━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"👋 <b>USER KICKED</b>\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                        f"User: <b>{target_name}</b>\n"
                        f"ID: <code>{target_id}</code>\n\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_admin_message("❌ Failed to kick user.\nMake sure I am an admin.", chat_id=chat_id, reply_to_message_id=user_message_id)
                return
            
            elif command['type'] == 'mute':
                target_id = command['target_id']
                target_name = command['target_name']
                
                success = restrict_chat_member(chat_id, target_id, False)
                if success:
                    send_admin_message(
                        f"━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"🔇 <b>USER MUTED</b>\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                        f"User: <b>{target_name}</b>\n"
                        f"ID: <code>{target_id}</code>\n\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_admin_message("❌ Failed to mute user.\nMake sure I am an admin.", chat_id=chat_id, reply_to_message_id=user_message_id)
                return
            
            elif command['type'] == 'unmute':
                target_id = command['target_id']
                target_name = command['target_name']
                
                success = restrict_chat_member(chat_id, target_id, True)
                if success:
                    send_admin_message(
                        f"━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"🔊 <b>USER UNMUTED</b>\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                        f"User: <b>{target_name}</b>\n"
                        f"ID: <code>{target_id}</code>\n\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_admin_message("❌ Failed to unmute user.\nMake sure I am an admin.", chat_id=chat_id, reply_to_message_id=user_message_id)
                return
            
            elif command['type'] == 'shadowban':
                target_id = command['target_id']
                target_name = command['target_name']
                
                if target_id == int(ADMIN_ID):
                    send_admin_message(
                        "━━━━━━━━━━━━━━━━━━━━━━\n"
                        "❌ <b>ERROR</b>\n"
                        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
                        "You cannot shadowban yourself, my king.\n\n"
                        "━━━━━━━━━━━━━━━━━━━━━━",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                    return
                
                add_shadowban(target_id)
                send_admin_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"👻 <b>SHADOWBAN ACTIVATED</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"User: <b>{target_name}</b>\n"
                    f"ID: <code>{target_id}</code>\n\n"
                    f"All their messages will be silently deleted.\n\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                return
            
            elif command['type'] == 'unshadowban':
                target_id = command['target_id']
                target_name = command['target_name']
                
                remove_shadowban(target_id)
                send_admin_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"✅ <b>SHADOWBAN REMOVED</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"User: <b>{target_name}</b>\n"
                    f"ID: <code>{target_id}</code>\n\n"
                    f"The user can now send messages normally.\n\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                return
            
            elif command['type'] == 'purge':
                count = command.get('count', 35)
                
                message_ids = []
                current_id = user_message_id - 1
                
                while len(message_ids) < count and current_id > 0:
                    message_ids.append(current_id)
                    current_id -= 1
                
                deleted = delete_messages_bulk(chat_id, message_ids)
                
                notice = send_admin_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚡ <b>PURGE COMPLETED</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"✅ Deleted <b>{deleted}</b> messages\n\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                
                if notice and 'result' in notice:
                    time.sleep(3)
                    try:
                        delete_telegram_message(chat_id, notice['result']['message_id'])
                    except:
                        pass
                return
            
            elif command['type'] == 'lockdown':
                success = set_group_permissions(chat_id, locked=True)
                if success:
                    send_admin_message(
                        "━━━━━━━━━━━━━━━━━━━━━━\n"
                        "🚨 <b>LOCKDOWN ACTIVATED</b>\n"
                        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
                        "The group has been frozen.\n"
                        "No one can send messages.\n\n"
                        "Use <code>/unlock</code> to unfreeze.\n\n"
                        "━━━━━━━━━━━━━━━━━━━━━━",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_admin_message(
                        "❌ Failed to activate lockdown.\nMake sure I am an admin.",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                return
            
            elif command['type'] == 'unlock':
                success = set_group_permissions(chat_id, locked=False)
                if success:
                    send_admin_message(
                        "━━━━━━━━━━━━━━━━━━━━━━\n"
                        "🔓 <b>LOCKDOWN DEACTIVATED</b>\n"
                        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
                        "The group has been unfrozen.\n"
                        "Members can now send messages.\n\n"
                        "━━━━━━━━━━━━━━━━━━━━━━",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                else:
                    send_admin_message(
                        "❌ Failed to deactivate lockdown.\nMake sure I am an admin.",
                        chat_id=chat_id,
                        reply_to_message_id=user_message_id
                    )
                return
            
            elif command['type'] == 'server':
                stats = get_server_stats()
                message = format_server_stats(stats)
                send_admin_message(message, chat_id=chat_id, reply_to_message_id=user_message_id)
                return
                    
        except Exception as e:
            logger.error(f"❌ Error processing command: {e}")
        finally:
            self.active_commands -= 1

def add_command_to_queue(command_type, player_id=None, squad_type=None, team_code=None, duration=1, target_uid=None, chat_id=None, user_message_id=None, user_id=None, requester_name=None, days=None, target_group_id=None, ghost_name=None, target_id=None, target_name=None, count=None):
    """Add a command to the execution queue"""
    command = {
        'type': command_type,
        'player_id': player_id,
        'squad_type': squad_type,
        'team_code': team_code,
        'duration': duration,
        'target_uid': target_uid,
        'chat_id': chat_id,
        'user_message_id': user_message_id,
        'user_id': user_id,
        'requester_name': requester_name,
        'days': days,
        'target_group_id': target_group_id,
        'name': ghost_name,
        'target_id': target_id,
        'target_name': target_name,
        'count': count,
        'timestamp': time.time()
    }
    command_queue.put(command)
    return True

def execute_telegram_command(command, player_id=None, squad_type=None, team_code=None, duration=1, target_uid=None, chat_id=None, user_id=None, user_message_id=None, days=None, target_group_id=None, ghost_name=None, target_id=None, target_name=None, count=None):
    """Execute commands from Telegram"""
    global maintenance_mode
    
    try:
        if maintenance_mode and str(user_id) != ADMIN_ID:
            send_telegram_message(
                "⚙️ Bot is in maintenance mode.\nPlease wait until maintenance is complete.\nApologies for the inconvenience.",
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
            return ""
        
        if str(chat_id).startswith('-') is False:
            if str(user_id) == ADMIN_ID:
                pass
            else:
                send_telegram_message("🙂🖕", chat_id=user_id, no_signature=True, reply_to_message_id=user_message_id)
                return ""
            return ""

        if not is_group_active(chat_id):
            send_telegram_message(
                "⚠️ Bot Activation Expired\n"
                "This group's bot activation has expired.\n"
                "Please contact @JAGWAR_FF1 for reactivation.", 
                chat_id=chat_id,
                reply_to_message_id=user_message_id
            )
            return ""

        if command == "info" and player_id:
            if add_command_to_queue('info', player_id=player_id, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"

        if command == "like" and player_id:
            if add_command_to_queue('like', player_id=player_id, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"

        if command == "ghost" and team_code and ghost_name:
            if add_command_to_queue('ghost', team_code=team_code, ghost_name=ghost_name, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"

        if command == "visit" and target_uid:
            if add_command_to_queue('visit_spam', target_uid=target_uid, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"

        if command == "stop_visit" and target_uid:
            if add_command_to_queue('stop_visit_spam', target_uid=target_uid, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"

        if command == "spam_req" and target_uid:
            if add_command_to_queue('friend_spam', target_uid=target_uid, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"

        if command == "stop_req" and target_uid:
            if add_command_to_queue('stop_friend_spam', target_uid=target_uid, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"

        if command == "spamstatus":
            if add_command_to_queue('spam_status', chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"

        if command == "add" and player_id:
            if add_command_to_queue('add_friend', player_id=player_id, days=days, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id, requester_name=f"user_{user_id}"):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "remove" and player_id:
            if add_command_to_queue('remove_friend', player_id=player_id, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "list":
            if add_command_to_queue('list_friends', chat_id=chat_id, user_message_id=user_message_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "maintenance":
            if add_command_to_queue('maintenance_on', chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "unmaintenance":
            if add_command_to_queue('maintenance_off', chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "leave_group" and target_group_id:
            if add_command_to_queue('leave_group', target_group_id=target_group_id, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command in ["2", "3", "4", "5", "6"] and player_id:
            if add_command_to_queue('invite', player_id=player_id, squad_type=command, chat_id=chat_id, user_message_id=user_message_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "attack" and team_code:
            if add_command_to_queue('attack', team_code=team_code, chat_id=chat_id, user_message_id=user_message_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "lag" and team_code:
            if add_command_to_queue('lag', team_code=team_code, duration=duration, chat_id=chat_id, user_message_id=user_message_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "spam" and target_uid:
            username = f"user_{user_id}"
            if add_command_to_queue('spam', target_uid=target_uid, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id, requester_name=username):
                return ""
            else:
                return "❌ Failed to add spam command"
        
        elif command == "stop" and target_uid:
            if add_command_to_queue('stop_spam', target_uid=target_uid, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add stop command"
        
        elif command == "spam_list":
            if add_command_to_queue('spam_list', chat_id=chat_id, user_message_id=user_message_id):
                return ""
            else:
                return "❌ Failed to add list command"
        
        # ==================== NEW ADMIN COMMANDS ====================
        elif command in ["ban", "kick", "mute", "unmute", "shadowban", "unshadowban"] and target_id:
            if add_command_to_queue(command, target_id=target_id, target_name=target_name, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "purge":
            cnt = count if count else 35
            if add_command_to_queue('purge', count=cnt, chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "lockdown":
            if add_command_to_queue('lockdown', chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "unlock":
            if add_command_to_queue('unlock', chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        elif command == "server":
            if add_command_to_queue('server', chat_id=chat_id, user_message_id=user_message_id, user_id=user_id):
                return ""
            else:
                return "❌ Failed to add command"
        
        else:
            return ""
        
    except Exception as e:
        logger.error(f"Error in execute_telegram_command: {e}")
        return ""

def show_start_menu(chat_id, user_id, user_message_id=None):
    """Main commands menu (for regular users)"""
    user_id_str = str(user_id)
    
    # If user is admin, send admin menu in private chat only
    if user_id_str == ADMIN_ID:
        admin_menu = show_admin_menu(chat_id, user_id)
        if admin_menu:
            # If private chat, send menu directly
            if not str(chat_id).startswith('-'):
                return admin_menu
            # If group, send message that menu was sent to private
            else:
                send_admin_message(
                    "📩 Admin command menu has been sent to your private chat, my king.\n\n"
                    "⟨ ⟨ ⟨ @JAGWAR_FF1 ⟩ ⟩ ⟩",
                    chat_id=chat_id,
                    reply_to_message_id=user_message_id
                )
                return None
    
    # Regular user menu
    is_private = not str(chat_id).startswith('-')
    if is_private:
        return None
    
    menu = "━━━━━━━━━━━━━━━━━━━━━━\n"
    menu += "📋 <b>AVAILABLE COMMANDS</b>\n"
    menu += "━━━━━━━━━━━━━━━━━━━━━━\n\n"
    menu += "🎮 <b>SQUAD INVITES</b>\n"
    menu += "├─ <code>/2</code> (ID) - 2 Players\n"
    menu += "├─ <code>/3</code> (ID) - 3 Players\n"
    menu += "├─ <code>/4</code> (ID) - 4 Players\n"
    menu += "├─ <code>/5</code> (ID) - 5 Players\n"
    menu += "└─ <code>/6</code> (ID) - 6 Players\n\n"
    menu += "⚡ <b>ATTACK COMMANDS</b>\n"
    menu += "├─ <code>/attack</code> (CODE) - Force start\n"
    menu += "├─ <code>/lag</code> (CODE) (MIN) - Team suspend\n"
    menu += "└─ <code>/ghost</code> (CODE) (NAME) - Send ghosts\n\n"
    menu += "🎯 <b>SPAM COMMANDS</b>\n"
    menu += "├─ <code>/spam</code> (UID)\n"
    menu += "├─ <code>/stop</code> (UID)\n"
    menu += "└─ <code>/spam_list</code>\n\n"
    menu += "👁️ <b>VISIT & FRIEND SPAM</b>\n"
    menu += "├─ <code>/visit</code> (UID) - Visit spam\n"
    menu += "├─ <code>/stop_visit</code> (UID)\n"
    menu += "├─ <code>/spam_req</code> (UID) - Friend spam\n"
    menu += "├─ <code>/stop_req</code> (UID)\n"
    menu += "└─ <code>/spamstatus</code>\n\n"
    menu += "🔍 <b>PLAYER INFO</b>\n"
    menu += "└─ <code>/info</code> (UID)\n\n"
    menu += "❤️ <b>LIKES SYSTEM</b>\n"
    menu += "└─ <code>/like</code> (UID)\n\n"
    menu += "👥 <b>FRIEND SYSTEM</b>\n"
    menu += "├─ <code>/add</code> (ID)\n"
    menu += "├─ <code>/remove</code> (ID)\n"
    menu += "└─ <code>/list</code>\n\n"
    menu += "━━━━━━━━━━━━━━━━━━━━━━"
    
    return menu

def process_admin_command(command, parts, chat_id, user_id, user_message_id):
    """Process admin commands"""
    if str(user_id) != ADMIN_ID:
        if str(chat_id).startswith('-'):
            send_telegram_message("❌ Permission denied", chat_id=chat_id, reply_to_message_id=user_message_id)
        else:
            send_telegram_message("🙂🖕", chat_id=user_id, no_signature=True, reply_to_message_id=user_message_id)
        return
    
    if command == "sid" and len(parts) >= 2:
        try:
            days = int(parts[1])
            success, message = activate_group(chat_id, days, user_id)
            send_telegram_message(message, chat_id=chat_id, reply_to_message_id=user_message_id)
        except ValueError:
            send_telegram_message("❌ Days must be a number", chat_id=chat_id, reply_to_message_id=user_message_id)
    
    elif command == "stop" and len(parts) == 1:
        success, message = deactivate_group(chat_id, user_id)
        send_telegram_message(message, chat_id=chat_id, reply_to_message_id=user_message_id)
    
    elif command == "ginfo":
        info = get_group_info(chat_id)
        send_telegram_message(info, chat_id=chat_id, reply_to_message_id=user_message_id)
    
    elif command == "allgroups":
        groups_info = get_all_groups()
        send_telegram_message(groups_info, chat_id=chat_id, reply_to_message_id=user_message_id)

def edit_telegram_message(chat_id, message_id, new_text, parse_mode="HTML", reply_markup=None):
    """Edit an existing Telegram message"""
    try:
        signature = "\n\n────────────────────\n"
        signature += "👑 Developer: JAGWAR KING"
        
        new_text_with_signature = new_text + signature
        
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/editMessageText"
        data = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": new_text_with_signature,
            "parse_mode": parse_mode
        }
        
        if reply_markup:
            data["reply_markup"] = json.dumps(reply_markup)
        
        response = requests.post(url, data=data, timeout=10)
        return response.json()
    except Exception as e:
        logger.error(f"⚠️ Error editing Telegram message: {e}")

def monitor_telegram():
    """Monitor Telegram messages continuously"""
    global telegram_ready, last_update_id
    
    telegram_ready = True
    logger.info("🤖 Telegram bot monitoring started")
    
    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates"
            params = {"offset": last_update_id + 1, "timeout": 30}
            response = requests.get(url, params=params, timeout=35)
            
            if response.status_code == 200:
                data = response.json()
                if data["ok"] and data["result"]:
                    for update in data["result"]:
                        last_update_id = update["update_id"]
                        
                        # Handle normal messages
                        if "message" in update:
                            message = update["message"]
                            chat_id = message["chat"]["id"]
                            user_id = message["from"]["id"]
                            message_id = message["message_id"]
                            username = message["from"].get("username", f"user_{user_id}")
                            
                            if "text" in message:
                                text = message["text"]
                                process_telegram_message(message, chat_id, user_id, message_id, username)
                                
            time.sleep(1)
        except Exception as e:
            logger.error(f"Error in monitor_telegram: {e}")
            time.sleep(3)

def process_telegram_message(message, chat_id, user_id, message_id, username=None):
    """Process Telegram messages"""
    try:
        raw_text = str(message.get("text", "")).strip()
        m_text_lower = raw_text.lower()
        
        u_id = str(user_id)
        c_id = str(chat_id)
        a_id = str(ADMIN_ID)
        
        # No force subscribe check - removed completely
        
        is_private = not c_id.startswith('-')
        
        # Handle start command
        if m_text_lower.startswith('/start'):
            menu = show_start_menu(chat_id, user_id, message_id)
            if menu:
                send_telegram_message(menu, chat_id=chat_id, reply_to_message_id=message_id)
            return

        if not raw_text.startswith('/'):
            return
        
        parts = raw_text.split()
        command = parts[0][1:].lower()
        
        # ==================== NEW ADMIN COMMANDS (Require reply to message) ====================
        if command in ["ban", "kick", "mute", "unmute", "shadowban", "unshadowban"]:
            # Check admin permission
            if u_id != a_id:
                send_telegram_message("❌ You don't have permission to use this command.", chat_id=chat_id, reply_to_message_id=message_id)
                return
            
            # Check if there's a reply to a message
            if "reply_to_message" not in message or message["reply_to_message"] is None:
                send_admin_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"⚠️ <b>USAGE</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"❌ Please reply to a user's message:\n"
                    f"<code>/{command}</code>\n\n"
                    f"Example: Reply to the user's message\n"
                    f"then type <code>/{command}</code>\n\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━",
                    chat_id=chat_id,
                    reply_to_message_id=message_id
                )
                return
            
            # Get target user info from the replied message
            target_user = message["reply_to_message"]["from"]
            target_id = target_user["id"]
            target_name = target_user.get("username", target_user.get("first_name", f"user_{target_id}"))
            
            # Prevent admin from punishing themselves
            if command in ["ban", "kick", "mute", "shadowban"] and target_id == int(a_id):
                send_admin_message(
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"❌ <b>ERROR</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                    f"You cannot {command} yourself, my king.\n\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━",
                    chat_id=chat_id,
                    reply_to_message_id=message_id
                )
                return
            
            # Prevent punishing the bot itself
            try:
                bot_info = requests.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getMe").json()
                bot_id = bot_info.get("result", {}).get("id", 0)
                if target_id == bot_id:
                    send_admin_message(
                        f"━━━━━━━━━━━━━━━━━━━━━━\n"
                        f"❌ <b>ERROR</b>\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
                        f"I cannot {command} myself.\n\n"
                        f"━━━━━━━━━━━━━━━━━━━━━━",
                        chat_id=chat_id,
                        reply_to_message_id=message_id
                    )
                    return
            except:
                pass
            
            # Log the action
            logger.info(f"Admin {user_id} executing {command} on user {target_id} ({target_name}) in chat {chat_id}")
            
            # Execute the command
            execute_telegram_command(
                command,
                target_id=target_id,
                target_name=target_name,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        # ==================== PURGE COMMAND ====================
        if command == "purge" and u_id == a_id:
            count = 35
            if len(parts) > 1 and parts[1].isdigit():
                count = min(int(parts[1]), 200)
            execute_telegram_command(
                "purge",
                count=count,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        # ==================== LOCKDOWN/UNLOCK COMMANDS ====================
        if command == "lockdown" and u_id == a_id:
            execute_telegram_command(
                "lockdown",
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        if command == "unlock" and u_id == a_id:
            execute_telegram_command(
                "unlock",
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        # ==================== SERVER COMMAND ====================
        if command == "server" and u_id == a_id:
            execute_telegram_command(
                "server",
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        # ==================== VISIT & FRIEND SPAM COMMANDS ====================
        if command == "visit":
            if len(parts) < 2:
                send_telegram_message("❌ Usage: /visit [UID]\nExample: /visit 13088065300", chat_id=chat_id, reply_to_message_id=message_id)
                return
            target_uid = parts[1]
            if not target_uid.isdigit():
                send_telegram_message("❌ UID must be numbers only", chat_id=chat_id, reply_to_message_id=message_id)
                return
            execute_telegram_command(
                "visit",
                target_uid=target_uid,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        if command == "stop_visit":
            if len(parts) < 2:
                send_telegram_message("❌ Usage: /stop_visit [UID]\nExample: /stop_visit 13088065300", chat_id=chat_id, reply_to_message_id=message_id)
                return
            target_uid = parts[1]
            if not target_uid.isdigit():
                send_telegram_message("❌ UID must be numbers only", chat_id=chat_id, reply_to_message_id=message_id)
                return
            execute_telegram_command(
                "stop_visit",
                target_uid=target_uid,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        if command == "spam_req":
            if len(parts) < 2:
                send_telegram_message("❌ Usage: /spam_req [UID]\nExample: /spam_req 13088065300", chat_id=chat_id, reply_to_message_id=message_id)
                return
            target_uid = parts[1]
            if not target_uid.isdigit():
                send_telegram_message("❌ UID must be numbers only", chat_id=chat_id, reply_to_message_id=message_id)
                return
            execute_telegram_command(
                "spam_req",
                target_uid=target_uid,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        if command == "stop_req":
            if len(parts) < 2:
                send_telegram_message("❌ Usage: /stop_req [UID]\nExample: /stop_req 13088065300", chat_id=chat_id, reply_to_message_id=message_id)
                return
            target_uid = parts[1]
            if not target_uid.isdigit():
                send_telegram_message("❌ UID must be numbers only", chat_id=chat_id, reply_to_message_id=message_id)
                return
            execute_telegram_command(
                "stop_req",
                target_uid=target_uid,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        if command == "spamstatus":
            execute_telegram_command(
                "spamstatus",
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        # ==================== SPAM COMMANDS ====================
        if command == "spam":
            if len(parts) < 2:
                send_telegram_message("❌ Usage: /spam [UID]", chat_id=chat_id, reply_to_message_id=message_id)
                return
            target_uid = parts[1]
            if not target_uid.isdigit():
                send_telegram_message("❌ UID must be a number", chat_id=chat_id, reply_to_message_id=message_id)
                return
            execute_telegram_command(
                "spam",
                target_uid=target_uid,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        elif command == "stop":
            if len(parts) >= 2 and parts[1].isdigit():
                target_uid = parts[1]
                execute_telegram_command(
                    "stop",
                    target_uid=target_uid,
                    chat_id=chat_id,
                    user_id=user_id,
                    user_message_id=message_id
                )
                return
            elif len(parts) == 1 and u_id == a_id:
                process_admin_command(command, parts, chat_id, user_id, message_id)
                return
            else:
                send_telegram_message("❌ Usage: /stop [UID] or /stop (for admins)", chat_id=chat_id, reply_to_message_id=message_id)
                return
        
        elif command == "spam_list" or command == "spamlist":
            execute_telegram_command(
                "spam_list",
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return

        # ==================== INFO COMMAND ====================
        if command == "info":
            if len(parts) < 2:
                send_telegram_message("❌ Usage: /info [UID]\nExample: /info 9933949869", chat_id=chat_id, reply_to_message_id=message_id)
                return
            player_id = parts[1]
            if not player_id.isdigit():
                send_telegram_message("❌ UID must be numbers only", chat_id=chat_id, reply_to_message_id=message_id)
                return
            execute_telegram_command(
                "info",
                player_id=player_id,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        # ==================== LIKES COMMAND ====================
        if command == "like":
            if len(parts) < 2:
                send_telegram_message("❌ Usage: /like [UID]\nExample: /like 13088065300", chat_id=chat_id, reply_to_message_id=message_id)
                return
            target_uid = parts[1]
            if not target_uid.isdigit():
                send_telegram_message("❌ UID must contain numbers only", chat_id=chat_id, reply_to_message_id=message_id)
                return
            execute_telegram_command(
                "like",
                player_id=target_uid,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        # ==================== GHOST COMMAND ====================
        if command == "ghost":
            if len(parts) < 3:
                send_telegram_message("❌ Usage: /ghost [TEAM_CODE] [NAME]\nExample: /ghost 929293 JAGWAR", chat_id=chat_id, reply_to_message_id=message_id)
                return
            team_code = parts[1]
            ghost_name = parts[2]
            if not team_code.isdigit():
                send_telegram_message("❌ Team code must contain numbers only", chat_id=chat_id, reply_to_message_id=message_id)
                return
            execute_telegram_command(
                "ghost",
                team_code=team_code,
                ghost_name=ghost_name,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        # ==================== FRIEND SYSTEM ====================
        if command == "add":
            if len(parts) < 2:
                send_telegram_message("❌ Usage: /add [UID]", chat_id=chat_id, reply_to_message_id=message_id)
                return
            player_id = parts[1]
            if not player_id.isdigit():
                send_telegram_message("❌ UID must be a number", chat_id=chat_id, reply_to_message_id=message_id)
                return
            
            days = None
            if len(parts) >= 3 and u_id == a_id:
                days_str = parts[2]
                if days_str.isdigit():
                    days = int(days_str)
            
            execute_telegram_command(
                "add",
                player_id=player_id,
                days=days,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        elif command == "remove":
            if len(parts) < 2:
                send_telegram_message("❌ Usage: /remove [UID]", chat_id=chat_id, reply_to_message_id=message_id)
                return
            player_id = parts[1]
            if not player_id.isdigit():
                send_telegram_message("❌ UID must be a number", chat_id=chat_id, reply_to_message_id=message_id)
                return
            execute_telegram_command(
                "remove",
                player_id=player_id,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        elif command == "list":
            execute_telegram_command(
                "list",
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        # ==================== MAINTENANCE COMMANDS ====================
        elif command == "maintenance" and u_id == a_id:
            execute_telegram_command(
                "maintenance",
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        elif command == "unmaintenance" and u_id == a_id:
            execute_telegram_command(
                "unmaintenance",
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return
        
        elif command == "leave_group" and u_id == a_id:
            if len(parts) < 2:
                send_telegram_message("❌ Usage: /leave_group [GROUP_ID]", chat_id=chat_id, reply_to_message_id=message_id)
                return
            target_group_id = parts[1]
            if not target_group_id.lstrip('-').isdigit():
                send_telegram_message("❌ Group ID must be a number", chat_id=chat_id, reply_to_message_id=message_id)
                return
            execute_telegram_command(
                "leave_group",
                target_group_id=target_group_id,
                chat_id=chat_id,
                user_id=user_id,
                user_message_id=message_id
            )
            return

        # ==================== ADMIN COMMANDS ====================
        if command in ["sid", "ginfo", "allgroups"] and u_id == a_id:
            process_admin_command(command, parts, chat_id, user_id, message_id)
            return

        # ==================== ORIGINAL COMMANDS (Invite, Attack, Lag) ====================
        if command in ["2", "3", "4", "5", "6"]:
            if len(parts) < 2:
                send_telegram_message(f"❌ Usage: /{command} [Player ID]", chat_id=chat_id, reply_to_message_id=message_id)
                return
            target_data = parts[1]
            execute_telegram_command(
                command, 
                player_id=target_data,
                chat_id=chat_id, 
                user_id=user_id, 
                user_message_id=message_id
            )
        
        elif command in ["attack", "lag"]:
            if len(parts) < 2:
                send_telegram_message(f"❌ Usage: /{command} [Team Code]", chat_id=chat_id, reply_to_message_id=message_id)
                return
            target_data = parts[1]
            duration = int(parts[2]) if len(parts) > 2 and command == "lag" and parts[2].isdigit() else 1
            execute_telegram_command(
                command, 
                team_code=target_data,
                duration=duration,
                chat_id=chat_id, 
                user_id=user_id, 
                user_message_id=message_id
            )

    except Exception as e:
        logger.error(f"Error in process_telegram_message: {e}")

def start_game_clients():
    """Start all game accounts from JSON file"""
    accounts = load_accounts()
    if not accounts:
        logger.error("❌ No accounts found to start")
        return []
    
    clients = []
    for i, account_data in enumerate(accounts[:MAX_ACCOUNTS]):
        logger.info(f"🚀 Starting account #{i+1}: {account_data.get('name', 'Unknown')}")
        client = FF_CLIENT(account_data)
        client.start()
        clients.append(client)
        time.sleep(2)
    
    logger.info(f"✅ Started {len(clients)} game accounts")
    
    time.sleep(5)
    init_account_queue()
    
    return clients

def health_monitor():
    """Monitor bot health and restart if needed"""
    while True:
        try:
            check_connection_health()
            time.sleep(10)
        except Exception as e:
            logger.error(f"Error in health monitor: {e}")
            time.sleep(10)

def start_jwt_updater():
    """Start periodic JWT Token update"""
    time.sleep(5)
    update_jwt_periodically()

def start_masry_jwt_updater():
    """Start periodic JWT update for accounts in MaSrY.txt"""
    time.sleep(3)
    masry_update_jwt()

# ==================== JOIN TEAMCODE FUNCTION ====================
def join_teamcode(sock, team_code, key, iv):
    """Join a team using team code"""
    try:
        fields = {
            1: 14,
            2: {
                1: team_code
            }
        }
        
        packet = create_protobuf_packet(fields)
        packet = packet.hex()
        header_lenth = len(encrypt_packet(packet, key, iv))//2
        header_lenth_final = dec_to_hex(header_lenth)
        
        if len(header_lenth_final) == 2:
            final_packet = "0515000000" + header_lenth_final + encrypt_packet(packet, key, iv)
        elif len(header_lenth_final) == 3:
            final_packet = "051500000" + header_lenth_final + encrypt_packet(packet, key, iv)
        elif len(header_lenth_final) == 4:
            final_packet = "05150000" + header_lenth_final + encrypt_packet(packet, key, iv)
        elif len(header_lenth_final) == 5:
            final_packet = "0515000" + header_lenth_final + encrypt_packet(packet, key, iv)
        
        sock.send(bytes.fromhex(final_packet))
        return True
    except Exception as e:
        logger.error(f"Error in join_teamcode: {e}")
        return False

# ==================== MAIN ====================
if __name__ == "__main__":
    try:
        logger.info("🚀 Starting Free Fire Bot System...")
        logger.info("=" * 50)
        
        logger.info("📁 Loading Masry accounts from MaSrY.txt...")
        if not load_masry_tokens("MaSrY.txt"):
            logger.warning("⚠️ MaSrY.txt not found or empty - Visit/Friend spam will not work")
        else:
            logger.info(f"✅ Loaded {len(MaSrY_ToK)} Masry accounts")
        
        load_users()
        load_maintenance_status()
        
        logger.info("🔄 Fetching initial JWT token...")
        for initial_attempt in range(5):
            JWT_TOKEN = fetch_jwt_token(max_retries=3, retry_delay=3)
            if JWT_TOKEN:
                logger.info("✅ JWT token obtained successfully")
                break
            else:
                logger.warning(f"⚠️ Initial attempt {initial_attempt + 1}/5 failed, waiting 5 seconds...")
                time.sleep(5)
        else:
            logger.warning("⚠️ Failed to get JWT token after multiple attempts, some features may not work")
            logger.info("💡 The bot will continue trying to get token periodically")
        
        logger.info("1️⃣ Starting Telegram Bot...")
        telegram_thread = threading.Thread(target=monitor_telegram)
        telegram_thread.daemon = True
        telegram_thread.start()
        
        time.sleep(3)
        
        logger.info("2️⃣ Starting Command Processor...")
        command_processor = CommandProcessor()
        command_processor.start()
        
        logger.info("3️⃣ Starting Health Manager...")
        health_manager = HealthManager()
        health_thread = threading.Thread(
            target=health_manager.monitor_all_clients, 
            args=(current_clients,), 
            daemon=True
        )
        health_thread.start()
        
        logger.info("4️⃣ Starting Connection Health Monitor...")
        connection_health_thread = threading.Thread(target=health_monitor, daemon=True)
        connection_health_thread.start()
        
        logger.info("5️⃣ Starting JWT Token Updater...")
        jwt_updater_thread = threading.Thread(target=start_jwt_updater, daemon=True)
        jwt_updater_thread.start()
        
        logger.info("6️⃣ Starting Masry JWT Updater...")
        masry_jwt_thread = threading.Thread(target=start_masry_jwt_updater, daemon=True)
        masry_jwt_thread.start()
        
        logger.info("7️⃣ Starting Expired Users Checker...")
        expired_checker_thread = threading.Thread(target=check_expired_users_periodically, daemon=True)
        expired_checker_thread.start()
        
        logger.info("8️⃣ Starting Daily Reset Timer...")
        daily_reset_thread = threading.Thread(target=daily_reset_timer, daemon=True)
        daily_reset_thread.start()
        
        logger.info("9️⃣ Starting Game Clients from accounts.json...")
        game_clients = start_game_clients()
        
        logger.info("=" * 50)
        logger.info("✅ All systems started successfully!")
        logger.info(f"📱 Telegram: Ready")
        logger.info(f"🎮 Free Fire: {len(game_clients)} accounts loaded")
        logger.info(f"📁 Masry Accounts: {len(MaSrY_ToK)}")
        logger.info(f"🎫 Masry JWT Tokens: {len(JWT_ToKeNs)}")
        logger.info(f"⚡ Max concurrent requests: {MAX_CONCURRENT_REQUESTS}")
        logger.info(f"🎯 Spam System: Active")
        logger.info(f"👻 Ghost System: Active (Socket Based)")
        logger.info(f"👁️ Visit Spam System: Active (Masry System - HTTP Based)")
        logger.info(f"👥 Friend Spam System: Active (Masry System - HTTP Based)")
        logger.info(f"👥 Friend System: Active (Users: {get_total_users_count()})")
        logger.info(f"🔍 Info System: Active")
        logger.info(f"❤️ Likes System: Active")
        logger.info(f"🔧 Maintenance Mode: {'ON' if maintenance_mode else 'OFF'}")
        logger.info(f"👑 Admin Commands: Active (ban, kick, mute, unmute, shadowban, unshadowban, purge, lockdown, unlock, server)")
        logger.info(f"👻 Shadowban: Active ({len(shadowbanned_users)} users shadowbanned)")
        logger.info("=" * 50)
        
        while True:
            try:
                time.sleep(30)
                connected_clients = sum(1 for client in current_clients if client.is_connected)
                connecting_clients = sum(1 for client in current_clients if client.is_connecting)
                total_requests = sum(active_requests_per_account.values())
                active_spam = len(get_active_spam_targets())
                total_friends = get_total_users_count()
                busy_ghosts = sum(1 for v in account_busy_for_commands.values() if v)
                
                masry_status = get_masry_spam_status()
                
                status_msg = f"📊 Status: Telegram=✅ | Game Clients={connected_clients}/{len(game_clients)} | Connecting={connecting_clients} | Active Requests={total_requests} | Queue={command_queue.qsize()} | Spam={active_spam} | VisitSpam={masry_status['visit_count']} | FriendSpam={masry_status['friend_count']} | Ghost=✅(Busy:{busy_ghosts}) | Friends={total_friends} | Info=✅ | Likes=✅ | MasryAccounts={masry_status['masry_accounts']} | JWTTokens={masry_status['jwt_tokens']} | Shadowban={len(shadowbanned_users)}"
                logger.info(status_msg)
                
            except KeyboardInterrupt:
                logger.info("\n🛑 Bot stopped by user")
                break
            except Exception as e:
                logger.error(f"Error in main loop: {e}")
                time.sleep(10)
            
    except Exception as e:
        logger.error(f"❌ Main bot error: {str(e)}")
        logger.info("🔄 Restarting in 5 seconds...")
        time.sleep(RESTART_DELAY)
        restart_bot()
