from flask import Blueprint

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/events/<int:event_id>/register', methods=['POST'])
def register_event(event_id):
    """
    報名活動
    輸入：event_id (URL 參數)
    處理邏輯：
        - 檢查使用者登入狀態
        - 查詢 Event 容量與目前正取人數
        - 若未滿額：Registration.create(status='Confirmed')
        - 若已滿額：Registration.create(status='Waitlist')
    輸出：重新導向至 /my_registrations 並顯示成功/候補訊息
    """
    pass

@registration_bp.route('/events/<int:event_id>/cancel', methods=['POST'])
def cancel_registration(event_id):
    """
    取消報名
    輸入：event_id (URL 參數)
    處理邏輯：
        - 尋找當前使用者的對應 Registration，將狀態改為 Cancelled
        - 檢查該活動是否有狀態為 Waitlist 的紀錄
        - 若有，取第一筆並更新為 Confirmed (自動遞補)
    輸出：重新導向至 /events/<event_id> 或 /my_registrations
    """
    pass

@registration_bp.route('/my_registrations', methods=['GET'])
def my_registrations():
    """
    個人報名紀錄查詢
    輸入：無
    處理邏輯：
        - 檢查登入狀態
        - 呼叫 Registration.get_user_registrations() 取得該使用者所有的報名
    輸出：渲染 templates/registrations/my_list.html
    """
    pass
