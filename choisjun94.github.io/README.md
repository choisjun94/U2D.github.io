# Seung Jun Choi — GitHub Pages 홈페이지

## 먼저 보기
index.html을 더블클릭하면 브라우저에서 바로 볼 수 있습니다. 모든 스타일과 검색 기능을 한 파일에 포함했습니다. 설치나 빌드는 필요 없습니다.

## GitHub에 게시하기
1. choisjun94 계정으로 로그인한 다음 https://github.com/new 에서 공개(Public) 저장소를 만드세요. 이름은 정확히 `choisjun94.github.io`로 입력하세요. 이미 있다면 기존 파일을 백업하고 해당 저장소를 사용하세요.
2. ZIP을 풀고 그 안의 index.html, .nojekyll, README.md를 저장소 최상위에 업로드하세요. ZIP 파일 자체나 상위 폴더를 업로드하지 마세요. 브라우저에서 .nojekyll이 안 보이면 생략해도 이 순수 HTML 사이트는 작동합니다.
3. Settings → Pages → Build and deployment에서 Source를 Deploy from a branch로 지정하세요.
4. Branch는 main, 폴더는 /(root)를 선택하고 Save를 누르세요.
5. 배포 완료 후 https://choisjun94.github.io/ 에서 확인하세요. 현재 이 패키지는 업로드 또는 게시되지 않았습니다.

## sjun.net 연결 (GitHub 주소에서 확인한 후)
현재 사이트의 연결은 변경하지 않았습니다. GitHub 계정에서 도메인 소유권을 먼저 인증하고 저장소 Settings → Pages → Custom domain에 www.sjun.net을 추가합니다. 그 다음 도메인 관리업체에서 www CNAME을 choisjun94.github.io로 변경합니다. 기존 Google Sites용 www 레코드와 충돌하지 않게 교체합니다. 루트 도메인 sjun.net도 사용하려면 GitHub 공식 문서에 따른 A/ALIAS/ANAME 설정을 추가합니다. 이메일용 MX/TXT 레코드는 유지하세요. DNS 확인 및 인증서 발급 후 Enforce HTTPS를 켭니다. 도메인 등록·갱신은 현재 업체에서 계속 관리합니다.

공식 문서:
- https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages

## 수정하기
GitHub에서 index.html → 연필 아이콘을 눌러 내용을 수정하고 Commit changes를 누르면 배포 설정에 따라 반영됩니다. 논문은 class="publication"인 article 요소를 복사하여 추가합니다. data-year와 표시 연도를 함께 수정하고 새 연도는 select에도 추가하세요. 초기 논문 수 문구도 갱신하세요.

## 내용과 범위
2026-09-13에 확인한 https://www.sjun.net/ 의 공개 내용을 기반으로 영문 소개와 레이아웃을 정리했습니다. 논문 19편, 보고서/칼럼 링크, 강의, 경력, 수상, 지원과제, 발표, 진행 연구를 반영했습니다. 논문 서지정보는 기존 사이트 기준이며 출판사별 별도 검증은 하지 않았습니다. 기존 사이트의 사진 갤러리와 연구 도해는 포함하지 않았으며 프로필 영역에는 SJC 모노그램을 사용했습니다. 원본 사진과 CV 파일을 제공하면 추가할 수 있습니다. CV/Google Scholar/연구실 외부 주소는 확인된 자료가 없어 임의 링크를 만들지 않았습니다. 별도 추적 도구나 외부 폰트는 없습니다.
