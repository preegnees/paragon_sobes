from cli_core import CLICore 

# тут воссоздаю то, что написал в script_imput.py

def main():
    if not CLICore._create_organization("IncIncInc" "contact@inc.com" "Russia"):
        raise "ошибка создания организации"
    
    if not CLICore._create_user("BestBoy" "Qwerty123" "Ivan" "Ivanov" "Bashkir" "Russian"):
        raise "ошибка создания пользователя"
    
    if not CLICore._set_access_config("for_ivan", "/api/v0", "https://paragon.paragonbox.com", \
                                 "IncIncInc", "contact@inc.com", "admin_user@inc.com", "Qwerty123"):
        raise "ошибка создания пользователя"
    
    if not CLICore._use_access_config("Oleg" "IncIncInc" "BestTeam" "Developer", None):
        raise "ошибка предоставления правк пользователю \"Ivan\" \"Ivanov\""
    
    if not CLICore._create_business_user("for_ivan"):
        raise "ошибка создания бизнес пользователя"
    
    if not CLICore._show_organizations():
        raise "ошибка отображения организаций"
    
    if not CLICore._login("api_key", "admin" "Difficult_password"):
        raise "ошибка логина для пользователя \"admin\""
    
    if not CLICore._raw_request_admin("/registry/admin/organizations", "GET", None, None):
        raise "ошибка создания raw"


if __name__ == "__main__":
    main()
