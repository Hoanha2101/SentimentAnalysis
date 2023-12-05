from MyFile.library import *

emoji_set_up = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗",
               "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "😎", "🤩", "🥳", "🤭", "🤑", "🤤", "🥱", "😴", "😪", "😺", "😸", "😹", 
               "😻", "😽", "🧐", "🥸", "😏", "🫢", "🤫", "🤥", "😶", "😶‍🌫️", "😐", "😑", "😬", "🫠", "🤢", "🤮", "🤧", "😷", 
               "🤒", "🤕", "🤨", "🥲", "🥹", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", 
               "😮‍💨", "🤧", "😷", "🤒", "🤕", "😵", "😵‍💫", "🫥", "🤐", '😠', '😡', '😑', '😤', '😈', '💩', '😕', '👎', '😩', 
               '☹', '🙄', '😔', '🤧', '🤬', '🫨', '🙄', '😯', '😦', '😧', '😮', '🤑', '🤠', '😲', '😼', '🙀', '😈', '👿', '👹', 
               '👺', '🤡', '👻', '💀', '☠️', '👽', '👾', '🤖', '🎃', '😰', '😨', '😱', '😨']

emoji_Enjoyment = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "☺️", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗",
                   "😙", "😚", "😋", "😛", "😝", "😜", "🤪", "😎", "🤩", "🥳", "🤭",  "🤑", "🤤","🥱", "😴", "😪", "😺","😸", "😹", "😻", "😽",]
emoji_Disgust = [ "🧐", "🥸", "😏", "🫢", "🤫", "🤥", "😶", "😶‍🌫️", "😐", "😑", "😬",  "🫠",  "🤢", "🤮", "🤧", "😷", "🤒", "🤕"]
emoji_Sadness = ["🤨", "🥲", "🥹",  "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "🥺", "😢", "😭", "😮‍💨","🤧", "😷", "🤒", "🤕"]
emoji_Anger = ["😵", "😵‍💫", "🫥", "🤐", '😠', '😡', '😑', '😤', '😈', '💩', '😕', '👎', '😩', '☹', '🙄', '😔', '🤧', '🤬',]
emoji_Surprise = ["🫨", "🙄","😯", "😦", "😧", "😮",  "🤑",  "🤠", "😲", "😼", "🙀",]
emoji_Fear = ["😈", "👿", "👹", "👺", "🤡", "👻", "💀", "☠️", "👽", "👾", "🤖", "🎃", '😰', '😨', '😱', '😨']

def emoji_pro(sentence):
    items = ["Enjoyment","Disgust", "Sadness", "Anger", "Surprise", "Fear"]
    list_char = [i for i in sentence.split()]
    len_list_char = len(list_char)
    count = 0
    for char in list_char:
        if ej.emoji_count(char):
            count += 1
    if count == len_list_char:
        count_emoji_Enjoyment = 0
        count_emoji_Disgust = 0
        count_emoji_Sadness = 0
        count_emoji_Anger = 0
        count_emoji_Surprise = 0
        count_emoji_Fear = 0
        
        for emoji in list_char:
            if emoji in emoji_Enjoyment:
                count_emoji_Enjoyment += 1
            if emoji in emoji_Disgust:
                count_emoji_Disgust += 1
            if emoji in emoji_Sadness:
                count_emoji_Sadness += 1
            if emoji in emoji_Anger:
                count_emoji_Anger += 1
            if emoji in emoji_Surprise:
                count_emoji_Surprise += 1
            if emoji in emoji_Fear:
                count_emoji_Fear += 1
                
        sum = count_emoji_Enjoyment + count_emoji_Disgust + count_emoji_Sadness + count_emoji_Anger + count_emoji_Surprise + count_emoji_Fear
        if sum >= int(len_list_char - 3):
            count_list = [count_emoji_Enjoyment, count_emoji_Disgust, count_emoji_Sadness, count_emoji_Anger, count_emoji_Surprise, count_emoji_Fear]
            max_value = max(count_list)
            index_of_max = count_list.index(max_value)
            label = str(items[index_of_max])
            return label
        else:
            label = "Other"
            return label
    else:
        label = "STR"
        return label


punctuation_to_remove = [
    '.', ',', ';', ':', '?', '!', "'", '"', '-', '_', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '/', '\\',
    '...', '^',
]

# Stopwords
StopWords = [
        'chs','cerrrr','aaaaa','aaaaaaa','aamir','abcxyz','ac','18','200','500','dek','thg','đg','đs',
        'kkk','dcm','cu','ừm','xl','01','10','100', '11','12','13','14','15','150',
        '17','1700''1967','20','21','22','225','23','24','25','26','28','2_','2_3','30','300','3000','320','333',
        '33333','40','400','42','45','48', '50','5000','580','60','63','66','75','78','80','800','81','850','90','900',
        '99','99999','_200','_5','ah','bn','c3','chg','cp','dòg','hlin',
        'vcb','trươ','trưen','amir','ga','1700','1967','oaaaaaaa','bg','chaiii','cmm','cmnl','cã',
        'hloz','imdb','kau','kbh','matlon','muô','nh','nhma','p30','16','250','56','adm','ngươ','per',
        'lă', 'miê' , 'haizzz','haiz','dlm','quàooo','hee','nv', 'hmmmmmmm','beep',
        'zoe','pogba','mu','lòa','haizzzz','dg','pk','lz','thă','nhồn','tn','toau','bankon',
        'haizaaa','vcd','aw','kkkk','nghr','ds','anw','pg','ml','haaa','dma','cigar','vanew','doume',
        'oy','azz','1imdb','valak','haizz','xd','p30','x10','x20','vll','ss','đcm','disme','xiaolon','disss','tml',
        'móe','sury','fucklong','uwu','mlz','dumehuhonchimen','vks','ewww','ph','awwww','minvolum','kp','evn',
        'oimeoi','đư','rv', 'per ơ ơ ơ','ah', 'ơ ơ ơ'
]

EditSpelling = {
    "trog": "trong", "ne": "nè", "thi ch": "thích", "va i": "vãi", "hs": "học sinh","kbh": "không bao giờ","thí ch":"thích","fanpage":"trang mạng","showbiz":"truyền hình",
     "pạt": "phạt", "oto": "ô tô", "sgk": "sách giáo khoa", "cv": "công việc", "kq": "kết quả", "mj": "mình",
     "ne": "nè",  "nhìu": "nhiều", "rụnng": "rụng", "cta": "chúng ta",  "ks": "khách sạn", "admin": "người quản trị","gym":"thể hình", "wtf":"vãi","cute":"dễ thương",
     "àk": "à", "nyc": "người yêu cũ",  "củng": "cũng",
     "chowi": "chơi", "gane": "game", "vẩn": "vẫn", "fải": "phải", "yêuc": "yêu", "viẹc": "việc", "láp": "láo",
     "zo": "vào",  "nta": "người ta", "lsao": "làm sao", "tươ": "tươi", "bươ c": "bước",
     "hàg": "hàng", "luônnn": "luôn", "mink": "mình", "đươ c": "được", "vãi_chưởng": "vãi chưởng",
     "kha c": "khác", "ko": "không", "chờiiiii": "trời", "biê": "biết", "quáaaaa": "quá", "tôiii": "tôi",
     "uiiiii": "ui", "pheee": "phê", "pha i": "phải",  "đấyyyy": "đấy",
     "yêuc": "yêu", "ntnay": "như thế này",  "thôiiii": "thôi", "2 ac": "2 anh chị",
     "vớiiiiii": "với", "zay": "vậy", "záy": "váy", "hlv": "huấn luyện viên",  "bth": "bình thường",
    "nge": "nghe", "taooo": "tao", "bùn": "buồn", "inter": "internet", "xanhhhh": "xanh", "xog": "xong",
      "chaii": "chai",  "đzai": "đẹp trai", "t":"tao",
     "toau": "tao", "đag": "đang", "bỉu": "bảo", "ctay": "chia tay",  "qtrong": "quan trọng",
    "nghr": "nghe", "saoooo": "sao", "nhaaaaaaaa": "nha", "dòm": "nhìn", "thẳg": "thẳng", "giốg": "giống",
    "nhưg": "nhưng", "rồiii": "rồi", "sug": "sung", "vẫ": "vẫn", "mõi": "mỏi", "rồiiiii": "rồi",
      "qcao": "quảng cáo", "xiền": "tiền", "thạ timmmmm": "thả tim ", "thươnggg": "thương", "chữi": "chửi",
    "thiì": "thì", "mất dậy": "mất dạy", "chj": "chị", "viê c": "việc", "aiii ": "ai",
    "chổ": "chỗ",  "chaiii": "trai", "kinhh": "kinh", "tau": "tao", "vâ y": "vậy", "phảu": "phải","t":"tao",
    "dth": "dễ thương", "đâyy": "đây", " zai": "trai",  "ngiu": "người yêu", "b trai": "bạn trai",
    "cungz": "cũng vậy", "thcs": "trung học cơ sở", "màaaa": "mà", "thèn": "thằng", "stk": "số tài khoản",
    "nhma": "nhưng mà", "ơiii": "ơi", "uiii": "ui", "lênnnnn": "lên", "csgt": "cảnh sát giao thông", "điiii": "đi",
    "thíck": "thích", "ơiiii": "ơi", "vậyyyyy": "vậy", "yêuu": "yêu", "vãiii": "vãi", "điii": "đi", "vãiiii": "vãi",
    "hỏg ": "hỏng", "dòg": "dòng", "mxh": "mạng xã hội", "vk": "vợ", "ngừoi": "người", "càrôt": "cà rốt", "rồii": "rồi",
    "nhaaaa": "nha", "caooooo": "cao", "cug": "cũng", "ngỗg": "ngỗng", "mún": "muốn", "rụg": "rụng", "trờiiiiii": "trời",
    "khôg": "không", "ròii": "rồi", "gvcn": "giáo viên chủ nhiệm", "hqua": "hôm qua", "nhaaa": "nha", "géc": "ghét",
    "thik ": "thích", "tayyy": "tay", "gê": "ghê", "troai": "trai", "thoii": "thôi", "taoooo": "tao", "thé": "thế",
    "c an": "công an", "zại": "dạy", "moiij ": "một", "cườ": "cười", "hiếmkkk": "hiếm", "nưa": "nữa", "êiiii": "ơi",
    "tỵ": "tí", "cũg": "cũng", "2e": "2 em", "nổiiiii": "nổi", "tnao": "thế nào", "du rú": "ru rú", "ôiii": "ôi",
    "pải": "phải", "thix": "thích", "dụng trứng": "rụng trứng", "bjt": "biết","or": "hoặc","of": "của","you": "bạn", "crush": "người yêu",  "be carefull": "quan tâm",
    "tui thi ́ ch va ̉ i ́ mày ma ̀ ăn nhỉ ̀ u no ́ người ́ mày mọi người anh ̣ bi ̣ lơ ̉ ̣ người":"Tôi thích vải, mày mà ăn nhiều, người mày bị lở đấy"
}
Key_EditSpelling = list(EditSpelling.keys())

labels = {
        "Enjoyment": 0,
        "Disgust": 1,
        "Sadness": 2,
        "Anger": 3,
        "Surprise": 4,
        "Fear" : 5,
        "Other" : 6
}

def remove_extra_spaces(text):
    # Hà Khải    Hoàn -> Hà Khải Hoàn
    return re.sub(r"\s+", " ", text)

def clean_Sentence(sentence):
    for punctuation in punctuation_to_remove:
        if punctuation in sentence:
            str_new = sentence.replace(punctuation,"")
            sentence = str_new
    
    for i in range(len(StopWords)):
        stop_word = StopWords[i].lower()
        sentence = sentence.lower().strip()
        sentence = " " + sentence.strip() + " "
        stop_word_space = " " + stop_word + " "
        if stop_word_space in sentence:
            str_new = sentence.replace(stop_word,"")
            sentence = str_new.strip()

    for i in range(len(Key_EditSpelling)):
        spellingword = Key_EditSpelling[i].lower()
        sentence = " " + sentence.lower().strip() + " "
        spellingword_space = " " + spellingword + " "
        if spellingword_space in sentence:
            good_spelling = sentence.replace(spellingword,EditSpelling[spellingword])
            sentence = good_spelling.strip()
    
    sentence = ViTokenizer.tokenize(" ".join(list(tf.keras.preprocessing.text.text_to_word_sequence(remove_extra_spaces(sentence)))).lower())
    
    return sentence


#-------------------------Model-------------------------
class SentimentClassifier(nn.Module):
    def __init__(self, n_classes):
        super(SentimentClassifier, self).__init__()
        self.bert = AutoModel.from_pretrained("vinai/phobert-base")
        self.drop = nn.Dropout(p=0.3)
        self.fc = nn.Linear(self.bert.config.hidden_size, n_classes)
        nn.init.normal_(self.fc.weight, std=0.02)
        nn.init.normal_(self.fc.bias, 0)

    def forward(self, input_ids, attention_mask):
        last_hidden_state, output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask,
            return_dict=False # Dropout will errors if without this
        )

        x = self.drop(output)
        x = self.fc(x)
        return x