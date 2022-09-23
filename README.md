# RARBG-Subs-Renamer

If you download a tv show from RARBG, chances are that the subtitles files will be in separate directories and each one will have almost the same name.
This simple program takes each .srt file, it renames the file and copies it in a new directory. The new file name will be the one of its father directory, so make sure it suits your case. 
Here's an example:
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
├── Ok
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
