from flask import Blueprint, redirect, flash, url_for, render_template, request, jsonify
from flask_restful import Resource
from .forms import UnitForm
from tfteamaker.models import Unit
from tfteamaker import db
from flask_cors import cross_origin

from .cors_bypass import _build_cors_prelight_response, _corsify_actual_response

teams = Blueprint('teams', __name__)


@teams.route('/new_team')
def new_team():
    units = Unit.query.all()
    return render_template('new_team.html', title='New Team', units=units)


class CompSerializer:
    def __init__(self, units):
        self.units = units

        # to bedzie zwracac funkcja serializer, dalem to tutaj zeby sie latwiej przepisywalo klasy
        r_dict = {"units": self.units,
                  "synergies": {

                  }}

        self.soulbound = set()
        self.warden = set()
        self.summoner = set()
        self.ranger = set()
        self.predator = set()
        self.blademaster = set()
        self.mage = set()
        self.mystic = set()
        self.berserker = set()
        self.druid = set()
        self.assassin = set()
        self.alchemist = set()

        self.light = set()
        self.crystal = set()
        self.glacial = set()
        self.electric = set()
        self.inferno = set()
        self.desert = set()
        self. cloud = set()
        self.poison = set()
        self.lunar = set()
        self.shadow = set()
        self.steel = set()
        self.variable = set()
        self.woodland = set()
        self.ocean = set()
        self.mountain = set()

    def serialize(self):
        units_ = []
        for unit in self.units:
            u = Unit.query.filter_by(name=unit).first()
            units_.append(u)

        instance_dict = self.__dict__.items()
        for class_, set_ in instance_dict:
            for unit in units_:
                if unit.class1 == class_:
                    set_.add(unit)
                if unit.class2 == class_:
                    set_.add(unit)
                if unit.class3 == class_:
                    set_.add(unit)

        r_dict = {}
        for class_, set_ in instance_dict:
            if class_ != 'units':
                if len(set_) != 0:
                    r_dict[class_] = {}
                    units = {'units': []}
                    for unit in set_:
                        units['units'].append(str(unit))
                    r_dict[class_] = units
        return r_dict


@teams.route('/api/new_team', methods=["POST", "OPTIONS"])
def comp():
    if request.method == "OPTIONS":
        return _build_cors_prelight_response()
    if request.method == "POST":
        json_data = request.get_json()
        cs = CompSerializer(json_data.get('units'))
        r_dict = cs.serialize()
        response = jsonify(r_dict)
        return _corsify_actual_response(response)
























# @teams.route('/new_unit', methods=['GET', 'POST'])
# def new_unit():
#     form = UnitForm()
#     if form.validate_on_submit():
#         unit = Unit(name=form.name.data.capitalize(), cost=form.cost.data, clean_name=form.name.data.lower(), class1=form.class1.data, class2=form.class2.data, class3=form.class3.data)
#         db.session.add(unit)
#         db.session.commit()
#         flash(f'Created unit name={unit.name}, cost={form.cost.data}, clean_name={unit.clean_name}, class1={form.class1.data}, class2={form.class2.data}, class3={form.class3.data})', category='warning')
#         return redirect(url_for('teams.new_unit'))
#     return render_template('new_unit.html', form=form)
