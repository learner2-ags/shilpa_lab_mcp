from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app=FastAPI(title='Thermal Console')
SAMPLE={'Sensor':'CPU1','ReadingCelsius':72.0}
def health_status(celsius:float)->str:
    if celsius>=85: return 'Critical'
    if celsius>=75: return 'Warning'
    return 'OK'
@app.get('/health')
def health(): return {'status':'ok'}
@app.get('/api/thermal')
def thermal(): return {**SAMPLE,'Health':health_status(SAMPLE['ReadingCelsius'])}
@app.get('/',response_class=HTMLResponse)
def home():
    return HTMLResponse('''<!doctype html><html><head><meta charset='utf-8'><title>Thermal Console</title><style>body{font-family:Arial;margin:40px}.badge{padding:6px 10px;border-radius:14px;background:#ddd}.badge.ok{background:#2e7d32;color:#fff}.badge.warning{background:#f9a825}.badge.critical{background:#c62828;color:#fff}</style></head><body><h1>Thermal Console</h1><p>Sensor: <span id='sensor'></span></p><p>Reading: <span id='reading'></span> °C</p><span id='health' class='badge'>Unknown</span><script>fetch('/api/thermal').then(r=>r.json()).then(x=>{sensor.textContent=x.Sensor;reading.textContent=x.ReadingCelsius;health.textContent=x.Health;health.className='badge '+x.Health.toLowerCase();});</script></body></html>''')
