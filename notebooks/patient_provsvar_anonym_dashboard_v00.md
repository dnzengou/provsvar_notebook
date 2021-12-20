source:
- [voila]()
- [gallery](https://voila-gallery.org/)
- [web]()

# Patient provsvar anonym resultat

## Intro
### Why

> ...`

![SU Image](https://static.nichehuset.dk/annoncer/jobannoncer/images/annoncoerer/logoer/2123/1322.png)


```python
!pip install seaborn
```

    Requirement already satisfied: seaborn in c:\users\dsinz1\anaconda3\lib\site-packages (0.11.1)
    Requirement already satisfied: numpy>=1.15 in c:\users\dsinz1\anaconda3\lib\site-packages (from seaborn) (1.20.1)
    Requirement already satisfied: matplotlib>=2.2 in c:\users\dsinz1\anaconda3\lib\site-packages (from seaborn) (3.3.4)
    Requirement already satisfied: scipy>=1.0 in c:\users\dsinz1\anaconda3\lib\site-packages (from seaborn) (1.6.2)
    Requirement already satisfied: pandas>=0.23 in c:\users\dsinz1\anaconda3\lib\site-packages (from seaborn) (1.2.4)
    Requirement already satisfied: cycler>=0.10 in c:\users\dsinz1\anaconda3\lib\site-packages (from matplotlib>=2.2->seaborn) (0.10.0)
    Requirement already satisfied: kiwisolver>=1.0.1 in c:\users\dsinz1\anaconda3\lib\site-packages (from matplotlib>=2.2->seaborn) (1.3.1)
    Requirement already satisfied: pillow>=6.2.0 in c:\users\dsinz1\anaconda3\lib\site-packages (from matplotlib>=2.2->seaborn) (8.2.0)
    Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.3 in c:\users\dsinz1\anaconda3\lib\site-packages (from matplotlib>=2.2->seaborn) (2.4.7)
    Requirement already satisfied: python-dateutil>=2.1 in c:\users\dsinz1\anaconda3\lib\site-packages (from matplotlib>=2.2->seaborn) (2.8.1)
    Requirement already satisfied: six in c:\users\dsinz1\anaconda3\lib\site-packages (from cycler>=0.10->matplotlib>=2.2->seaborn) (1.15.0)
    Requirement already satisfied: pytz>=2017.3 in c:\users\dsinz1\anaconda3\lib\site-packages (from pandas>=0.23->seaborn) (2021.1)
    


```python
# importing libraries

from __future__ import print_function
from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.core.display import display, HTML

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import folium
import plotly.graph_objects as go
import seaborn as sns
import ipywidgets as widgets
```


```python
data1 = pd.read_csv("https://raw.githubusercontent.com/dnzengou/provsvar_visu/main/assets/data/provsvar_sept_anonym_122021-Blad11_mal_full.csv")

data1.head()
```




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
      <th>Personnummer</th>
      <th>ProvsvarsDate</th>
      <th>provsvar 1</th>
      <th>värde 1</th>
      <th>bedömning 1</th>
      <th>provsvar 2</th>
      <th>värde 2</th>
      <th>bedömning 2</th>
      <th>provsvar 3</th>
      <th>värde 3</th>
      <th>bedömning 3</th>
      <th>provsvar 4</th>
      <th>värde 4</th>
      <th>bedömning 4</th>
      <th>provsvar 5</th>
      <th>värde 5</th>
      <th>bedömning 5</th>
      <th>Total bedomning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8201113227</td>
      <td>19-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.0</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.7</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.44</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.24</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8201113245</td>
      <td>13-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>13</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.0</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>2.3</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.80</td>
      <td>GUL</td>
      <td>ALAT, P-</td>
      <td>0.92</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8201113242</td>
      <td>14-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>13</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.3</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>2.3</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.79</td>
      <td>GUL</td>
      <td>ALAT, P-</td>
      <td>0.92</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8201113206</td>
      <td>26-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.2</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.4</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.40</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.18</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8201113239</td>
      <td>15-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.2</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.8</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.44</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.24</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
  </tbody>
</table>
</div>




```python
# data cleaning

# renaming the df column names to lowercase
data1.columns = map(str.lower, data1.columns)

data1.head()
```




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
      <th>personnummer</th>
      <th>provsvarsdate</th>
      <th>provsvar 1</th>
      <th>värde 1</th>
      <th>bedömning 1</th>
      <th>provsvar 2</th>
      <th>värde 2</th>
      <th>bedömning 2</th>
      <th>provsvar 3</th>
      <th>värde 3</th>
      <th>bedömning 3</th>
      <th>provsvar 4</th>
      <th>värde 4</th>
      <th>bedömning 4</th>
      <th>provsvar 5</th>
      <th>värde 5</th>
      <th>bedömning 5</th>
      <th>total bedomning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8201113227</td>
      <td>19-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.0</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.7</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.44</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.24</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8201113245</td>
      <td>13-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>13</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.0</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>2.3</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.80</td>
      <td>GUL</td>
      <td>ALAT, P-</td>
      <td>0.92</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8201113242</td>
      <td>14-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>13</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.3</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>2.3</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.79</td>
      <td>GUL</td>
      <td>ALAT, P-</td>
      <td>0.92</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8201113206</td>
      <td>26-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.2</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.4</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.40</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.18</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8201113239</td>
      <td>15-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.2</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.8</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.44</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.24</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(data1.columns)
```

    Index(['personnummer', 'provsvarsdate', 'provsvar 1', 'värde 1', 'bedömning 1',
           'provsvar 2', 'värde 2', 'bedömning 2', 'provsvar 3', 'värde 3',
           'bedömning 3', 'provsvar 4', 'värde 4', 'bedömning 4', 'provsvar 5',
           'värde 5', 'bedömning 5', 'total bedomning'],
          dtype='object')
    


```python
data1.rename(columns = {'provsvar 1':'provsvar1', 'provsvar 2':'provsvar2', 'provsvar 3':'provsvar3', 'provsvar 4':'provsvar4', 'provsvar 5':'provsvar5', 'provsvar 6':'provsvar6', 'värde 1':'varde1', 'värde 2':'varde2', 'värde 3':'varde3', 'värde 4':'varde4', 'värde 5':'varde5',
                              'värde 6':'varde6', 'bedömning 1':'bedomning1', 'bedömning 2':'bedomning2', 'bedömning 3':'bedomning3', 'bedömning 4':'bedomning4', 'bedömning 5':'bedomning5', 'total bedomning':'total_bedomning'}, inplace = True)
#df1 = data1.rename(columns = {'total bedomning':'total_bedomning'}, inplace = True)

```


```python
# total number of confirmed, death and recovered cases
data1_total = int(data1['total_bedomning'].count())

data1_total
```




    40




```python
# counting unique values
n = len(pd.unique(data1['total_bedomning']))
  
print("No.of.unique values :", 
      n)
```

    No.of.unique values : 3
    


```python
data1_mean_varde1 = int(data1['varde1'].mean())

data1_mean_varde1
```




    14




```python
data1_mean_varde2 = int(data1['varde2'].mean())

data1_mean_varde2
```




    1




```python
data1_mean_varde3 = int(data1['varde3'].mean())

data1_mean_varde3
```




    2




```python
data1_mean_varde4 = int(data1['varde4'].mean())

data1_mean_varde4
```




    0




```python
data1_mean_varde5 = int(data1['varde5'].mean())

data1_mean_varde5
```




    0




```python
#from datetime import date

#today = date.today()
#print("Today's date:", today)
```


```python
# displaying the total stats

display(HTML("<div style = 'background-color: #504e4e; padding: 30px '>" +
             "<span style='color: #fff; font-size:30px;'> Total bedömning: "  + str(data1_total) +"</span>" +
             "<span style='color: red; font-size:30px;margin-left:20px;'> medelvärde 1: " + str(data1_mean_varde1) + "</span>"+
             "<span style='color: lightgreen; font-size:30px; margin-left:20px;'> medelvärde 2: " + str(data1_mean_varde2) + "</span>"+
             "<span style='color: lightblue; font-size:30px; margin-left:20px;'> medelvärde 3: " + str(data1_mean_varde3) + "</span>"+
             "<span style='color: lightyellow; font-size:30px; margin-left:20px;'> medelvärde 4: " + str(data1_mean_varde4) + "</span>"+
             "<span style='color: lightpink; font-size:30px; margin-left:20px;'> medelvärde 5: " + str(data1_mean_varde5) + "</span>"+
             "</div>")
       )
```


<div style = 'background-color: #504e4e; padding: 30px '><span style='color: #fff; font-size:30px;'> Total bedömning: 40</span><span style='color: red; font-size:30px;margin-left:20px;'> medelvärde 1: 14</span><span style='color: lightgreen; font-size:30px; margin-left:20px;'> medelvärde 2: 1</span><span style='color: lightblue; font-size:30px; margin-left:20px;'> medelvärde 3: 2</span><span style='color: lightyellow; font-size:30px; margin-left:20px;'> medelvärde 4: 0</span><span style='color: lightpink; font-size:30px; margin-left:20px;'> medelvärde 5: 0</span></div>


# COVID-19 Confirmed/Death/Recovered cases by countries

## Enter number of countries you want the data for


```python
data1_clean = data1.dropna()

#country_df_clean.drop(['people_tested', 'people_hospitalized'], axis=1)
#country_df_clean = country_df.drop(columns=['people_tested', 'people_hospitalized'])
data1_clean.head()
 
```




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
      <th>personnummer</th>
      <th>provsvarsdate</th>
      <th>provsvar1</th>
      <th>varde1</th>
      <th>bedomning1</th>
      <th>provsvar2</th>
      <th>varde2</th>
      <th>bedomning2</th>
      <th>provsvar3</th>
      <th>varde3</th>
      <th>bedomning3</th>
      <th>provsvar4</th>
      <th>varde4</th>
      <th>bedomning4</th>
      <th>provsvar5</th>
      <th>varde5</th>
      <th>bedomning5</th>
      <th>total_bedomning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8201113227</td>
      <td>19-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.0</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.7</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.44</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.24</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8201113245</td>
      <td>13-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>13</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.0</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>2.3</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.80</td>
      <td>GUL</td>
      <td>ALAT, P-</td>
      <td>0.92</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8201113242</td>
      <td>14-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>13</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.3</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>2.3</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.79</td>
      <td>GUL</td>
      <td>ALAT, P-</td>
      <td>0.92</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8201113206</td>
      <td>26-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.2</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.4</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.40</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.18</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8201113239</td>
      <td>15-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.2</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.8</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.44</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.24</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
  </tbody>
</table>
</div>




```python
type(data1_clean)
```




    pandas.core.frame.DataFrame




```python
print(data1_clean.columns)
```

    Index(['personnummer', 'provsvarsdate', 'provsvar1', 'varde1', 'bedomning1',
           'provsvar2', 'varde2', 'bedomning2', 'provsvar3', 'varde3',
           'bedomning3', 'provsvar4', 'varde4', 'bedomning4', 'provsvar5',
           'varde5', 'bedomning5', 'total_bedomning'],
          dtype='object')
    


```python
data1_clean.head()
```




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
      <th>personnummer</th>
      <th>provsvarsdate</th>
      <th>provsvar1</th>
      <th>varde1</th>
      <th>bedomning1</th>
      <th>provsvar2</th>
      <th>varde2</th>
      <th>bedomning2</th>
      <th>provsvar3</th>
      <th>varde3</th>
      <th>bedomning3</th>
      <th>provsvar4</th>
      <th>varde4</th>
      <th>bedomning4</th>
      <th>provsvar5</th>
      <th>varde5</th>
      <th>bedomning5</th>
      <th>total_bedomning</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8201113227</td>
      <td>19-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.0</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.7</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.44</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.24</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8201113245</td>
      <td>13-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>13</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.0</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>2.3</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.80</td>
      <td>GUL</td>
      <td>ALAT, P-</td>
      <td>0.92</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8201113242</td>
      <td>14-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>13</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.3</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>2.3</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.79</td>
      <td>GUL</td>
      <td>ALAT, P-</td>
      <td>0.92</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8201113206</td>
      <td>26-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.2</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.4</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.40</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.18</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
    <tr>
      <th>4</th>
      <td>8201113239</td>
      <td>15-11-2021</td>
      <td>T4, fritt, P-</td>
      <td>16</td>
      <td>GRON</td>
      <td>T3, P-</td>
      <td>1.2</td>
      <td>GRON</td>
      <td>TSH, P-</td>
      <td>1.8</td>
      <td>GRON</td>
      <td>ASAT, P-</td>
      <td>0.44</td>
      <td>GRON</td>
      <td>ALAT, P-</td>
      <td>0.24</td>
      <td>GRON</td>
      <td>GRON</td>
    </tr>
  </tbody>
</table>
</div>



#### Let's subset the whole dataset by color values (GRON, GUL, RÖD)
#### and do conditional formatting


```python
## Highlight cells by string value (GRÖN, GUL, RÖD)
## source: https://queirozf.com/entries/pandas-dataframe-examples-styling-cells-and-conditional-formatting

def colored_background(cell_value):

    highlight_green = 'background-color: green;'
    highlight_yellow = 'background-color: yellow;'
    highlight_red = 'background-color: red;'
    default = ''

    if type(cell_value) in [str]:
        if cell_value == 'GRON':
            return highlight_green
        if cell_value == 'GUL':
            return highlight_yellow
        if cell_value == 'RÖD':
            return highlight_red
    return default

#data1_clean.style.applymap(colored_background)

```


```python
def show_latest_cases(n):
    n = int(n)
    return data1_clean.sort_values('provsvarsdate', ascending= False).head(n).style.applymap(colored_background)

interact(show_latest_cases, n='10')

ipywLayout = widgets.Layout(border='solid 2px green')
ipywLayout.display='none' # uncomment this, run cell again - then the graph/figure disappears
widgets.VBox([fig], layout=ipywLayout)
```


    interactive(children=(Text(value='10', description='n'), Output()), _dom_classes=('widget-interact',))



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-42-9cb47a757667> in <module>
          7 ipywLayout = widgets.Layout(border='solid 2px green')
          8 ipywLayout.display='none' # uncomment this, run cell again - then the graph/figure disappears
    ----> 9 widgets.VBox([fig], layout=ipywLayout)
    

    NameError: name 'fig' is not defined





```python
# Save as an excel file for later visualization
## source: https://stackoverflow.com/questions/47398937/saving-pandas-styler-object-in-anyway

data1_clean.sort_values('provsvarsdate', ascending= False).head(n).style.applymap(colored_background) \
   .to_excel('provsvar_tabel.xlsx', engine='openpyxl')

```

#### Let's subset the dataset over its total_bedomning different values (GRÖN, GUL, RÖD)


```python
#gron = data1_clean[[4,7,10,16,17]=='GRON']

# Select rows with last_name equal to some values, all columns
data_green = data1_clean.loc[data1_clean['total_bedomning'].isin(['GRON'])]  

#gron = data1_clean[data1_clean['bedomning1', 'bedomning2', 'bedomning3', 'bedomning4', 'bedomning5', 'total_bedomning']=='GRON']

data_green.tail(3)
```


```python
data_yellow = data1_clean[data1_clean['total_bedomning']=='GUL']

data_yellow.tail(3)
```


```python
data_red = data1_clean[data1_clean['total_bedomning']=='RÖD']

data_red.tail()
```

## Slide to check for the highest provsvar and bedomning


```python
## plotting the 10 highest provsvar

def bubble_chart(n):
    fig = px.scatter(...)
    fig.update_layout(
    title=str(n) +" Highest provsvar",
    xaxis_title="",
    yaxis_title="",
    width = 700
    )
    fig.show();

interact(bubble_chart, n=10)

ipywLayout = widgets.Layout(border='solid 2px green')
ipywLayout.display='none'
widgets.VBox([fig], layout=ipywLayout)
```

### Set personnummer as index


```python
#data1_clean.set_index("personnummer", inplace=True)

#data1_clean.head()
#data1_index[8201113179]
```


```python

```

## [Notebook covers:](https://github.com/datasciencewithharshit/voila-covid-19-dashboard)

## Link to the analysis and other resources:
* [Link to GitHub repo: ](https://github.com/dnzengou/provsvar_visu)
* #voila <notebook_name>.ipynb --strip_sources=False
* [Link to Author's Youtube: ](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ?view_as=subscriber)



```python

```
