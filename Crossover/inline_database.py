def solution(queries):
    db = dict()
    time_db = dict()
    values = []
    get_fv = lambda k,v: f'{k}({v})'
    
    def scan_by_name(d,prefix=None):
        scans = list()
        for k,v in d.items():
            if prefix and not k.startswith(prefix):
                continue
            scans.append(
                get_fv(k,v)
            )
        scans.sort()
        return ', '.join(scans)
    
    def scan_at_by_name(d,td,tprefix=None):
        scans = list()
        for k,v in td.items():
            if prefix and not k.startswith(prefix):
                continue
            _key = td.get(f)
            ts = _key.get('t')
            if ts > t:
                scans.append(
                    get_fv(k,d.get(k))
                )
        scans.sort()
        return ', '.join(scans)
        
        
        
    for query in queries:
        oper = query[0].lower()
        if oper == 'set':
            k,f,v = query[1:]
            key = db.get(k)
            if key:
                key.update({f:v})
            else:
                key = {f:v}
            db.update({k:key})
            values.append('')
        elif oper == 'get':
            k,f = query[1:]
            key = db.get(k)
            if key:
                values.append(key.get(f,''))
            else:    
                values.append('')
        elif oper == 'delete':
            k,f = query[1:]
            key = db.get(k)
            if key and (f in key.keys()):
                key.pop(f)
                values.append('true')
            else: values.append('false')
        elif oper == 'scan':
            k = query[1]
            key = db.get(k)
            if key:
                values.append(scan_by_name(key))
            else: values.append('')
        elif oper == 'scan_by_prefix':
            k,p = query[1:]
            key = db.get(k)
            if key:
                values.append(scan_by_name(key,prefix=p))
            else: values.append('')
            
            
        elif oper == 'set_at':
            k,f,v,t = query[1:]
            key = db.get(k)
            if key:
                key.update({f:v})
            else:
                key = {f:v}
            db.update({k:key})
            key.update({'t':1000})
            time_db.update({k:key})
            values.append('')
        elif oper == 'set_at_with_ttl':
            k,f,v,t,tl = query[1:]
            key = db.get(k)
            if key:
                key.update({f:v})
            else:
                key = {f:v}
            db.update({k:key})
            key.update({'t':t+tl})
            time_db.update({k:key})
            values.append('')
            
        elif oper == 'delete_at':
            k,f,t = query[1:]
            key = time_db.get(k)
            key2 = db.get(k)
            if key and (f in key.keys()):
                _key = key.get(f)
                ts = _key.get('t')
                if ts < t:
                    key.pop(f)
                    key2.pop(f)
                    values.append('true')
                else: values.append('false')
            else: values.append('false')
            
        elif oper == 'get_at':
            k,f,t = query[1:]
            key = time_db.get(k)
            if key:
                _key = key.get(f)
                ts = _key.get('t')
                if ts > t:
                    values.append(key.get(f,''))
                else:values.append('')
            else:    
                values.append('')
        
        elif oper == 'scan_at':
            k,t = query[1:]
            key = time_db.get(k)
            key2 = db.get(k)
            
            if key:
                values.append(scan_at_by_name(key2,key,t))
            else: values.append('')
        elif oper == 'scan_by_prefix':
            k,p,t = query[1:]
            key = time_db.get(k)
            key2 = db.get(k)
            if key:
                values.append(scan_at_by_name(key2,key,t,prefix=p))
            else: values.append('')
            
            
            
    return values
                
            

