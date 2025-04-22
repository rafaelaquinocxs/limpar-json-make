app = Flask(name)

@app.route('/') def home(): return 'API funcionando!'

@app.route('/limpar-json', methods=['POST']) def limpar_json(): try: raw = request.json.get("conteudo", "") # Remove escapes como \n, \", etc. raw_clean = raw.encode('utf-8').decode('unicode_escape') # Transforma a string limpa em dicionário data = json.loads(raw_clean) return jsonify(data) except Exception as e: return jsonify({"erro": str(e)}), 400

if name == 'main': app.run(debug=True)
