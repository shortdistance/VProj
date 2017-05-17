from flask import render_template, request, redirect, url_for
from . import bpmain, bpmain_filter
from script.services.hpp import hpp_search
from script.services.sale import sale_search
import json
from filter import login_filter
from script.models.database import db_session

bpmain_filter.before_request(login_filter)


@bpmain.after_request
def close_session_after_request(response):
    db_session.remove()
    return response


@bpmain.route('/')
@bpmain.route('/hpp/search')
def hpp_search_page():
    return render_template('hpp/search.html')


@bpmain_filter.route('/sale/search')
def sale_search_page():
    return render_template('sale/search.html')


@bpmain.route('/hpp/area/detail')
def location_hpp_details():
    loc_str = request.args.get('location')
    price_flag = request.args.get('price-selection')
    date_flag = request.args.get('daterange-selection')

    bexist, ptype, poutput = hpp_search(loc_str, price_flag, date_flag)
    qry_str = {
        'loc': loc_str,
        'price': price_flag,
        'date': date_flag
    }

    if bexist and poutput['district_list'] and poutput['district_hpp_analysis']:
        return render_template('/hpp/details.html', qry_str=qry_str, bexist=bexist, ptype=ptype, poutput=poutput)
    else:
        return render_template('hpp/search.html')


@bpmain_filter.route('/hpp/history/records')
def hpp_history_records():
    return redirect(url_for('bpmain.hpp_search_page'))


@bpmain_filter.route('/hpp/report/2017')
def hpp_report_2017():
    return redirect(url_for('static', filename='data/housing_market_report_q1_2017.pdf'))


@bpmain_filter.route('/hpp/report/2016')
def hpp_report_2016():
    return redirect(url_for('static', filename='data/2015-16_EHS_Headline_Report.pdf'))



@bpmain_filter.route('/sale/area/detail')
def location_sale_details():
    loc_str = request.args.get('location')
    price_flag = request.args.get('price-selection')
    type_flag = request.args.get('type-selection')

    bexist, ptype, poutput = sale_search(loc_str, price_flag=None, type_flag=None)
    qry_str = {
        'loc': loc_str,
        'price': price_flag,
        'type': type_flag

    }

    if bexist and poutput and poutput['sale_analysis']:
        return render_template('/sale/details.html', qry_str=qry_str, bexist=bexist, ptype=ptype, poutput=poutput)
    else:
        return render_template('sale/search.html')


@bpmain.route('/sale/property/see_details')
def see_property_details():
    pass


@bpmain.route('/admin/<string:pagename>')
def admin(pagename):
    return render_template('admin/%s' % pagename)


@bpmain.route('/google/<string:pagename>')
def google(pagename):
    return render_template('google/%s' % pagename)
