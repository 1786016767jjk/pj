from flask import Blueprint,render_template,request,jsonify,session
from flask.views import MethodView
import pymysql

bp = Blueprint('user_bp',__name__)


class SignIn(MethodView) :
    def get(self):
        return render_template("signin.html")

    def post(self):
        username = request.values.get("username")
        password = request.values.get("password")
        con = pymysql.Connect(host="127.0.0.1", user="root", password="123456", database="pjarticle", port=3306,
                              charset="utf8", use_unicode=True)
        cur = con.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'select * from `pjuser` WHERE  `username` = %(username)s'
        cur.execute(sql,{'username':username})
        r = cur.fetchone()
        cur.close()
        con.close()
        if not r : # 用户名输入错误
            return jsonify({'code':405,'msg':'用户名错误','data':None})
        if r['password'] == password :  #正确
            r['password'] = None
            session['user_id'] = r['id']  # 登录成功保存用户的id
            return jsonify({'code': 200, 'msg': '登录成功', 'data': r})
        else:  # 密码错误
            return jsonify({'code': 405, 'msg': '密码错误', 'data': None})


class SignUp(MethodView):
    def get(self):
        return render_template('signup.html')

    def post(self):
        username = request.values.get("username")
        password = request.values.get("password")
        con = pymysql.Connect(host="127.0.0.1",user="root",password="123456",database="pjarticle",port=3306,charset="utf8",use_unicode=True)
        cur = con.cursor()
        sql = "insert into  `pjuser` (`username`,`password`) value (%(username)s,%(password)s)"
        try:
            r = cur.execute(sql, {'username': username, 'password': password})
            con.commit()
        except:
            return jsonify({'code':405,'msg':'用户名不能重复','data':None})
        finally:
            cur.close()
            con.close()
        return jsonify({'code':200,'msg':'注册成功','data':None})

bp.add_url_rule("/signup/",view_func=SignUp.as_view("signup"))
bp.add_url_rule("/signin/",view_func=SignIn.as_view("signin"))
