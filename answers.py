class Id:
    def __init__(self, artist, work, location, year_range, art_group=""):
        self.artist = artist  # or, architect
        self.work = work  # or, building
        self.place = location
        self.year_range = year_range
        self.art_group = art_group  # e.g. '85 New Wave'; leave blank if none


ALL = range(50)
INDIA_AND_BANGLADESH = range(5)
JAPAN = range(5, 13)
GUTAI = range(5, 9)  # >=1955
JIKKEN_KOBO = range(9, 13)  # <=1955
MAO = range(13, 17)
POST_MAO = range(17, 22)
KOREA_AND_JAPAN = range(22, 25)
NEW = range(46, 55)

"""
all of Louis Kahn's works were in 1962-1982
the only thing we need to know "Tokyo" for is the performance of Pierrot Lunaire
there's no "general" anything. it's "Central Secretariat" by Le Corbusier
"Legislative Assembly" is by Le Corbusier and "National Assembly" is by Louis Kahn
    it's on water and it's from 1961-1964
"""
answers = {
    "ha1.webp": Id("Le Corbusier", "Central Secretariat", "Chandigarh, India", "1955"),
    "ha2.webp": Id("Le Corbusier", "Legislative Assembly", "Chandigarh, India", "1961-1964"),
    "ha3.webp": Id("Louis Kahn", "Mosque, National Assembly", "Dhaka, Bangladesh", "1962-1982"),
    "ha4.1.webp": Id("Louis Kahn", "National Assembly", "Dhaka, Bangladesh", "1962-1982"),  # exterior
    "ha4.2.webp": Id("Louis Kahn", "National Assembly", "Dhaka, Bangladesh", "1962-1982"),  # interior

    "ha5.webp": Id("Shiraga Kazuo", "Challenging Mud", "Japan", "1955", "Gutai"),
    "ha6.webp": Id("Shiraga Kazuo", "Work II", "Japan", "1958", "Gutai"),
    "ha7.1.webp": Id("Murakami Saburō", "Passing Through (Tsūka)", "Japan", "1956", "Gutai"),
    "ha7.2.webp": Id("Murakami Saburō", "Passing Through (Tsūka)", "Japan", "1956", "Gutai"),
    "ha8.webp": Id("Tanaka Atsuko", "Work (Bell)", "Japan", "1955", "Gutai"),

    "ha9.webp": Id("Jikken Kōbō", "performance of Pierrot Lunaire", "Tokyo, Japan", "1955", "Jikken Kōbō"),
    "ha10.1.webp": Id("Jikken Kōbō", "performance of Pierrot Lunaire", "Tokyo, Japan", "1955", "Jikken Kōbō"),
    "ha10.2.webp": Id("Jikken Kōbō", "performance of Pierrot Lunaire", "Tokyo, Japan", "1955", "Jikken Kōbō"),
    "ha11.webp": Id("Katsuhiro Yamaguchi", "Vitorīnu: Yoru no shinkō [Vitrine: Deep into the Night]", "Japan", "1954", "Jikken Kōbō"),
    "ha12.webp": Id("Katsuhiro Yamaguchi", "Vitrine No. 1", "Japan", "1952", "Jikken Kōbō"),

    "ha13.webp": Id("Luo Gongliu", "Mao Zedong Reporting on the Rectification in Yan'an", "China", "1951", "Socialist Realism"),
    "ha14.webp": Id("Dong Xiwen", "The Founding of the Nation", "China", "1952-1953", "Socialist Realism"),
    "ha15.webp": Id("Hou Yimin", "Liu Shaoqi and the Anyuan Coal Miners", "China", "1961", "Socialist Realism"),
    "ha16.1.webp": Id("", "Rent Collection Courtyard", "China", "1965"),  # made by a collective of sculptors from the Sichuan Fine Arts Institute
    "ha16.2.webp": Id("", "Rent Collection Courtyard", "China", "1965"),
    "ha16.3.webp": Id("", "Rent Collection Courtyard", "China", "1965"),

    "ha17.png": Id("Chen Yifei", "Looking at History from My Space", "China", "1979", "Post-Mao Socialist Realism"),
    "ha18.png": Id("Luo Zhongli", "Father", "China", "1980", "Post-Mao Scar Painting"),
    "ha19.png": Id("Li Xiaobin", "Dancing party at the ancient Summer Palace", "China", "1980", "Post-Mao Stars Art Collective"),
    "ha20.png": Id("Huang Yong Ping", "Towing Away the National Gallery", "China", "1988", "Post-Mao '85 New Wave"),
    "ha21.png": Id("Xiao Lu", "Dialogue", "China", "1989", "Post-Mao '85 New Wave"),

    "ha22.png": Id("Quac Insik", "Work 63", "Korea", "1963"),
    "ha23.png": Id("Sekine Nobuo", "Phase—Mother Earth", "Japan", "1968", "Mono-ha"),
    "ha24.png": Id("Lee Ufan", "Phenomena and Perception B [later retitled Relatum]", "Korea and Japan", "1968", "Mono-ha"),

    "ha25.png": Id("Oh Yoon", "Marketing I: Hell Painting", "Korea", "1980", ""),
    "ha26.png": Id("Hong Sung-dam", "May Print: Utopia", "Korea", "1984", ""),
    "ha27.png": Id("Kang Kuk-jin, Chan S. Chung, and Jung Kangja", "Murder on the Han River", "Korea", "1968", ""),
    "ha28.png": Id("Oh Yoon", "Ga 1960", "Korea", "1969", ""),
    "ha29.png": Id("Oh Yoon", "cover for Children at Work", "Korea", "1978", ""),
    "ha30.png": Id("collective protest", "Funeral procession for twenty-one-year-old economics student Lee Han Yeol", "Korea", "July 9, 1987", ""),
    "ha31.png": Id("Kim Jungheun", "Creating a Life of Plenty--Lucky Monolium", "Korea", "1981", ""),
    "ha32.png": Id("Min Joungki", "Pigs (A Pig Dream)", "Korea", "1981", ""),
    "ha33.png": Id("Lee Kiyeon", "On the Verge of Life or Death", "Korea", "1984", ""),
    "ha34.png": Id("Naeem Mohaiemen", "Still from a Missing Can of Film", "Bangladesh, Ireland, India", "2025", ""),
    "ha35.png": Id("Zahir Raihan", "Stop Genocide", "Bangladesh", "1971", ""),

    "ha36.png": Id("S. Sudjojono", "Straight Path", "Indonesia", "1941", ""),
    "ha37.png": Id("S. Sudjojono", "Friends of the Revolution", "Indonesia", "1947", ""),
    "ha38.png": Id("Ahmad Sadali", "Abstraction of a Landscape", "Indonesia", "1962", ""),
    "ha39.png": Id("FX Harsono", "Top Most", "Indonesia", "1975, remade in 2006", ""),
    "ha40.png": Id("FX Harsono", "Victim--Destruction I", "Indonesia", "1997", ""),
    "ha41.png": Id("Tran Van Can", "Little Sister Thuy", "Vietnam", "1943", ""),
    "ha42.png": Id("Mai Van Hien", "Five-dong note", "Vietnam", "1945", ""),
    "ha43.png": Id("Pham Thanh Tam", "On the Road to Khe Sanh", "Vietnam", "1967", ""),
    "ha44.png": Id("Le Minh", "To protect the crops, to feed the troops", "Vietnam", "1968", ""),
    "ha45.png": Id("Mai Van Hien", "Uncle Ho and the Courier", "Vietnam", "1990-1991", ""),

    "ha46.png": Id("Tsang Tsou-choi (King of Kowloon)", "Calligraphy on street furniture, Argyle Street at Sai Yee Street, Mong Kok", "Hong Kong", "1990-2007", ""),
    "ha47.png": Id("Lui Shou-kwan", "Lotus", "China", "1968", ""),
    "ha48.png": Id("Oscar Ho", "Anecdote about Chinese Dress", "Hong Kong", "1997", ""),
    "ha49.png": Id("Frog King (Kwok Mang-ho)", "Wearing Life Body Installation", "Hong Kong", "2014", ""),
    "ha50.png": Id("S. Sudjojono", "Straight Path", "Indonesia", "1941", ""),
    "ha51.png": Id("FX Harsono", "Top Most", "Indonesia", "1975, remade in 2006", ""),
    "ha52.png": Id("Tran Van Can", "Little Sister Thuy", "Vietnam", "1943", ""),
    "ha53.png": Id("Mai Van Hien", "Five-dong note", "Vietnam", "1945", ""),
    "ha54.png": Id("Mai Van Hien", "Uncle Ho and the Courier", "Vietnam", "1990-1991", ""),
}


def print_answer_key(answer_key=None):
    if answer_key is None:
        answer_key = answers

    file_w = max(len("File"), max(len(k) for k in answer_key.keys()))
    artist_w = max(len("Artist"), max(len(v.artist) for v in answer_key.values()))
    work_w = max(len("Work"), max(len(v.work) for v in answer_key.values()))
    place_w = max(len("Location"), max(len(v.place) for v in answer_key.values()))
    year_w = max(len("Year"), max(len(v.year_range) for v in answer_key.values()))
    group_w = max(len("Art group"), max(len(v.art_group) for v in answer_key.values()))

    header = (
        f"{'File':<{file_w}} | {'Artist':<{artist_w}} | {'Work':<{work_w}} | "
        f"{'Location':<{place_w}} | {'Year':<{year_w}} | {'Art group':<{group_w}}"
    )
    print(header)
    print("-" * len(header))

    for filename, obj in answer_key.items():
        print(
            f"{filename:<{file_w}} | {obj.artist:<{artist_w}} | {obj.work:<{work_w}} | "
            f"{obj.place:<{place_w}} | {obj.year_range:<{year_w}} | {obj.art_group:<{group_w}}"
        )
