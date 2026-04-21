from flask import Blueprint

event_bp = Blueprint('event', __name__, url_prefix='/events')

@event_bp.route('/create', methods=['GET', 'POST'])
def create_event():
    """
    建立新活動
    輸入：[GET] 無 / [POST] 表單 (title, description, event_date, location, capacity)
    處理邏輯：
        - 檢查登入狀態與身份 (限 organizer)
        - [GET] 渲染建立活動表單
        - [POST] 驗證資料並呼叫 Event.create() 寫入資料庫
    輸出：成功重導向至 /events/<id>，失敗重新渲染表單
    """
    pass

@event_bp.route('/<int:event_id>', methods=['GET'])
def event_detail(event_id):
    """
    活動詳細資訊
    輸入：event_id (URL 參數)
    處理邏輯：
        - 查詢 Event.get_by_id(event_id)
        - 計算目前的報名人數與剩餘名額
        - 若使用者已登入，查詢其是否已報名該活動
    輸出：渲染 templates/events/detail.html
    """
    pass
