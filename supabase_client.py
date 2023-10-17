from supabase import create_client, Client
import os

#connect to supabase database
urL: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(urL, key)

def get_prompt(bot_name):
    data, count = supabase.table("bots_dev").select("*").eq("id", bot_name).execute()
    bot_info = data[1][0]

    system_prompt = bot_info['system_prompt']
    return system_prompt



