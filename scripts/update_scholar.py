"""One public-profile request. Preserve last verified metrics on any failure."""
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
import json, re, urllib.request

PROFILE='https://scholar.google.com/citations?user=eAgMSOMAAAAJ&hl=en'
class MetricsParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.table=False; self.row=None; self.cell=None; self.rows=[]
    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if tag=='table' and attrs.get('id')=='gsc_rsb_st': self.table=True
        if not self.table:return
        if tag=='tr':self.row=[]
        if tag=='td':self.cell=''
    def handle_data(self,data):
        if self.table and self.cell is not None:self.cell+=data
    def handle_endtag(self,tag):
        if not self.table:return
        if tag=='td' and self.cell is not None:
            if self.row is not None:self.row.append(self.cell.strip())
            self.cell=None
        if tag=='tr' and self.row is not None:self.rows.append(self.row);self.row=None
        if tag=='table':self.table=False

def parse_metrics(html):
    p=MetricsParser();p.feed(html);out={}
    mapping={'Citations':'citations','h-index':'h_index','i10-index':'i10_index'}
    for row in p.rows:
        if len(row)>=2 and row[0] in mapping:
            value=row[1].replace(',','').strip()
            if not re.fullmatch(r'\d+',value):raise ValueError('Non-numeric metric')
            out[mapping[row[0]]]=int(value)
    if set(out)!=set(mapping.values()):raise ValueError('Missing Scholar metrics (blocked response or layout change)')
    return out

def refresh(path,fetch):
    original=path.read_text()
    try:
        metrics=parse_metrics(fetch())
        metrics['updated_at']=datetime.now(timezone.utc).isoformat()
        updated,n=re.subn(r'(<script id="scholar-data" type="application/json">).*?(</script>)',lambda m:m[1]+json.dumps(metrics)+m[2],original,flags=re.S)
        if n!=1:raise ValueError('Expected one metrics data block')
    except Exception as exc:
        print('::warning::Scholar refresh unavailable; retained last verified data. '+str(exc))
        return False
    path.write_text(updated);print('Updated verified Scholar metrics.');return True

def fetch_profile():
    req=urllib.request.Request(PROFILE,headers={'User-Agent':'U2D-Academic-Profile/1.0 (weekly public citation check)'})
    with urllib.request.urlopen(req,timeout=25) as response:return response.read().decode('utf-8')

if __name__=='__main__':refresh(Path(__file__).resolve().parents[1]/'index.html',fetch_profile)
