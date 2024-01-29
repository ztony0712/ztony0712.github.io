from pybtex.database.input import bibtex

def get_personal_data():
    name = ["Yimin", "Zhao"]
    email = "ztony0712@outlook.com"
    twitter = "ztony0712"
    github = "ztony0712"
    linkedin = "yimin-zhao-570993289"
    bio_text = f"""
                <p>
                    I am studying MSc in Robotics program in <a href="https://nus.edu.sg/" target="_blank">National University of Singapore (NUS)</a>, 
                    where I am a member of NUS Autonomous Bus Group supervised by <a href="https://guppy.mpe.nus.edu.sg/~mpeangh/" target="_blank">Prof. Marcelo H. Ang Jr.</a> in 
                    <a href="https://arc.nus.edu.sg/" target="_blank">Advanced Robotics Centre</a>.
                    <span style="color: red;">Looking for fully funded PhD positions!</span>
                </p>
                <p>
                    <span style="font-weight: bold;">Interests:</span>
                    Robot; EEG; Deep Learning; Autonomous Vehicles; Drone
                </p>
                <p>
                    <span style="font-weight: bold;">Bio:</span> 
                    I graduated as a BSc from <a href="https://en.swjtu.edu.cn/" target="_blank">Southwest Jiaotong University (SWJTU)</a> in China.
                    During that time, I focused on the applications of Deep Learning for EEG analysis, surpervised by <a href="https://scholar.google.com/citations?user=eLsZxC4AAAAJ&hl=zh-CN" target="_blank">Prof. Tianrui Li</a>.
                    Also, I am exciting for winning the second prize of <a href="https://chinaus-maker.cscse.edu.cn/chinaus-maker/hjzp/503460/index.html" target="_blank">China-US Young Maker Competition (CUYMC) in 2021</a>.
                </p>
                <p>Please do not hesitate to contact me for any inquiries!</p>
                <p>
                    <a href="assets/pdf/CV_Yimin_ZHAO.pdf" target="_blank" style="margin-right: 15px"><i class="fa fa-address-card fa-lg"></i> CV</a>
                    <a href="mailto:ztony0712@outlook.com" style="margin-right: 15px"><i class="far fa-envelope-open fa-lg"></i> Mail</a>
                    <a href="https://twitter.com/ztony0712" target="_blank" style="margin-right: 15px"><i class="fab fa-twitter fa-lg"></i> X</a>
                    <a href="https://scholar.google.com/citations?user=NNnZnvAAAAAJ&hl=en" target="_blank" style="margin-right: 15px"><i class="fa-solid fa-book"></i> Scholar</a>
                    <a href="https://github.com/ztony0712" target="_blank" style="margin-right: 15px"><i class="fab fa-github fa-lg"></i> Github</a>
                    <a href="https://www.linkedin.com/in/yimin-zhao-570993289/" target="_blank" style="margin-right: 15px"><i class="fab fa-linkedin fa-lg"></i> LinkedIn</a>
                    <a href="https://space.bilibili.com/11305755?spm_id_from=333.1007.0.0" target="_blank" style="margin-right: 15px"><i class="fa-brands fa-bilibili fa-lg"></i> Bilibili</a>
                    <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#demo" data-toggle="collapse" style="margin-left: -6px; margin-top: -2px;"><i class="fa-solid fa-trophy"></i>Awards</button>
                    <div id="demo" class="collapse">
                    <span style="font-weight: bold;">Awards</span><br>
                    National Second Prize, China-US Young Maker Competition (CUYMC) <br>
                    National Third Prize, 17th “Challenge Up” <br>
                    Provincial First Prize, 16th “Challenge Up” <br>
                    Successful Participant, 2021 Mathematical Contest in Modeling <br>
                    First Prize, SWJTU, 13th Extracurricular Scientific and Technological Innovation Experimental Competition <br>
                    Third Prize, SWJTU, 12th Extracurricular Scientific and Technological Innovation Experimental Competition <br>
                    Comprehensive Second-Prize Scholarship, SWJTU, 2020-2021 <br>
                    Excellent Student Cadre, SWJTU, 2020-2021 <br>
                </div>
                </p>
    """
    footer = """
            <div class="col-sm-12" style="">
                <h4>Homepage Template</h4>
                <p>
                    This web page is developed based on <a href="https://m-niemeyer.github.io/">Michael Niemeyer</a>\'s template. 
                    You can visit his <a href="https://github.com/m-niemeyer/m-niemeyer.github.io">Github Repository</a> to create your own personal website.
                </p>
            </div>
    """
    return name, bio_text, footer

def get_author_dict():
    return {
        'Haohong Wang': 'https://www.researchgate.net/profile/Haohong-Wang',
        'Damien Rompapas': 'https://scholar.google.co.jp/citations?user=BD7CuEcAAAAJ&hl=en',
        }

def generate_person_html(persons, connection=", ", make_bold=True, make_bold_name='Yimin Zhao', add_links=True):
    links = get_author_dict() if add_links else {}
    s = ""
    for p in persons:
        string_part_i = ""
        for name_part_i in p.get_part('first') + p.get_part('last'): 
            if string_part_i != "":
                string_part_i += " "
            string_part_i += name_part_i
        if string_part_i in links.keys():
            string_part_i = f'<a href="{links[string_part_i]}" target="_blank">{string_part_i}</a>'
        if make_bold and string_part_i == make_bold_name:
            string_part_i = f'<span style="font-weight: bold";>{make_bold_name}</span>'
        if p != persons[-1]:
            string_part_i += connection
        s += string_part_i
    return s

def get_paper_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""

    if 'award' in entry.fields.keys():
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <span style="color: red;">({entry.fields['award']})</span><br>"""
    else:
        s += f"""<a href="{entry.fields['html']}" target="_blank">{entry.fields['title']}</a> <br>"""

    s += f"""{generate_person_html(entry.persons['author'])} <br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'html': 'Project Page', 'pdf': 'Paper', 'supp': 'Supplemental', 'video': 'Video', 'poster': 'Poster', 'code': 'Code'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')

    cite = "<pre><code>@InProceedings{" + f"{entry_key}, \n"
    cite += "\tauthor = {" + f"{generate_person_html(entry.persons['author'], make_bold=False, add_links=False, connection=' and ')}" + "}, \n"
    for entr in ['title', 'booktitle', 'year']:
        cite += f"\t{entr} = " + "{" + f"{entry.fields[entr]}" + "}, \n"
    cite += """}</pre></code>"""
    s += " /" + f"""<button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse{entry_key}" aria-expanded="false" aria-controls="collapseExample" style="margin-left: -6px; margin-top: -2px;">Expand bibtex</button><div class="collapse" id="collapse{entry_key}"><div class="card card-body">{cite}</div></div>"""
    s += """ </div> </div> </div>"""
    return s

def get_talk_entry(entry_key, entry):
    s = """<div style="margin-bottom: 3em;"> <div class="row"><div class="col-sm-3">"""
    s += f"""<img src="{entry.fields['img']}" class="img-fluid img-thumbnail" alt="Project image">"""
    s += """</div><div class="col-sm-9">"""
    s += f"""{entry.fields['title']}<br>"""
    s += f"""<span style="font-style: italic;">{entry.fields['booktitle']}</span>, {entry.fields['year']} <br>"""

    artefacts = {'slides': 'Slides', 'video': 'Recording'}
    i = 0
    for (k, v) in artefacts.items():
        if k in entry.fields.keys():
            if i > 0:
                s += ' / '
            s += f"""<a href="{entry.fields[k]}" target="_blank">{v}</a>"""
            i += 1
        else:
            print(f'[{entry_key}] Warning: Field {k} missing!')
    s += """ </div> </div> </div>"""
    return s

def get_publications_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('publication_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_paper_entry(k, bib_data.entries[k])
    return s

def get_talks_html():
    parser = bibtex.Parser()
    bib_data = parser.parse_file('talk_list.bib')
    keys = bib_data.entries.keys()
    s = ""
    for k in keys:
        s+= get_talk_entry(k, bib_data.entries[k])
    return s

def get_index_html():
    pub = get_publications_html()
    talks = get_talks_html()
    name, bio_text, footer = get_personal_data()
    s = f"""
    <!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" integrity="sha512-xh6O/CkQoPOWDdYTDqeRdPCVd1SpvCA9XXcUnZS2FmJNp1coAFzvtCN9BmamE+4aHK8yyUHUSCcJHgXloTyT2A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

  <title>{name[0] + ' ' + name[1]}</title>
  <link rel="icon" type="image/x-icon" href="assets/robot.png">
</head>

<body>
    <div class="container">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-10">
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="margin-bottom: 1em;">
                    <h3 class="display-4" style="text-align: center;"><span style="font-weight: bold;">{name[0]}</span> {name[1]}</h3>
                    </div>
                    <br>
                    <div class="col-md-9" style="">
                        {bio_text}
                    </div>
                    <div class="col-md-3" style="">
                        <img src="assets/img/profile.jpg" class="img-thumbnail" width="280px" alt="Profile picture">
                    </div>
                </div>
                <div class="row" style="margin-top: 1em;">
                    <div class="col-sm-12" style="">
                        <h4>Publications</h4>
                        {pub}
                    </div>
                </div>
                <div class="row" style="margin-top: 3em;">
                    <div class="col-sm-12" style="">
                        <!-- <h4>Projects</h4> -->
                        {talks}
                    </div>
                </div>
                <div class="row" style="margin-top: 3em; margin-bottom: 1em;">
                    {footer}
                </div>
            </div>
            <div class="col-md-1"></div>
        </div?
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"></script>
</body>

</html>
    """
    return s


def write_index_html(filename='index.html'):
    s = get_index_html()
    with open(filename, 'w') as f:
        f.write(s)
    print(f'Written index content to {filename}.')

if __name__ == '__main__':
    write_index_html('index.html')
