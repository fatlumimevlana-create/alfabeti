from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Të dhënat fillestare për sallat dhe tavolinat
kafe_data = {
    "Salla Kryesore": {f"T-{i:02d}": {"statusi": "E lirë", "detaje": "", "totali": "0.00€"} for i in range(1, 22)},
    "Terrace1": {f"T-{i:02d}": {"statusi": "E lirë", "detaje": "", "totali": "0.00€"} for i in range(1, 11)}
}

# Navbar e përbashkët për të gjitha faqet
NAVBAR_HTML = """
<div style="background-color: #121f33; padding: 10px; display: flex; gap: 10px; justify-content: center; flex-wrap: wrap; margin-bottom: 20px; border-radius: 8px;">
    <a href="/" style="background: #1b2d4f; color: white; padding: 8px 14px; text-decoration: none; border-radius: 6px; font-weight: bold;">Salla Kryesore</a>
    <a href="/salla/Terrace1" style="background: #1b2d4f; color: white; padding: 8px 14px; text-decoration: none; border-radius: 6px; font-weight: bold;">Terrace1</a>
    <a href="/porosite" style="background: #1b2d4f; color: white; padding: 8px 14px; text-decoration: none; border-radius: 6px; font-weight: bold;">Porositë</a>
    <a href="/stafi" style="background: #1b2d4f; color: white; padding: 8px 14px; text-decoration: none; border-radius: 6px; font-weight: bold;">Stafi</a>
    <a href="/limi" style="background: #1b2d4f; color: white; padding: 8px 14px; text-decoration: none; border-radius: 6px; font-weight: bold;">Limi</a>
</div>
"""

@app.route('/')
def index():
    return redirect(url_for('salla_view', salla_name='Salla Kryesore'))

@app.route('/salla/<salla_name>')
def salla_view(salla_name):
    tavolinat = kafe_data.get(salla_name, {})
    
    html = f"""
    <!DOCTYPE html>
    <html lang="sq">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sistemi i Kafenesë</title>
        <style>
            body {{ font-family: -apple-system, sans-serif; background-color: #0b111e; color: white; margin: 0; padding: 15px; }}
            h2 {{ text-align: center; color: #fff; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; max-width: 1000px; margin: 0 auto; }}
            .card {{ background: #121f33; border: 2px solid #1b2d4f; border-radius: 10px; padding: 15px; text-align: center; text-decoration: none; color: white; display: block; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
            .card:hover {{ border-color: #007bff; }}
            .t-num {{ font-size: 20px; font-weight: bold; }}
            .t-price {{ font-size: 16px; color: #4cd137; margin-top: 5px; }}
            .t-detal {{ font-size: 12px; color: #dcdde1; margin-top: 5px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
        </style>
    </head>
    <body>
        {NAVBAR_HTML}
        <h2>{salla_name}</h2>
        <div class="grid">
    """
    
    for tav_id, info in tavolinat.items():
        numri = tav_id.split("-")[1]
        html += f"""
        <a href="/tavolina/{salla_name}/{numri}" class="card">
            <div class="t-num">Tavolina {numri}</div>
            <div class="t-price">{info['totali']}</div>
            <div class="t-detal">{info['detaje'] if info['detaje'] else 'E lirë'}</div>
        </a>
        """
        
    html += """
        </div>
    </body>
    </html>
    """
    return html

@app.route('/tavolina/<salla>/<tav_id>', methods=['GET', 'POST'])
def tavolina_detaje(salla, tav_id):
    tav_key = f"T-{tav_id.zfill(2)}"
    if tav_key not in kafe_data.get(salla, {}):
        tav_key = f"T-{tav_id}"
        
    if request.method == 'POST':
        detaje = request.form.get('detaje')
        totali = request.form.get('totali')
        kafe_data[salla][tav_key]['detaje'] = detaje
        kafe_data[salla][tav_key]['totali'] = totali + "€" if not totali.endswith("€") else totali
        kafe_data[salla][tav_key]['statusi'] = "Zënë"
        return redirect(url_for('salla_view', salla_name=salla))
        
    info = kafe_data.get(salla, {}).get(tav_key, {"detaje": "", "totali": "0.00€"})
    
    return f"""
    <!DOCTYPE html>
    <html lang="sq">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Tavolina {tav_id}</title>
        <style>
            body {{ font-family: -apple-system, sans-serif; background-color: #0b111e; color: white; margin: 0; padding: 20px; }}
            .box {{ max-width: 400px; margin: 0 auto; background: #121f33; padding: 20px; border-radius: 10px; border: 2px solid #1b2d4f; }}
            input, textarea {{ width: 100%; padding: 10px; margin-top: 8px; margin-bottom: 15px; background: #0b111e; border: 1px solid #1b2d4f; color: white; border-radius: 5px; box-sizing: border-box; }}
            .btn {{ display: block; width: 100%; background: #007bff; color: white; border: none; padding: 12px; border-radius: 5px; font-size: 16px; cursor: pointer; text-align: center; text-decoration: none; margin-top: 10px; }}
            .btn-fatura {{ background: #28a745; }}
            .btn-back {{ background: #6c757d; }}
        </style>
    </head>
    <body>
        <div class="box">
            <h2>Tavolina: {tav_id}</h2>
            <p>Salla: {salla}</p>
            <form method="POST">
                <label>Porosia / Artikujt:</label>
                <textarea name="detaje" rows="3">{info['detaje']}</textarea>
                
                <label>Totali (€):</label>
                <input type="text" name="totali" value="{info['totali'].replace('€', '')}">
                
                <button type="submit" class="btn">Ruaj Porosinë</button>
            </form>
            <a href="/tavolina/{salla}/{tav_id}/fatura" class="btn btn-fatura">Printo Faturën</a>
            <a href="/salla/{salla}" class="btn btn-back">Kthehu te Paneli</a>
        </div>
    </body>
    </html>
    """

@app.route('/tavolina/<salla>/<tav_id>/fatura')
def fatura(salla, tav_id):
    tav_key = f"T-{tav_id.zfill(2)}"
    if tav_key not in kafe_data.get(salla, {}):
        tav_key = f"T-{tav_id}"
    data = kafe_data.get(salla, {}).get(tav_key, {"detaje": "", "totali": "0.00€"})
    
    return f"""
    <!DOCTYPE html>
    <html lang="sq">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Fatura - Tavolina {tav_id}</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f4f4; color: #333; padding: 20px; }}
            .receipt {{ background: white; max-width: 350px; margin: 0 auto; padding: 20px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h2, h3 {{ text-align: center; margin: 0 0 10px 0; }}
            .info {{ margin-bottom: 15px; font-size: 14px; }}
            .total {{ font-size: 18px; font-weight: bold; border-top: 2px dashed #333; padding-top: 10px; margin-top: 15px; text-align: right; }}
            .btn {{ display: block; width: 100%; background: #007bff; color: white; border: none; padding: 10px; border-radius: 5px; font-size: 16px; cursor: pointer; text-align: center; text-decoration: none; margin-top: 15px; }}
            .btn-print {{ background: #28a745; }}
        </style>
    </head>
    <body>
        <div class="receipt">
            <h2>Kafene XPOS</h2>
            <h3>Faturë Tavolina: {tav_id}</h3>
            <div class="info">
                <p><strong>Salla:</strong> {salla}</p>
                <p><strong>Artikujt / Porosia:</strong><br>{data['detaje']}</p>
            </div>
            <div class="total">
                Totali: {data['totali']}
            </div>
            <button class="btn btn-print" onclick="window.print()">Printo Faturën</button>
            <a href="/tavolina/{salla}/{tav_id}" class="btn">Kthehu te Tavolina</a>
        </div>
    </body>
    </html>
    """

@app.route('/porosite')
def porosite():
    return "<body style='background:#0b111e; color:white; font-family:sans-serif; padding:20px;'>" + NAVBAR_HTML + "<h2>Paneli i Porosive</h2><p>Këtu do të shfaqen të gjitha porositë aktive.</p></body>"

@app.route('/stafi')
def stafi():
    return "<body style='background:#0b111e; color:white; font-family:sans-serif; padding:20px;'>" + NAVBAR_HTML + "<h2>Menaxhimi i Stafit</h2><p>Këtu menaxhohen llogaritë e kamarierëve.</p></body>"

@app.route('/limi')
def limi():
    return "<body style='background:#0b111e; color:white; font-family:sans-serif; padding:20px;'>" + NAVBAR_HTML + "<h2>Limi / Bilanci</h2><p>Këtu shfaqet xhiroja ditore.</p></body>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
