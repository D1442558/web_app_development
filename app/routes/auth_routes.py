from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    使用者註冊
    輸入：[GET] 無 / [POST] 表單 (username, email, password)
    處理邏輯：
        - [GET] 渲染註冊表單
        - [POST] 驗證 email 是否重複。將密碼加密後寫入 DB (User.create)。
    輸出：成功重導至 /auth/login，失敗重新渲染 register.html
    """
    pass

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    使用者登入
    輸入：[GET] 無 / [POST] 表單 (email, password)
    處理邏輯：
        - [GET] 渲染登入表單
        - [POST] 驗證帳號密碼，成功則記錄 Session
    輸出：成功重導至首頁 (/)，失敗重新渲染 login.html
    """
    pass

@auth_bp.route('/logout', methods=['POST'])
def logout():
    """
    使用者登出
    輸入：無 (通常透過點擊隱藏表單或按鈕發送 POST)
    處理邏輯：清除 Session
    輸出：重導向至首頁 (/)
    """
    pass
