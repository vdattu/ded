









@app.route('national_committee/')
def national_committee():
    return render_template('national-committee.html')



@app.route('ima_ap_state_committee/')
def ima_ap_state_committee():
    return render_template('ima-ap-state-committe.html')




@app.route('mission_statement/')
def national_committee():
    return render_template('mission-statement.html')



@app.route('rules_nav/')
def rules_nav():
    return render_template('rules.html')



@app.route('contact/')
def contact():
    return render_template('contact.html')



@app.route('venue_sports_schedule/')
def venue_sports_schedule():
    return render_template('schedule.html')



@app.route('games_subgames/')
def games_subgames():
    return render_template('games.html')



@app.route('terms_conditions/')
def terms_conditions():
    return render_template('terms_conditions.html')

@app.route('privacy_policy/')
def privacy_policy():
    return render_template('privacy-policy.html')


@app.route('refund_returns/')
def refund_returns():
    return render_template('refund-schedule.html')


