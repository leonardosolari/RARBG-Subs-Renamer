# RARBG-Subs-Renamer

If you download a movie or a tv show from RARBG, chances are that the subtitles files will be in separate directories and each one will have almost the same name.
This simple program takes each .srt file, it renames the file and copies it in a new location. The new file name will be the one of the video file it referes to.
At the moment the program works with the typical structure of RARBG releases of movies and tv shows. It ignores every subtitle file that is not in english. A simple workaround would be to change the ```substring``` variable content in /models/RARBGmovies.py and /models/RARBGtvshows.py 

Feel free to contribute by suggesting any typical file structure you know of.

# Example
Here's an example of the folder structure before and after using the program:

## RARBG TV Shows
### Before
```bash
.
├── Better.Call.Saul.S02E01.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E02.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E03.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E04.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E05.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E06.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E07.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E08.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E09.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E10.1080p.BluRay.x265-RARBG.mp4
└── Subs
    ├── Better.Call.Saul.S02E01.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E02.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   ├── 4_English.srt
    │   └── 5_English.srt
    ├── Better.Call.Saul.S02E03.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E04.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E05.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E06.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   ├── 4_English.srt
    │   └── 5_English.srt
    ├── Better.Call.Saul.S02E07.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E08.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E09.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    └── Better.Call.Saul.S02E10.1080p.BluRay.x265-RARBG
        ├── 3_English.srt
        └── 4_English.srt

11 directories, 32 files
```
### After
```bash
.
├── Better.Call.Saul.S02E01.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E02.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E03.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E04.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E05.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E06.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E07.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E08.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E09.1080p.BluRay.x265-RARBG.mp4
├── Better.Call.Saul.S02E10.1080p.BluRay.x265-RARBG.mp4
├── renamedSubtitles
│   ├── Better.Call.Saul.S02E01.1080p.BluRay.x265-RARBG-0.srt
│   ├── Better.Call.Saul.S02E01.1080p.BluRay.x265-RARBG-1.srt
│   ├── Better.Call.Saul.S02E02.1080p.BluRay.x265-RARBG-0.srt
│   ├── Better.Call.Saul.S02E02.1080p.BluRay.x265-RARBG-1.srt
│   ├── Better.Call.Saul.S02E02.1080p.BluRay.x265-RARBG-2.srt
│   ├── Better.Call.Saul.S02E03.1080p.BluRay.x265-RARBG-0.srt
│   ├── Better.Call.Saul.S02E03.1080p.BluRay.x265-RARBG-1.srt
│   ├── Better.Call.Saul.S02E04.1080p.BluRay.x265-RARBG-0.srt
│   ├── Better.Call.Saul.S02E04.1080p.BluRay.x265-RARBG-1.srt
│   ├── Better.Call.Saul.S02E05.1080p.BluRay.x265-RARBG-0.srt
│   ├── Better.Call.Saul.S02E05.1080p.BluRay.x265-RARBG-1.srt
│   ├── Better.Call.Saul.S02E06.1080p.BluRay.x265-RARBG-0.srt
│   ├── Better.Call.Saul.S02E06.1080p.BluRay.x265-RARBG-1.srt
│   ├── Better.Call.Saul.S02E06.1080p.BluRay.x265-RARBG-2.srt
│   ├── Better.Call.Saul.S02E07.1080p.BluRay.x265-RARBG-0.srt
│   ├── Better.Call.Saul.S02E07.1080p.BluRay.x265-RARBG-1.srt
│   ├── Better.Call.Saul.S02E08.1080p.BluRay.x265-RARBG-0.srt
│   ├── Better.Call.Saul.S02E08.1080p.BluRay.x265-RARBG-1.srt
│   ├── Better.Call.Saul.S02E09.1080p.BluRay.x265-RARBG-0.srt
│   ├── Better.Call.Saul.S02E09.1080p.BluRay.x265-RARBG-1.srt
│   ├── Better.Call.Saul.S02E10.1080p.BluRay.x265-RARBG-0.srt
│   └── Better.Call.Saul.S02E10.1080p.BluRay.x265-RARBG-1.srt
└── Subs
    ├── Better.Call.Saul.S02E01.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E02.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   ├── 4_English.srt
    │   └── 5_English.srt
    ├── Better.Call.Saul.S02E03.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E04.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E05.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E06.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   ├── 4_English.srt
    │   └── 5_English.srt
    ├── Better.Call.Saul.S02E07.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E08.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    ├── Better.Call.Saul.S02E09.1080p.BluRay.x265-RARBG
    │   ├── 3_English.srt
    │   └── 4_English.srt
    └── Better.Call.Saul.S02E10.1080p.BluRay.x265-RARBG
        ├── 3_English.srt
        └── 4_English.srt

12 directories, 54 files

```

## RARBG Movies
### Before
```bash
.
└── Armageddon.1998.1080p.BluRay.x265-RARBG
    ├── Armageddon.1998.1080p.BluRay.x265-RARBG.mp4
    ├── RARBG.txt
    ├── RARBG_DO_NOT_MIRROR.exe
    └── Subs
        └── 2_English.srt

2 directories, 4 files

```
### After
```bash
.
└── Armageddon.1998.1080p.BluRay.x265-RARBG
    ├── Armageddon.1998.1080p.BluRay.x265-RARBG.mp4
    ├── RARBG.txt
    ├── RARBG_DO_NOT_MIRROR.exe
    └── Subs
        └── 2_English.srt

2 directories, 4 files

```

As you can see it should handle duplicates and the original files are not touched. 
Anyway I DO NOT TAKE ANY RESPONSIBILITY FOR ANY EVENTUAL FILE LOSS.

## Installation 

### Optional: Create virtual environment before installing dependencies
```bash 
git clone https://github.com/leonardosolari/RARBG-Subs-Renamer
cd RARBG-Subs-Renamer
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 SubsRenamer.py
```

### Basic install
```bash 
git clone https://github.com/leonardosolari/RARBG-Subs-Renamer
cd RARBG-Subs-Renamer
pip install -r requirements.txt
python3 SubsRenamer.py
```
