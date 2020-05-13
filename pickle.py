import pickle

favorite_color = {"lion":"yellow", "kitty":"red"}
print(favorite_color)   # 인스턴스화 시키기 전의 favorite_color

pickle.dump( favorite_color, open( "save.pkl", "wb" ) )
favorite_color_load = pickle.load( open( "save.pkl", "rb" ) )
favorite_color_load
print(favorite_color)   # 인스턴스화 시킨 후의 favorite_color