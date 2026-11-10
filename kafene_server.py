from flask import Flask, request, redirect, url_for

app = Flask(__name__)

kafe_data = {
    "Salla Kryesore": {f"Tavolina {i:02d}": {"statusi": "E lirë", "detaje": "", "totali": 0.0} for i in range(1, 22)},
    "Terrace1": {f"T-0{i}": {"statusi": "E lirë", "detaje": "", "totali": 0.0} for i in range(1, 6)}
}

stafi_lista = ["Bekim", "Kamarier 1"]
mbyllja_ditor = 0.0

NAVBAR = '''
<div style="background: #121f33; padding: 12px; display: flex; justify-content: center; gap: 10px; border-radius: 8px; margin-bottom: 20px;">
    <a href="/salla/Salla Kryesore" style="color: white; padding: 8px 16px; text-decoration: none; font-weight: bold;">Salla Kryesore</a>
    <a href="/salla/Terrace1" style="color: white; padding: 8px 16px; text-decoration: none; font-weight: bold;">Terrace1</a>
    <a href="/stafi" style="color: white; padding: 8px 16px; text-decoration: none; font-weight: bold;">Stafi</a>
    <a href="/limi" style="color: white; padding: 8px 16px; text-decoration: none; font-weight: bold;">Limi</a>
</div>
'''

@app.route('/')
def index():
    return redirect(url_for('salla_view', salla_name='Salla Kryesore'))

@app.route('/salla/<salla_name>')
def salla_view(salla_name):
    tavolinat = kafe_data.get(salla_name, {})
    cards = ""
    for emri, data in tavolinat.items():
        cards += f'''
            <a href="/tavolina/{salla_name}/{emri}" style="background: #162235; border: 1px solid #22344f; border-radius: 10px; padding: 15px; text-align: center; text-decoration: none; color: white; display: block;">
                <div style="font-weight: bold; font-size: 1.1em; margin-bottom: 8px;">{emri}</div>
                <div style="color: #4ade80; font-size: 1.1em; font-weight: bold;">{data['totali']:.2f}€</div>
                <div style="font-size: 0.85em; color: #94a3b8; margin-top: 5px;">{data['statusi']}</div>
            </a>
        '''
    
    return f'''
    <!DOCTYPE html>
    <html lang="sq">
    <head><meta charset="UTF-8"><title>{salla_name}</title></head>
    <body style="font-family: Arial; background: #0d1520; color: white; padding: 20px;">
        {NAVBAR}
        <h2>{salla_name}</h2>
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 15px;">
            {cards}
        </div>
    </body>
    </html>
    '''

@app.route('/tavolina/<salla_name>/<tavolina_id>', methods=['GET', 'POST'])
def tavolina_detaje(salla_name, tavolina_id):
    tavolina = kafe_data.get(salla_name, {}).get(tavolina_id, {"statusi": "E lirë", "detaje": "", "totali": 0.0})
    
    if request.method == 'POST':
        cmimi = float(request.form.get('cmimi', 0))
        artikulli = request.form.get('artikulli', 'Pije')
        tavolina['totali'] += cmimi
        tavolina['statusi'] = "E zënë"
        tavolina['detaje'] += f"<br>- {artikulli}: {cmimi:.2f}€"
        
        global mbyllja_ditor
        mbyllja_ditor += cmimi
        return redirect(url_for('tavolina_detaje', salla_name=salla_name, tavolina_id=tavolina_id))

    return f'''
    <!DOCTYPE html>
    <html lang="sq">
    <head><meta charset="UTF-8"><title>{tavolina_id}</title></head>
    <body style="font-family: Arial; background: #0d1520; color: white; padding: 20px;">
        {NAVBAR}
        <div style="background: #162235; padding: 25px; border-radius: 10px; max-width: 500px; margin: 0 auto;">
            <a href="/salla/{salla_name}" style="color: #3b82f6; text-decoration: none; font-weight: bold;">← Kthehu</a>
            <h2>{tavolina_id}</h2>
            <p>Totali: <strong style="color: #4ade80;">{tavolina['totali']:.2f}€</strong></p>
            <p>Porositë: {tavolina['detaje'] if tavolina['detaje'] else 'Asnjë porosi.'}</p>
            <hr style="border-color: #22344f;">
            <form method="POST">
                <input type="text" name="artikulli" placeholder="Emri i pijes..." required style="width:100%; padding:10px; margin-top:10px;">
                <input type="number" step="0.01" name="cmimi" placeholder="Çmimi (€)..." required style="width:100%; padding:10px; margin-top:10px;">
                <button type="submit" style="width:100%; padding:10px; margin-top:10px; background:#22c55e; color:white; border:none; font-weight:bold; cursor:pointer;">Shto</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/stafi', methods=['GET', 'POST'])
def stafi_view():
    if request.method == 'POST':
        emri = request.form.get('emri')
        if emri and emri not in stafi_lista:
            stafi_lista.append(emri)
        return redirect(url_for('stafi_view'))
    
    list_html = "".join([f"<li style='padding:8px; border-bottom:1px solid #22344f;'>👤 {s}</li>" for s in stafi_lista])
    return f'''
    <!DOCTYPE html>
    <html lang="sq">
    <head><meta charset="UTF-8"><title>Stafi</title></head>
    <body style="font-family: Arial; background: #0d1520; color: white; padding: 20px;">
        {NAVBAR}
        <div style="background: #162235; padding: 25px; border-radius: 10px; max-width: 500px; margin: 0 auto;">
            <h2>Stafi</h2>
            <ul style="list-style:none; padding:0;">{list_html}</ul>
            <form method="POST">
                <input type="text" name="emri" placeholder="Emri..." required style="width:100%; padding:10px; margin-top:10px;">
                <button type="submit" style="width:100%; padding:10px; margin-top:10px; background:#22c55e; color:white; border:none; font-weight:bold; cursor:pointer;">Shto</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/limi')
def limi_view():
    return f'''
    <!DOCTYPE html>
    <html lang="sq">
    <head><meta charset="UTF-8"><title>Limi</title></head>
    <body style="font-family: Arial; background: #0d1520; color: white; padding: 20px;">
        {NAVBAR}
        <div style="background: #162235; padding: 25px; border-radius: 10px; max-width: 500px; margin: 0 auto; text-align: center;">
            <h2>Xhiroja Sot</h2>
            <div style="color: #4ade80; font-size: 1.8em; font-weight: bold; margin: 15px 0;">{mbyllja_ditor:.2f}€</div>
            <form action="/mbyll" method="POST">
                <button type="submit" style="width:100%; padding:12px; background:#ef4444; color:white; border:none; font-weight:bold; cursor:pointer;">Mbyll Ditën / Reseto</button>
            </form>
        </div>
    </body>
    </html>
    '''

@app.route('/mbyll', methods=['POST'])
def mbyll():
    global mbyllja_ditor
    mbyllja_ditor = 0.0
    for salla in kafe_data.values():
        for t in salla.values():
            t['totali'] = 0.0
            t['statusi'] = "E lirë"
            t['detaje'] = ""
    return redirect(url_for('limi_view'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
