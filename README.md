# Flutter Laboratory (24CS2016)

Complete laboratory submission for Flutter application development, covering **Experiments 1 to 12**. Each experiment is cleanly separated into its own folder with dedicated Dart code, dependencies, and configuration. All experiments are compiled and hosted directly on **GitHub Pages**.

---

## 🌐 Hosted Experiments on GitHub Pages

| Exp No. | Experiment Title | Direct Hosted Link | Interactive Route |
|:---:|:---|:---:|:---:|
| **01** | Basic Widgets and Layouts | [Launch Exp 1](https://anmol-0705.github.io/FlutterLab/exp1/) | [Route #/exp1](https://anmol-0705.github.io/FlutterLab/#/exp1) |
| **02** | Adaptive & Responsive UI Design | [Launch Exp 2](https://anmol-0705.github.io/FlutterLab/exp2/) | [Route #/exp2](https://anmol-0705.github.io/FlutterLab/#/exp2) |
| **03** | Interactivity, Input & Form Validation | [Launch Exp 3](https://anmol-0705.github.io/FlutterLab/exp3/) | [Route #/exp3](https://anmol-0705.github.io/FlutterLab/#/exp3) |
| **04** | Assets and Media (Image & Video) | [Launch Exp 4](https://anmol-0705.github.io/FlutterLab/exp4/) | [Route #/exp4](https://anmol-0705.github.io/FlutterLab/#/exp4) |
| **05** | Navigation and Routing (Named Routes) | [Launch Exp 5](https://anmol-0705.github.io/FlutterLab/exp5/) | [Route #/exp5](https://anmol-0705.github.io/FlutterLab/#/exp5) |
| **06** | Animations & Transitions (AnimatedContainer) | [Launch Exp 6](https://anmol-0705.github.io/FlutterLab/exp6/) | [Route #/exp6](https://anmol-0705.github.io/FlutterLab/#/exp6) |
| **07** | State Management & JSON Serialization | [Launch Exp 7](https://anmol-0705.github.io/FlutterLab/exp7/) | [Route #/exp7](https://anmol-0705.github.io/FlutterLab/#/exp7) |
| **08** | Data Persistence (SQLite + Firebase) | [Launch Exp 8](https://anmol-0705.github.io/FlutterLab/exp8/) | [Route #/exp8](https://anmol-0705.github.io/FlutterLab/#/exp8) |
| **09** | REST API HTTP Client | [Launch Exp 9](https://anmol-0705.github.io/FlutterLab/exp9/) | [Route #/exp9](https://anmol-0705.github.io/FlutterLab/#/exp9) |
| **10** | Android Build Target | [Launch Exp 10](https://anmol-0705.github.io/FlutterLab/exp10/) | [Route #/exp10](https://anmol-0705.github.io/FlutterLab/#/exp10) |
| **11** | iOS Build Target | [Launch Exp 11](https://anmol-0705.github.io/FlutterLab/exp11/) | [Route #/exp11](https://anmol-0705.github.io/FlutterLab/#/exp11) |
| **12** | Responsive Web App with Flutter | [Launch Exp 12](https://anmol-0705.github.io/FlutterLab/exp12/) | [Route #/exp12](https://anmol-0705.github.io/FlutterLab/#/exp12) |

---

## 📁 Repository Structure

```
FlutterLab/
├── .github/workflows/deploy.yml
├── docs/ (Web Build & GitHub Pages artifacts)
│   ├── index.html
│   ├── 404.html
│   └── exp1/ to exp12/
├── Experiment_01_Basic_Widgets/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/main.dart
├── Experiment_02_Responsive_UI/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/main.dart
├── Experiment_03_Input_and_Forms/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/main.dart
├── Experiment_04_Assets_and_Media/
│   ├── pubspec.yaml
│   ├── README.md
│   ├── assets/
│   └── lib/main.dart
├── Experiment_05_Navigation_and_Routing/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/
│       ├── main.dart
│       ├── home.dart
│       ├── profile.dart
│       └── details.dart
├── Experiment_06_Animations_and_Transitions/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/main.dart
├── Experiment_07_State_Management_and_Serialization/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/
│       ├── main.dart
│       └── student.dart
├── Experiment_08_Data_Persistence_SQLite_Firebase/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/
│       ├── main.dart
│       ├── database_helper.dart
│       └── firebase_options.dart
├── Experiment_09_REST_API/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/main.dart
├── Experiment_10_Android_Build_Target/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/main.dart
├── Experiment_11_iOS_Build_Target/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/main.dart
├── Experiment_12_Web_Application/
│   ├── pubspec.yaml
│   ├── README.md
│   └── lib/main.dart
├── Working links.txt
└── README.md
```

## 🚀 How to Run Any Experiment Locally

To run any individual experiment locally with Flutter:
```bash
cd Experiment_01_Basic_Widgets
flutter pub get
flutter run
```
