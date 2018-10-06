
$(function () {
    $("#send_sms_code_btn").click(function (ev) {
        telephone = $('input[name=telephone]').val();
        csrf = $('meta[name=csrf_token]').attr("value");
        // s = 'zhanghendenvpengyou';
        // v = telephone+s;
        // sign = md5(v);
        ev.preventDefault();
        $.ajax({
            url:'/send_sms_code/',
            type:'post',
            data:{
                'telephone':telephone,
                'csrf_token':csrf,

            },
            success:function (data) {
                if (data.code == 200) {
                    xtalert.alertSuccessToast("发送短信验证码成功");
                    // window.location.href = '/'  // 跳转到首页
                } else {  // 提示出错误
                    xtalert.alertErrorToast(data.msg);
                }
            }
        })
    })
    // 处理图片验证码
    $(".captcha").click(function (ev) {
        ev.preventDefault();
        r = Math.random(); // [0,1)的随机数
        self = $(this); // 把js的self变成jq的self
        url = self.attr('data-src') + '?a=' + r ; //    /img_code/?a=随机数
        self.attr("src",url);
    })

    // 提交注册请求
     $("#signup_btn").click(function (ev) {
        telephone = $('input[name=telephone]').val();
        csrf = $('meta[name=csrf_token]').attr("value");
        smscode = $('input[name=smscode]').val();
        username = $('input[name=username]').val();
        password = $('input[name=password]').val();
        password1 = $('input[name=password1]').val();
        captchacode = $('input[name=captchacode]').val();

        ev.preventDefault();
        $.ajax({
            url:'/signup/',
            type:'post',
            data:{
                'telephone':telephone,
                'csrf_token':csrf,
                'sign':"123",
                'smscode':smscode,
                'username':username,
                'password':password,
                'password1':password1,
                'captchacode':captchacode
            },
            success:function (data) {
                if (data.code == 200) {
                    xtalert.alertSuccessToast("注册成功");
                     window.location.href = $('meta[name=from]').attr('value')
                } else {  // 提示出错误
                    xtalert.alertErrorToast(data.msg);
                }
            }
        })
    })

})




