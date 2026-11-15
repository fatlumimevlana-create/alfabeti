from flask import Flask, request, redirect, url_for

app = Flask(__name__)

kafe_data = {
    "Salla Kryesore": {f"Tavolina {i:02d}": {"statusi": "E lire", "detaje": "", "totali": 0.0, "kamarieri": ""} for i in range(1, 22)},
    "Terrace1": {f"T-0{i}": {"statusi": "E lire", "detaje": "", "totali": 0.0, "kamarieri": ""} for i in range(1, 6)}
}

stafi_lista = ["Dashnor", "Kamarier 1", "kamarier 2"]

NAVBAR = '''
<div style="background:#121f33; padding: 12px; display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; border-radius: 8px; margin-bottom: 20px;">
    <a href="/salla/Salla Kryesore" style="color: white; padding: 10px 14px; text-decoration: none; font-weight: bold; font-size: 14px; background: #1a2d4a; border-radius: 6px;">Salla Kryesore</a>
    <a href="/salla/Terrace1" style="color: white; padding: 10px 14px; text-decoration: none; font-weight: bold; font-size: 14px; background: #1a2d4a; border-radius: 6px;">Terrace1</a>
    <a href="/porosite" style="color: white; padding: 10px 14px; text-decoration: none; font-weight: bold; font-size: 14px; background: #1a2d4a; border-radius: 6px;">Porositë</a>
    <a href="/stafi" style="color: white; padding: 10px 14px; text-decoration: none; font-weight: bold; font-size: 14px; background: #1a2d4a; border-radius: 6px;">Stafi</a>
    <a href="/limi" style="color: white; padding: 10px 14px; text-decoration: none; font-weight: bold; font-size: 14px; background: #1a2d4a; border-radius: 6px;">Limi</a>
</div>
'''

def render_page(content):
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Kafic Loli</title>
    </head>
    <body style="background: #0b131e; color: white; font-family: Arial, sans-serif; margin: 0; padding: 15px;">
        {NAVBAR}
        <div style="margin-top: 10px;">
            {content}
        </div>
    </body>
    </html>
    '''

@app.route('/')
def index():
    return redirect(url_for('salla_view', salla_name='Salla Kryesore'))

@app.route('/salla/<salla_name>')
def salla_view(salla_name):
    tavolinat = kafe_data.get(salla_name, {})
    cards = f"<h2 style='color:white; margin-bottom: 15px;'>{salla_name}</h2><div style='display: flex; flex-wrap: wrap; gap: 15px;'>"
    for emri, data in tavolinat.items():
        bg = "#228B22" if data['statusi'] == 'E zene' else "#162235"
        kam_info = f"<div style='font-size: 0.8em; color: #ffd700; margin-top: 4px;'>👤 {data['kamarieri']}</div>" if data['kamarieri'] else ""
        cards += f'''
        <a href="/tavolina/{salla_name}/{emri}" style="background: {bg}; border: 1px solid #233446; padding: 15px; border-radius: 8px; width: 140px; text-decoration: none; color: white; display: inline-block;">
            <div style="font-weight: bold; font-size: 1.1em; margin-bottom: 6px;">{emri}</div>
            <div style="font-size: 0.85em; color: #ddd;">Statusi: {data['statusi']}</div>
            {kam_info}
            <div style="font-size: 0.85em; color: #ddd; margin-top: 4px;">Totali: {data['totali']}€</div>
        </a>
        '''
    cards += "</div>"
    return render_page(cards)

@app.route('/tavolina/<salla_name>/<tav_name>', methods=['GET', 'POST'])
def tavolina_detaje(salla_name, tav_name):
    if request.method == 'POST':
        statusi = request.form.get('statusi')
        detaje = request.form.get('detaje')
        kamarieri = request.form.get('kamarieri', '')
        tot_str = request.form.get('totali', '0')
        try:
            totali = float(tot_str) if tot_str else 0.0
        except ValueError:
            totali = 0.0
            
        kafe_data[salla_name][tav_name]['statusi'] = statusi
        kafe_data[salla_name][tav_name]['detaje'] = detaje
        kafe_data[salla_name][tav_name]['kamarieri'] = kamarieri
        kafe_data[salla_name][tav_name]['totali'] = totali
        return redirect(url_for('salla_view', salla_name=salla_name))
         
    tav = kafe_data[salla_name][tav_name]
    sel_lire = "selected" if tav['statusi'] == "E lire" else ""
    sel_zene = "selected" if tav['statusi'] == "E zene" else ""
    
    options_kamarier = ""
    for k in stafi_lista:
        sel = "selected" if tav.get('kamarieri') == k else ""
        options_kamarier += f'<option value="{k}" {sel}>{k}</option>'
    
    content = f'''
    <div>
        <h2>Tavolina: {tav_name} ({salla_name})</h2>
        <form method="POST" style="background:#162235; padding:20px; border-radius:8px; width:300px; margin-top: 15px;">
            <label>Statusi:</label><br>
            <select name="statusi" style="width:100%; padding:8px; margin-top:5px; margin-bottom:15px;">
                <option value="E lire" {sel_lire}>E lire</option>
                <option value="E zene" {sel_zene}>E zene</option>
            </select><br>
            
            <label>Kamarieri:</label><br>
            <select name="kamarieri" style="width:100%; padding:8px; margin-top:5px; margin-bottom:15px; background:white; color:black;">
                <option value="">-- Zgjidh Kamarierin --</option>
                {options_kamarier}
            </select><br>

            <label>Detaje / Porosia:</label><br>
            <input type="text" name="detaje" value="{tav['detaje']}" style="width:100%; padding:8px; margin-top:5px; margin-bottom:15px;"><br>
            
            <label>Totali (€):</label><br>
            <input type="number" step="0.1" name="totali" value="{tav['totali']}" style="width:100%; padding:8px; margin-top:5px; margin-bottom:20px;"><br>
            
            <button type="submit" style="background:green; color:white; padding:10px 20px; border:none; border-radius:4px; width:100%; font-weight:bold; cursor:pointer;">Ruaj</button>
        </form>
        <br><a href="/salla/{salla_name}" style="color:cyan; text-decoration:none;">&larr; Kthehu te Salla</a>
    </div>
    '''
    return render_page(content)

@app.route('/porosite')
def porosite_view():
    html = "<div><h2>Paneli i Porosive</h2><p style='color:#bbb;'>Të gjitha porositë aktive:</p><div style='margin-top:15px;'>"
    aktiv = False
    for salla_name, salla_data in kafe_data.items():
        for tav_name, tav_info in salla_data.items():
            t_tot = tav_info.get('totali', 0)
            try:
                t_tot_val = float(t_tot) if t_tot else 0.0
            except ValueError:
                t_tot_val = 0.0
                
            if tav_info['statusi'] == 'E zene' or t_tot_val > 0 or tav_info.get('detaje'):
                aktiv = True
                kam_name = tav_info.get('kamarieri', 'Pa caktuar')
                html += f"<div style='background:#162235; margin:10px 0; padding:15px; border-radius:8px; border: 1px solid #233446;'><b>Salla:</b> {salla_name} | <b>Tavolina:</b> {tav_name} | <b>Kamarieri:</b> <span style='color:#ffd700;'>👤 {kam_name}</span> | <b>Detaje:</b> {tav_info['detaje']} | <b>Totali:</b> {t_tot_val}€</div>"
    
    if not aktiv:
        html += "<p style='color:#aaa;'>Nuk ka asnjë porosi aktive për momentin.</p>"
    html += "</div></div>"
    return render_page(html)

@app.route('/stafi', methods=['GET', 'POST'])
def stafi_view():
    if request.method == 'POST':
        emri_ri = request.form.get('kamarier')
        if emri_ri and emri_ri not in stafi_lista:
            stafi_lista.append(emri_ri)
            
    html = "<div><h2>Menaxhimi i Stafit</h2><p style='color:#bbb;'>Kamarierët e regjistruar:</p><div style='margin-top:15px;'>"
    for k in stafi_lista:
        html += f"<div style='background:#162235; margin:8px 0; padding:12px; border-radius:8px; border: 1px solid #233446;'>👤 {k}</div>"
        
    html += '''
    <form method="POST" style="margin-top:20px;">
        <input type="text" name="kamarier" placeholder="Emri i kamarierit..." style="padding:10px; width:220px; border-radius:4px; border:1px solid #233446; background:#162235; color:white; margin-right:10px;">
        <button type="submit" style="padding:10px 20px; background:green; color:white; border:none; border-radius:4px; cursor:pointer; font-weight:bold;">Shto Kamarierin</button>
    </form>
    </div></div>
    '''
    return render_page(html)

@app.route('/limi')
def limi_view():
    total_xhiro = 0.0
    kamarieri_totals = {}
    
    for salla_name, salla_data in kafe_data.items():
        for t_name, t_info in salla_data.items():
            val = t_info.get('totali', 0.0)
            try:
                num_val = float(val) if val else 0.0
            except ValueError:
                num_val = 0.0
            
            total_xhiro += num_val
            kam = t_info.get('kamarieri') or 'Pa caktuar'
            kamarieri_totals[kam] = kamarieri_totals.get(kam, 0.0) + num_val
            
    breakdown_html = ""
    for kam, amt in kamarieri_totals.items():
        breakdown_html += f"<div style='margin-top:8px; color:#ddd;'>👤 <b>{kam}:</b> {amt:.2f} €</div>"

    html = f"""
    <div>
        <h2>Limi / Bilanci</h2>
        <p style='color:#bbb;'>Xhiroja ditore e kafenesë sipas kamarierëve.</p>
        <div style='background:#162235; padding:20px; border-radius:8px; margin-top:20px; width:320px; border: 1px solid #233446;'>
            <h3 style='color:lightgreen; margin:0 0 10px 0; font-size: 1.3em;'>Xhiro Totale: {total_xhiro:.2f} €</h3>
            <hr style='border:0; border-top:1px solid #233446; margin:10px 0;'>
            <h4 style='color:white; margin:0 0 8px 0;'>Sipas Kamarierëve:</h4>
            {breakdown_html}
        </div>
    </div>
    """
    return render_page(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  
