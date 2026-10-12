import asyncio
import edge_tts


async def main():
    text = "안녕하세요. 파이썬 음성 변환 테스트입니다."

    tts = edge_tts.Communicate(text=text, voice="ko-KR-SunHiNeural", rate="+0%")

    await tts.save("female.mp3")
    print("MP3 생성 완료")


if __name__ == "__main__":
    asyncio.run(main())
