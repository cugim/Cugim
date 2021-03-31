m = float(input('Uma distancia em metros: '))
km = m / 1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('''A medida em {} corresponde a: 
{} KM
{} HM
{} DAM
{} DM
{} CM
{} MM'''.format(m, km, hm, dam, dm, cm, mm))

