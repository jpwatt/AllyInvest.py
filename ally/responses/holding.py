class Holding():
    def __init__(self):
        pass

    def from_xml(self, xml):
        pass

    def from_json(self, json):
        # Feeling thankful for Notepad++ macros...
        if 'accounttype' in json:
        	self.accounttype = json['accounttype']
        if 'assetclass' in json:
        	self.assetclass = json['assetclass']
        if 'cfi' in json:
        	self.cfi = json['cfi']
        if 'change' in json:
        	self.change = json['change']
        if 'costbasis' in json:
        	self.costbasis = json['costbasis']
        if 'cusip' in json:
        	self.cusip = json['cusip']
        if 'desc' in json:
        	self.desc = json['desc']
        if 'factor' in json:
        	self.factor = json['factor']
        if 'gainloss' in json:
        	self.gainloss = json['gainloss']
        if 'lastprice' in json:
        	self.lastprice = json['lastprice']
        if 'marketvalue' in json:
        	self.marketvalue = json['marketvalue']
        if 'marketvaluechange' in json:
        	self.marketvaluechange = json['marketvaluechange']
        if 'matdt' in json:
        	self.matdt = json['matdt']
        if 'mmy' in json:
        	self.mmy = json['mmy']
        if 'mult' in json:
        	self.mult = json['mult']
        if 'price' in json:
        	self.price = json['price']
        if 'purchaseprice' in json:
        	self.purchaseprice = json['purchaseprice']
        if 'putcall' in json:
        	self.putcall = json['putcall']
        if 'qty' in json:
        	self.qty = json['qty']
        if 'sectyp' in json:
        	self.sectyp = json['sectyp']
        if 'strkpx' in json:
        	self.strkpx = json['strkpx']
        if 'sym' in json:
        	self.sym = json['sym']
        if 'symbol' in json:
        	self.symbol = json['symbol']
        if 'totalsecurities' in json:
        	self.totalsecurities = json['totalsecurities']
