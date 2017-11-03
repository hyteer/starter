## Instructions


### Sample

新建一个服务时，拷贝sample工程目录，需要做如下初始修改：
* 重命名工程目录，如'message'
* blueprints目录下的各模块根据需要相应做修改
如：bp = Blueprint('message', __name__, url_prefix='/message')
* 通过gunicorn行运（详情参考下面gunicor部署说明）

### Sample-dist
此为可独立公开分发的工程结构，增加PiPy的setup配置，配置步骤如下：
新建一个服务时，拷贝sample工程目录，需要做如下初始修改：
* 重命名工程目录，如'message'
* 重命名工程目录内部程序主目录，如'ytmsg'
* 修改分别修改setup.py及MANIFEST.in文件中的对应配置信息
* 修改manager.py文件中register_blueprints函数中的find_modules函数参数为对应的主程序目录名
如：find_modules('ytmsg.blueprints')
* blueprints目录下的各模块根据需要相应做修改
如：bp = Blueprint('message', __name__, url_prefix='/message')

### install
* install app
pip install --editable .
pip install -r requirements.txt
set FLASK_APP=ytmsg
set FLASK_DEBUG=1
flask run --reload -p 5001

* local develop
export FLASK_APP=__init__.py
或 set FLASK_APP=__init__.py  在Windows下
flask run

### Deploy
* deploy with gunicorn
pip install gunicorn
gunicorn -b 0.0.0.0:8001 main:app

* deploy with docker
docker run -d --name yt-consul -p 8500:8500 registry.cn-hangzhou.aliyuncs.com/hyteer/ytegg:consul-001

docker run -d --name yt-admin -p 8002:8000 registry.cn-hangzhou.aliyuncs.com/hyteer/ytegg:admin-20171103

### Usage

* flask-sqlalchemy
query:
users = User.query.all()
user = User.query.filter_by(username='tony').first()
create:
u1 = User(email='u1@qq.com')
u1.username = 'user1'
u1.password = '111'
db.session.add(u1)
db.session.commit()
