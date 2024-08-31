from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:201830011@localhost/test_01'

db = SQLAlchemy(app)

class MonthlyTradeSummary(db.Model):
    # __tablename__ = 'monthly_trade_summary'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trade_month = db.Column(db.String)
    buy_value = db.Column(db.Float, default=0.0)
    sell_value = db.Column(db.Float, default=0.0)
    net_value = db.Column(db.Float, default=0.0)
    total_value = db.Column(db.Float, default=0.0)
    buy_orders = db.Column(db.BigInteger, default=0)
    sell_orders = db.Column(db.BigInteger, default=0)
    total_orders = db.Column(db.BigInteger, default=0)
    buy_trades = db.Column(db.BigInteger, default=0)
    sell_trades = db.Column(db.BigInteger, default=0)
    total_trades = db.Column(db.BigInteger, default=0)
    last_update_date = db.Column(db.String)
    dse_buy_value = db.Column(db.Float, default=0.0)
    dse_sell_value = db.Column(db.Float, default=0.0)
    dse_net_value = db.Column(db.Float, default=0.0)
    dse_total_value = db.Column(db.Float, default=0.0)
    dse_buy_orders = db.Column(db.BigInteger, default=0)
    dse_sell_orders = db.Column(db.BigInteger, default=0)
    dse_total_orders = db.Column(db.BigInteger, default=0)
    dse_buy_trades = db.Column(db.BigInteger, default=0)
    dse_sell_trades = db.Column(db.BigInteger, default=0)
    dse_total_trades = db.Column(db.BigInteger, default=0)
    cse_buy_value = db.Column(db.Float, default=0.0)
    cse_sell_value = db.Column(db.Float, default=0.0)
    cse_net_value = db.Column(db.Float, default=0.0)
    cse_total_value = db.Column(db.Float, default=0.0)
    cse_buy_orders = db.Column(db.BigInteger, default=0)
    cse_sell_orders = db.Column(db.BigInteger, default=0)
    cse_total_orders = db.Column(db.BigInteger, default=0)
    cse_buy_trades = db.Column(db.BigInteger, default=0)
    cse_sell_trades = db.Column(db.BigInteger, default=0)
    cse_total_trades = db.Column(db.BigInteger, default=0)
    is_sended = db.Column(db.Boolean, default=False)


    # def __init__(self, trade_month=None, buy_value=0.0, sell_value=0.0, net_value=0.0, 
    #              total_value=0.0, buy_orders=0, sell_orders=0, total_orders=0, 
    #              buy_trades=0, sell_trades=0, total_trades=0, last_update_date=None, 
    #              dse_buy_value=0.0, dse_sell_value=0.0, dse_net_value=0.0, 
    #              dse_total_value=0.0, dse_buy_orders=0, dse_sell_orders=0, 
    #              dse_total_orders=0, dse_buy_trades=0, dse_sell_trades=0, 
    #              dse_total_trades=0, cse_buy_value=0.0, cse_sell_value=0.0, 
    #              cse_net_value=0.0, cse_total_value=0.0, cse_buy_orders=0, 
    #              cse_sell_orders=0, cse_total_orders=0, cse_buy_trades=0, 
    #              cse_sell_trades=0, cse_total_trades=0, is_sended=False):
    #     self.trade_month = trade_month
    #     self.buy_value = buy_value
    #     self.sell_value = sell_value
    #     self.net_value = net_value
    #     self.total_value = total_value
    #     self.buy_orders = buy_orders
    #     self.sell_orders = sell_orders
    #     self.total_orders = total_orders
    #     self.buy_trades = buy_trades
    #     self.sell_trades = sell_trades
    #     self.total_trades = total_trades
    #     self.last_update_date = last_update_date
    #     self.dse_buy_value = dse_buy_value
    #     self.dse_sell_value = dse_sell_value
    #     self.dse_net_value = dse_net_value
    #     self.dse_total_value = dse_total_value
    #     self.dse_buy_orders = dse_buy_orders
    #     self.dse_sell_orders = dse_sell_orders
    #     self.dse_total_orders = dse_total_orders
    #     self.dse_buy_trades = dse_buy_trades
    #     self.dse_sell_trades = dse_sell_trades
    #     self.dse_total_trades = dse_total_trades
    #     self.cse_buy_value = cse_buy_value
    #     self.cse_sell_value = cse_sell_value
    #     self.cse_net_value = cse_net_value
    #     self.cse_total_value = cse_total_value
    #     self.cse_buy_orders = cse_buy_orders
    #     self.cse_sell_orders = cse_sell_orders
    #     self.cse_total_orders = cse_total_orders
    #     self.cse_buy_trades = cse_buy_trades
    #     self.cse_sell_trades = cse_sell_trades
    #     self.cse_total_trades = cse_total_trades
    #     self.is_sended = is_sended

    # def __repr__(self):
    #     return f'<MonthlyTradeSummary {self.id}>'


class RmsBrokerTrade(db.Model):
    # __tablename__ = 'rms_broker_trade'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trade_date = db.Column(db.String)
    buy_value = db.Column(db.Float, default=0.0)
    sell_value = db.Column(db.Float, default=0.0)
    net_value = db.Column(db.Float, default=0.0)
    total_value = db.Column(db.Float, default=0.0)
    buy_orders = db.Column(db.BigInteger, default=0)
    sell_orders = db.Column(db.BigInteger, default=0)
    total_orders = db.Column(db.BigInteger, default=0)
    buy_trades = db.Column(db.BigInteger, default=0)
    sell_trades = db.Column(db.BigInteger, default=0)
    total_trades = db.Column(db.BigInteger, default=0)
    last_update = db.Column(db.String)
    dse_buy_value = db.Column(db.Float, default=0.0)
    dse_sell_value = db.Column(db.Float, default=0.0)
    dse_net_value = db.Column(db.Float, default=0.0)
    dse_total_value = db.Column(db.Float, default=0.0)
    dse_buy_orders = db.Column(db.BigInteger, default=0)
    dse_sell_orders = db.Column(db.BigInteger, default=0)
    dse_total_orders = db.Column(db.BigInteger, default=0)
    dse_buy_trades = db.Column(db.BigInteger, default=0)
    dse_sell_trades = db.Column(db.BigInteger, default=0)
    dse_total_trades = db.Column(db.BigInteger, default=0)
    cse_buy_value = db.Column(db.Float, default=0.0)
    cse_sell_value = db.Column(db.Float, default=0.0)
    cse_net_value = db.Column(db.Float, default=0.0)
    cse_total_value = db.Column(db.Float, default=0.0)
    cse_buy_orders = db.Column(db.BigInteger, default=0)
    cse_sell_orders = db.Column(db.BigInteger, default=0)
    cse_total_orders = db.Column(db.BigInteger, default=0)
    cse_buy_trades = db.Column(db.BigInteger, default=0)
    cse_sell_trades = db.Column(db.BigInteger, default=0)
    cse_total_trades = db.Column(db.BigInteger, default=0)
    is_sended = db.Column(db.Boolean, default=False)


    # def __init__(self, trade_date=None, buy_value=0.0, sell_value=0.0, net_value=0.0, 
    #              total_value=0.0, buy_orders=0, sell_orders=0, total_orders=0, 
    #              buy_trades=0, sell_trades=0, total_trades=0, last_update=None, 
    #              dse_buy_value=0.0, dse_sell_value=0.0, dse_net_value=0.0, 
    #              dse_total_value=0.0, dse_buy_orders=0, dse_sell_orders=0, 
    #              dse_total_orders=0, dse_buy_trades=0, dse_sell_trades=0, 
    #              dse_total_trades=0, cse_buy_value=0.0, cse_sell_value=0.0, 
    #              cse_net_value=0.0, cse_total_value=0.0, cse_buy_orders=0, 
    #              cse_sell_orders=0, cse_total_orders=0, cse_buy_trades=0, 
    #              cse_sell_trades=0, cse_total_trades=0, is_sended=False):
    #     self.trade_date = trade_date
    #     self.buy_value = buy_value
    #     self.sell_value = sell_value
    #     self.net_value = net_value
    #     self.total_value = total_value
    #     self.buy_orders = buy_orders
    #     self.sell_orders = sell_orders
    #     self.total_orders = total_orders
    #     self.buy_trades = buy_trades
    #     self.sell_trades = sell_trades
    #     self.total_trades = total_trades
    #     self.last_update = last_update
    #     self.dse_buy_value = dse_buy_value
    #     self.dse_sell_value = dse_sell_value
    #     self.dse_net_value = dse_net_value
    #     self.dse_total_value = dse_total_value
    #     self.dse_buy_orders = dse_buy_orders
    #     self.dse_sell_orders = dse_sell_orders
    #     self.dse_total_orders = dse_total_orders
    #     self.dse_buy_trades = dse_buy_trades
    #     self.dse_sell_trades = dse_sell_trades
    #     self.dse_total_trades = dse_total_trades
    #     self.cse_buy_value = cse_buy_value
    #     self.cse_sell_value = cse_sell_value
    #     self.cse_net_value = cse_net_value
    #     self.cse_total_value = cse_total_value
    #     self.cse_buy_orders = cse_buy_orders
    #     self.cse_sell_orders = cse_sell_orders
    #     self.cse_total_orders = cse_total_orders
    #     self.cse_buy_trades = cse_buy_trades
    #     self.cse_sell_trades = cse_sell_trades
    #     self.cse_total_trades = cse_total_trades
    #     self.is_sended = is_sended

    # def __repr__(self):
    #     return f'<RmsBrkerTrade {self.id}>'



class CircuitLimits(db.Model):
    # __tablename__ = 'circuit_limits'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    circuit_up_below_200 = db.Column(db.Float, default=1.10)
    circuit_down_below_200 = db.Column(db.Float, default=0.90)
    circuit_up_between_200_500 = db.Column(db.Float, default=1.0875)
    circuit_down_between_200_500 = db.Column(db.Float, default=0.9125)
    circuit_up_between_500_1000 = db.Column(db.Float, default=1.075)
    circuit_down_between_500_1000 = db.Column(db.Float, default=0.925)
    circuit_up_between_1000_2000 = db.Column(db.Float, default=1.0625)
    circuit_down_between_1000_2000 = db.Column(db.Float, default=0.9375)
    circuit_up_between_2000_5000 = db.Column(db.Float, default=1.05)
    circuit_down_between_2000_5000 = db.Column(db.Float, default=0.95)
    circuit_up_above_5000 = db.Column(db.Float, default=1.0375)
    circuit_down_above_5000 = db.Column(db.Float, default=0.9625)

    # def __init__(self, 
    #              circuit_up_below_200=1.10, circuit_down_below_200=0.90, 
    #              circuit_up_between_200_500=1.0875, circuit_down_between_200_500=0.9125,
    #              circuit_up_between_500_1000=1.075, circuit_down_between_500_1000=0.925,
    #              circuit_up_between_1000_2000=1.0625, circuit_down_between_1000_2000=0.9375,
    #              circuit_up_between_2000_5000=1.05, circuit_down_between_2000_5000=0.95,
    #              circuit_up_above_5000=1.0375, circuit_down_above_5000=0.9625):
    #     self.circuit_up_below_200 = circuit_up_below_200
    #     self.circuit_down_below_200 = circuit_down_below_200
    #     self.circuit_up_between_200_500 = circuit_up_between_200_500
    #     self.circuit_down_between_200_500 = circuit_down_between_200_500
    #     self.circuit_up_between_500_1000 = circuit_up_between_500_1000
    #     self.circuit_down_between_500_1000 = circuit_down_between_500_1000
    #     self.circuit_up_between_1000_2000 = circuit_up_between_1000_2000
    #     self.circuit_down_between_1000_2000 = circuit_down_between_1000_2000
    #     self.circuit_up_between_2000_5000 = circuit_up_between_2000_5000
    #     self.circuit_down_between_2000_5000 = circuit_down_between_2000_5000
    #     self.circuit_up_above_5000 = circuit_up_above_5000
    #     self.circuit_down_above_5000 = circuit_down_above_5000

    # def __repr__(self):
    #     return f'<CircuitLimits {self.id}>'



with app.app_context():
    db.create_all()



@app.route('/api/rms_trade_list', methods=['GET'])
def get_rms_trade_list():
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 5, type=int)
    
    # Search filter
    search = request.args.get('search', '', type=str)

    # Query the database
    query = RmsBrokerTrade.query.order_by(RmsBrokerTrade.trade_date.desc())
    if search:
        query = RmsBrokerTrade.query.filter(RmsBrokerTrade.trade_date.like(f'%{search}%'))
    
    paginated_data = query.paginate(page=page, per_page=per_page, error_out=False)
    
    # Serialize the data
    data = {
        'items': [{
            'id': item.id,
            'trade_date': item.trade_date,
            'total_value': item.total_value,
            'total_trades': item.total_trades,

        } for item in paginated_data.items],
        'total': paginated_data.total,
        'pages': paginated_data.pages,
        'per_page': paginated_data.per_page,
        'current_page': paginated_data.page
    }
    
    return jsonify(data)


@app.route('/api/trade_summary', methods=['GET'])
def get_trade_summary():
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    
    # Search filter
    search = request.args.get('search', '', type=str)

    # Query the database
    query = MonthlyTradeSummary.query
    if search:
        query = query.filter(MonthlyTradeSummary.trade_month.like(f'%{search}%')).order_by(MonthlyTradeSummary.trade_month.desc())
    
    paginated_data = query.paginate(page=page, per_page=per_page, error_out=False)
    
    # Serialize the data
    data = {
        'items': [{
            'id': item.id,
            'trade_month': item.trade_month,
            'total_value': item.total_value,
            'total_trades': item.total_trades,

        } for item in paginated_data.items],
        'total': paginated_data.total,
        'pages': paginated_data.pages,
        'per_page': paginated_data.per_page,
        'current_page': paginated_data.page
    }
    
    return jsonify(data)




@app.route('/')
def monthly_trade_index_view():
    return render_template('trade_summary.html')

@app.route('/rms')
def rms_broker_index_view():
    return render_template('rms_broker_list.html')

@app.route('/update')
def circuit_limit_view():
    return render_template('update_cl.html')


@app.route('/api/update_circuit_limit/', methods=['GET','POST'])
def update_circuit_limit():
    circuit_limit = CircuitLimits.query.first()
    
    
    if not circuit_limit:
        return jsonify({"error": "Circuit limit not found"}), 404
    
    if request.method == 'GET':
        data = {
            'circuit_up_below_200': circuit_limit.circuit_up_below_200,
            'circuit_down_below_200': circuit_limit.circuit_down_below_200,
            'circuit_up_between_200_500': circuit_limit.circuit_up_between_200_500,
            'circuit_down_between_200_500': circuit_limit.circuit_down_between_200_500,
            'circuit_up_between_500_1000': circuit_limit.circuit_up_between_500_1000,
            'circuit_down_between_500_1000': circuit_limit.circuit_down_between_500_1000,
            'circuit_up_between_1000_2000': circuit_limit.circuit_up_between_1000_2000,
            'circuit_down_between_1000_2000': circuit_limit.circuit_down_between_1000_2000,
            'circuit_up_between_2000_5000': circuit_limit.circuit_up_between_2000_5000,
            'circuit_down_between_2000_5000': circuit_limit.circuit_down_between_2000_5000,
            'circuit_up_above_5000': circuit_limit.circuit_up_above_5000,
            'circuit_down_above_5000': circuit_limit.circuit_down_above_5000,
        }

        return jsonify(data), 200

    if request.method == 'POST':
        data = request.get_json()

        if 'circuit_up_below_200' in data:
            circuit_limit.circuit_up_below_200 = data['circuit_up_below_200']
        if 'circuit_down_below_200' in data:
            circuit_limit.circuit_down_below_200 = data['circuit_down_below_200']
        if 'circuit_up_between_200_500' in data:
            circuit_limit.circuit_up_between_200_500 = data['circuit_up_between_200_500']
        if 'circuit_down_between_200_500' in data:
            circuit_limit.circuit_down_between_200_500 = data['circuit_down_between_200_500']
        if 'circuit_up_between_500_1000' in data:
            circuit_limit.circuit_up_between_500_1000 = data['circuit_up_between_500_1000']
        if 'circuit_down_between_500_1000' in data:
            circuit_limit.circuit_down_between_500_1000 = data['circuit_down_between_500_1000']
        if 'circuit_up_between_1000_2000' in data:
            circuit_limit.circuit_up_between_1000_2000 = data['circuit_up_between_1000_2000']
        if 'circuit_down_between_1000_2000' in data:
            circuit_limit.circuit_down_between_1000_2000 = data['circuit_down_between_1000_2000']
        if 'circuit_up_between_2000_5000' in data:
            circuit_limit.circuit_up_between_2000_5000 = data['circuit_up_between_2000_5000']
        if 'circuit_down_between_2000_5000' in data:
            circuit_limit.circuit_down_between_2000_5000 = data['circuit_down_between_2000_5000']
        if 'circuit_up_above_5000' in data:
            circuit_limit.circuit_up_above_5000 = data['circuit_up_above_5000']
        if 'circuit_down_above_5000' in data:
            circuit_limit.circuit_down_above_5000 = data['circuit_down_above_5000']

        db.session.commit()

        return jsonify({"message": "Circuit limit updated successfully!"}), 200


if __name__ == '__main__':
    app.run(debug=True)
