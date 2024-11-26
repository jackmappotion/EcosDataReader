# EcosDataReader

ECOS : 한국은행 경제통계시스템

ECOS의 API를 적절하게 정제하여 제공합니다.

```python
from EcosDataReader import EcosDataReader
```


```python
api_key = "YOUR_API_KEY"
ecos_data_reader = EcosDataReader(api_key)
```


```python
start_date, end_date = '2024-01-01', '2024-12-01'
```


```python
# 중앙은행의 자산 데이터 반환
bok_asset_df = ecos_data_reader.bank_data_reader.get_bok_asset_df(start_date,end_date)
print('한국은행의 자산 데이터 반환')
display(bok_asset_df.head())

# 소유자별 예금 데이터를 반환
deposit_by_owner_df = ecos_data_reader.bank_data_reader.get_deposit_by_owner_df(start_date,end_date)
print('소유자별 예금 데이터를 반환')
display(deposit_by_owner_df.head())

# 은행 예금 데이터를 반환
deposit_df = ecos_data_reader.bank_data_reader.get_deposit_df(start_date,end_date)
print('은행 예금 데이터를 반환')
display(deposit_df.head())

# 은행 대출 데이터를 반환
loan_df = ecos_data_reader.bank_data_reader.get_loan_df(start_date,end_date)
print('은행 대출 데이터를 반환')
display(loan_df.head())

# 연체 대출 비율 데이터를 반환
overdue_loan_rate_df = ecos_data_reader.bank_data_reader.get_overdue_loan_rate_df(start_date,end_date)
print('연체 대출 비율 데이터를 반환')
display(overdue_loan_rate_df.head())
```

    한국은행의 자산 데이터 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>IMF포지션</th>
      <th>금</th>
      <th>외환</th>
      <th>특별인출권</th>
      <th>합계</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>4561308</td>
      <td>4794759</td>
      <td>391467140</td>
      <td>14935556</td>
      <td>415758762</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>4548620</td>
      <td>4794759</td>
      <td>391327307</td>
      <td>15067803</td>
      <td>415738489</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>4333425</td>
      <td>4794759</td>
      <td>395420268</td>
      <td>14702874</td>
      <td>419251325</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>4365827</td>
      <td>4794759</td>
      <td>389456672</td>
      <td>14642880</td>
      <td>413260138</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>4381064</td>
      <td>4794759</td>
      <td>388909215</td>
      <td>14747040</td>
      <td>412832077</td>
    </tr>
  </tbody>
</table>
</div>


    소유자별 예금 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>가계</th>
      <th>기업</th>
      <th>기타</th>
      <th>요구불예금</th>
      <th>저축성예금</th>
      <th>총예금</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>926055.8</td>
      <td>608701.4</td>
      <td>429431.2</td>
      <td>315117.3</td>
      <td>1649071.2</td>
      <td>1964188.4</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>941265.2</td>
      <td>616783.1</td>
      <td>455561.6</td>
      <td>330390</td>
      <td>1683219.9</td>
      <td>2013610</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>956543.3</td>
      <td>649919.7</td>
      <td>443467.8</td>
      <td>346377.2</td>
      <td>1703553.6</td>
      <td>2049930.9</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>955759.1</td>
      <td>610446</td>
      <td>434133.5</td>
      <td>333683.8</td>
      <td>1666654.7</td>
      <td>2000338.5</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>956436.6</td>
      <td>618181.9</td>
      <td>440730</td>
      <td>330668.3</td>
      <td>1684680.3</td>
      <td>2015348.6</td>
    </tr>
  </tbody>
</table>
</div>


    은행 예금 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>수신합계</th>
      <th>외화예금</th>
      <th>원화예금</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>2501526</td>
      <td>135780.2</td>
      <td>1964188.4</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>2535286</td>
      <td>133176.1</td>
      <td>2013610</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>2576160.1</td>
      <td>133660.7</td>
      <td>2049930.9</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>2540276.9</td>
      <td>131485.2</td>
      <td>2000338.5</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>2560661.9</td>
      <td>127281.6</td>
      <td>2015348.6</td>
    </tr>
  </tbody>
</table>
</div>


    은행 대출 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>금융자금</th>
      <th>재정자금</th>
      <th>주택자금</th>
      <th>총대출금</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>2227003.3</td>
      <td>48751.6</td>
      <td>322694.8</td>
      <td>2275754.9</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>2236811.7</td>
      <td>49199.1</td>
      <td>325064.6</td>
      <td>2286010.8</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>2246646.2</td>
      <td>48794.3</td>
      <td>323385.4</td>
      <td>2295440.4</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>2263673.7</td>
      <td>49286.9</td>
      <td>325693</td>
      <td>2312960.6</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>2277271.4</td>
      <td>49926.5</td>
      <td>329832</td>
      <td>2327198</td>
    </tr>
  </tbody>
</table>
</div>


    연체 대출 비율 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>가계대출</th>
      <th>기업대출</th>
      <th>신용카드대출 2)</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>0.4</td>
      <td>0.6</td>
      <td>1.7</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>0.4</td>
      <td>0.7</td>
      <td>2</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>0.4</td>
      <td>0.6</td>
      <td>1.8</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>0.4</td>
      <td>0.6</td>
      <td>1.8</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>0.4</td>
      <td>0.7</td>
      <td>1.9</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 무역 수지 데이터를 반환
trade_balance_df = ecos_data_reader.trade_data_reader.get_trade_balance_df(start_date,end_date)
print('무역 수지 데이터를 반환')
display(trade_balance_df.head())

# 국가별 수출 데이터를 반환
trade_export_country_df = ecos_data_reader.trade_data_reader.get_trade_export_country_df(start_date,end_date)
print('국가별 수출 데이터를 반환')
display(trade_export_country_df.head())

# 품목별 수출 데이터를 반환
trade_export_product_df = ecos_data_reader.trade_data_reader.get_trade_export_product_df(start_date,end_date)
print('품목별 수출 데이터를 반환')
display(trade_export_product_df.head())

# 국가별 수입 데이터를 반환
trade_import_country_df = ecos_data_reader.trade_data_reader.get_trade_import_country_df(start_date,end_date)
print('국가별 수입 데이터를 반환')
display(trade_import_country_df.head())

# 품목별 수입 데이터를 반환
trade_import_product_df = ecos_data_reader.trade_data_reader.get_trade_import_product_df(start_date,end_date)
print('품목별 수입 데이터를 반환')
display(trade_import_product_df.head())
```

    무역 수지 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>경상수지</th>
      <th>본원소득수지</th>
      <th>상품수지</th>
      <th>서비스수지</th>
      <th>이전소득수지</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>3045.7</td>
      <td>1616</td>
      <td>4240.4</td>
      <td>-2656.8</td>
      <td>-153.9</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>6858.3</td>
      <td>2439.5</td>
      <td>6607.9</td>
      <td>-1773</td>
      <td>-416.1</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>6931.4</td>
      <td>1827.3</td>
      <td>8092.6</td>
      <td>-2431.3</td>
      <td>-557.2</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>-285.2</td>
      <td>-3370.6</td>
      <td>5111.4</td>
      <td>-1663.9</td>
      <td>-362.1</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>8922.5</td>
      <td>1764.3</td>
      <td>8751.5</td>
      <td>-1285.6</td>
      <td>-307.7</td>
    </tr>
  </tbody>
</table>
</div>


    국가별 수출 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>국별수출(관세청)</th>
      <th>수출총액(네덜란드)</th>
      <th>수출총액(대만)</th>
      <th>수출총액(독일)</th>
      <th>수출총액(러시아)</th>
      <th>수출총액(말레이지아)</th>
      <th>수출총액(미국)</th>
      <th>수출총액(브라질)</th>
      <th>수출총액(사우디아라비아)</th>
      <th>수출총액(스위스)</th>
      <th>...</th>
      <th>수출총액(인도네시아)</th>
      <th>수출총액(일본)</th>
      <th>수출총액(중국)</th>
      <th>수출총액(캐나다)</th>
      <th>수출총액(태국)</th>
      <th>수출총액(파나마)</th>
      <th>수출총액(프랑스)</th>
      <th>수출총액(필리핀)</th>
      <th>수출총액(호주)</th>
      <th>수출총액(홍콩)</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>54762079</td>
      <td>538032</td>
      <td>1773996</td>
      <td>759853</td>
      <td>424032</td>
      <td>774758</td>
      <td>10251959</td>
      <td>421343</td>
      <td>503072</td>
      <td>108264</td>
      <td>...</td>
      <td>614603</td>
      <td>2543338</td>
      <td>10698527</td>
      <td>905997</td>
      <td>637341</td>
      <td>12954</td>
      <td>271970</td>
      <td>708991</td>
      <td>1454845</td>
      <td>2678331</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>52114064</td>
      <td>586970</td>
      <td>1531947</td>
      <td>850542</td>
      <td>716851</td>
      <td>938936</td>
      <td>9810109</td>
      <td>412914</td>
      <td>409402</td>
      <td>88397</td>
      <td>...</td>
      <td>681353</td>
      <td>2374277</td>
      <td>9644749</td>
      <td>771399</td>
      <td>608847</td>
      <td>177339</td>
      <td>335088</td>
      <td>871712</td>
      <td>1259284</td>
      <td>2983281</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>56520783</td>
      <td>705339</td>
      <td>1988563</td>
      <td>797188</td>
      <td>308274</td>
      <td>806446</td>
      <td>10882206</td>
      <td>453865</td>
      <td>381871</td>
      <td>108939</td>
      <td>...</td>
      <td>495889</td>
      <td>2127715</td>
      <td>10520927</td>
      <td>868824</td>
      <td>605897</td>
      <td>447730</td>
      <td>503266</td>
      <td>677320</td>
      <td>1590762</td>
      <td>3699084</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>56149624</td>
      <td>577584</td>
      <td>2086983</td>
      <td>916502</td>
      <td>316421</td>
      <td>862511</td>
      <td>11401962</td>
      <td>496115</td>
      <td>479791</td>
      <td>124415</td>
      <td>...</td>
      <td>650345</td>
      <td>2438629</td>
      <td>10475883</td>
      <td>972102</td>
      <td>668784</td>
      <td>102637</td>
      <td>503525</td>
      <td>847069</td>
      <td>1427204</td>
      <td>2933565</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>58012786</td>
      <td>550032</td>
      <td>2517037</td>
      <td>910145</td>
      <td>313514</td>
      <td>834728</td>
      <td>10929788</td>
      <td>452056</td>
      <td>445712</td>
      <td>121004</td>
      <td>...</td>
      <td>679144</td>
      <td>2606088</td>
      <td>11378144</td>
      <td>942686</td>
      <td>646910</td>
      <td>147470</td>
      <td>330498</td>
      <td>985097</td>
      <td>1253380</td>
      <td>2706674</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 25 columns</p>
</div>


    품목별 수출 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>총지수</th>
      <th>과일</th>
      <th>채소및과실</th>
      <th>농산물</th>
      <th>신선수산물</th>
      <th>신선수산물</th>
      <th>냉동수산물</th>
      <th>냉동건조수산물</th>
      <th>수산물</th>
      <th>농림수산품</th>
      <th>...</th>
      <th>자동차</th>
      <th>운송장비</th>
      <th>금속가구</th>
      <th>기타가구</th>
      <th>가구</th>
      <th>기타제조업제품</th>
      <th>기타제조업제품</th>
      <th>기타제조업제품</th>
      <th>기타제조업제품</th>
      <th>공산품</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>126.78</td>
      <td>120.91</td>
      <td>113.31</td>
      <td>103.8</td>
      <td>82.92</td>
      <td>82.92</td>
      <td>107.49</td>
      <td>107.49</td>
      <td>101.38</td>
      <td>101.19</td>
      <td>...</td>
      <td>173.79</td>
      <td>173.7</td>
      <td>117.16</td>
      <td>111.58</td>
      <td>109.65</td>
      <td>93.84</td>
      <td>93.84</td>
      <td>106.7</td>
      <td>106.7</td>
      <td>126.67</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>122.73</td>
      <td>26.72</td>
      <td>82.85</td>
      <td>77.3</td>
      <td>84.27</td>
      <td>84.27</td>
      <td>126.36</td>
      <td>126.36</td>
      <td>115.89</td>
      <td>102.09</td>
      <td>...</td>
      <td>152.15</td>
      <td>152.14</td>
      <td>121.01</td>
      <td>98.56</td>
      <td>102.45</td>
      <td>95.85</td>
      <td>95.85</td>
      <td>99.49</td>
      <td>99.49</td>
      <td>122.56</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>132.77</td>
      <td>14.57</td>
      <td>75.71</td>
      <td>79.34</td>
      <td>90.91</td>
      <td>90.91</td>
      <td>106.82</td>
      <td>106.82</td>
      <td>102.86</td>
      <td>97.68</td>
      <td>...</td>
      <td>172.4</td>
      <td>172.33</td>
      <td>128.31</td>
      <td>109.41</td>
      <td>111.89</td>
      <td>112.24</td>
      <td>112.24</td>
      <td>110.52</td>
      <td>110.52</td>
      <td>132.78</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>131.75</td>
      <td>1.72</td>
      <td>58.65</td>
      <td>93.51</td>
      <td>105.34</td>
      <td>105.34</td>
      <td>200.6</td>
      <td>200.6</td>
      <td>176.9</td>
      <td>141.2</td>
      <td>...</td>
      <td>186.9</td>
      <td>186.86</td>
      <td>128.84</td>
      <td>114.93</td>
      <td>115.35</td>
      <td>127.79</td>
      <td>127.79</td>
      <td>117.93</td>
      <td>117.93</td>
      <td>131.69</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>136.32</td>
      <td>1.43</td>
      <td>39.83</td>
      <td>88.63</td>
      <td>97.48</td>
      <td>97.48</td>
      <td>97.23</td>
      <td>97.23</td>
      <td>97.29</td>
      <td>96.53</td>
      <td>...</td>
      <td>177.68</td>
      <td>177.66</td>
      <td>122.4</td>
      <td>120.69</td>
      <td>117.87</td>
      <td>125.9</td>
      <td>125.9</td>
      <td>117.39</td>
      <td>117.39</td>
      <td>136.37</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 236 columns</p>
</div>


    국가별 수입 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>국별수입(관세청)</th>
      <th>수입총액(네덜란드)</th>
      <th>수입총액(대만)</th>
      <th>수입총액(독일)</th>
      <th>수입총액(러시아)</th>
      <th>수입총액(말레이지아)</th>
      <th>수입총액(미국)</th>
      <th>수입총액(브라질)</th>
      <th>수입총액(사우디아라비아)</th>
      <th>수입총액(스위스)</th>
      <th>...</th>
      <th>수입총액(인도네시아)</th>
      <th>수입총액(일본)</th>
      <th>수입총액(중국)</th>
      <th>수입총액(캐나다)</th>
      <th>수입총액(태국)</th>
      <th>수입총액(파나마)</th>
      <th>수입총액(프랑스)</th>
      <th>수입총액(필리핀)</th>
      <th>수입총액(호주)</th>
      <th>수입총액(홍콩)</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>54441200</td>
      <td>288481</td>
      <td>2196643</td>
      <td>1516714</td>
      <td>531514</td>
      <td>1365251</td>
      <td>6136084</td>
      <td>680255</td>
      <td>2662661</td>
      <td>278859</td>
      <td>...</td>
      <td>1335823</td>
      <td>3752928</td>
      <td>12394182</td>
      <td>595575</td>
      <td>551815</td>
      <td>12569</td>
      <td>588114</td>
      <td>396619</td>
      <td>3305739</td>
      <td>189115</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>48145771</td>
      <td>564398</td>
      <td>2191481</td>
      <td>1730590</td>
      <td>602404</td>
      <td>1115519</td>
      <td>5612040</td>
      <td>661156</td>
      <td>2367707</td>
      <td>261337</td>
      <td>...</td>
      <td>1052903</td>
      <td>3721714</td>
      <td>9412816</td>
      <td>545072</td>
      <td>554572</td>
      <td>3776</td>
      <td>543999</td>
      <td>394329</td>
      <td>2336518</td>
      <td>223006</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>52334598</td>
      <td>692094</td>
      <td>2129157</td>
      <td>1814825</td>
      <td>556323</td>
      <td>1061566</td>
      <td>5973454</td>
      <td>450516</td>
      <td>2608253</td>
      <td>283539</td>
      <td>...</td>
      <td>1025579</td>
      <td>4386318</td>
      <td>11401252</td>
      <td>698095</td>
      <td>601629</td>
      <td>2630</td>
      <td>613285</td>
      <td>416479</td>
      <td>2393609</td>
      <td>291266</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>54749920</td>
      <td>468450</td>
      <td>2298344</td>
      <td>1949805</td>
      <td>528149</td>
      <td>1027005</td>
      <td>6011795</td>
      <td>648981</td>
      <td>2842655</td>
      <td>354204</td>
      <td>...</td>
      <td>1060882</td>
      <td>4128159</td>
      <td>12420435</td>
      <td>630791</td>
      <td>635068</td>
      <td>1995</td>
      <td>640413</td>
      <td>461088</td>
      <td>2964439</td>
      <td>376290</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>53139337</td>
      <td>539532</td>
      <td>2791949</td>
      <td>1976489</td>
      <td>619671</td>
      <td>1015389</td>
      <td>6371207</td>
      <td>653536</td>
      <td>3041728</td>
      <td>288609</td>
      <td>...</td>
      <td>1084273</td>
      <td>3443088</td>
      <td>12286653</td>
      <td>424014</td>
      <td>608548</td>
      <td>1836</td>
      <td>615623</td>
      <td>353790</td>
      <td>2270675</td>
      <td>141276</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 25 columns</p>
</div>


    품목별 수입 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>총지수</th>
      <th>곡류</th>
      <th>맥류및잡곡</th>
      <th>콩류</th>
      <th>곡물및식량작물</th>
      <th>과일</th>
      <th>채소및과실</th>
      <th>잎담배</th>
      <th>천연고무</th>
      <th>기타식용작물</th>
      <th>...</th>
      <th>기타운송장비</th>
      <th>운송장비</th>
      <th>기타가구</th>
      <th>가구</th>
      <th>장난감및오락용품</th>
      <th>운동및경기용품</th>
      <th>기타제조업제품</th>
      <th>기타제조업제품</th>
      <th>기타제조업제품</th>
      <th>공산품</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>140.62</td>
      <td>163.03</td>
      <td>141.75</td>
      <td>139.17</td>
      <td>144.37</td>
      <td>107.43</td>
      <td>112.6</td>
      <td>208.74</td>
      <td>96.12</td>
      <td>121.85</td>
      <td>...</td>
      <td>83.57</td>
      <td>92.44</td>
      <td>112.98</td>
      <td>107.76</td>
      <td>106.93</td>
      <td>117.94</td>
      <td>117.83</td>
      <td>113.3</td>
      <td>113.3</td>
      <td>125.33</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>123.51</td>
      <td>15.68</td>
      <td>134.57</td>
      <td>103.36</td>
      <td>120.32</td>
      <td>105.38</td>
      <td>108.18</td>
      <td>270.94</td>
      <td>77.08</td>
      <td>105.81</td>
      <td>...</td>
      <td>120.06</td>
      <td>100.54</td>
      <td>90.51</td>
      <td>86.52</td>
      <td>65.96</td>
      <td>94.43</td>
      <td>85.49</td>
      <td>85.96</td>
      <td>85.96</td>
      <td>109.93</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>134.17</td>
      <td>215.36</td>
      <td>120.15</td>
      <td>107.76</td>
      <td>127.78</td>
      <td>214.79</td>
      <td>205.07</td>
      <td>161.58</td>
      <td>82.51</td>
      <td>144.93</td>
      <td>...</td>
      <td>132.73</td>
      <td>116.13</td>
      <td>95.96</td>
      <td>88.19</td>
      <td>82.56</td>
      <td>111.11</td>
      <td>102.21</td>
      <td>95.9</td>
      <td>95.9</td>
      <td>127.07</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>140.71</td>
      <td>93.41</td>
      <td>149.27</td>
      <td>103.58</td>
      <td>139.3</td>
      <td>222.23</td>
      <td>213.4</td>
      <td>166.25</td>
      <td>95.87</td>
      <td>155.9</td>
      <td>...</td>
      <td>128.46</td>
      <td>127.93</td>
      <td>120.84</td>
      <td>112.12</td>
      <td>120.68</td>
      <td>115.67</td>
      <td>126.86</td>
      <td>120.23</td>
      <td>120.23</td>
      <td>128.8</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>137.14</td>
      <td>51.82</td>
      <td>119.46</td>
      <td>230.93</td>
      <td>128.64</td>
      <td>185.83</td>
      <td>175.6</td>
      <td>123.19</td>
      <td>93.95</td>
      <td>157.85</td>
      <td>...</td>
      <td>145.54</td>
      <td>127.03</td>
      <td>116.75</td>
      <td>108.38</td>
      <td>99.62</td>
      <td>111.06</td>
      <td>116.46</td>
      <td>112.82</td>
      <td>112.82</td>
      <td>126.75</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 274 columns</p>
</div>



```python
# 주시식장 예금 데이터를 반환
balance_df = ecos_data_reader.market_data_reader.get_balance_df(start_date,end_date)
print('시장 잔고 데이터를 반환')
display(balance_df.head())

# 파생상품 관련 데이터를 반환
derivative_df = ecos_data_reader.market_data_reader.get_derivative_df(start_date,end_date)
print('파생상품 관련 데이터를 반환')
display(derivative_df.head())

# KOSPI (코스피) 데이터 반환
kospi_df = ecos_data_reader.market_data_reader.get_kospi_df(start_date,end_date)
print('KOSPI (코스피) 데이터 반환')
display(kospi_df.head())

# KOSDAQ (코스닥) 데이터 반환
kosdaq_df = ecos_data_reader.market_data_reader.get_kosdaq_df(start_date,end_date)
print('KOSDAQ (코스닥) 데이터 반환')
display(kosdaq_df.head())
```

    시장 잔고 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>투자자_예탁금</th>
      <th>파생거래_예탁금</th>
      <th>미수금</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>50743424</td>
      <td>11098228</td>
      <td>953252</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>54335607</td>
      <td>10832461</td>
      <td>988582</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>56522918</td>
      <td>10987581</td>
      <td>958709</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>57230646</td>
      <td>11272437</td>
      <td>928925</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>54396417</td>
      <td>11394204</td>
      <td>981503</td>
    </tr>
  </tbody>
</table>
</div>


    파생상품 관련 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>선물_계약수</th>
      <th>선물_계약금액</th>
      <th>CALL_옵션_계약수</th>
      <th>CALL_옵션_계약금액</th>
      <th>PUT_옵션_계약수</th>
      <th>PUT_옵션_계약금액</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>6001167</td>
      <td>512151112</td>
      <td>24950756</td>
      <td>5601982</td>
      <td>18606112</td>
      <td>5169447</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>4839936</td>
      <td>427272274</td>
      <td>16570843</td>
      <td>4058921</td>
      <td>12818976</td>
      <td>2850769</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>5594151</td>
      <td>510624442</td>
      <td>14935080</td>
      <td>4164901</td>
      <td>12262550</td>
      <td>2822631</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>5392592</td>
      <td>493054799</td>
      <td>17490588</td>
      <td>4694969</td>
      <td>16089521</td>
      <td>4436327</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>4862286</td>
      <td>450031261</td>
      <td>13164285</td>
      <td>3533776</td>
      <td>11503203</td>
      <td>3078326</td>
    </tr>
  </tbody>
</table>
</div>


    KOSPI (코스피) 데이터 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>코스피_지수</th>
      <th>코스피_거래량</th>
      <th>코스피_거래대금</th>
      <th>코스피_외국인순매수</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20240102</th>
      <td>2669.81</td>
      <td>40430</td>
      <td>95177</td>
      <td>2282</td>
    </tr>
    <tr>
      <th>20240103</th>
      <td>2607.31</td>
      <td>45593</td>
      <td>99927</td>
      <td>-973</td>
    </tr>
    <tr>
      <th>20240104</th>
      <td>2587.02</td>
      <td>76145</td>
      <td>88448</td>
      <td>1149</td>
    </tr>
    <tr>
      <th>20240105</th>
      <td>2578.08</td>
      <td>51478</td>
      <td>82718</td>
      <td>-510</td>
    </tr>
    <tr>
      <th>20240108</th>
      <td>2567.82</td>
      <td>31358</td>
      <td>66527</td>
      <td>1700</td>
    </tr>
  </tbody>
</table>
</div>


    KOSDAQ (코스닥) 데이터 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>코스닥_지수</th>
      <th>코스닥_거래량</th>
      <th>코스닥_거래대금</th>
      <th>코스닥_외국인순매수</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20240102</th>
      <td>878.93</td>
      <td>115442</td>
      <td>90164</td>
      <td>1284</td>
    </tr>
    <tr>
      <th>20240103</th>
      <td>871.57</td>
      <td>125915</td>
      <td>103469</td>
      <td>-879</td>
    </tr>
    <tr>
      <th>20240104</th>
      <td>866.25</td>
      <td>122426</td>
      <td>101521</td>
      <td>-1322</td>
    </tr>
    <tr>
      <th>20240105</th>
      <td>878.33</td>
      <td>104792</td>
      <td>101738</td>
      <td>1413</td>
    </tr>
    <tr>
      <th>20240108</th>
      <td>879.34</td>
      <td>116238</td>
      <td>102810</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 금리 데이터를 반환
interest_rate_df = ecos_data_reader.interest_data_reader.get_interest_rate_df(start_date,end_date)
print('금리 데이터를 반환')
display(interest_rate_df.head())

# 국채 데이터를 반환
national_treasury_df = ecos_data_reader.interest_data_reader.get_national_treasury_df(start_date,end_date)
print('국채 데이터를 반환')
display(national_treasury_df.head())

```

    금리 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>기준금리</th>
      <th>수신금리</th>
      <th>대출금리</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>3.5</td>
      <td>3.67</td>
      <td>5.04</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>3.5</td>
      <td>3.63</td>
      <td>4.85</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>3.5</td>
      <td>3.58</td>
      <td>4.85</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>3.5</td>
      <td>3.53</td>
      <td>4.77</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>3.5</td>
      <td>3.55</td>
      <td>4.78</td>
    </tr>
  </tbody>
</table>
</div>


    국채 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>국고채_1년</th>
      <th>국고채_3년</th>
      <th>국고채_5년</th>
      <th>국고채_10년</th>
      <th>국고채_20년</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20240102</th>
      <td>3.466</td>
      <td>3.24</td>
      <td>3.266</td>
      <td>3.306</td>
      <td>3.243</td>
    </tr>
    <tr>
      <th>20240103</th>
      <td>3.471</td>
      <td>3.278</td>
      <td>3.313</td>
      <td>3.338</td>
      <td>3.247</td>
    </tr>
    <tr>
      <th>20240104</th>
      <td>3.451</td>
      <td>3.227</td>
      <td>3.256</td>
      <td>3.288</td>
      <td>3.211</td>
    </tr>
    <tr>
      <th>20240105</th>
      <td>3.46</td>
      <td>3.283</td>
      <td>3.312</td>
      <td>3.344</td>
      <td>3.252</td>
    </tr>
    <tr>
      <th>20240108</th>
      <td>3.455</td>
      <td>3.297</td>
      <td>3.312</td>
      <td>3.344</td>
      <td>3.238</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 전체 신용카드 사용 데이터를 반환
total_credit_card_df = ecos_data_reader.payment_data_reader.get_total_credit_card_df(start_date, end_date)
print('전체 신용카드 사용 데이터를 반환')
display(total_credit_card_df)

# 은행 발급 신용카드 사용 데이터를 반환
bank_credit_card_df = ecos_data_reader.payment_data_reader.get_bank_credit_card_df(start_date, end_date)
print('은행 발급 신용카드 사용 데이터를 반환')
display(bank_credit_card_df)

# 비은행 신용카드 사용 데이터를 반환
not_bank_credit_card_df = ecos_data_reader.payment_data_reader.get_not_bank_credit_card_df(start_date, end_date)
print('비은행 신용카드 사용 데이터를 반환')
display(not_bank_credit_card_df)

# 결제 횟수 데이터를 반환
payment_cnt_df = ecos_data_reader.payment_data_reader.get_payment_cnt_df(start_date, end_date)
print('결제 횟수 데이터를 반환')
display(payment_cnt_df)

# 결제 금액 데이터를 반환
payment_won_df = ecos_data_reader.payment_data_reader.get_payment_won_df(start_date, end_date)
print('결제 금액 데이터를 반환')
display(payment_won_df)

```

    전체 신용카드 사용 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>개인 신용카드 발급장수</th>
      <th>개인 이용건수</th>
      <th>개인 이용금액</th>
      <th>개인 일반구매 이용건수</th>
      <th>개인 일반구매 이용금액</th>
      <th>개인 할부구매 이용건수</th>
      <th>개인 할부구매 이용금액</th>
      <th>개인 현금서비스 이용건수</th>
      <th>개인 현금서비스 이용금액</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>118886</td>
      <td>1421405</td>
      <td>71204004</td>
      <td>1374333</td>
      <td>52304914</td>
      <td>41962</td>
      <td>14024020</td>
      <td>5110</td>
      <td>4875071</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>119216</td>
      <td>1303452</td>
      <td>65231848</td>
      <td>1261278</td>
      <td>48755279</td>
      <td>37526</td>
      <td>11922204</td>
      <td>4648</td>
      <td>4554364</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>119563</td>
      <td>1436394</td>
      <td>70463501</td>
      <td>1391059</td>
      <td>52706219</td>
      <td>40383</td>
      <td>12969098</td>
      <td>4952</td>
      <td>4788184</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>119927</td>
      <td>1487268</td>
      <td>69635523</td>
      <td>1441101</td>
      <td>52072486</td>
      <td>41207</td>
      <td>12806256</td>
      <td>4960</td>
      <td>4756781</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>120360</td>
      <td>1522895</td>
      <td>71470287</td>
      <td>1475203</td>
      <td>53499092</td>
      <td>42604</td>
      <td>13083041</td>
      <td>5088</td>
      <td>4888154</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>120588</td>
      <td>1476731</td>
      <td>69465828</td>
      <td>1431300</td>
      <td>52135546</td>
      <td>40602</td>
      <td>12624201</td>
      <td>4829</td>
      <td>4706080</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>120834</td>
      <td>1530272</td>
      <td>72481951</td>
      <td>1482562</td>
      <td>53659153</td>
      <td>42676</td>
      <td>13896605</td>
      <td>5034</td>
      <td>4926193</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>121008</td>
      <td>1533186</td>
      <td>71014563</td>
      <td>1487545</td>
      <td>53355590</td>
      <td>40717</td>
      <td>12768837</td>
      <td>4924</td>
      <td>4890137</td>
    </tr>
  </tbody>
</table>
</div>


    은행 발급 신용카드 사용 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>개인 신용카드 발급장수</th>
      <th>개인 이용건수</th>
      <th>개인 이용금액</th>
      <th>개인 일반구매 이용건수</th>
      <th>개인 일반구매 이용금액</th>
      <th>개인 할부구매 이용건수</th>
      <th>개인 할부구매 이용금액</th>
      <th>개인 현금서비스 이용건수</th>
      <th>개인 현금서비스 이용금액</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>70976</td>
      <td>856470</td>
      <td>40996700</td>
      <td>830191</td>
      <td>30302742</td>
      <td>22920</td>
      <td>7474411</td>
      <td>3359</td>
      <td>3219548</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>71172</td>
      <td>782319</td>
      <td>37666919</td>
      <td>758895</td>
      <td>28285863</td>
      <td>20384</td>
      <td>6394446</td>
      <td>3040</td>
      <td>2986610</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>71368</td>
      <td>857051</td>
      <td>40540879</td>
      <td>831911</td>
      <td>30472935</td>
      <td>21914</td>
      <td>6952543</td>
      <td>3226</td>
      <td>3115401</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>71586</td>
      <td>896448</td>
      <td>39905178</td>
      <td>870763</td>
      <td>30022059</td>
      <td>22453</td>
      <td>6829634</td>
      <td>3232</td>
      <td>3053485</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>71852</td>
      <td>910902</td>
      <td>40703561</td>
      <td>885071</td>
      <td>30777422</td>
      <td>22528</td>
      <td>6789467</td>
      <td>3303</td>
      <td>3136672</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>71959</td>
      <td>878367</td>
      <td>39634268</td>
      <td>854122</td>
      <td>30130957</td>
      <td>21153</td>
      <td>6526832</td>
      <td>3093</td>
      <td>2976479</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>72047</td>
      <td>920051</td>
      <td>41342673</td>
      <td>893454</td>
      <td>30852819</td>
      <td>23343</td>
      <td>7360701</td>
      <td>3255</td>
      <td>3129153</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>72103</td>
      <td>913654</td>
      <td>40717205</td>
      <td>888587</td>
      <td>30911312</td>
      <td>21901</td>
      <td>6710899</td>
      <td>3166</td>
      <td>3094994</td>
    </tr>
  </tbody>
</table>
</div>


    비은행 신용카드 사용 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>개인 신용카드 발급장수</th>
      <th>개인 이용건수</th>
      <th>개인 이용금액</th>
      <th>개인 일반구매 이용건수</th>
      <th>개인 일반구매 이용금액</th>
      <th>개인 할부구매 이용건수</th>
      <th>개인 할부구매 이용금액</th>
      <th>개인 현금서비스 이용건수</th>
      <th>개인 현금서비스 이용금액</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>47910</td>
      <td>564935</td>
      <td>30207304</td>
      <td>544142</td>
      <td>22002172</td>
      <td>19042</td>
      <td>6549609</td>
      <td>1751</td>
      <td>1655523</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>48044</td>
      <td>521134</td>
      <td>27564929</td>
      <td>502383</td>
      <td>20469417</td>
      <td>17143</td>
      <td>5527758</td>
      <td>1608</td>
      <td>1567754</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>48195</td>
      <td>579343</td>
      <td>29922622</td>
      <td>559148</td>
      <td>22233284</td>
      <td>18469</td>
      <td>6016555</td>
      <td>1726</td>
      <td>1672783</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>48342</td>
      <td>590821</td>
      <td>29730345</td>
      <td>570338</td>
      <td>22050427</td>
      <td>18755</td>
      <td>5976623</td>
      <td>1729</td>
      <td>1703296</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>48509</td>
      <td>611993</td>
      <td>30766726</td>
      <td>590131</td>
      <td>22721670</td>
      <td>20077</td>
      <td>6293574</td>
      <td>1785</td>
      <td>1751482</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>48629</td>
      <td>598364</td>
      <td>29831560</td>
      <td>577178</td>
      <td>22004590</td>
      <td>19449</td>
      <td>6097369</td>
      <td>1737</td>
      <td>1729602</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>48787</td>
      <td>610221</td>
      <td>31139278</td>
      <td>589109</td>
      <td>22806334</td>
      <td>19333</td>
      <td>6535903</td>
      <td>1779</td>
      <td>1797040</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>48905</td>
      <td>619532</td>
      <td>30297358</td>
      <td>598958</td>
      <td>22444277</td>
      <td>18817</td>
      <td>6057938</td>
      <td>1758</td>
      <td>1795143</td>
    </tr>
  </tbody>
</table>
</div>


    결제 횟수 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>계좌이체</th>
      <th>신용카드</th>
      <th>신용카드(물품및용역구매)</th>
      <th>신용카드(현금서비스)</th>
      <th>입금이체</th>
      <th>체크카드</th>
      <th>출금이체</th>
      <th>카드</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>1196039.5</td>
      <td>1529028.1</td>
      <td>1523918.3</td>
      <td>5109.8</td>
      <td>851911.1</td>
      <td>808547.3</td>
      <td>344128.3</td>
      <td>2354938.5</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>1148485.7</td>
      <td>1402698.2</td>
      <td>1398050.2</td>
      <td>4648</td>
      <td>810031.7</td>
      <td>765423.8</td>
      <td>338454</td>
      <td>2187277.7</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>1203844.4</td>
      <td>1548922.7</td>
      <td>1543970.3</td>
      <td>4952.4</td>
      <td>855227.9</td>
      <td>855916.3</td>
      <td>348616.5</td>
      <td>2425543.6</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>1214755.5</td>
      <td>1599950</td>
      <td>1594989.9</td>
      <td>4960.1</td>
      <td>863083.4</td>
      <td>889803.1</td>
      <td>351672.1</td>
      <td>2508092.1</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>1251231</td>
      <td>1638305.4</td>
      <td>1633216.9</td>
      <td>5088.5</td>
      <td>883887.6</td>
      <td>915364.5</td>
      <td>367343.4</td>
      <td>2572006.1</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>1200030.3</td>
      <td>1589082.5</td>
      <td>1584253.1</td>
      <td>4829.4</td>
      <td>843677.9</td>
      <td>879321.3</td>
      <td>356352.5</td>
      <td>2486134.6</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>1284553.8</td>
      <td>1647628.5</td>
      <td>1642594.8</td>
      <td>5033.8</td>
      <td>909089.2</td>
      <td>903626.6</td>
      <td>375464.6</td>
      <td>2569151</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>1242326.6</td>
      <td>1648615.4</td>
      <td>1643691.4</td>
      <td>4924.1</td>
      <td>874190.7</td>
      <td>906525.7</td>
      <td>368135.9</td>
      <td>2573896</td>
    </tr>
  </tbody>
</table>
</div>


    결제 금액 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>계좌이체</th>
      <th>신용카드</th>
      <th>신용카드(물품및용역구매)</th>
      <th>신용카드(현금서비스)</th>
      <th>입금이체</th>
      <th>체크카드</th>
      <th>출금이체</th>
      <th>카드</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>16151359.4</td>
      <td>87232.6</td>
      <td>82357.5</td>
      <td>4875.1</td>
      <td>16083156.8</td>
      <td>19960.4</td>
      <td>68202.6</td>
      <td>107565.4</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>13984292.3</td>
      <td>80913.3</td>
      <td>76358.9</td>
      <td>4554.4</td>
      <td>13913545.8</td>
      <td>19531</td>
      <td>70746.4</td>
      <td>100904.8</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>15189136.8</td>
      <td>86623.8</td>
      <td>81835.6</td>
      <td>4788.2</td>
      <td>15118696.4</td>
      <td>20866.5</td>
      <td>70440.4</td>
      <td>107924.1</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>15880250.1</td>
      <td>86930.2</td>
      <td>82173.5</td>
      <td>4756.8</td>
      <td>15812195.5</td>
      <td>20834.3</td>
      <td>68054.6</td>
      <td>108115.6</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>14731347.5</td>
      <td>89871.1</td>
      <td>84983</td>
      <td>4888.2</td>
      <td>14662583.6</td>
      <td>21764.6</td>
      <td>68763.9</td>
      <td>111981</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>14696088.4</td>
      <td>87217</td>
      <td>82510.9</td>
      <td>4706.1</td>
      <td>14630123.2</td>
      <td>20697.2</td>
      <td>65965.1</td>
      <td>108241.6</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>17159983</td>
      <td>90054.6</td>
      <td>85128.4</td>
      <td>4926.2</td>
      <td>17089982.8</td>
      <td>21272.4</td>
      <td>70000.2</td>
      <td>111653</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>15436797.1</td>
      <td>88499</td>
      <td>83608.9</td>
      <td>4890.1</td>
      <td>15367912.7</td>
      <td>21442.2</td>
      <td>68884.4</td>
      <td>110273.3</td>
    </tr>
  </tbody>
</table>
</div>



```python
# M0 (본원통화) 데이터를 반환
m0_df = ecos_data_reader.monetary_data_reader.get_m0_df(start_date,end_date)
print('M0 (본원통화) 데이터를 반환')
display(m0_df)

# M1 (협의통화) 데이터를 반환
m1_df = ecos_data_reader.monetary_data_reader.get_m1_df(start_date,end_date)
print('M1 (협의통화) 데이터를 반환')
display(m1_df)

# M2 (광의통화) 데이터를 반환
m2_df = ecos_data_reader.monetary_data_reader.get_m2_df(start_date,end_date)
print('M2 (광의통화) 데이터를 반환')
display(m2_df)

# M2 비율 데이터를 반환
m2_ratio_df = ecos_data_reader.monetary_data_reader.get_m2_ratio_df(start_date,end_date)
print('M2 비율 데이터를 반환')
display(m2_ratio_df)
```

    M0 (본원통화) 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>본원_평잔_원계열</th>
      <th>본원_평잔_계절조정</th>
      <th>본원_말잔_원계열</th>
      <th>본원_말잔_계절조정</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>264131.8</td>
      <td>266647.2</td>
      <td>269093.6</td>
      <td>276191.6</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>268145.7</td>
      <td>266089.7</td>
      <td>270376.7</td>
      <td>262939.4</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>268754.8</td>
      <td>269229.1</td>
      <td>279877.8</td>
      <td>277038.7</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>266890.8</td>
      <td>269227.9</td>
      <td>268507.5</td>
      <td>268784.8</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>270118.9</td>
      <td>270799.6</td>
      <td>277730.5</td>
      <td>277993.1</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>269488.6</td>
      <td>267248.8</td>
      <td>285032.5</td>
      <td>278969.2</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>273888.2</td>
      <td>273108.2</td>
      <td>268519.7</td>
      <td>278552.2</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>272576.4</td>
      <td>272190</td>
      <td>284296.6</td>
      <td>279263.9</td>
    </tr>
    <tr>
      <th>202409</th>
      <td>274793.7</td>
      <td>272480.2</td>
      <td>282293.9</td>
      <td>277509.6</td>
    </tr>
  </tbody>
</table>
</div>


    M1 (협의통화) 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M1_평잔_원계열</th>
      <th>M1_평잔_계절조정</th>
      <th>M1_말잔_원계열</th>
      <th>M1_말잔_계절조정</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>1204441.4</td>
      <td>1221110</td>
      <td>1194126.4</td>
      <td>1223535.4</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>1208167.1</td>
      <td>1217657.3</td>
      <td>1231111.7</td>
      <td>1233052.5</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>1242708.5</td>
      <td>1244401.2</td>
      <td>1275823.2</td>
      <td>1263441.2</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>1241048.6</td>
      <td>1234805.6</td>
      <td>1222260.1</td>
      <td>1224278.2</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>1225588.3</td>
      <td>1221570.3</td>
      <td>1228881.1</td>
      <td>1225491.1</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>1232864.3</td>
      <td>1220524.7</td>
      <td>1266760.1</td>
      <td>1229771.1</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>1229849.5</td>
      <td>1216576.2</td>
      <td>1221205.9</td>
      <td>1227490.1</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>1221016.4</td>
      <td>1217831.6</td>
      <td>1231616.6</td>
      <td>1229276.8</td>
    </tr>
    <tr>
      <th>202409</th>
      <td>1232880.2</td>
      <td>1224666.3</td>
      <td>1245848.9</td>
      <td>1240052.1</td>
    </tr>
  </tbody>
</table>
</div>


    M2 (광의통화) 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M2_평잔_원계열</th>
      <th>M2_평잔_계절조정</th>
      <th>M2_말잔_원계열</th>
      <th>M2_말잔_계절조정</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>3909835.3</td>
      <td>3924203.2</td>
      <td>3903018.5</td>
      <td>3914860.5</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>3937145.6</td>
      <td>3929858</td>
      <td>3967852</td>
      <td>3954147.7</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>4000898.1</td>
      <td>3996216.6</td>
      <td>4014175.2</td>
      <td>4006388.9</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>4011114.1</td>
      <td>4013228.2</td>
      <td>3971094.3</td>
      <td>3987422</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>4008655.8</td>
      <td>4014130.8</td>
      <td>4009360.8</td>
      <td>4017989.2</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>4034006.7</td>
      <td>4037580.8</td>
      <td>4040147.1</td>
      <td>4027787.4</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>4059021.9</td>
      <td>4054967.4</td>
      <td>4042364.7</td>
      <td>4061527.4</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>4065009.9</td>
      <td>4062635.6</td>
      <td>4072330.6</td>
      <td>4065280.5</td>
    </tr>
    <tr>
      <th>202409</th>
      <td>4078455.9</td>
      <td>4070711</td>
      <td>4076483</td>
      <td>4084611.5</td>
    </tr>
  </tbody>
</table>
</div>


    M2 비율 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>M2_가계_비영리단체</th>
      <th>M2_기업</th>
      <th>M2_기타_금융기관</th>
      <th>M2_기타</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>2022838.9</td>
      <td>1097138.1</td>
      <td>582901.6</td>
      <td>200139.9</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>2064309.1</td>
      <td>1092282.7</td>
      <td>585563</td>
      <td>225697.2</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>2096486.4</td>
      <td>1121640.9</td>
      <td>580681.3</td>
      <td>215366.5</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>2087824.7</td>
      <td>1087490.7</td>
      <td>584852.7</td>
      <td>210926.2</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>2100289.8</td>
      <td>1100476.2</td>
      <td>593351.2</td>
      <td>215243.6</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>2121709.7</td>
      <td>1122811.5</td>
      <td>590682.7</td>
      <td>204943.3</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>2117939.5</td>
      <td>1122833.1</td>
      <td>600327.9</td>
      <td>201264.2</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>2124097.6</td>
      <td>1125109.1</td>
      <td>608236.7</td>
      <td>214887.2</td>
    </tr>
    <tr>
      <th>202409</th>
      <td>2126980.4</td>
      <td>1125432.4</td>
      <td>617428.9</td>
      <td>206641.3</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 소비자물가지수(CPI) 데이터를 반환
cpi_df = ecos_data_reader.price_index_data_reader.get_cpi_df(start_date,end_date)
print('소비자물가지수(CPI) 데이터를 반환')
display(cpi_df.head())

# 생산자물가지수(PPI) 데이터를 반환
ppi_df = ecos_data_reader.price_index_data_reader.get_ppi_df(start_date,end_date)
print('생산자물가지수(PPI) 데이터를 반환')
display(ppi_df.head())

# 수입 물가지수 데이터를 반환
import_pi_df = ecos_data_reader.price_index_data_reader.get_import_pi_df(start_date,end_date)
print('수입 물가지수 데이터를 반환')
display(import_pi_df.head())

# 수출 물가지수 데이터를 반환
export_pi_df = ecos_data_reader.price_index_data_reader.get_export_pi_df(start_date,end_date)
print('수출 물가지수 데이터를 반환')
display(export_pi_df.head())

# 주택 가격 데이터를 반환
housing_price_df = ecos_data_reader.price_index_data_reader.get_housing_price_df(start_date,end_date)
print('주택 가격 데이터를 반환')
display(housing_price_df.head())

```

    소비자물가지수(CPI) 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>가정용품 및 가사 서비스</th>
      <th>교육</th>
      <th>교통</th>
      <th>기타 상품 및 서비스</th>
      <th>보건</th>
      <th>식료품 및 비주류음료</th>
      <th>오락 및 문화</th>
      <th>음식 및 숙박</th>
      <th>의류 및 신발</th>
      <th>주류 및 담배</th>
      <th>주택, 수도, 전기 및 연료</th>
      <th>총지수</th>
      <th>통신</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>113.74</td>
      <td>104.96</td>
      <td>111.97</td>
      <td>118.38</td>
      <td>103.98</td>
      <td>122.2</td>
      <td>107.35</td>
      <td>119.09</td>
      <td>113.61</td>
      <td>104.4</td>
      <td>113.84</td>
      <td>113.17</td>
      <td>101.24</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>113.94</td>
      <td>105.09</td>
      <td>113.64</td>
      <td>118.25</td>
      <td>104.06</td>
      <td>123.96</td>
      <td>108.41</td>
      <td>119.39</td>
      <td>113.63</td>
      <td>104.33</td>
      <td>114.22</td>
      <td>113.78</td>
      <td>101.24</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>114.69</td>
      <td>105.43</td>
      <td>114</td>
      <td>118.49</td>
      <td>104.25</td>
      <td>124.22</td>
      <td>107.96</td>
      <td>119.78</td>
      <td>113.65</td>
      <td>104.43</td>
      <td>114.11</td>
      <td>113.95</td>
      <td>101.24</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>114.7</td>
      <td>105.76</td>
      <td>115.02</td>
      <td>119.14</td>
      <td>104.26</td>
      <td>122.75</td>
      <td>108.45</td>
      <td>120.14</td>
      <td>113.59</td>
      <td>104.7</td>
      <td>114.15</td>
      <td>114.01</td>
      <td>101.24</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>114.48</td>
      <td>105.9</td>
      <td>115.74</td>
      <td>119.13</td>
      <td>104.52</td>
      <td>121.9</td>
      <td>108.81</td>
      <td>120.38</td>
      <td>114.3</td>
      <td>104.46</td>
      <td>114.26</td>
      <td>114.1</td>
      <td>101.32</td>
    </tr>
  </tbody>
</table>
</div>


    생산자물가지수(PPI) 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>공산품</th>
      <th>광산품</th>
      <th>농림수산품</th>
      <th>서비스</th>
      <th>전력,가스,수도및폐기물</th>
      <th>총지수</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>122.13</td>
      <td>135.42</td>
      <td>121.18</td>
      <td>109.5</td>
      <td>144.76</td>
      <td>118.19</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>122.76</td>
      <td>136.2</td>
      <td>121.96</td>
      <td>109.71</td>
      <td>143.51</td>
      <td>118.55</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>123.09</td>
      <td>135.82</td>
      <td>123.49</td>
      <td>109.79</td>
      <td>143.92</td>
      <td>118.82</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>123.97</td>
      <td>136.48</td>
      <td>119.75</td>
      <td>110</td>
      <td>143.01</td>
      <td>119.16</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>123.97</td>
      <td>135.38</td>
      <td>114.93</td>
      <td>110.55</td>
      <td>143.63</td>
      <td>119.25</td>
    </tr>
  </tbody>
</table>
</div>


    수입 물가지수 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>공산품</th>
      <th>광산품</th>
      <th>농림수산품</th>
      <th>총지수</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>108.25</td>
      <td>167.46</td>
      <td>111.5</td>
      <td>121.42</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>108.14</td>
      <td>170.02</td>
      <td>111.53</td>
      <td>121.87</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>108.57</td>
      <td>171.73</td>
      <td>111.64</td>
      <td>122.57</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>108.83</td>
      <td>176.27</td>
      <td>113.05</td>
      <td>123.79</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>108.69</td>
      <td>170.55</td>
      <td>112.33</td>
      <td>122.44</td>
    </tr>
  </tbody>
</table>
</div>


    수출 물가지수 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>공산품</th>
      <th>농림수산품</th>
      <th>총지수</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>111.08</td>
      <td>95.46</td>
      <td>111</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>112.14</td>
      <td>94.68</td>
      <td>112.05</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>112.59</td>
      <td>91.92</td>
      <td>112.48</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>114.39</td>
      <td>87.25</td>
      <td>114.26</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>113.92</td>
      <td>88.62</td>
      <td>113.8</td>
    </tr>
  </tbody>
</table>
</div>


    주택 가격 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>단독주택</th>
      <th>아파트</th>
      <th>아파트(서울)</th>
      <th>연립주택</th>
      <th>총지수</th>
      <th>총지수(서울)</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>100.75</td>
      <td>89.94</td>
      <td>90.551</td>
      <td>101.302</td>
      <td>93.24</td>
      <td>94.76</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>100.752</td>
      <td>89.842</td>
      <td>90.442</td>
      <td>101.273</td>
      <td>93.167</td>
      <td>94.719</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>100.761</td>
      <td>89.698</td>
      <td>90.308</td>
      <td>101.278</td>
      <td>93.068</td>
      <td>94.664</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>100.769</td>
      <td>89.503</td>
      <td>90.158</td>
      <td>101.284</td>
      <td>93.038</td>
      <td>94.681</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>100.796</td>
      <td>89.387</td>
      <td>90.13</td>
      <td>101.294</td>
      <td>92.961</td>
      <td>94.685</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 주택 정보 데이터를 반환
house_info_df =ecos_data_reader.economic_index_data_reader.get_house_info_df(start_date,end_date)
print('주택 정보 데이터를 반환')
display(house_info_df.head())

# 거시경제지수 데이터를 반환
macro_economic_index_df =ecos_data_reader.economic_index_data_reader.get_macro_economic_index_df(start_date,end_date)
print('거시경제지수 데이터를 반환')
display(macro_economic_index_df.head())

# 실업 수당 취득자 수를 반환
unemployment_cnt_df =ecos_data_reader.economic_index_data_reader.get_unemployment_cnt_df(start_date,end_date)
print('실업 수당 취득자 수를 반환')
display(unemployment_cnt_df.head())

# 실업 수당 가격 데이터를 반환
unemployment_won_dfstart_date =ecos_data_reader.economic_index_data_reader.get_unemployment_won_df(start_date,end_date)
print('실업 수당 가격 데이터를 반환')
display(unemployment_won_dfstart_date.head())
```

    주택 정보 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>미분양_서울</th>
      <th>미분양_전국</th>
      <th>건축허가_용도별</th>
      <th>건축허가_주거용</th>
      <th>건축허가_상업용</th>
      <th>건축착공_용도별</th>
      <th>건축착공_주거용</th>
      <th>건축착공_상업용</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>997</td>
      <td>63755</td>
      <td>10779480.94</td>
      <td>3555861.8</td>
      <td>3690196.9</td>
      <td>6013383.22</td>
      <td>2221996.31</td>
      <td>1435771.5</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>1018</td>
      <td>64874</td>
      <td>8350849.79</td>
      <td>2811166.18</td>
      <td>1889347.16</td>
      <td>5778233.1</td>
      <td>2276014.13</td>
      <td>1050379.19</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>968</td>
      <td>64964</td>
      <td>10379723.65</td>
      <td>3984566.62</td>
      <td>2163312.17</td>
      <td>5114385.66</td>
      <td>1256999.31</td>
      <td>1207801.96</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>936</td>
      <td>71997</td>
      <td>10784160.19</td>
      <td>3512744.16</td>
      <td>2532764.12</td>
      <td>7782586.15</td>
      <td>2561547.44</td>
      <td>1870687.11</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>974</td>
      <td>72129</td>
      <td>9233555.63</td>
      <td>3491671.34</td>
      <td>1957247.63</td>
      <td>6603729.34</td>
      <td>2024454.31</td>
      <td>1745049.5</td>
    </tr>
  </tbody>
</table>
</div>


    거시경제지수 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>경기종합지수</th>
      <th>설비투자지수</th>
      <th>생산자제품 재고지수(원지수)</th>
      <th>생산자제품 출하지수(원지수)</th>
      <th>생산지수(원지수)</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>111.5</td>
      <td>100.6</td>
      <td>111.6</td>
      <td>105.4</td>
      <td>109.4</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>112</td>
      <td>97.6</td>
      <td>114.1</td>
      <td>97.1</td>
      <td>100.8</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>111.9</td>
      <td>110</td>
      <td>110</td>
      <td>108.7</td>
      <td>112.3</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>112</td>
      <td>110.1</td>
      <td>112.1</td>
      <td>103.6</td>
      <td>109.6</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>111.6</td>
      <td>107.1</td>
      <td>112.2</td>
      <td>105.8</td>
      <td>112</td>
    </tr>
  </tbody>
</table>
</div>


    실업 수당 취득자 수를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>가구 내 고용활동 및 달리 분류되지 않은 자가소비 생산활동</th>
      <th>건설업</th>
      <th>공공행정, 국방 및 사회보장 행정</th>
      <th>광업</th>
      <th>교육 서비스업</th>
      <th>국제 및 외국기관</th>
      <th>금융 및 보험업</th>
      <th>농업, 임업 및 어업</th>
      <th>도매 및 소매업</th>
      <th>보건업 및 사회복지 서비스업</th>
      <th>...</th>
      <th>수도, 하수 및 폐기물 처리, 원료 재생업</th>
      <th>숙박 및 음식점업</th>
      <th>예술, 스포츠 및 여가관련 서비스업</th>
      <th>운수 및 창고업</th>
      <th>전기, 가스, 증기 및 공기조절 공급업</th>
      <th>전문, 과학 및 기술 서비스업</th>
      <th>정보통신업</th>
      <th>제조업</th>
      <th>합계</th>
      <th>협회 및 단체, 수리 및 기타 개인 서비스업</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>2</td>
      <td>65739</td>
      <td>43017</td>
      <td>489</td>
      <td>29806</td>
      <td>246</td>
      <td>11343</td>
      <td>2939</td>
      <td>67573</td>
      <td>71502</td>
      <td>...</td>
      <td>3620</td>
      <td>42835</td>
      <td>10623</td>
      <td>22476</td>
      <td>1148</td>
      <td>29925</td>
      <td>26240</td>
      <td>101676</td>
      <td>628872</td>
      <td>13434</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>1</td>
      <td>67869</td>
      <td>43991</td>
      <td>446</td>
      <td>27853</td>
      <td>227</td>
      <td>12383</td>
      <td>3025</td>
      <td>66134</td>
      <td>72170</td>
      <td>...</td>
      <td>3792</td>
      <td>42023</td>
      <td>11368</td>
      <td>23285</td>
      <td>1095</td>
      <td>30778</td>
      <td>26948</td>
      <td>104986</td>
      <td>641145</td>
      <td>14065</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>2</td>
      <td>70377</td>
      <td>41647</td>
      <td>448</td>
      <td>35119</td>
      <td>240</td>
      <td>13646</td>
      <td>2977</td>
      <td>67049</td>
      <td>90128</td>
      <td>...</td>
      <td>3840</td>
      <td>42516</td>
      <td>11586</td>
      <td>23534</td>
      <td>1143</td>
      <td>31449</td>
      <td>27872</td>
      <td>105846</td>
      <td>673054</td>
      <td>14239</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>2</td>
      <td>69834</td>
      <td>34818</td>
      <td>429</td>
      <td>37155</td>
      <td>257</td>
      <td>14173</td>
      <td>2998</td>
      <td>69145</td>
      <td>96797</td>
      <td>...</td>
      <td>3680</td>
      <td>43325</td>
      <td>10608</td>
      <td>23882</td>
      <td>1342</td>
      <td>31817</td>
      <td>28829</td>
      <td>107066</td>
      <td>680322</td>
      <td>14145</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>1</td>
      <td>68851</td>
      <td>30025</td>
      <td>332</td>
      <td>35229</td>
      <td>261</td>
      <td>13899</td>
      <td>2842</td>
      <td>69157</td>
      <td>95824</td>
      <td>...</td>
      <td>3448</td>
      <td>42942</td>
      <td>9441</td>
      <td>23486</td>
      <td>1232</td>
      <td>30953</td>
      <td>28590</td>
      <td>105342</td>
      <td>663801</td>
      <td>13669</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>


    실업 수당 가격 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>가구 내 고용활동 및 달리 분류되지 않은 자가소비 생산활동</th>
      <th>건설업</th>
      <th>공공행정, 국방 및 사회보장 행정</th>
      <th>광업</th>
      <th>교육 서비스업</th>
      <th>국제 및 외국기관</th>
      <th>금융 및 보험업</th>
      <th>농업, 임업 및 어업</th>
      <th>도매 및 소매업</th>
      <th>보건업 및 사회복지 서비스업</th>
      <th>...</th>
      <th>수도, 하수 및 폐기물 처리, 원료 재생업</th>
      <th>숙박 및 음식점업</th>
      <th>예술, 스포츠 및 여가관련 서비스업</th>
      <th>운수 및 창고업</th>
      <th>전기, 가스, 증기 및 공기조절 공급업</th>
      <th>전문, 과학 및 기술 서비스업</th>
      <th>정보통신업</th>
      <th>제조업</th>
      <th>합계</th>
      <th>협회 및 단체, 수리 및 기타 개인 서비스업</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>2767080</td>
      <td>116704769850</td>
      <td>52465930590</td>
      <td>987293300</td>
      <td>41001720950</td>
      <td>478085740</td>
      <td>18034340690</td>
      <td>4413018700</td>
      <td>113387448150</td>
      <td>105026372880</td>
      <td>...</td>
      <td>5512614820</td>
      <td>69482824410</td>
      <td>14482809200</td>
      <td>36696157660</td>
      <td>1901490100</td>
      <td>47969678060</td>
      <td>42750123790</td>
      <td>171029385700</td>
      <td>988437357110</td>
      <td>19383362490</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>1848000</td>
      <td>118043404200</td>
      <td>66290897930</td>
      <td>830841350</td>
      <td>39994454060</td>
      <td>372454000</td>
      <td>19803594630</td>
      <td>4978121140</td>
      <td>104312842680</td>
      <td>106987061290</td>
      <td>...</td>
      <td>6238213650</td>
      <td>63771118140</td>
      <td>17314771260</td>
      <td>37491763040</td>
      <td>1911588470</td>
      <td>49893913830</td>
      <td>42849073970</td>
      <td>177129918040</td>
      <td>1017507591030</td>
      <td>21398484470</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>2094270</td>
      <td>119957479110</td>
      <td>62634703270</td>
      <td>798724650</td>
      <td>40376337560</td>
      <td>399624480</td>
      <td>22074869630</td>
      <td>4697931310</td>
      <td>104309177920</td>
      <td>115603772640</td>
      <td>...</td>
      <td>6390990280</td>
      <td>63164596510</td>
      <td>17544707020</td>
      <td>38126960320</td>
      <td>2050076130</td>
      <td>50182520750</td>
      <td>43905022030</td>
      <td>179663463950</td>
      <td>1035491237530</td>
      <td>21910423440</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>3369950</td>
      <td>124689318890</td>
      <td>54149846380</td>
      <td>790191860</td>
      <td>54843618310</td>
      <td>478672640</td>
      <td>24969668240</td>
      <td>4513993730</td>
      <td>112554500210</td>
      <td>147487973340</td>
      <td>...</td>
      <td>6532251180</td>
      <td>67724471950</td>
      <td>16817587600</td>
      <td>40356518230</td>
      <td>2356417160</td>
      <td>53577430020</td>
      <td>48050413380</td>
      <td>189957530820</td>
      <td>1121645414680</td>
      <td>22536230910</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>861950</td>
      <td>126612795180</td>
      <td>47112744440</td>
      <td>596314720</td>
      <td>59272913910</td>
      <td>458950490</td>
      <td>25544775200</td>
      <td>4778455820</td>
      <td>116260427510</td>
      <td>155587937500</td>
      <td>...</td>
      <td>6185187120</td>
      <td>69656370900</td>
      <td>15701389490</td>
      <td>40701902830</td>
      <td>2676525850</td>
      <td>54184136220</td>
      <td>48811956260</td>
      <td>192698917880</td>
      <td>1140702225430</td>
      <td>22748586810</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 23 columns</p>
</div>



```python
# 주요국 소비자물가지수(CPI) 데이터를 반환
global_cpi_df = ecos_data_reader.global_index_data_reader.get_global_cpi_df(start_date,end_date)
print('주요국 소비자물가지수(CPI) 데이터를 반환')
display(global_cpi_df)

# 주요국 생산자물가지수(PPI) 데이터를 반환
global_ppi_df = ecos_data_reader.global_index_data_reader.get_global_ppi_df(start_date,end_date)
print('주요국 생산자물가지수(PPI) 데이터를 반환')
display(global_ppi_df)

# 주요국 금리 데이터를 반환
global_interest_df = ecos_data_reader.global_index_data_reader.get_global_interest_df(start_date,end_date)
print('주요국 금리 데이터를 반환')
display(global_interest_df)

# 주요국 장기 금리 데이터를 반환
global_long_interest_df = ecos_data_reader.global_index_data_reader.get_global_long_interest_df(start_date,end_date)
print('주요국 장기 금리 데이터를 반환')
display(global_long_interest_df)

# 주요국 단기 금리 데이터를 반환
global_short_interest_df = ecos_data_reader.global_index_data_reader.get_global_short_interest_df(start_date,end_date)
print('주요국 단기 금리 데이터를 반환')
display(global_short_interest_df)
```

    주요국 소비자물가지수(CPI) 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>미국</th>
      <th>일본</th>
      <th>중국</th>
      <th>한국</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>141.44</td>
      <td>112.74</td>
      <td>132.17</td>
      <td>131.03</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>142.32</td>
      <td>112.74</td>
      <td>133.58</td>
      <td>131.73</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>143.24</td>
      <td>113.06</td>
      <td>132.42</td>
      <td>131.93</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>143.79</td>
      <td>113.59</td>
      <td>132.29</td>
      <td>132</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>144.03</td>
      <td>114.01</td>
      <td>132.29</td>
      <td>132.1</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>144.08</td>
      <td>114.11</td>
      <td>131.91</td>
      <td>131.8</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>144.25</td>
      <td>114.54</td>
      <td>132.55</td>
      <td>132.14</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>144.37</td>
      <td>115.06</td>
      <td>133.06</td>
      <td>132.61</td>
    </tr>
    <tr>
      <th>202409</th>
      <td>144.6</td>
      <td>114.85</td>
      <td>133.06</td>
      <td>132.74</td>
    </tr>
    <tr>
      <th>202410</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>132.79</td>
    </tr>
  </tbody>
</table>
</div>


    주요국 생산자물가지수(PPI) 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>미국</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>138.58</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>139.63</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>140.02</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>140.77</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>140.67</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>141.22</td>
    </tr>
  </tbody>
</table>
</div>


    주요국 금리 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>미국</th>
      <th>유로 지역</th>
      <th>일본</th>
      <th>한국</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>5.375</td>
      <td>4.5</td>
      <td>-0.1</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>5.375</td>
      <td>4.5</td>
      <td>-0.1</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>5.375</td>
      <td>4.5</td>
      <td>0.05</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>5.375</td>
      <td>4.5</td>
      <td>0.05</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>5.375</td>
      <td>4.5</td>
      <td>0.05</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>5.375</td>
      <td>4.25</td>
      <td>0.05</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>5.375</td>
      <td>4.25</td>
      <td>0.05</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>5.375</td>
      <td>4.25</td>
      <td>0.25</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>202409</th>
      <td>4.875</td>
      <td>3.5</td>
      <td>0.25</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>202410</th>
      <td>4.875</td>
      <td>3.25</td>
      <td>0.25</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>


    주요국 장기 금리 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>남아프리카 공화국</th>
      <th>노르웨이</th>
      <th>뉴질랜드</th>
      <th>덴마크</th>
      <th>독일</th>
      <th>멕시코</th>
      <th>미국</th>
      <th>브라질</th>
      <th>스웨덴</th>
      <th>스위스</th>
      <th>영국</th>
      <th>오스트레일리아</th>
      <th>이탈리아</th>
      <th>인도</th>
      <th>인도네시아</th>
      <th>일본</th>
      <th>중국</th>
      <th>캐나다</th>
      <th>프랑스</th>
      <th>한국</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>11.42</td>
      <td>3.5</td>
      <td>4.65</td>
      <td>2.4</td>
      <td>2.17</td>
      <td>9.31</td>
      <td>4.06</td>
      <td>6.53</td>
      <td>2.23</td>
      <td>0.83</td>
      <td>3.93</td>
      <td>4.15</td>
      <td>3.81</td>
      <td>7.2</td>
      <td>6.56</td>
      <td>0.73</td>
      <td>2.43</td>
      <td>3.35</td>
      <td>2.74</td>
      <td>3.35</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>11.61</td>
      <td>3.7</td>
      <td>4.81</td>
      <td>2.48</td>
      <td>2.33</td>
      <td>NaN</td>
      <td>4.21</td>
      <td>6.53</td>
      <td>2.43</td>
      <td>0.83</td>
      <td>4.12</td>
      <td>4.14</td>
      <td>3.87</td>
      <td>7.09</td>
      <td>6.6</td>
      <td>0.71</td>
      <td>2.34</td>
      <td>3.5</td>
      <td>2.85</td>
      <td>3.43</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>11.9</td>
      <td>3.61</td>
      <td>4.65</td>
      <td>2.39</td>
      <td>2.35</td>
      <td>9.2</td>
      <td>4.21</td>
      <td>6.53</td>
      <td>2.4</td>
      <td>0.64</td>
      <td>4.03</td>
      <td>4.05</td>
      <td>3.7</td>
      <td>7.07</td>
      <td>6.68</td>
      <td>0.73</td>
      <td>2.29</td>
      <td>3.44</td>
      <td>2.82</td>
      <td>3.39</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>12.27</td>
      <td>3.74</td>
      <td>4.83</td>
      <td>2.48</td>
      <td>2.45</td>
      <td>9.85</td>
      <td>4.54</td>
      <td>6.67</td>
      <td>2.51</td>
      <td>0.69</td>
      <td>4.22</td>
      <td>4.27</td>
      <td>3.86</td>
      <td>7.15</td>
      <td>7.22</td>
      <td>0.87</td>
      <td>2.3</td>
      <td>3.7</td>
      <td>2.97</td>
      <td>3.57</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>12.04</td>
      <td>3.68</td>
      <td>4.75</td>
      <td>2.52</td>
      <td>2.52</td>
      <td>9.64</td>
      <td>4.48</td>
      <td>6.67</td>
      <td>2.38</td>
      <td>0.92</td>
      <td>4.22</td>
      <td>4.33</td>
      <td>3.84</td>
      <td>7.05</td>
      <td>6.9</td>
      <td>1.07</td>
      <td>2.29</td>
      <td>3.64</td>
      <td>3.03</td>
      <td>3.53</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>11.68</td>
      <td>3.54</td>
      <td>4.64</td>
      <td>2.52</td>
      <td>2.48</td>
      <td>NaN</td>
      <td>4.31</td>
      <td>6.67</td>
      <td>2.26</td>
      <td>0.56</td>
      <td>4.16</td>
      <td>4.24</td>
      <td>3.94</td>
      <td>7.02</td>
      <td>7.03</td>
      <td>1.05</td>
      <td>2.21</td>
      <td>3.39</td>
      <td>3.15</td>
      <td>3.34</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>11.02</td>
      <td>3.54</td>
      <td>4.51</td>
      <td>2.45</td>
      <td>2.46</td>
      <td>9.95</td>
      <td>4.25</td>
      <td>6.91</td>
      <td>2.13</td>
      <td>0.45</td>
      <td>4.14</td>
      <td>4.33</td>
      <td>3.83</td>
      <td>7.01</td>
      <td>6.89</td>
      <td>1.05</td>
      <td>2.15</td>
      <td>3.41</td>
      <td>3.14</td>
      <td>3.17</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>10.7</td>
      <td>3.3</td>
      <td>4.22</td>
      <td>2.2</td>
      <td>2.21</td>
      <td>9.74</td>
      <td>3.87</td>
      <td>6.91</td>
      <td>1.93</td>
      <td>0.45</td>
      <td>3.94</td>
      <td>3.98</td>
      <td>3.68</td>
      <td>6.91</td>
      <td>6.62</td>
      <td>0.89</td>
      <td>2.17</td>
      <td>3.07</td>
      <td>2.94</td>
      <td>3</td>
    </tr>
    <tr>
      <th>202409</th>
      <td>10.3</td>
      <td>3.3</td>
      <td>4.19</td>
      <td>2.11</td>
      <td>2.17</td>
      <td>9.21</td>
      <td>3.72</td>
      <td>6.91</td>
      <td>1.93</td>
      <td>0.41</td>
      <td>3.91</td>
      <td>3.92</td>
      <td>3.57</td>
      <td>6.83</td>
      <td>6.43</td>
      <td>0.86</td>
      <td>2.15</td>
      <td>2.94</td>
      <td>2.9</td>
      <td>3.01</td>
    </tr>
    <tr>
      <th>202410</th>
      <td>10.46</td>
      <td>3.53</td>
      <td>4.39</td>
      <td>2.1</td>
      <td>2.22</td>
      <td>10.06</td>
      <td>4.1</td>
      <td>7.43</td>
      <td>2.04</td>
      <td>0.45</td>
      <td>4.2</td>
      <td>4.26</td>
      <td>3.5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.94</td>
      <td>NaN</td>
      <td>3.19</td>
      <td>2.99</td>
      <td>3.07</td>
    </tr>
  </tbody>
</table>
</div>


    주요국 단기 금리 데이터를 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>남아프리카 공화국</th>
      <th>노르웨이</th>
      <th>뉴질랜드</th>
      <th>덴마크</th>
      <th>독일</th>
      <th>멕시코</th>
      <th>미국</th>
      <th>스웨덴</th>
      <th>스위스</th>
      <th>영국</th>
      <th>오스트레일리아</th>
      <th>이탈리아</th>
      <th>인도</th>
      <th>인도네시아</th>
      <th>일본</th>
      <th>중국</th>
      <th>캐나다</th>
      <th>프랑스</th>
      <th>한국</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>202401</th>
      <td>8.48</td>
      <td>4.71</td>
      <td>5.64</td>
      <td>3.89</td>
      <td>3.93</td>
      <td>11.66</td>
      <td>5.26</td>
      <td>3.97</td>
      <td>1.69</td>
      <td>5.32</td>
      <td>4.35</td>
      <td>3.93</td>
      <td>6.96</td>
      <td>6.94</td>
      <td>0.03</td>
      <td>2.79</td>
      <td>5.17</td>
      <td>3.93</td>
      <td>3.74</td>
    </tr>
    <tr>
      <th>202402</th>
      <td>8.46</td>
      <td>4.71</td>
      <td>5.71</td>
      <td>3.88</td>
      <td>3.92</td>
      <td>11.65</td>
      <td>5.22</td>
      <td>4.04</td>
      <td>1.7</td>
      <td>5.33</td>
      <td>4.34</td>
      <td>3.92</td>
      <td>7.03</td>
      <td>6.94</td>
      <td>0.03</td>
      <td>2.69</td>
      <td>5.09</td>
      <td>3.92</td>
      <td>3.69</td>
    </tr>
    <tr>
      <th>202403</th>
      <td>8.45</td>
      <td>4.73</td>
      <td>5.64</td>
      <td>3.88</td>
      <td>3.92</td>
      <td>11.61</td>
      <td>5.29</td>
      <td>4.05</td>
      <td>1.5</td>
      <td>5.32</td>
      <td>4.35</td>
      <td>3.92</td>
      <td>6.92</td>
      <td>6.93</td>
      <td>0.11</td>
      <td>2.53</td>
      <td>5.04</td>
      <td>3.92</td>
      <td>3.65</td>
    </tr>
    <tr>
      <th>202404</th>
      <td>8.43</td>
      <td>4.72</td>
      <td>5.63</td>
      <td>3.82</td>
      <td>3.89</td>
      <td>11.41</td>
      <td>5.33</td>
      <td>3.95</td>
      <td>1.5</td>
      <td>5.3</td>
      <td>4.37</td>
      <td>3.89</td>
      <td>6.89</td>
      <td>6.99</td>
      <td>0.11</td>
      <td>2.49</td>
      <td>5.02</td>
      <td>3.89</td>
      <td>3.57</td>
    </tr>
    <tr>
      <th>202405</th>
      <td>8.53</td>
      <td>4.71</td>
      <td>5.62</td>
      <td>3.73</td>
      <td>3.81</td>
      <td>11.4</td>
      <td>5.33</td>
      <td>3.79</td>
      <td>1.5</td>
      <td>5.3</td>
      <td>4.36</td>
      <td>3.81</td>
      <td>6.94</td>
      <td>7.18</td>
      <td>0.13</td>
      <td>2.32</td>
      <td>4.99</td>
      <td>3.81</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>202406</th>
      <td>8.53</td>
      <td>4.73</td>
      <td>5.62</td>
      <td>3.65</td>
      <td>3.72</td>
      <td>11.39</td>
      <td>5.28</td>
      <td>3.68</td>
      <td>1.43</td>
      <td>5.3</td>
      <td>4.39</td>
      <td>3.72</td>
      <td>6.83</td>
      <td>7.18</td>
      <td>0.15</td>
      <td>2.23</td>
      <td>4.83</td>
      <td>3.72</td>
      <td>3.6</td>
    </tr>
    <tr>
      <th>202407</th>
      <td>8.45</td>
      <td>4.76</td>
      <td>5.55</td>
      <td>3.59</td>
      <td>3.68</td>
      <td>11.4</td>
      <td>5.31</td>
      <td>3.58</td>
      <td>1.19</td>
      <td>5.3</td>
      <td>4.46</td>
      <td>3.68</td>
      <td>6.75</td>
      <td>7.18</td>
      <td>0.17</td>
      <td>2.21</td>
      <td>4.7</td>
      <td>3.68</td>
      <td>3.54</td>
    </tr>
    <tr>
      <th>202408</th>
      <td>8.23</td>
      <td>4.74</td>
      <td>5.3</td>
      <td>3.45</td>
      <td>3.55</td>
      <td>11.23</td>
      <td>5.12</td>
      <td>3.37</td>
      <td>1.07</td>
      <td>5.3</td>
      <td>4.38</td>
      <td>3.55</td>
      <td>6.64</td>
      <td>7.18</td>
      <td>0.26</td>
      <td>2.04</td>
      <td>4.23</td>
      <td>3.55</td>
      <td>3.5</td>
    </tr>
    <tr>
      <th>202409</th>
      <td>8.1</td>
      <td>4.73</td>
      <td>5.05</td>
      <td>3.34</td>
      <td>3.43</td>
      <td>11.14</td>
      <td>4.86</td>
      <td>3.14</td>
      <td>1.02</td>
      <td>5.3</td>
      <td>4.42</td>
      <td>3.43</td>
      <td>6.64</td>
      <td>7.08</td>
      <td>0.26</td>
      <td>2.06</td>
      <td>4.04</td>
      <td>3.43</td>
      <td>3.52</td>
    </tr>
    <tr>
      <th>202410</th>
      <td>8</td>
      <td>4.7</td>
      <td>4.65</td>
      <td>3.08</td>
      <td>3.17</td>
      <td>10.89</td>
      <td>4.62</td>
      <td>2.92</td>
      <td>0.9</td>
      <td>5.3</td>
      <td>4.41</td>
      <td>3.17</td>
      <td>NaN</td>
      <td>6.92</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3.71</td>
      <td>3.17</td>
      <td>3.43</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 외환 데이터를 반환
foreign_currency_df = ecos_data_reader.foreign_currency_data_reader.get_foreign_currency_df(start_date,end_date)
print('외환데이터 반환')
display(foreign_currency_df.head())

```

    외환데이터 반환



<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>원_달러</th>
      <th>원_엔</th>
      <th>원_유로</th>
      <th>원_위안</th>
    </tr>
    <tr>
      <th>TIME</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>20240102</th>
      <td>1289.4</td>
      <td>915.6</td>
      <td>1423.63</td>
      <td>180.84</td>
    </tr>
    <tr>
      <th>20240103</th>
      <td>1299.3</td>
      <td>914.55</td>
      <td>1421.82</td>
      <td>182.63</td>
    </tr>
    <tr>
      <th>20240104</th>
      <td>1308.8</td>
      <td>914.76</td>
      <td>1429.86</td>
      <td>183.19</td>
    </tr>
    <tr>
      <th>20240105</th>
      <td>1310.2</td>
      <td>905.68</td>
      <td>1434.28</td>
      <td>182.94</td>
    </tr>
    <tr>
      <th>20240108</th>
      <td>1313.7</td>
      <td>907.47</td>
      <td>1437.19</td>
      <td>183</td>
    </tr>
  </tbody>
</table>
</div>



```python

```
