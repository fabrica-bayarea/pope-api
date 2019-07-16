from app.models.auth import User
from . import auth
from flask import render_template, \
    redirect, url_for, request, flash, g
from .forms import LoginForm
from flask_login import logout_user, \
    login_required, login_user, current_user
from .. import login_manager


@auth.before_request
def get_current_user():
    g.user = current_user


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('dashboard.dashboard')
            return redirect(next)
        flash('Senha, email ou número de telefone inválidos.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@login_manager.user_loader
def load_user(id_user):
    return User.query.get(int(id_user))
