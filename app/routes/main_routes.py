from flask import Blueprint

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    """
    首頁 / 活動列表
    輸入：無
    處理邏輯：呼叫 Event.get_all() 取出所有活動，按時間排序
    輸出：渲染 templates/index.html
    """
    pass
