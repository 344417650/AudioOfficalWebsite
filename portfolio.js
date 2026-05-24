document.addEventListener('DOMContentLoaded', () => {
    // --- Music Player Element References ---
    const playBtn = document.getElementById('btn-play');

    const iconPlay = playBtn.querySelector('.icon-play');
    const iconPause = playBtn.querySelector('.icon-pause');

    const currentTimeEl = document.getElementById('current-time');
    const totalTimeEl = document.getElementById('total-time');

    const titleEl = document.getElementById('current-title');

    let playlistItems = [];

    let currentTrackIndex = 0;
    let isPlaying = false;
    let pendingPlay = false;

    // Format time in seconds to mm:ss
    function formatTime(seconds) {
        if (isNaN(seconds) || Math.floor(seconds) < 0) return "0:00";
        const m = Math.floor(seconds / 60);
        const s = Math.floor(seconds % 60);
        return `${m}:${s.toString().padStart(2, '0')}`;
    }

    // Initialize WaveSurfer
    const wavesurfer = WaveSurfer.create({
        container: '#waveform-container',
        waveColor: 'rgba(255, 255, 255, 0.35)',
        progressColor: '#ff4a1a',
        cursorColor: '#ffffff',
        cursorWidth: 1,
        height: window.matchMedia('(max-width: 768px)').matches ? 56 : 108,
        normalize: true,
        backend: 'WebAudio'
    });

    // Initialize Player
    function loadTrack(index) {
        playlistItems.forEach(item => item.classList.remove('active'));

        if(playlistItems.length === 0) return;

        const item = playlistItems[index];
        item.classList.add('active');

        const src = item.getAttribute('data-src');
        const title = item.getAttribute('data-title');

        titleEl.textContent = title;

        wavesurfer.load(src);
    }

    function togglePlay() {
        wavesurfer.playPause();
    }

    function updatePlayState() {
        if (isPlaying) {
            iconPlay.style.display = 'none';
            iconPause.style.display = 'block';
        } else {
            iconPlay.style.display = 'block';
            iconPause.style.display = 'none';
        }
    }

    function nextTrack() {
        currentTrackIndex = (currentTrackIndex + 1) % playlistItems.length;
        loadTrack(currentTrackIndex);
    }

    function prevTrack() {
        currentTrackIndex = (currentTrackIndex - 1 + playlistItems.length) % playlistItems.length;
        loadTrack(currentTrackIndex);
    }

    // Mobile progress bar
    const mobileProgress = document.getElementById('mobile-progress');

    function updateMobileProgress(currentTime) {
        const duration = wavesurfer.getDuration();
        if (mobileProgress && duration > 0) {
            mobileProgress.value = currentTime / duration;
        }
    }

    if (mobileProgress) {
        mobileProgress.addEventListener('input', () => {
            wavesurfer.seekTo(parseFloat(mobileProgress.value));
        });
    }

    // WaveSurfer Events
    wavesurfer.on('play', () => {
        isPlaying = true;
        updatePlayState();
    });

    wavesurfer.on('pause', () => {
        isPlaying = false;
        updatePlayState();
    });

    wavesurfer.on('audioprocess', (currentTime) => {
        currentTimeEl.textContent = formatTime(currentTime);
        updateMobileProgress(currentTime);
    });

    wavesurfer.on('seeking', (currentTime) => {
        currentTimeEl.textContent = formatTime(currentTime);
        updateMobileProgress(currentTime);
    });

    wavesurfer.on('ready', () => {
        const duration = wavesurfer.getDuration();
        totalTimeEl.textContent = formatTime(duration);
        if (mobileProgress) mobileProgress.value = 0;

        wavesurfer.seekTo(0);
        if (pendingPlay) {
            pendingPlay = false;
            wavesurfer.play();
        }
    });

    wavesurfer.on('finish', () => {
        currentTrackIndex = (currentTrackIndex + 1) % playlistItems.length;
        pendingPlay = true;
        loadTrack(currentTrackIndex);
    });

    // Control Buttons
    if(playBtn) playBtn.addEventListener('click', togglePlay);

    // Volume Slider
    const volumeSlider = document.getElementById('volume-slider');
    if(volumeSlider) {
        wavesurfer.setVolume(parseFloat(volumeSlider.value));
        volumeSlider.addEventListener('input', (e) => {
            wavesurfer.setVolume(parseFloat(e.target.value));
        });
    }

    // --- Render playlist from JSON and initialize ---
    function renderPlaylist(items) {
        const ul = document.getElementById('playlist');
        let firstTrack = true;
        ul.innerHTML = items.map(item => {
            if (item.type === 'section') {
                return `<li class="playlist-section-header"><span>- ${item.label} -</span></li>`;
            }
            const activeClass = firstTrack ? ' active' : '';
            firstTrack = false;
            return `<li class="playlist-item${activeClass}" data-src="${item.src}" data-title="${item.title}">
                <div class="track-name-wrapper"><div class="track-name">${item.title}</div></div>
                <div class="track-duration">${item.duration}</div>
            </li>`;
        }).join('');
    }

    function initPlaylist() {
        playlistItems = Array.from(document.querySelectorAll('.playlist-item'));

        // Playlist Clicks
        let clickCooldown = false;
        playlistItems.forEach((item, index) => {
            item.addEventListener('click', () => {
                if (clickCooldown) return;
                clickCooldown = true;
                setTimeout(() => { clickCooldown = false; }, 300);

                if(currentTrackIndex === index) {
                    togglePlay();
                } else {
                    pendingPlay = true;
                    currentTrackIndex = index;
                    loadTrack(index);
                }
            });
        });

        // Marquee effect for overflowing track names
        const marqueeObserver = new ResizeObserver(entries => {
            entries.forEach(entry => {
                const wrapper = entry.target;
                const trackName = wrapper.querySelector('.track-name');
                if (!trackName) return;

                if (trackName.scrollWidth > wrapper.clientWidth + 2) {
                    trackName.classList.add('scroll-pingpong');
                    const scrollDist = trackName.scrollWidth - wrapper.clientWidth + 20;
                    trackName.style.setProperty('--scroll-dist', `-${scrollDist}px`);
                    wrapper.style.maskImage = 'linear-gradient(to right, transparent 0%, black 5%, black 95%, transparent 100%)';
                    wrapper.style.webkitMaskImage = 'linear-gradient(to right, transparent 0%, black 5%, black 95%, transparent 100%)';
                } else {
                    trackName.classList.remove('scroll-pingpong');
                    trackName.style.removeProperty('--scroll-dist');
                    wrapper.style.maskImage = 'none';
                    wrapper.style.webkitMaskImage = 'none';
                }
            });
        });

        document.querySelectorAll('.track-name-wrapper').forEach(wrapper => {
            marqueeObserver.observe(wrapper);
        });

        // Load first track
        if (playlistItems.length > 0) {
            loadTrack(0);
        }

    }

    // --- Render Credits Grid from JSON ---
    let creditsItems = [];

    function renderCredits(items, lang) {
        if (items) creditsItems = items;
        const grid = document.getElementById('credits-poster-grid');
        if (!grid) return;
        const isZh = (lang || localStorage.getItem('luminium-lang') || 'en') === 'zh';
        grid.innerHTML = creditsItems.map(item => {
            const title   = isZh ? item.title   : (item.title_en   || item.title);
            const company = isZh ? item.company  : (item.company_en || item.company);
            const role    = isZh ? item.role     : (item.role_en    || item.role);
            const companyHtml = company ? `<span class="ct-company">${company}</span>` : '';
            return `<div class="credit-poster">
                <img src="assets/prortfolio/credit/${item.file}" alt="${title}">
                <div class="credit-tooltip">
                    <span class="ct-title">${title}</span>
                    ${companyHtml}
                    <span class="ct-platform">${item.platform}</span>
                    <span class="ct-role">${role}</span>
                </div>
            </div>`;
        }).join('');
    }

    document.addEventListener('langchange', function (e) {
        renderCredits(null, e.detail.lang);
    });

    // --- Render Video List from JSON ---
    let videoItems = [];

    function renderVideos(items, lang) {
        if (items) videoItems = items;
        const ul = document.getElementById('video-list');
        if (!ul) return;
        const isZh = (lang || localStorage.getItem('luminium-lang') || 'en') === 'zh';
        ul.innerHTML = videoItems.map(item => {
            if (item.type === 'section') {
                const label = isZh ? item.label : (item.label_en || item.label);
                return `<li class="video-list-section-header"><span>- ${label} -</span></li>`;
            }
            const title = isZh ? item.title : (item.title_en || item.title);
            const game = isZh ? item.game : (item.game_en || item.game || '');
            const role = isZh ? item.role : (item.role_en || item.role || '');
            return `<li class="video-list-item"
                data-url-cn="${item.url_cn || ''}"
                data-url-global="${item.url_global || ''}"
                data-title="${title}">
                <div class="vl-title">${title}</div>
                <div class="vl-game">${game}</div>
                <div class="vl-role">${role}</div>
            </li>`;
        }).join('');

        ul.querySelectorAll('.video-list-item').forEach(item => {
            item.addEventListener('click', () => {
                openJumpModal(
                    item.getAttribute('data-title'),
                    item.getAttribute('data-url-cn'),
                    item.getAttribute('data-url-global')
                );
            });
        });
    }

    document.addEventListener('langchange', function(e) {
        renderVideos(null, e.detail.lang);
    });

    function loadData(globalVar, fetchUrl, onData, onError) {
        if (window[globalVar]) {
            onData(window[globalVar]);
        } else {
            fetch(fetchUrl)
                .then(r => r.json())
                .then(onData)
                .catch(onError);
        }
    }

    loadData('videosData', 'assets/prortfolio/doc/videos.json',
        data => renderVideos(data.videos),
        err => console.error('Failed to load videos:', err));

    loadData('creditsData', 'assets/prortfolio/doc/credits.json',
        data => renderCredits(data.credits),
        err => console.error('Failed to load credits:', err));

    loadData('playlistData', 'assets/prortfolio/doc/playlist.json',
        data => { renderPlaylist(data.tracks); initPlaylist(); },
        err => console.error('Failed to load playlist:', err));

    // --- Volume Click-Toggle ---
    const volWrapper = document.querySelector('.hx-volume-wrapper');
    const volBtn = document.querySelector('.hx-volume-btn');
    if (volBtn && volWrapper) {
        volBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            volWrapper.classList.toggle('vol-open');
        });
        document.addEventListener('click', (e) => {
            if (!volWrapper.contains(e.target)) {
                volWrapper.classList.remove('vol-open');
            }
        });
    }

    // --- Sticky Player Shrink Detection ---
    const playerContainer = document.querySelector('.audio-player');
    if (playerContainer) {
        // Calculate threshold while player is still visible
        const threshold = playerContainer.offsetHeight;

        function checkSticky() {
            if (window.scrollY > threshold) {
                playerContainer.classList.add('is-stuck');
            } else {
                playerContainer.classList.remove('is-stuck');
            }
            requestAnimationFrame(checkSticky);
        }
        requestAnimationFrame(checkSticky);

        // Hide player on init if default tab is not music
        const initialTab = document.querySelector('.nav-sub-tab.active');
        if (!initialTab || initialTab.getAttribute('data-tab') !== 'audio-showcase') {
            playerContainer.classList.add('hidden');
        }
    }

    // --- Tab Navigation ---
    const tabBtns = document.querySelectorAll('.nav-sub-tab');
    const tabSections = document.querySelectorAll('.tab-section');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            tabBtns.forEach(b => b.classList.remove('active'));
            tabSections.forEach(s => s.classList.remove('active'));

            btn.classList.add('active');
            const targetId = btn.getAttribute('data-tab');
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                targetSection.classList.add('active');
            }

            if (targetId === 'audio-showcase') {
                playerContainer.classList.remove('hidden');
            } else {
                if (isPlaying) togglePlay();
                playerContainer.classList.add('hidden');
            }

            // Scroll to top on tab switch
            window.scrollTo({ top: 0, behavior: 'instant' });

            setTimeout(() => {
                if (window.locomotive) {
                    window.locomotive.update();
                } else if (window.scroll) {
                    window.scroll.update();
                }
            }, 550);
        });
    });

    // --- Video Jump Modal ---
    const vjOverlay = document.getElementById('video-jump-modal');
    const vjTitleEl = vjOverlay.querySelector('.vj-title');
    const vjBtnCn = document.getElementById('vj-btn-cn');
    const vjBtnGlobal = document.getElementById('vj-btn-global');
    const vjClose = vjOverlay.querySelector('.vj-close');

    function openJumpModal(title, urlCn, urlGlobal) {
        const isZh = (localStorage.getItem('luminium-lang') || 'en') === 'zh';
        vjTitleEl.textContent = title;

        const labelCn     = isZh ? '国内观看' : 'Watch (CN)';
        const labelGlobal = isZh ? '国外观看' : 'Watch (Global)';
        const labelNone   = isZh ? '暂无渠道'  : 'Not Available';

        if (urlCn) {
            vjBtnCn.textContent = labelCn;
            vjBtnCn.classList.remove('unavailable');
            vjBtnCn.onclick = () => window.open(urlCn, '_blank');
        } else {
            vjBtnCn.textContent = labelNone;
            vjBtnCn.classList.add('unavailable');
            vjBtnCn.onclick = null;
        }

        if (urlGlobal) {
            vjBtnGlobal.textContent = labelGlobal;
            vjBtnGlobal.classList.remove('unavailable');
            vjBtnGlobal.onclick = () => window.open(urlGlobal, '_blank');
        } else {
            vjBtnGlobal.textContent = labelNone;
            vjBtnGlobal.classList.add('unavailable');
            vjBtnGlobal.onclick = null;
        }

        vjOverlay.classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeJumpModal() {
        vjOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    vjClose.addEventListener('click', closeJumpModal);
    vjOverlay.addEventListener('click', (e) => { if (e.target === vjOverlay) closeJumpModal(); });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeJumpModal(); });
});
