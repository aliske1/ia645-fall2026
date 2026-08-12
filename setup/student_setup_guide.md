# Student Setup Guide — IA 645

This guide covers everything you need to get your course environment running. Work through it top to bottom. If something fails, note the exact error message and post it in the Week 2 QCC board on Canvas.

---

## Troubleshooting Common Issues

### "Docker daemon is not running"
Docker Desktop is not open. Launch it from the Start menu and wait for "Engine running" before trying again.

### "Port 8888 is already in use"
Something else is using that port. Run the container on a different port:
```
docker run -p 8889:8888 -v "%~dp0:/course" ia645-base
```
Then go to http://localhost:8889 instead.

### "Cannot connect to the Docker daemon"
Verify Docker Desktop shows "Engine running." Try restarting Docker Desktop.

### Git is not recognized
Download and install Git from https://git-scm.com/download/win then restart PowerShell.

### Build fails with pip errors
Make sure Docker Desktop is running and you have an active internet connection during the build step.

---

## Mac and Linux Users

The course environment works on Mac and Linux but instructor support is limited. Replace the .bat file with:

```
docker run -p 8888:8888 -v "$(pwd):/course" ia645-base
```

---

## Stopping the Environment

In the PowerShell window running Docker, press Ctrl+C to stop the container. Your work is saved in the repository folder on your machine.
