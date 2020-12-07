# from flask import Blueprint, render_template, request
# from flask_login import login_required

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db


splitting = Blueprint('splitting', __name__)


def split(people):
    # Sorted based on val
    people = sorted(people, key=lambda val: val[1])
    # Get total owed for each person
    tot_owed = 0.0
    for person, value in people:
        tot_owed += value
    tot_owed /= len(people)

    # Who should send to who
    send_to_who = []

    # Mark start and end in list
    start = 0
    end = len(people)-1

    owed = tot_owed-people[start][1]
    diff = people[end][1]-tot_owed

    # Pay off everyone
    while(start < end):
        # Need to keep paying off end but start is paid off
        if(diff-owed >= 0):
            send_to_who.append(
                (people[start][0], people[end][0], format(owed, '.2f'))
            )
            diff -= owed
            start += 1
            owed = tot_owed-people[start][1]
        # End is payed off but still have money at start
        else:
            send_to_who.append(
                (people[start][0], people[end][0], format(diff, '.2f'))
            )
            owed -= diff
            end -= 1
            diff = people[end][1]-tot_owed
    return send_to_who


@splitting.route('/split_wiser', methods=['POST'])
@login_required
def split_wiser_post():
    event_name = request.form.get('event-name')
    event_value = request.form.get('event-value')

    # TODO Make an SQL query of the added event

    print("Name: {} Event: {}".format(event_name, event_value))
    return redirect(url_for('splitting.split_wiser'))


@splitting.route('/split_wiser')
@login_required
def split_wiser():
    persons = [
        ('Lucas', 23),
        ('Erik', 0),
        ('Miriam', 91),
        ('Emma', 100),
        ('Ludde', 103),
        ('Musen', 400),
        ('Daniel', 600)
    ]
    splitted = split(persons)
    return render_template('split_wiser.html', persons=persons, splitted=splitted)
