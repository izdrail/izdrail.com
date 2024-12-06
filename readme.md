# Izdrail.com
I'm a Full-Stack Developer who loves making high-quality web applications. Fascinated by everything that's web related. Connect with me on [LinkedIn](https://www.linkedin.com/in/izdrail/) , [GitHub](https://github.com/izdrail) and [Twitter](https://twitter.com/activistcoder).


## Getting Started
### Prerequisites
- Docker
- Docker Compose
- Python 3.11
- NodeJS 20
- Java 17
- Android SDK 11.07.6708
- Android Build Tools 34.0.0
- Android Platforms 34
- Gradle 8.2.1
- Ionic 7.2.0
- Capacitor 6.0.0

### Installation
1. Clone the repository
2. Run `docker compose up -d`
3. Open the browser at `http://localhost:12000`

## Development
### Frontend
The frontend is built using Ionic and Angular. To run the frontend, run `docker compose up -d` and open the browser at `http://localhost:12000`.
### Backend
The backend is built using FastAPI and Python. To run the backend, run `docker compose up -d` and open the browser at `http://localhost:12001`.

## Contributing
Contributions are welcome! If you find a bug or have a suggestion, please open an issue or submit a pull request.


Docker image for building Ionic apps with Capacitor. 

## How to use this image

<!-- ### Pull image

Pull from Docker Registry:  
`docker pull robingenz/ionic-capacitor` -->

### Build image

Build from GitHub:  
```
docker build -t robingenz/ionic-capacitor github.com/robingenz/docker-ionic-capacitor#main
```

Available build arguments:  

- JAVA_VERSION (Default: `17`)
- NODEJS_VERSION (Default: `20`)
- ANDROID_SDK_VERSION (Default: `11076708`)
- ANDROID_BUILD_TOOLS_VERSION (Default: `34.0.0`)
- ANDROID_PLATFORMS_VERSION (Default: `34`)
- GRADLE_VERSION (Default: `8.2.1`)
- IONIC_VERSION (Default: `7.2.0`)
- CAPACITOR_VERSION (Default: `6.0.0`)




## License
This project is licensed under the CC BY-NC-SA 4.0 license.