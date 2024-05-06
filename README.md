# Visualization for Travel Time Map

## はじめに
**Travel_time_map**は、2Dマップ上の点間のエッジの長さとして旅行時間を表現することで視覚化するPythonプロジェクトです。このプロジェクトは北海道の電車の旅行時間データを使用し、旅行ルートと所要時間が最適化された2Dグラフを作成します。

## インストール手順
### 前提条件
- Python 3.10 以降
- ライブラリ：matplotlib、networkx、numpy、scipy

### セットアップ
1. リポジトリをローカルにクローンします。
2. pipを使用して必要なPythonライブラリをインストールします：
   ```bash
   pip install matplotlib networkx numpy scipy
   ```
3. プロジェクトディレクトリに移動します。

## 設定
`config`ディレクトリにある`settings.py`ファイルで、様々なパラメータを調整できます。また、対応する値をTrueに設定することで様々な機能をON/OFFを設定できます。

```Python
config = {
    'year': 2024, # "plot_initial_optimized_positions", "display_sorted_optimizations_by_weight", "animate_iterations"で使用する年
    #以下4つの関数のON/OFF設定
    'plot_initial_vs_optimized': True,  # これらの機能を使用するには、"True"を設定します
    'animate_yearly_optimizations': True,
    'display_sorted_by_the_weight_of_angle': False,
    'animate_iterations': True,

    # グラフ最適化に関するパラメータ
    'optimization_params': {
        'angle_weight': 0.5, # "plot_initial_optimized_positions", "animate_yearly_optimizations", "animate_iterations"で使用する角度の重み
        'angle_weights': [0,0.1, 0.5, 1.0,10,100,1000], # "display_sorted_optimizations_by_weight"で使用する様々な角度の重み
        'animation_interval': 50,          # アニメーションフレームの間隔（ミリ秒）
    }
}
```

`data`ディレクトリに新しい旅行時間データを追加できます。新しいデータが既存のファイルで示されているJSON形式に従っていることを確認してください。

## 使用方法
ターミナルで次のコマンドを実行してプロジェクトを起動します：
```bash
python main.py
```
これにより、データの処理が開始され、任意の関数が実行されます。

## データ説明
`data/1980`,`data/2000`および`data/2024`ディレクトリには、北海道の電車の移動時間データが含まれています。このデータは、位置と距離を最適化して時間地図を表現するために使用されます。  
新しくデータを追加する場合は、`data`内のJSON形式と同じ構造を持つようにしてください。  
**例** 
```json
{
    "positions": {
      "Sapporo": [0.0, 0.0],
      "Obihiro": [18.511, -1.506]
    },
      "distances": [
        {"from": "Sapporo", "to": "Chitose", "distance": 46.0},
        {"from": "Sapporo", "to": "Otaru", "distance": 39.0}
      ]
    }    
```
## 機能
- `plot_initial_optimized_positions`: 提供されたデータに基づいて初期位置と最適化位置をプロットします。  
![IMAGE PIC](https://github.com/adyngo/Travel_time_map/blob/main/img/Optimization2000.png?raw=true)

- `display_sorted_optimizations_by_weight`: 重みによってソートされた最適化グラフを表示します。  
![Sample Image](https://github.com/adyngo/Travel_time_map/blob/main/img/Angle_wight_change_2000.png?raw=true)

- `animate_yearly_optimizations`: 最適化された地図の推移を示すアニメーションを作成します。  
![Sample Animation](https://github.com/adyngo/Travel_time_map/blob/main/Animation/YearlyChange.mp4?raw=true)

- `animate_iterations`: 最適化の反復プロセスを示すアニメーションを生成します。  
![Sample Animation](https://github.com/adyngo/Travel_time_map/blob/main/Animation/IterationoAnimation.mp4?raw=true)

  
# Visualization for Travel Time Map

## Project Description
**Visualization for Travel Time Map** is a Python project designed to visualize travel times by representing them as the lengths of edges between points on a 2D map. This project uses train travel time data from Hokkaido to create an optimized graphical representation of travel routes and durations.

## Installation Instructions
### Prerequisites
- Python 3.10 or later
- Libraries: matplotlib, networkx, numpy, scipy

### Setup
1. Clone the repository to your local machine.
2. Install the required Python libraries using pip:
   ```bash
   pip install matplotlib networkx numpy scipy
   ```
3. Navigate to the project directory.

## Settings
In the `settings.py` file located in the `config` directory, you can adjust various parameters that affect the visualization and processing of the travel times. Also, you can activate various functions by setting their corresponding values to True.

```Python
config = {
    'year': 2024, #year to use in "plot_initial_optimized_positions", "display_sorted_optimizations_by_weight", and "animate_iterations"
    'plot_initial_vs_optimized': True,  #You can use these functions by setting this "True"
    'animate_yearly_optimizations': True,
    'display_sorted_by_the_weight_of_angle': False,
    'animate_iterations': True,

    # Parameters specific to graph optimization
    'optimization_params': {
        'angle_weight': 0.5, #Angle weight to use in "plot_initial_optimized_positions", "animate_yearly_optimizations", and "animate_iterations"
        'angle_weights': [0,0.1, 0.5, 1.0,10,100,1000], # Different angle weights to use in "display_sorted_optimizations_by_weight"
        'animation_interval': 50,          # Interval for animation frames in milliseconds
    }
}
```

 You can add new travel time data to the `data` directory. Ensure the new data follows the JSON format as shown in existing files.

## Usage
To run the project, execute the following command in the terminal:
```bash
python main.py
```
This will initiate the script to process the data and display the travel time maps.

## Data Description
The data in the `data/1980`, `data/2000`, and `data/2024` directories represent train travel time data in Hokkaido. This data is used to plot locations and optimize the 2D graph to visually represent travel times. Each data file should contain positions and distances structured similarly to the provided JSON format.  
Example
```json
{
    "positions": {
      "Sapporo": [0.0, 0.0],
      "Obihiro": [18.511, -1.506]
    },
      "distances": [
        {"from": "Sapporo", "to": "Chitose", "distance": 46.0},
        {"from": "Sapporo", "to": "Otaru", "distance": 39.0}
      ]
    }    
```
## Features and Functionalities
- `plot_initial_optimized_positions`: Plots the initial and optimized positions based on provided data.  
Here's an example;
![IMAGE PIC](https://github.com/adyngo/Travel_time_map/blob/main/img/Optimization2000.png?raw=true)

- `display_sorted_optimizations_by_weight`: Displays optimized graphs sorted by their weight.  
Here's an example;
![Sample Image](https://github.com/adyngo/Travel_time_map/blob/main/img/Angle_wight_change_2000.png?raw=true)

- `animate_yearly_optimizations`: Creates an animation showing yearly changes in optimizations.  
![Sample Animation](https://github.com/adyngo/Travel_time_map/blob/main/Animation/YearlyChange.mp4?raw=true)

- `animate_iterations`: Generates animations showing the iterative process of optimizations.  
![Sample Animation](https://github.com/adyngo/Travel_time_map/blob/main/Animation/IterationoAnimation.mp4?raw=true)
