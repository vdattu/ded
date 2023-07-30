from flask import Flask, request, redirect, render_template, url_for, flash,session,abort
import flask_excel as excel
from flask_session import Session
import mysql.connector
import random
from io import BytesIO
from key import secret_key, salt, salt2
from itsdangerous import URLSafeTimedSerializer
from stoken import token
from cmail import sendmail
import os
import uuid
from werkzeug.utils import secure_filename
from flask_bcrypt import Bcrypt
import stripe

app = Flask(__name__)
app.secret_key = secret_key
app.config['SESSION_TYPE'] = 'filesystem'
excel.init_excel(app)
Session(app)
mydb = mysql.connector.connect(host='localhost', user='root', password='Eswar@2001', db='doctors',pool_name='DED',pool_size=30)
'''db= os.environ['RDS_DB_NAME']
user=os.environ['RDS_USERNAME']
password=os.environ['RDS_PASSWORD']
host=os.environ['RDS_HOSTNAME']
port=os.environ['RDS_PORT']
with mysql.connector.connect(host=host,user=user,password=password,db=db) as conn:
  cursor=conn.cursor(buffered=True)
  cursor.execute("CREATE TABLE if not exists register (ID int NOT NULL AUTO_INCREMENT,FirstName varchar(25) DEFAULT NULL,LastName varchar(25) DEFAULT NULL,Email varchar(50) DEFAULT NULL,PASSWORD longblob,mobileno bigint DEFAULT NULL,age int DEFAULT NULL,gender varchar(10) DEFAULT NULL,DOB date DEFAULT NULL,city text,address text,state text,country text,degree varchar(10) DEFAULT NULL,MCI_ID varchar(20) DEFAULT NULL,member varchar(20) DEFAULT NULL,SHIRT_SIZE enum('S','M','L','XL','XXL','XXXL','XXXXL') DEFAULT NULL,acception varchar(30) DEFAULT 'No',status varchar(20) NOT NULL DEFAULT 'pending',PRIMARY KEY (ID),UNIQUE KEY Email (Email),UNIQUE KEY mobileno (mobileno))")
  cursor.execute("CREATE TABLE if not exists game (ID INT, GAME ENUM('ATHLETICS','ARCHERY','BADMINTON','CARROM','CHESS','CYCLOTHON','JUMPS','WALKATHON','SWIMMING','TENNKOIT','THROW','ROWING','ROLLER SKATING','FENCING','SHOOTING','TABLE TENNIS','LAWN TENNIS'),FOREIGN KEY(ID) REFERENCES register(ID),AMOUNT INT UNSIGNED)")
  cursor.close()
mydb=mysql.connector.connect(host=host,user=user,password=password,db=db,pool_name='DED',pool_size=30)'''

stripe.api_key='sk_test_51NTKipSDmVNK7hRpj4DLpymMTojbp0sntuHknEF9Kv3cGY79VkNbmBcfxDmTLXa9UIGKiiqp8drQQhzsjoia58Sm00Kuzg9vYt'

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads/certificates')
app.config['UPLOAD_FOLDERS'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/uploads/photos')

bcrypt = Bcrypt(app)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/national_committee')
def national_committee():
    return render_template('national-committee.html')



@app.route('/ima_ap_state_committee')
def ima_ap_state_committee():
    return render_template('ima-ap-state-committe.html')




@app.route('/mission_statement')
def mission_statement():
    return render_template('mission-statement.html')



@app.route('/rules_nav')
def rules_nav():
    return render_template('rules.html')



@app.route('/contact')
def contact():
    return render_template('contact.html')



@app.route('/venue_sports_schedule')
def venue_sports_schedule():
    return render_template('schedule.html')



@app.route('/games_subgames')
def games_subgames():
    return render_template('games.html')



@app.route('/terms_conditions')
def terms_conditions():
    return render_template('terms_conditions.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy-policy.html')


@app.route('/refund_returns')
def refund_returns():
    return render_template('refund-schedule.html')




@app.route('/rules', methods=['GET', 'POST'])
def rules():

    if request.method == 'POST':
        if 'accept' in request.form:
            user_accept =request.form['accept']
            return redirect(url_for('register', user_accept=user_accept))
        else:
            user_accept = False
            return render_template('rules1.html')

    return render_template('rules1.html')

@app.route('/register/<user_accept>', methods=['GET', 'POST'])
def register(user_accept):
    if user_accept=='Yes':

        if request.method == 'POST':
            acception = user_accept
            fname = request.form['fname']
            lname = request.form['lname']
            email = request.form['email']
            password = request.form['password']
            mobile = request.form['mobile']
            age = request.form['age']
            gender = request.form['gender']
            dob = request.form['dob']
            city = request.form['city']
            address = request.form['address']
            state = request.form['state']
            country = request.form['country']
            degree = request.form['degree']
            mci = request.form['mci']
            game = request.form['game']
            selectmember = request.form['selectmember']
            shirtsize = request.form['shirtsize']
            
            # Get the uploaded certificate and photo files
            certificate_file = request.files['certificate']
            photo_file = request.files['photo']

            # Generate unique filenames for certificate and photo using UUID
            certificate_filename = f'{mobile}.{certificate_file.filename.split(".")[-1]}'
            photo_filename = f'{mobile}.{photo_file.filename.split(".")[-1]}'

            # Save the certificate and photo files to the upload folder
            certificate_file.save(os.path.join(app.config['UPLOAD_FOLDER'], certificate_filename))
            photo_file.save(os.path.join(app.config['UPLOAD_FOLDERS'], photo_filename))
            
            if selectmember == 'IMA Member':
                amount = 3500
            else:
                amount = 4000
            
            full_name = fname + ' ' + lname  # Combine first name and last name

            cursor = mydb.cursor(buffered=True)
            # cursor.execute('SELECT COUNT(*) FROM register WHERE CONCAT(FirstName, " ", LastName) = %s', [full_name])
            # count = cursor.fetchone()[0]
            cursor.execute('SELECT COUNT(*) FROM register WHERE Email = %s', [email])
            count1 = cursor.fetchone()[0]
            cursor.execute('SELECT COUNT(*) FROM register WHERE mobileno = %s', [mobile])
            count2 = cursor.fetchone()[0]
            cursor.close()


            if count2 == 1:
                flash('Mobile number already exists.')
                return render_template('register.html')
            elif count1 == 1:
                flash('Email already in use')
                
                return render_template('register.html')


            # Hash the password using bcrypt
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            

            data = {
                'fname': fname, 'lname': lname, 'email': email, 'password': hashed_password, 'mobile': mobile,
                'age': age, 'gender': gender, 'dob': dob, 'city': city, 'address': address, 'state': state,
                'country': country, 'degree': degree, 'mci': mci, 'game': game, 'selectmember': selectmember,
                'acception': acception, 'amount': amount,'shirtsize': shirtsize,
            }
            

            subject = 'Email Confirmation'
            body = f"Thanks for signing up\n\nfollow this link for further steps-{url_for('confirm', token=token(data, salt), _external=True)}"
            sendmail(to=email, subject=subject, body=body)

            flash('Confirmation link sent to mail')

        return render_template('register.html')
    else:
        abort(404,'Page not found')

@app.route('/confirm/<token>')
def confirm(token):
    try:
        serializer = URLSafeTimedSerializer(secret_key)
        data = serializer.loads(token, salt=salt, max_age=3600)
    except Exception as e:
        return 'Link Expired register again'
    else:
        cursor = mydb.cursor(buffered=True)
        name = data['email']
        cursor.execute('SELECT COUNT(*) FROM register WHERE email=%s', [name])
        count = cursor.fetchone()[0]
        if count == 1:
            cursor.close()
            flash('You are already registered!')
            return redirect(url_for('login'))
        else:
            cursor.execute('INSERT INTO register(FirstName,LastName,Email,password,mobileno,age,gender,DOB,city,address,state,country,degree,MCI_ID,member,shirt_size,acception) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', [data['fname'], data['lname'], data['email'], data['password'], data['mobile'], data['age'], data['gender'], data['dob'], data['city'], data['address'], data['state'], data['country'], data['degree'], data['mci'], data['selectmember'],data['shirtsize'], data['acception']])
            cursor.execute('select id from register where email=%s', [data['email']])
            eid=cursor.fetchone()[0]
            cursor.execute('INSERT INTO game (id,game,amount) VALUES (%s,%s,%s)', [eid,data['game'],data['amount']])
            mydb.commit()
            cursor.close()
            flash ('Registration successful! Complete the payment process.')
            return redirect(url_for('payment',eid=eid,game=data['game']))
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = mydb.cursor(buffered=True)
        cursor.execute('SELECT * FROM register WHERE Email = %s', [email])
        user = cursor.fetchone()
        cursor.close()

        if user:
            # Check the hashed password with the entered password
            if bcrypt.check_password_hash(user[4], password):
                # Log the user in by setting the 'user' in the session

                # Check if the status is 'success'
                if user[18] == 'success':
                    session['user'] = user[0]
                    flash('Login successful!', 'success')
                    return redirect(url_for('dashboard'))
                    # return('Ram ram')
                else:
                    cursor = mydb.cursor(buffered=True)
                    cursor.execute('select id from register where email=%s', [email])
                    eid=cursor.fetchone()[0]
                    cursor.execute('SELECT game,amount FROM game where id=%s', [eid])
                    game,amount=cursor.fetchone()
                    cursor.close()
                    # If the status is not 'success', redirect to the payment page
                    return redirect(url_for('payment',game=game,eid=eid))

            else:
                flash('Invalid password! Please try again.', 'error')
        else:
            flash('User not found! Please check your email and try again.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    if session.get('user'):
        session.pop('user')
        return redirect(url_for('home'))
    else:
        flash("already logged out")
        return redirect(url_for('login'))


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']

        cursor = mydb.cursor(buffered=True)
        cursor.execute('SELECT COUNT(*) FROM register WHERE Email=%s', [email])
        count = cursor.fetchone()[0]
        cursor.close()

        if count == 0:
            flash('Email not found. Please enter a registered email.')
            return render_template('forgot_password.html')

        # Generate a one-time token for password reset
        serializer = URLSafeTimedSerializer(secret_key)
        token = serializer.dumps(email, salt=salt2)

        # Send the reset link to the user's email
        subject = 'Password Reset Link'
        body = f"Please follow this link to reset your password: {url_for('reset_password', token=token, _external=True)}"
        sendmail(to=email, subject=subject, body=body)

        flash('Password reset link sent to your email.')
        return redirect(url_for('login'))

    return render_template('forgot_password.html')

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        serializer = URLSafeTimedSerializer(secret_key)
        email = serializer.loads(token, salt=salt2, max_age=180)
    except Exception as e:
        flash('Invalid or expired token. Please request a new password reset.')
        return redirect(url_for('forgot_password'))

    if request.method == 'POST':
        # Validate and update the new password
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash('Passwords do not match. Please try again.')
            return render_template('reset_password.html', token=token)

        # Hash the new password using bcrypt
        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')

        cursor = mydb.cursor(buffered=True)
        cursor.execute('UPDATE register SET password=%s WHERE Email=%s', [hashed_password, email])
        mydb.commit()
        cursor.close()

        flash('Password reset successful. You can now log in with your new password.')
        return redirect(url_for('login'))

    return render_template('reset_password.html', token=token)


@app.route('/payment/<eid>/<game>', methods=['GET', 'POST'])
def payment(eid,game):
    cursor = mydb.cursor(buffered=True)
    cursor.execute("SELECT ID, CONCAT(FirstName, ' ', LastName) AS FullName, Email, MobileNo, member FROM register WHERE id=%s", [eid])
    data1 = cursor.fetchall()
    cursor.execute('SELECT status from register WHERE id=%s', [eid])
    status=cursor.fetchone()[0]
    if status=='pending':
        cursor.execute("SELECT game, amount FROM game WHERE id=%s", [eid])
        cursor.close()
        game,amount = cursor.fetchone()
    else:
        cursor.execute('select amount from games where game_name=%s',[game])
        amount=cursor.fetchone()[0]
        cursor.close()
    ref=uuid.uuid4()
    return render_template('payment.html', data1=data1,game=game,amount=amount,eid=eid,ref=ref)


@app.route('/pay/<eid>/<game>/<ref>',methods=['POST'])
def pay(eid,game,ref):
    cursor = mydb.cursor(buffered=True)
    cursor.execute('SELECT status from register WHERE id=%s', [eid])
    status=cursor.fetchone()[0]
    if status=='pending':
        cursor.execute('SELECT amount FROM game WHERE id=%s', [eid])
        amount = cursor.fetchone()[0]
        cursor.close()
    else:
        cursor.execute('select amount from games where game_name=%s',[game])
        amount=cursor.fetchone()[0]
        #q=int(request.form['qty'])
    q = 1
    checkout_session=stripe.checkout.Session.create(
        success_url=url_for('success',eid=eid,game=game,amount=amount,ref=ref,_external=True),
        line_items=[
            {
                'price_data': {
                    'product_data': {
                        'name': game,
                    },
                    'unit_amount': amount*100,
                    'currency': 'inr',
                },
                'quantity':q
            },
            ],
        mode="payment",)
    return redirect(checkout_session.url)
@app.route('/success/<eid>/<ref>/<game>/<amount>')
def success(eid,ref,game,amount):
    cursor = mydb.cursor(buffered=True)
    cursor.execute('SELECT status from register WHERE id=%s', [eid])
    status=cursor.fetchone()[0]
    if status=='pending':
        cursor.execute('update register set status=%s WHERE ID=%s',['success',eid])
        cursor.execute('INSERT into payments (ordid,id,game,amount) VALUES (%s,%s,%s,%s)',[ref,eid,game,amount])
        mydb.commit()
        cursor.close()
        flash('Payment Successful ! Login in to continue.')
        return redirect(url_for('login'))
    else:
        cursor.execute('INSERT into payments (ordid,id,game,amount) VALUES (%s,%s,%s,%s)',[ref,eid,game,amount])
        cursor.execute('INSERT INTO game (id,game,amount) VALUES (%s,%s,%s)', [eid,game,amount])
        mydb.commit()
        cursor.close()
        flash('Payment Successful')
        return redirect(url_for('dashboard'))
    


'''@app.route('/dashboard')
def dashboard():
    if session.get('user'):
        cursor = mydb.cursor(buffered=True)
        cursor.execute("SELECT ID, CONCAT(FirstName, ' ', LastName) AS FullName, Email, MobileNo, member, status FROM register WHERE id=%s", [session.get('user')])
        user_data = cursor.fetchone()
        cursor.execute("SELECT game, amount FROM game where id=%s", [session.get('user')])
        game,amount = cursor.fetchone()
        cursor.close()
        

        if user_data[5] == 'success':
            # User has completed the payment successfully
            return render_template('dashboard.html', user_data=user_data,game=game,amount=amount)
        else:
            # User hasn't completed the payment, redirect to the payment page
            flash('Complete your payment to access the dashboard.', 'info')
            return redirect(url_for('payment'))
    else:
        flash('You must log in to access the dashboard.', 'error')
        return redirect(url_for('login'))'''
@app.route('/dashboard')
def dashboard():
    if session.get('user'):
        return render_template('my-account.html')
    else:
        return redirect(url_for('login'))
@app.route('/individual')
def individual():
    if session.get('user'):
        return render_template('game-cards-individual.html')
    else:
        return redirect(url_for('login'))
@app.route('/sport/<game>',methods=['GET','POST'])
def sport(game):
    if session.get('user'):
        cursor = mydb.cursor(buffered=True)
        cursor.execute('select count(*) from game where game=%s and id=%s',[game,session.get('user')])
        count = cursor.fetchone()[0]
        cursor.execute('select gender from register where id=%s',[session.get('user')])
        gender=cursor.fetchone()[0]
        cursor.execute('select email from register where id=%s',[session.get('user')])
        email_id=cursor.fetchone()[0]
        cursor.close()
        if count==0:
            return redirect(url_for('payment',eid=session.get('user'),game=game))
        else:
            cursor = mydb.cursor(buffered=True)
            cursor.execute('select count(*) from sub_games where game=%s and id=%s',[game,session.get('user')])
            count=cursor.fetchone()[0]
            cursor.close()
            if count==0:
                if game in ('ATHLETICS','ARCHERY','CHESS','CYCLOTHON','JUMPS','WALKATHON','SWIMMING','TENNKOIT','THROW','ROWING','ROLLER_SKATING','FENCING','SHOOTING'):
                    if request.method=='POST':
                        cursor = mydb.cursor(buffered=True)
                        for i in request.form:
                            cursor.execute('insert into sub_games (game,id,category) values(%s,%s,%s)',[game,session.get('user'),i])
                        mydb.commit()
                        cursor.close()
                        subject='Doctors Olympiad Games registration'
                        body=f'You are successfully registered to {" ".join(request.form.values())}\n\nThanks and regards\nDoctors Olympiad 2023'
                        sendmail(email_id,subject,body)
                        return redirect(url_for('dashboard'))
                    return render_template(f'/games-individual-team/individual/{game}.html',gender=gender)
                else:
                    if game in ('TABLETENNIS','LAWNTENNIS','BADMINTON','CARROMS'):

                        return render_template(f'/games-individual-team/individual/{game}.html',gender=gender)
                    pass




            elif count>=1:
                if game in ('ATHLETICS','ARCHERY','CHESS','CYCLOTHON','JUMPS','WALKATHON','SWIMMING','TENNKOIT','THROW','ROWING','ROLLER_SKATING','FENCING','SHOOTING'):
                    flash('You already registered for this game')
                    return redirect(url_for('individual'))
                else:
                    return game
    else:
        return redirect(url_for('login'))
@app.route('/allindividualgames')
def allindividualgames():
    if session.get('user'):
        cursor = mydb.cursor(buffered=True)
        cursor.execute('SELECT game_name from games where game_name not in (select game from game where id=%s)',[session.get('user')])
        add_games=cursor.fetchall()
        cursor.execute('SELECT game from game where id=%s',[session.get('user')])
        games=cursor.fetchall()
        cursor.close()
        '''cursor.execute('select count(*) from game where game=%s and id=%s',[game,session.get('user')])
        count = cursor.fetchone()[0]
        cursor.execute('select gender from register where id=%s',[session.get('user')])
        gender=cursor.fetchone()[0]
        cursor.execute('select email from register where id=%s',[session.get('user')])
        email_id=cursor.fetchone()[0]
        cursor.close()'''
        return render_template('userdashboard.html',games=games,add_games=add_games)
    else:
        return redirect(url_for('login'))
@app.route('/buyaddon/<game>')
def buyaddon(game):
    if session.get('user'):
        return redirect(url_for('payment',eid=session.get('user'),game=game))
    else:
        return redirect(url_for('login'))
@app.route('/registeredgame/<game>',methods=['GET','POST'])
def registeredgame(game):
    cursor = mydb.cursor(buffered=True)
    cursor.execute('select gender from register where id=%s',[session.get('user')])
    gender=cursor.fetchone()[0]
    cursor.execute('select email from register where id=%s',[session.get('user')])
    email_id=cursor.fetchone()[0]
    cursor.close()
    if game in ('ARCHERY','CHESS','CYCLOTHON','TENNKOIT','THROW','ROWING','ROLLER_SKATING','FENCING'):
        cursor = mydb.cursor(buffered=True)
        cursor.execute('select count(*) from sub_games where game=%s and id=%s',[game,session.get('user')])
        count = cursor.fetchone()[0]
        cursor.close()
        if count>=1:
            flash('Already registered!refer your games profile')
            return redirect(url_for('dashboard'))
        if request.method=='POST':
            cursor = mydb.cursor(buffered=True)
            for i in request.form:
                cursor.execute('insert into sub_games (game,id,category) values(%s,%s,%s)',[game,session.get('user'),i])
                mydb.commit()
            cursor.close()
            subject='Doctors Olympiad Games registration'
            body=f'You are successfully registered to {" ".join(request.form.values())}\n\nThanks and regards\nDoctors Olympiad 2023'
            sendmail(email_id,subject,body)
            return redirect(url_for('dashboard'))
        return render_template(f'/games-individual-team/individual/{game}.html',gender=gender)
    else:
        return game
    

if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)