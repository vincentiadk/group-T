from flask import Blueprint, render_template, redirect, url_for

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    return redirect(url_for('auth.login'))

@auth.route('/signin', methods=['POST'])
def singin_post():
    # code to validate sign in
    return redirect(url_for('auth.login'))