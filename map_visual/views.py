from django.shortcuts import render
import json
import folium
import pandas as pd


# Create your views here.
def KoreaMap(request):
    path = "map_visual/TL_SCCO_SIG_WGS84.json"
    state_geo = json.load(open(path, encoding="euc-kr"))
    # state_geo = "map_visual/TL_SCCO_SIG_WGS84.json"
    state_unemployment = "map_visual/Total_People_2018.csv"
    state_data = pd.read_csv(state_unemployment, encoding="euc-kr")

    korea_map = folium.Map(location=[38, 128], zoom_start=8)

    korea_choro = folium.Choropleth(
        geo_data=state_geo,  # GeoJSON file
        name="korea-map",
        data=state_data,  # DataFrame
        # CSV 파일 첫번째 줄에서 지정한 내용
        columns=["Code", "Population"],
        # JSON지도와 CSV를 매칭할때 사용할 data
        key_on="feature.properties.SIG_CD",
        fill_color="YlGn",  # color
        fill_opacity=0.7,  # 투명도
        line_opacity=0.5,
        legend_name="Population Rate (%)",
    ).add_to(korea_map)

    folium.LayerControl().add_to(korea_map)

    korea_map = korea_map._repr_html_()
    context = {"korea_map": korea_map}
    return render(request, "map_visual/korea_map.html", context)


def SeoulMap(request):
    seoul_geo = "https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json"

    # 임시데이터
    raw_data = [
        ["강동구", 9912224],
        ["송파구", 8203005],
        ["강남구", 5236343],
        ["서초구", 7718434],
        ["관악구", 2671968],
        ["동작구", 6474852],
        ["영등포구", 7006927],
        ["금천구", 1163259],
        ["구로구", 2465648],
        ["강서구", 9770965],
        ["양천구", 6186435],
        ["마포구", 28175066],
        ["서대문구", 6190094],
        ["은평구", 6367052],
        ["노원구", 6512900],
        ["도봉구", 1675107],
        ["강북구", 8406888],
        ["성북구", 1558420],
        ["중랑구", 6268679],
        ["동대문구", 7288276],
        ["광진구", 129881],
        ["성동구", 1754089],
        ["용산구", 39018545],
        ["중구", 10321901],
        ["종로구", 10048909],
    ]

    data = pd.DataFrame(raw_data, columns=["name", "value"])

    map = folium.Map(location=[37.566345, 126.977893], zoom_start=12)
    choro = folium.Choropleth(
        seoul_geo,
        name="지역구",
        data=data,
        columns=["name", "value"],  # columns[1] = 시각화 하고자 하는 변수
        key_on="feature.properties.name",  # columns[0]과 매핑되는 값.(String값)
        fill_color="OrRd",  # 시각화할 색상
        fill_opacity=0.7,  # 색 투명도
        line_opacity=0.2,  # 경계선 투명도
        legend_name="임시데이터",  # 색상 범주 이름
    ).add_to(map)

    choro.geojson.add_child(folium.features.GeoJsonTooltip(["name"], labels=False))

    # 지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환
    map = map._repr_html_()
    context = {"my_map": map}
    return render(request, "map_visual/seoul_map.html", context)


def _render_map():
    seoul_geo = "https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json"

    # 임시데이터
    raw_data = [
        ["강동구", 9912224],
        ["송파구", 8203005],
        ["강남구", 5236343],
        ["서초구", 7718434],
        ["관악구", 2671968],
        ["동작구", 6474852],
        ["영등포구", 7006927],
        ["금천구", 1163259],
        ["구로구", 2465648],
        ["강서구", 9770965],
        ["양천구", 6186435],
        ["마포구", 28175066],
        ["서대문구", 6190094],
        ["은평구", 6367052],
        ["노원구", 6512900],
        ["도봉구", 1675107],
        ["강북구", 8406888],
        ["성북구", 1558420],
        ["중랑구", 6268679],
        ["동대문구", 7288276],
        ["광진구", 129881],
        ["성동구", 1754089],
        ["용산구", 39018545],
        ["중구", 10321901],
        ["종로구", 10048909],
    ]

    data = pd.DataFrame(raw_data, columns=["name", "value"])

    map = folium.Map(location=[37.566345, 126.977893], zoom_start=12)
    choro = folium.Choropleth(
        seoul_geo,
        name="지역구",
        data=data,
        columns=["name", "value"],  # columns[1] = 시각화 하고자 하는 변수
        key_on="feature.properties.name",  # columns[0]과 매핑되는 값.(String값)
        fill_color="OrRd",  # 시각화할 색상
        fill_opacity=0.7,  # 색 투명도
        line_opacity=0.2,  # 경계선 투명도
        legend_name="임시데이터",  # 색상 범주 이름
    ).add_to(map)

    choro.geojson.add_child(folium.features.GeoJsonTooltip(["name"], labels=False))

    # 지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환
    map = map._repr_html_()
    return map


def dong_maps(request):
    path = "map_visual/HangJeongDong_ver20230701.json"
    geo = json.load(open(path, encoding="utf-8"))

    detail_map = folium.Map(location=[37.566345, 126.977893], zoom_start=12)

    folium.Choropleth(geo, name="dong_map").add_to(detail_map)

    # popup event
    folium.GeoJson(
        data=geo,
        name="dong_map_info",
        popup=folium.GeoJsonPopup(
            fields=["sidonm", "adm_nm", "sgg", "adm_cd"],
            aliases=["시이름", "지역명", "시코드번호", "지역코드번호"],
        ),
    ).add_to(detail_map)

    detail_map = detail_map._repr_html_()
    context = {"detail_map": detail_map}
    return render(request, "map_visual/dong_map.html", context)
