from apscheduler.schedulers.asyncio import AsyncIOScheduler

def job():
    print("Scheduled job executed!")

async def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(job, "interval", seconds=30)
    scheduler.start()
