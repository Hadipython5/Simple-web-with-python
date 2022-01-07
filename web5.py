from flask import Flask
application = Flask(__name__)

@application.route('/')
def index():
    return '''<html>
    <head>
        <title>web gua</title>
    </head>
    <button>tab untuk makan nasi</button>
    <body>
        <p><strong>halo semuaya selamat datang di website gua</strong></p>
        <p><em>gua buat web site ini utuk menjebak kalian</em></p>
        <h1>Welcome</h1>
        <label for="username">nama:</label>
        <input type="text" id="username">
        <br>
        <lable for="pass">password:</lable>
        <input type="password" id="pass">
        <br>
        <form>
            <input type="radio" id="pria" name="klamin"><label for="pria">pria</label>
            <input type="radio" id="wanita" name="klamin"><label for="wanita">wanita</label>
            <h2>anda makan apa</h2>
            <input type="checkbox" id="makan"><table for="makan">ayam goreng</table>
            <input type="checkbox" id="h"><table for="h">nasi goreng</table>
            <p>kota asal kalian</p>
            <select>
                <option>indramayu</option>
                <option>jakarta</option>
                <option>bandung</option>
                <option>bogor</option>
                <option>cirebon</option>
                <option>majalengka</option>
                <option>sumedang</option>
                <option>subang</option>
                <option>dan lain lain</option>
            </select>
            <br>
            <h4>komentar</h4>
            <textarea></textarea>
            <button type="submit">kirim</button>
        </form>
        <p>klik <a href="http://youtube.com" target="_blank">disini</a> untuk masuk ke youtube</p>
        <p>website ini dibuat dengan python dan html sederhana</p>
        <b>mungkin kalin juga bisa membuatnya</b>
        <h3>about</h3>
        <ul type="circle">
            <li>devloper   by:samsul hadi</li>
            <li>disainer   by:samsul hadi</li>
            <li>programmer by:samsul hadi</li>
        </ul>
        <a href="http://github.com/"><img src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.mainmain.id%2Fuploads%2Fpost%2F2020%2F05%2F09%2Fagar_akun_tidak_mudah_diretas.jpg&imgrefurl=https%3A%2F%2Fwww.mainmain.id%2Fr%2F6887%2Fbiar-nggak-jadi-korban-hacker-lakukan-hal-ini-di-semua-akun-kalian&tbnid=i93oE9mdmIUj1M&vet=1&docid=O2lBdZnj93UViM&w=1200&h=800&itg=1&hl=id&source=sh%2Fx%2Fim"/>
        </a>
        <h3><font href="color:green">system builder</font></h3>
        <dl>
            <dt>hacking</dt>
            <dd>ddos dengan hammer</dd>
            <dt>developer</dt>
            <dd>AI builder</dd>
            <dd>npc builder</dd>
            <website disainer</dd>
            <dd>server semimpel</dd>
        </dl>
        <p>silakan klik <a href="index" target="_blank">disini</a> untuk halaman selanjutnya</p>
        <hr/>
        <br/>
        <i>saya bisa membuat chatbot dengan python</i>
        </br>
        <u>silakan kunjungi sesialedia saya,github,youtube,facebook</u>
        </br>
        <font style="color:green">terima kasih suda membaca web gua..</font>
        <h1>help</h1>
        <h2>help</h2>
        <h3>help</h3>
        <h4>help</h4>
        <h5>help</h5>
        <h6>help</h6>
        <blockquote>&copy;samsul company copyright 2021</blockquote>
    </body>
</html>'''
def index():
    return '''<p>helo</p>
    
    '''

if __name__ == '__main__':
    application.run(debug=True)