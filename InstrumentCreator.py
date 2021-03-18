def prepare_fly(Fmonth, Dmonth1, Dmonth2, year, period, instType='spread'):

  Fmonth, Fmonth_n, Fmonth_d = load_data(Fmonth, year, interval='1min')
  Fmonth = resamplePeriod(Fmonth, period=period)

  Dmonth1, Dmonth_n1, Dmonth_d1 = load_data(Dmonth1, year, interval='1min')
  Dmonth1 = resamplePeriod(Dmonth1, period=period)

  Dmonth2, Dmonth_n2, Dmonth_d2 = load_data(Dmonth2, year, interval='1min')
  Dmonth2 = resamplePeriod(Dmonth2, period=period)

  x = Fmonth.loc[Fmonth.index.intersection(Dmonth1.index.values),:].dropna()
  y = Dmonth1.loc[Dmonth1.index.intersection(x.index.values),:]
  z = Dmonth2.loc[Dmonth2.index.intersection(x.index.values),:].dropna()
  x = x.loc[x.index.intersection(z.index.values),:].dropna()
  y = y.loc[y.index.intersection(z.index.values),:].dropna()

  s1 = (x-y).Close
  s2 = (y-z).Close
  if instType='spread':
    return s1, s2
  if instType='fly':
    return (s1-s2).dropna()
