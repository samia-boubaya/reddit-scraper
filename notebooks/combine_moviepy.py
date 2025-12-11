from moviepy.editor import VideoFileClip, AudioFileClip
from pathlib import Path

def merge_audio_video():
    audio_base = Path("../data/audio").resolve()
    video_base = Path("../data/visuals").resolve()
    
    print("🎥🔊 MOVIEPY - VIDEO + AUDIO")
    print(f"Audio: {audio_base}")
    print(f"Video: {video_base}")
    print("-" * 50)
    
    combined = 0
    
    for audio_folder in audio_base.iterdir():
        if not audio_folder.is_dir():
            continue
            
        folder_name = audio_folder.name
        video_folder = video_base / folder_name
        
        if not video_folder.exists():
            continue
            
        print(f"📁 {folder_name}")
        audio_files = list(audio_folder.glob("*_audio.m4a"))
        
        for audio_path in audio_files:
            video_stem = audio_path.stem.replace('_audio', '_vid')
            video_path = video_folder / f"{video_stem}.mp4"
            
            if not video_path.exists():
                continue
            
            print(f"   🔄 {video_path.name} + {audio_path.name}")
            
            try:
                video = VideoFileClip(str(video_path))
                audio = AudioFileClip(str(audio_path))
                final = video.set_audio(audio)
                final.write_videofile(str(video_path), codec='libx264', audio_codec='aac', verbose=False, logger=None)
                video.close()
                audio.close()
                final.close()
                print(f"   ✅ SUCCESS! 🎥🔊")
                combined += 1
            except Exception as e:
                print(f"   ❌ ERROR: {e}")
    
    print(f"\n🎉 {combined} VIDEOS TERMINÉES!")

merge_audio_video()
