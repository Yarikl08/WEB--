from waitress import serve
import os

from flask import Flask, render_template, redirect, request, abort, make_response, jsonify, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, EmailField, PasswordField, DateField, \
    TextAreaField
from wtforms.validators import DataRequired
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_restful import abort, Api

from WEB_project_TуСОВКА_Igoshin_11_04_2024 import users_resource, events_resource, communities_resource
from WEB_project_TуСОВКА_Igoshin_11_04_2024.data import db_session
from WEB_project_TуСОВКА_Igoshin_11_04_2024.data.communities import Communities
from WEB_project_TуСОВКА_Igoshin_11_04_2024.data.events import Events
from WEB_project_TуСОВКА_Igoshin_11_04_2024.data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)


class RegisterForm(FlaskForm):
    login_email = EmailField('Логин / Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    repeat_password = PasswordField('Повторить пароль', validators=[DataRequired()])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст')
    about_me = TextAreaField('Немного о себе')
    hobbies = StringField('Хобби')
    city_from = StringField('Ваш город?')
    phone = StringField("Телефон")
    submit = SubmitField('Сохранить')


class CommunitiesForm(FlaskForm):
    topic = StringField("Тема", validators=[DataRequired()])
    title = StringField("Название сообщества", validators=[DataRequired()])
    in_detail = TextAreaField("Описание", validators=[DataRequired()])
    organizer = IntegerField("Организатор", validators=[DataRequired()])
    members = StringField("Участники", validators=[DataRequired()])
    contacts = StringField("Контакты", validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class EventsForm(FlaskForm):
    topic = StringField("Тема", validators=[DataRequired()])
    community = StringField("Название мероприятия", validators=[DataRequired()])
    organizer = IntegerField("Организатор")
    age_limit = IntegerField("Возрастное ограничение (+)")
    area = StringField("Площадка")
    start_date = DateField("Начало")
    end_date = DateField("Окончание")
    is_finished = BooleanField("Закончено?")
    submit = SubmitField('Сохранить')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Сохранить')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


@app.route('/events_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def events_delete(id):
    db_sess = db_session.create_session()
    events = db_sess.query(Events).filter(Events.id == id,
                                      Events.user == current_user
                                      ).first()
    if events:
        db_sess.delete(events)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/communities_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def communities_delete(id):
    db_sess = db_session.create_session()
    communities = db_sess.query(Communities).filter(Communities.id == id,
                                      Communities.user == current_user
                                      ).first()
    if communities:
        db_sess.delete(communities)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/index_communities')


@app.route('/events/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_events(id):
    form = EventsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        events = db_sess.query(Events).filter(Events.id == id,
                                          Events.user == current_user
                                          ).first()
        if events:
            form.topic.data = events.topic
            form.community.data = events.community
            form.organizer.data = events.organizer
            form.age_limit.data = events.age_limit
            form.area.data = events.area
            form.start_date.data = events.start_date
            form.end_date.data = events.end_date
            form.is_finished.data = events.is_finished
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        events = db_sess.query(Events).filter(Events.id == id,
                                          Events.user == current_user
                                          ).first()
        if events:
            events.topic = form.topic.data
            events.community = form.community.data
            events.organizer = form.organizer.data
            events.age_limit = form.age_limit.data
            events.area = form.area.data
            events.start_date = form.start_date.data
            events.end_date = form.end_date.data
            events.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('events.html',
                           title='Список мероприятий',
                           form=form
                           )


@app.route('/communities/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_communities(id):
    form = CommunitiesForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        communities = db_sess.query(Communities).filter(Communities.id == id,
                                          Communities.user == current_user
                                          ).first()
        if communities:
            form.topic.data = communities.topic
            form.title.data = communities.title
            form.in_detail.data = communities.in_detail
            form.organizer.data = communities.organizer
            form.members.data = communities.members
            form.contacts.data = communities.contacts
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        communities = db_sess.query(Communities).filter(Communities.id == id,
                                          Communities.user == current_user
                                          ).first()
        if communities:
            communities.topic = form.topic.data
            communities.title = form.title.data
            communities.organizer = form.organizer.data
            communities.in_detail = form.in_detail.data
            communities.members = form.members.data
            communities.contacts = form.contacts.data
            db_sess.commit()
            return redirect('/index_communities')
        else:
            abort(404)
    return render_template('communities.html',
                           title='Добавить сообщество',
                           form=form
                           )


@app.route('/events',  methods=['GET', 'POST'])
@login_required
def add_events():
    form = EventsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        events = Events()
        events.topic = form.topic.data
        events.community = form.community.data
        events.organizer = form.organizer.data
        events.age_limit = form.age_limit.data
        events.area = form.area.data
        events.start_date = form.start_date.data
        events.end_date = form.end_date.data
        events.is_finished = form.is_finished.data
        current_user.events.append(events)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('events.html', title='Добавить мероприятие', form=form)


@app.route('/communities',  methods=['GET', 'POST'])
@login_required
def add_communities():
    form = CommunitiesForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        communities = Communities()
        communities.topic = form.topic.data
        communities.title = form.title.data
        communities.in_detail = form.in_detail.data
        communities.organizer = form.organizer.data
        communities.members = form.members.data
        communities.contacts = form.contacts.data
        current_user.communities.append(communities)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/index_communities')
    return render_template('communities.html', title='Добавить сообщество', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
@app.route("/index")
def index():
    themes = ['Спорт', 'Театр', 'Кино', 'Рыбалка', 'Мастер-классы', 'Экскурсии', 'Ярмарки', 'Питомцы', 'Игры',
              'Книги', 'Транспорт', 'Рукоделие', 'Поездки']
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        events = db_sess.query(Events).filter(Events.user == current_user)
    else:
        events = db_sess.query(Events)
    return render_template("index.html", title='ТуСОВКА - портал для совместного проведения досуга', themes=themes,
                           events=events)


@app.route("/index_communities")
def index_communities():
    db_sess = db_session.create_session()
    communities = db_sess.query(Communities).filter(Communities.title != '')
    return render_template("index_communities.html", title='Список сообществ', communities=communities)


@app.route("/login_1")
def login_1():
    return render_template("login_1.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.repeat_password.data:
            return render_template('register.html', title='Регистрация', form=form, message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.login_email.data).first():
            return render_template('register.html', title='Регистрация', form=form, message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            about_me=form.about_me.data,
            hobbies=form.hobbies.data,
            city_from=form.city_from.data,
            phone=form.phone.data,
            email=form.login_email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <title>Галерея фотографий с мероприятий</title>
    </head>
      <body>
      <p><a href="index" class="link-primary">на Главную страницу</a></p>
        <h1 class="text-center">Галерея фотографий с мероприятий</h1>
        <div id="carouselExampleIndicators" class="carousel slide">
          <div class="carousel-indicators">
            <button type="button" data-bs-target="#carouselExampleIndicators"
             data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators"
             data-bs-slide-to="1" aria-label="Slide 2"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators"
             data-bs-slide-to="2" aria-label="Slide 3"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators"
             data-bs-slide-to="3" aria-label="Slide 4"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators"
             data-bs-slide-to="4" aria-label="Slide 5"></button>
            <button type="button" data-bs-target="#carouselExampleIndicators"
             data-bs-slide-to="5" aria-label="Slide 6"></button>
          </div>
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="{url_for('static', filename='img/1.jpg')}" class="d-block w-100"
               alt="здесь должна была быть картинка, но не нашлась">
            </div>
            <div class="carousel-item">
              <img src="{url_for('static', filename='img/2.jpg')}" class="d-block w-100"
               alt="здесь должна была быть картинка, но не нашлась">
            </div>
            <div class="carousel-item">
              <img src="{url_for('static', filename='img/3.jpg')}" class="d-block w-100"
               alt="здесь должна была быть картинка, но не нашлась">
            </div>
            <div class="carousel-item">
              <img src="{url_for('static', filename='img/4.jpg')}" class="d-block w-100"
               alt="здесь должна была быть картинка, но не нашлась">
            </div>
            <div class="carousel-item">
              <img src="{url_for('static', filename='img/5.jpg')}" class="d-block w-100"
               alt="здесь должна была быть картинка, но не нашлась">
            </div>
        </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators"
           data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators"
           data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
         integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
          crossorigin="anonymous"></script>
      </body>
    </html>'''


db_session.global_init("db/party.sqlite")
session = db_session.create_session()
session.commit()

# для списка объектов
api.add_resource(users_resource.UsersListResource, '/api/v2/users')

# для одного объекта
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')

# для списка объектов
api.add_resource(events_resource.EventsListResource, '/api/v2/events')

# для одного объекта
api.add_resource(events_resource.EventResource, '/api/v2/events/<int:event_id>')

# для списка объектов
api.add_resource(communities_resource.CommunitiesListResource, '/api/v2/communities')

# для одного объекта
api.add_resource(communities_resource.CommunitiesResource, '/api/v2/communities/<int:communities_id>')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # serve(app, host='0.0.0.0', port=5000)