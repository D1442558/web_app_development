from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯設置：一個主辦方可以建立多個活動；一個使用者可以擁有多筆報名紀錄
    events_organized = db.relationship('Event', backref='organizer', lazy=True)
    registrations = db.relationship('Registration', backref='user', lazy=True)

    @classmethod
    def create(cls, username, email, password_hash, role='student'):
        new_user = cls(username=username, email=email, password_hash=password_hash, role=role)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(user_id)


class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    organizer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    event_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 關聯設置：一個活動可以有多筆報名紀錄
    registrations = db.relationship('Registration', backref='event', lazy=True)

    @classmethod
    def create(cls, organizer_id, title, description, event_date, location, capacity):
        new_event = cls(
            organizer_id=organizer_id, 
            title=title, 
            description=description, 
            event_date=event_date, 
            location=location, 
            capacity=capacity
        )
        db.session.add(new_event)
        db.session.commit()
        return new_event

    @classmethod
    def get_all(cls):
        return cls.query.order_by(cls.created_at.desc()).all()

    @classmethod
    def get_by_id(cls, event_id):
        return cls.query.get(event_id)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        db.session.commit()

    def delete(self):
        # 刪除活動時，可選擇一併處理相關報名紀錄 (在此我們先只刪除活動本身)
        db.session.delete(self)
        db.session.commit()


class Registration(db.Model):
    __tablename__ = 'registrations'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.String(20), nullable=False) # 狀態有: 'Confirmed', 'Waitlist', 'Cancelled'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, event_id, user_id, status):
        new_reg = cls(event_id=event_id, user_id=user_id, status=status)
        db.session.add(new_reg)
        db.session.commit()
        return new_reg

    @classmethod
    def get_by_id(cls, reg_id):
        return cls.query.get(reg_id)

    @classmethod
    def get_user_registrations(cls, user_id):
        return cls.query.filter_by(user_id=user_id).order_by(cls.created_at.desc()).all()

    def update_status(self, new_status):
        self.status = new_status
        db.session.commit()
