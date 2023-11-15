import json
import folium
import pandas as pd
import geopandas

sido_coordinate = {
    "서울특별시": [37.5311, 126.9814],
    "강원특별자치도": [37.6911, 127.8787],
    "경기도": [37.6034, 127.1396],
    "경상북도": [36.3509, 128.6874],
    "경상남도": [35.8313, 128.6097],
    "대구광역시": [35.8313, 128.6097],
    "광주광역시": [35.1502, 126.8565],
    "대전광역시": [36.3503, 127.3662],
    "부산광역시": [35.2048, 129.0835],
    "세종특별자치시": [36.4801, 127.2889],
    "울산광역시": [35.5664, 129.3190],
    "인천광역시": [37.4753, 126.6369],
    "전라남도": [35.0675, 126.9940],
    "전라북도": [35.8242, 127.1489],
    "제주특별자치도": [33.4996, 126.5312],
    "충청남도": [36.4548, 126.7946],
    "충청북도": [36.8109, 127.7952],
}


def SidoMap(sido_data):
    sido_path = "map_visual/geojson/si_do/HangJeongSiDo_ver20230701.json"
    # sido_geo = json.load(open(sido_path, encoding="utf-8"))
    sido_geo = geopandas.read_file(sido_path)
    data = pd.DataFrame(sido_data)
    result = pd.merge(sido_geo, data, on="sidonm")

    sido_map = folium.Map(location=[37.541, 126.986], zoom_start=7)

    folium.Choropleth(
        sido_geo,
        data=data,
        columns=["sidonm", "trading_volume"],
        key_on="feature.properties.sidonm",
        name="sido-map",
    ).add_to(sido_map)
    # print(sido_data)

    folium.GeoJson(
        name="sido_info",
        data=result,
        # click
        # popup=folium.GeoJsonPopup(
        #    fields=["sidonm", "sido_cd"], aliases=["시이름", "코드번호"]
        # ),
        tooltip=folium.GeoJsonTooltip(
            fields=["sidonm", "trading_volume", "average_price"],
            aliases=["지역이름", "거래량", "평균 매매가"],
            style=("font-size : 15px"),
        ),
    ).add_to(sido_map)

    sido_map = sido_map._repr_html_()
    return sido_map


def SigugunMap(sido_name, sigugun_data):
    sigugun_path = f"map_visual/geojson/si_gu_gun/{sido_name}.json"
    # sigugun_geo = json.load(open(sigugun_path, encoding="utf-8"))
    sigugun_geo = geopandas.read_file(sigugun_path)
    data = pd.DataFrame(sigugun_data)
    result = pd.merge(sigugun_geo, data, on="sgg_nm")

    sigugun_map = folium.Map(
        location=[sido_coordinate[sido_name][0], sido_coordinate[sido_name][1]],
        zoom_start=11,
    )

    sigugun_boundary = folium.Choropleth(
        sigugun_geo,
        name="sigugun-map",
        data=data,
        # columns=["Code", "Population"],
        columns=["sgg_nm", "trading_volume"],
        key_on="feature.properties.sgg_nm",
        fill_color="OrRd",  # 시각화할 색상
        fill_opacity=0.7,  # 색 투명도
        line_opacity=0.2,  # 경계선 투명도
        # legend_name="2018년 인구수",  # 색상 범주 이름
    ).add_to(sigugun_map)

    folium.GeoJson(
        data=result,
        name="sigugun_info",
        # click
        # popup=folium.GeoJsonPopup(
        #    fields=["sgg_nm", "trading_volume"], aliases=["지역이름", "거래량"]
        # ),
        tooltip=folium.GeoJsonTooltip(
            fields=["sgg_nm", "trading_volume", "average_price"],
            aliases=["지역 이름", "거래량", "평균 매매가"],
        ),
    ).add_to(sigugun_map)

    sigugun_boundary.geojson.zoom_on_click = False
    folium.LayerControl().add_to(sigugun_map)

    sigugun_map = sigugun_map._repr_html_()
    return sigugun_map


def DongMap(sido_name, sigugun_name, dong_data):
    sigugun_name = sigugun_name.replace(" ", "")
    dong_path = f"map_visual/geojson/dong/{sido_name}/{sigugun_name}.json"
    # dong_geo = json.load(open(dong_path, encoding="utf-8"))
    dong_geo = geopandas.read_file(dong_path)
    data = pd.DataFrame(dong_data)
    data["adm_nm"] = sido_name + " " + sigugun_name + " " + data["dong_nm"]

    result = pd.merge(dong_geo, data, on="adm_nm")

    dong_map = folium.Map(
        location=[sido_coordinate[sido_name][0], sido_coordinate[sido_name][1]],
        zoom_start=11,
    )

    dong_boundary = folium.Choropleth(
        dong_geo,
        data=data,
        # columns=["Code", "Population"],
        columns=["adm_nm", "trading_volume"],
        key_on="feature.properties.adm_nm",
        name="dong-map",
    ).add_to(dong_map)

    folium.GeoJson(
        data=result,
        name="dong_info",
        # click
        # popup=folium.GeoJsonPopup(
        #    fields=["adm_nm", "adm_cd2"], aliases=["지역명", "코드번호"]
        # ),
        tooltip=folium.GeoJsonTooltip(
            fields=["adm_nm", "trading_volume", "average_price"],
            aliases=["지역이름", "거래량", "평균 매매가"],
        ),
    ).add_to(dong_map)

    dong_boundary.geojson.zoom_on_click = False
    folium.LayerControl().add_to(dong_map)

    dong_map = dong_map._repr_html_()
    return dong_map
