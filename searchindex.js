Search.setIndex({"docnames": ["installation", "intro", "ocb_dc_ose_2021_data"], "filenames": ["installation.md", "intro.md", "ocb_dc_ose_2021_data.md"], "titles": ["Setup", "OceanBench DataChallenge", "Data Access for the Oceanbench v2 datachallenge demo"], "terms": {"prerequisit": 0, "mamba": 0, "merg": 0, "pip": 0, "ipython": 0, "jupyt": 0, "The": [0, 1, 2], "requir": [0, 2], "depend": 0, "you": [0, 1], "usag": 0, "mai": 0, "full": 0, "have": 0, "therefor": 0, "been": 0, "split": 0, "differ": [0, 1], "file": [0, 2], "env": [0, 2], "folder": 0, "repositori": 0, "quentinf00": [0, 1, 2], "ocb": [0, 1], "dc": [0, 1, 2], "os": [0, 1, 2], "2021": [0, 1, 2], "git": [0, 1, 2], "reli": 0, "compil": 0, "multipl": 0, "one": [0, 2], "suit": [0, 1], "your": [0, 2], "below": 0, "an": [0, 1], "exampl": [0, 1], "wget": 0, "nc": [0, 2], "http": [0, 1, 2], "raw": 0, "githubusercont": 0, "com": [0, 1, 2], "doc": 0, "base": [0, 2], "dvc": [0, 1, 2], "s3": 0, "yaml": [0, 2], "quiet": 0, "n": [0, 2], "f": 0, "In": 0, "first": [0, 2], "cell": 0, "run": 0, "q": [0, 2], "condacolab": 0, "import": [0, 2], "install_mambaforg": 0, "If": [0, 2], "don": 0, "t": 0, "go": 0, "here": [0, 1], "login": 0, "us": [0, 1], "cli": [0, 1, 2], "copernicusmarin": [0, 2], "can": [0, 1], "authentif": 0, "configur": [0, 1], "set": 0, "variabl": [0, 2], "aws_endpoint_url": 0, "aws_default_region": 0, "aws_secret_access_kei": 0, "aws_access_key_id": 0, "we": 1, "provid": [1, 2], "document": 1, "notebook": 1, "associ": 1, "github": [1, 2], "thi": 1, "aim": 1, "lai": 1, "foundat": 1, "build": 1, "ecosystem": 1, "facilit": 1, "develop": 1, "applic": 1, "ocean": [1, 2], "observ": [1, 2], "scienc": 1, "work": 1, "i": [1, 2], "built": 1, "upon": 1, "exist": [1, 2], "should": 1, "check": 1, "out": 1, "data": 1, "challeng": 1, "well": 1, "thought": 1, "evalu": 1, "case": 1, "input": 1, "download": 1, "instruct": 1, "metric": 1, "code": 1, "method": 1, "tool": 1, "ml": 1, "hydra": [1, 2], "zen": 1, "python": 1, "workflow": 1, "share": 1, "adapt": 1, "config": [1, 2], "integr": 1, "easi": 1, "comput": [1, 2], "local": [1, 2], "cluster": 1, "log": 1, "version": 1, "pipelin": 1, "paramet": [1, 2], "artefact": 1, "descript": 1, "orchestr": 1, "make": 1, "through": 1, "follow": 1, "5": [1, 2], "min": [1, 2], "walkthrough": 1, "video": 1, "demonstr": 1, "new": 1, "brought": 1, "implement": 1, "access": 1, "reproduct": [1, 2], "autom": 1, "leaderboard": 1, "updat": 1, "usecas": 1, "scale": 1, "oper": 1, "idea": 1, "project": 1, "defin": 1, "guidelin": 1, "so": 1, "actor": 1, "add": 1, "brick": 1, "while": [1, 2], "good": 1, "interoper": 1, "exit": 1, "compon": 1, "clarifi": 1, "how": 1, "do": [1, 2], "To": 1, "continu": 1, "setup": 1, "v2": 1, "demo": 1, "param": 2, "sat": 2, "j2g": 2, "2024": 2, "04": 2, "10": 2, "08": 2, "48": 2, "49": 2, "688": 2, "aprl": 2, "appareil": 2, "info": 2, "start": 2, "part": 2, "_01_dl_track": 2, "fetch": 2, "catalog": 2, "0": 2, "3": 2, "00": 2, "": 2, "33": 2, "1": 2, "14": 2, "29": 2, "89": 2, "100": 2, "4": 2, "96": 2, "10t08": 2, "04z": 2, "dataset": 2, "wa": 2, "specifi": 2, "latest": 2, "select": 2, "202112": 2, "844": 2, "copernicus_marine_root_logg": 2, "default": 2, "servic": 2, "origin": 2, "66": 2, "2": 2, "02": 2, "52": 2, "65": 2, "6": 2, "03": 2, "40": 2, "54it": 2, "9": 2, "24": 2, "28it": 2, "15": 2, "05": 2, "25": 2, "23it": 2, "26": 2, "17": 2, "07": 2, "12it": 2, "30": 2, "20": 2, "12": 2, "67it": 2, "38": 2, "09": 2, "11": 2, "42it": 2, "39": 2, "33it": 2, "45": 2, "98it": 2, "50": 2, "25it": 2, "34": 2, "02it": 2, "62": 2, "41": 2, "13": 2, "26it": 2, "74": 2, "83": 2, "55": 2, "16": 2, "62it": 2, "86": 2, "57": 2, "21": 2, "88it": 2, "08it": 2, "743": 2, "done": 2, "_02_prepare_track": 2, "744": 2, "ocb_dc_ose_2021": 2, "mod": 2, "prepare_track": 2, "269": 2, "300": 2, "0m": 2, "xarrai": 2, "xr": 2, "d": 2, "open_mfdataset": 2, "combin": 2, "nest": 2, "concat_dim": 2, "time": 2, "lt": 2, "gt": 2, "size": 2, "450kb": 2, "dimens": 2, "14060": 2, "coordin": 2, "datetime64": 2, "112kb": 2, "2017": 2, "11t14": 2, "44": 2, "772069888": 2, "lon": 2, "float64": 2, "dask": 2, "arrai": 2, "chunksiz": 2, "meta": 2, "np": 2, "ndarrai": 2, "lat": 2, "ssh": 2, "attribut": 2, "convent": 2, "cf": 2, "metadata_convent": 2, "unidata": 2, "discoveri": 2, "v1": 2, "cdm_data_typ": 2, "swath": 2, "comment": 2, "sea": 2, "surfac": 2, "height": 2, "measur": 2, "altimet": 2, "contact": 2, "servicedesk": 2, "cmem": 2, "mercat": 2, "eu": 2, "creator_email": 2, "summari": 2, "ssalto": 2, "duac": 2, "delai": 2, "level": 2, "su": 2, "time_coverage_dur": 2, "p12h19m2": 2, "66746": 2, "time_coverage_end": 2, "11t23": 2, "27z": 2, "time_coverage_resolut": 2, "p1": 2, "time_coverage_start": 2, "11t11": 2, "25z": 2, "titl": 2, "dt": 2, "ostm": 2, "jason": 2, "long": 2, "repeat": 2, "orbit": 2, "global": 2, "datasetdimens": 2, "14060coordin": 2, "x27": 2, "769939968": 2, "46": 2, "767809792": 2, "14t02": 2, "254863104": 2, "27": 2, "252733184": 2, "28": 2, "250603008": 2, "dtype": 2, "float64dask": 2, "unit": 2, "degrees_eaststandard_nam": 2, "longitudelong_nam": 2, "longitud": 2, "chunk": 2, "byte": 2, "109": 2, "84": 2, "kib": 2, "shape": 2, "graph": 2, "layer": 2, "type": 2, "numpi": 2, "degrees_northstandard_nam": 2, "latitudelong_nam": 2, "latitud": 2, "mstandard_nam": 2, "sea_surface_heightlong_nam": 2, "index": 2, "timepandasindexpandasindex": 2, "datetimeindex": 2, "47": 2, "765679872": 2, "763549952": 2, "761420032": 2, "759289856": 2, "51": 2, "757159936": 2, "755030016": 2, "53": 2, "752900096": 2, "01": 2, "56": 2, "35": 2, "469000960": 2, "36": 2, "466871040": 2, "37": 2, "464741120": 2, "462611200": 2, "460480768": 2, "458350848": 2, "456220928": 2, "name": 2, "length": 2, "freq": 2, "none": 2, "6metadata_convent": 2, "0cdm_data_typ": 2, "swathcom": 2, "referenc": 2, "1993": 2, "2012": 2, "period": 2, "addit": 2, "correct": 2, "propos": 2, "sla": 2, "alreadi": 2, "dac": 2, "ocean_tid": 2, "lwe": 2, "uncorrect": 2, "from": 2, "product": 2, "eucreator_email": 2, "eucreator_nam": 2, "themat": 2, "assembli": 2, "centercreator_url": 2, "marin": 2, "copernicu": 2, "eudate_cr": 2, "09t05": 2, "03zdate_issu": 2, "03zdate_modifi": 2, "03zgeospatial_lat_max": 2, "147938geospatial_lat_min": 2, "1426geospatial_lat_resolut": 2, "02496149999999986geospatial_lat_unit": 2, "degrees_northgeospatial_lon_max": 2, "359": 2, "98487geospatial_lon_min": 2, "000499geospatial_lon_resolut": 2, "02909299999999604geospatial_lon_unit": 2, "degrees_eastgeospatial_vertical_max": 2, "0geospatial_vertical_min": 2, "0geospatial_vertical_posit": 2, "downgeospatial_vertical_resolut": 2, "pointgeospatial_vertical_unit": 2, "mhistori": 2, "03z": 2, "creationinstitut": 2, "cl": 2, "cneskeyword": 2, "topographi": 2, "heightkeywords_vocabulari": 2, "netcdf": 2, "coard": 2, "climat": 2, "forecast": 2, "standard": 2, "nameslicens": 2, "web": 2, "commit": 2, "licenc": 2, "phpplatform": 2, "orbitprocessing_level": 2, "l3product_vers": 2, "vdec2021project": 2, "environ": 2, "monitor": 2, "refer": 2, "eusoftware_vers": 2, "7": 2, "0_duacs_dt2021_baselinesourc": 2, "measurementsssalto_duacs_com": 2, "mission": 2, "inter": 2, "calibr": 2, "topex": 2, "poseidon": 2, "between": 2, "2002": 2, "23": 2, "2008": 2, "18": 2, "19": 2, "2016": 2, "06": 2, "sinc": 2, "standard_name_vocabulari": 2, "metadata": 2, "tabl": 2, "v37summari": 2, "altimetri": 2, "over": 2, "66746stime_coverage_end": 2, "27ztime_coverage_resolut": 2, "p1stime_coverage_start": 2, "25ztitl": 2, "along": 2, "track": 2, "l3": 2, "2d": 2, "map": 2, "bin_siz": 2, "sel": 2, "assign": 2, "load": 2, "drop_var": 2, "to_datafram": 2, "groupbi": 2, "mean": 2, "to_xarrai": 2, "plot": 2, "matplotlib": 2, "collect": 2, "quadmesh": 2, "0x7172f238c250": 2, "multirun": 2, "true": 2, "403": 2, "launch": 2, "job": 2, "alg": 2, "516": 2, "517": 2, "h2ag": 2, "624": 2, "725": 2, "726": 2, "j2n": 2, "824": 2, "825": 2, "j3": 2, "925": 2, "926": 2, "s3a": 2, "050": 2, "store": 2, "repo": 2, "url": 2, "conveni": 2, "dc_repo": 2, "pretti": 2, "print": 2, "l": 2, "r": 2, "tree": 2, "fromfil": 2, "clone": 2, "obj": 2, "count": 2, "436": 2, "70obj": 2, "compress": 2, "223": 2, "34m": 2, "34mmetric": 2, "lambdax_4dvarnet": 2, "json": 2, "lambdax_duac": 2, "mu_4dvarnet": 2, "mu_duac": 2, "34mprepar": 2, "34minput": 2, "34mmethod_output": 2, "4dvarnet_on_track": 2, "duacs_on_track": 2, "psd_4dvarnet": 2, "psd_duac": 2, "34mref": 2, "c2": 2, "directori": 2, "get": 2, "11mb": 2, "353305": 2, "3mb": 2, "01t22": 2, "975349760": 2, "2018": 2, "78000": 2, "p23h18m50": 2, "723265": 2, "01t23": 2, "21z": 2, "01t00": 2, "30z": 2, "altika": 2, "drift": 2, "phase": 2, "al": 2, "353305coordin": 2, "031349760": 2, "087350016": 2, "31t14": 2, "678193152": 2, "678193408": 2, "70": 2, "mib": 2, "673": 2, "86207": 2, "22": 2, "143350016": 2, "199350016": 2, "255349760": 2, "311349760": 2, "367349760": 2, "423349760": 2, "479349760": 2, "31": 2, "08t13": 2, "36zdate_issu": 2, "36zdate_modifi": 2, "36zgeospatial_lat_max": 2, "81": 2, "509018geospatial_lat_min": 2, "77": 2, "038071geospatial_lat_resolut": 2, "052618500000001234geospatial_lat_unit": 2, "998917geospatial_lon_min": 2, "012548geospatial_lon_resolut": 2, "017998999999988996geospatial_lon_unit": 2, "36z": 2, "phaseprocessing_level": 2, "723265stime_coverage_end": 2, "21ztime_coverage_resolut": 2, "30ztitl": 2, "0x7172f0ab5bd0": 2, "test": 2, "assert_allclos": 2, "open_dataset": 2, "success": 2, "overview": 2, "credenti": 2, "sla_filt": 2, "mdt": 2, "basic": 2, "sat_id": 2, "specif": 2, "each": 2, "sat_list": 2, "max": 2, "_": 2, "bound": 2, "chang": 2, "cd": 2, "conf": 2, "overrid": 2, "my_conf": 2, "str": 2, "id": 2, "place": 2, "holder": 2, "min_tim": 2, "tempor": 2, "domain": 2, "max_tim": 2, "end": 2, "min_lon": 2, "lower": 2, "longitudin": 2, "max_lon": 2, "upper": 2, "min_lat": 2, "latitudin": 2, "max_lat": 2, "python_interfac": 2, "misc": 2, "verbos": 2, "displai": 2, "to_run": 2, "group": 2, "compos": 2, "those": 2, "option": 2, "dc_ose_2021_inference_data": 2, "arg": 2, "__placehold": 2, "anyth": 2, "foo": 2, "bar": 2, "valu": 2, "54": 2, "32": 2, "_target_": 2, "_partial_": 2, "dataset_id": 2, "cmems_get": 2, "duacs_l3": 2, "regex": 2, "month_regex_from_d": 2, "output_directori": 2, "force_download": 2, "overwrite_output_data": 2, "input_path": 2, "glob": 2, "iglob": 2, "pathnam": 2, "root_dir": 2, "null": 2, "dir_fd": 2, "recurs": 2, "include_hidden": 2, "fals": 2, "output_path": 2, "preprocess_track": 2, "sort_path": 2, "power": 2, "cc": 2, "view": 2, "937": 2, "debug": 2, "server": 2, "dataset_url": 2, "retriev": 2, "uniqu": 2, "identifi": 2, "dataset_vers": 2, "forc": 2, "dataset_part": 2, "usernam": 2, "authent": 2, "password": 2, "no_directori": 2, "bool": 2, "organ": 2, "show_outputnam": 2, "union": 2, "pathlib": 2, "path": 2, "where": 2, "save": 2, "credentials_fil": 2, "contain": 2, "skip": 2, "confirm": 2, "befor": 2, "overwrit": 2, "output": 2, "request_fil": 2, "request": 2, "overwrite_metadata_cach": 2, "cach": 2, "no_metadata_cach": 2, "filter": 2, "appli": 2, "regular": 2, "express": 2, "file_list": 2, "A": 2, "text": 2, "filenam": 2, "line": 2, "must": 2, "match": 2, "absolut": 2, "create_file_list": 2, "onli": 2, "creat": 2, "target": 2, "instead": 2, "them": 2, "It": 2, "write": 2, "current": 2, "other": 2, "action": 2, "perform": 2, "index_part": 2, "insitu": 2, "temporari": 2, "sync": 2, "synchron": 2, "remot": 2, "sync_delet": 2, "delet": 2, "ar": 2, "present": 2, "return": 2, "open": 2, "multifil": 2, "contaten": 2, "sequenc": 2, "callabl": 2, "function": 2, "whether": 2, "sort": 2, "concaten": 2}, "objects": {}, "objtypes": {}, "objnames": {}, "titleterms": {"setup": 0, "instal": 0, "conda": 0, "environ": 0, "without": [0, 2], "clone": 0, "With": 0, "On": [0, 1], "colab": 0, "credenti": 0, "need": 0, "reproduc": [0, 2], "demo": [0, 2], "notebook": 0, "cmem": 0, "fetch": 0, "sourc": 0, "data": [0, 2], "from": 0, "copernicu": 0, "portal": 0, "aw": 0, "push": 0, "prepar": [0, 2], "cloud": 0, "storag": 0, "upload": 0, "method": 0, "result": 0, "leaderboard": 0, "submiss": 0, "github": 0, "creat": 0, "pull": 0, "request": 0, "repo": 0, "origin": 0, "fork": 0, "oceanbench": [1, 2], "datachalleng": [1, 2], "overal": 1, "present": 1, "background": 1, "shoulder": 1, "giant": 1, "featur": 1, "showcas": 1, "contribut": 1, "access": 2, "v2": 2, "reus": 2, "process": 2, "step": 2, "us": 2, "configur": 2, "ocb": 2, "dc_ose_2021": 2, "input_data": 2, "pipelin": 2, "singl": 2, "satellit": 2, "dry": 2, "actual": 2, "execut": 2, "run": 2, "all": 2, "download": 2, "version": 2, "preprocess": 2, "list": 2, "content": 2, "input": 2, "visual": 2, "check": 2, "gener": 2, "v": 2, "more": 2, "usag": 2, "help": 2, "doc": 2}, "envversion": {"sphinx.domains.c": 2, "sphinx.domains.changeset": 1, "sphinx.domains.citation": 1, "sphinx.domains.cpp": 6, "sphinx.domains.index": 1, "sphinx.domains.javascript": 2, "sphinx.domains.math": 2, "sphinx.domains.python": 3, "sphinx.domains.rst": 2, "sphinx.domains.std": 2, "sphinx.ext.intersphinx": 1, "sphinxcontrib.bibtex": 9, "sphinx": 56}})