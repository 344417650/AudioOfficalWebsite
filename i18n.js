(function () {
    const translations = {
        en: {
            // Nav
            'nav.home': 'Home',
            'nav.studio': 'Studio',
            'nav.portfolio': 'Portfolio',
            'nav.blog': 'Blog',
            'nav.contact': "Let's Talk",
            // Footer
            'footer.copy': '\u00a9 2026 LUMINIUM STUDIO. ALL RIGHTS RESERVED.',
            // index.html — Hero
            'hero.subtitle': 'Luminium Studio is a premier creative audio house in Chongqing & Nanjing. We deliver AAA quality sound design, original music, voice over, and audio programming for global interactive media.',
            'hero.btn.reel': 'Watch Reel',
            'hero.btn.services': 'Our Services',
            // Founders section
            'section.founders': 'The Founders',
            'gk.title': 'Music Director<br>Lead Composer',
            'gk.desc': 'Former Audio Director at Sunborn Network and Sofunny Network; former Audio Director at Vanguard Sound.',
            'gk.skill.1': 'Music Production',
            'gk.skill.2': 'Audio Mixing',
            'gk.skill.3': 'Mastering',
            'gk.skill.4': 'Sound Design',
            'gk.works': '<strong>Selected Works:</strong> Audio Director on <em>Nano Core</em> and <em>Girls\' Frontline</em>; Lead Composer on <em>Boundary</em>; contributed to <em>Azur Lane</em>, <em>Punishing: Gray Raven</em>, and more.',
            'gk.extra': 'Business-level English and Japanese; experienced in overseas resource coordination and live performance direction.',
            'breakless.title': 'Sound Director<br>Lead Sound Designer / Audio Programmer',
            'breakless.desc': 'Former Audio Director at HyperGryph and BoomingTech; former Sound Designer at Vanguard Sound.',
            'breakless.skill.1': 'Sound Design',
            'breakless.skill.2': 'System Design',
            'breakless.skill.3': 'Audio Integration',
            'breakless.skill.4': 'Sound Direction',
            'breakless.works': '<strong>Selected Works:</strong> Audio Director on <em>Arknights</em>; Lead Sound Designer on <em>Langrisser Mobile</em>, <em>Love &amp; Producer</em>, and more; contributed to <em>Call of Duty Mobile</em>, <em>Punishing: Gray Raven</em>, and more.',
            'breakless.extra': 'Proficient in audio programming and architecture across major engines; extensive experience in audio system planning and implementation.',
            // Services
            'section.services': 'Our Services',
            'service.sd.title': 'Sound Design',
            'service.sd.desc': 'Award-winning AAA quality sound effects and custom audio synthesis.',
            'service.music.title': 'Original Music',
            'service.music.desc': 'Cinematic scores, interactive music systems, and emotive compositions.',
            'service.vo.title': 'Voice Over',
            'service.vo.desc': 'Global casting, directing, and localization tailored for immersive storytelling.',
            'service.impl.title': 'Audio Implementation',
            'service.impl.desc': 'Technical integration using Wwise, FMOD, Unreal, and Unity.',
            'service.prog.title': 'Audio Programming',
            'service.prog.desc': 'Custom audio systems, runtime DSP, and engine-level solutions built for performance and creative control.',
            // Clients
            'section.clients': 'Trusted By',
            // Portfolio
            'section.videoreel': 'Video Reel',
            'section.recentworks': 'Recent Works',
            'tab.credits': 'Credits',
            'tab.music': 'Music',
            'tab.video': 'Video',
            'player.select': 'SELECT A TRACK',
            'btn.downloadAll': 'DOWNLOAD ALL',
            'vj.label': 'WATCH ON',
            // Blog
            'blog.title.1': 'KNOWLEDGE',
            'blog.title.2': 'BASE',
            'blog.subtitle': 'Insights, tutorials, and behind the scenes from the Luminium Audio Team.',
            'blog.soon': 'Coming Soon',
            // Trust / About
            'trust.title': 'Reliability & Creativity',
            'trust.quote': '\u201cLuminium Studio stands as a cornerstone of reliability and excellence. Their dedication to delivering top-notch AAA quality, swift response to feedback, and profound expertise make them an invaluable partner in game audio.\u201d',
            'trust.client': 'Industry Leading Developers',
            // Lang toggle button label (shows current language)
            'lang.toggle': 'EN',
        },
        zh: {
            // Nav
            'nav.home': '\u9996\u9875',
            'nav.studio': '\u5de5\u4f5c\u5ba4',
            'nav.portfolio': '\u4f5c\u54c1\u96c6',
            'nav.blog': '\u535a\u5ba2',
            'nav.contact': '\u8054\u7cfb\u6211\u4eec',
            // Footer
            'footer.copy': '\u00a9 2026 LUMINIUM STUDIO. \u7248\u6743\u6240\u6709\u3002',
            // index.html — Hero
            'hero.subtitle': 'Luminium Studio \u662f\u4f4d\u4e8e\u91cd\u5e86\u4e0e\u5357\u4eac\u7684\u9876\u5c16\u521b\u610f\u97f3\u9891\u5de5\u4f5c\u5ba4\uff0c\u4e3a\u5168\u7403\u4e92\u52a8\u5a92\u4f53\u63d0\u4f9b AAA \u7ea7\u522b\u97f3\u6548\u5236\u4f5c\u3001\u539f\u521b\u97f3\u4e50\u3001\u914d\u97f3\u4ee5\u53ca\u97f3\u9891\u7a0b\u5e8f\u670d\u52a1\u3002',
            'hero.btn.reel': '\u89c2\u770b\u4f5c\u54c1\u96c6',
            'hero.btn.services': '\u6211\u4eec\u7684\u670d\u52a1',
            // Founders section
            'section.founders': '\u521b\u59cb\u4eba',
            'gk.title': '\u97f3\u4e50\u603b\u76d1<br>\u4e3b\u4f5c\u66f2',
            'gk.desc': '\u539f\u6563\u7206\u7f51\u7edc\u3001\u771f\u6709\u8da3\u7f51\u7edc\u97f3\u9891\u603b\u76d1\uff0c\u66fe\u4efbVanguard Sound\u97f3\u9891\u603b\u76d1\u3002',
            'gk.skill.1': '\u97f3\u4e50\u5236\u4f5c',
            'gk.skill.2': '\u97f3\u9891\u6df7\u97f3',
            'gk.skill.3': '\u6bcd\u5e26\u5904\u7406',
            'gk.skill.4': '\u97f3\u54cd\u6548\u679c',
            'gk.works': '<strong>\u4ee3\u8868\u4f5c:</strong>\u62c5\u4efb\u300a\u7eb3\u7c73\u6838\u5fc3\u300b\u300a\u5c11\u5973\u524d\u7ebf\u300b\u7b49\u9879\u76ee\u97f3\u9891\u603b\u76d1\uff1b\u300a\u8fb9\u5883\u300b\u4e3b\u4f5c\u66f2\uff1b\u53c2\u4e0e\u300a\u78a7\u84dd\u822a\u7ebf\u300b\u300a\u6218\u53cc\u5e15\u5f25\u4ec0\u300b\u7b49\u97f3\u4e50\u5236\u4f5c\u3002',
            'gk.extra': '\u7cbe\u901a\u5546\u52a1\u7ea7\u82f1\u65e5\u8bed\uff0c\u64c5\u957f\u6d77\u5916\u8d44\u6e90\u6574\u5408\uff0c\u5177\u591a\u573a\u6f14\u51fa\u4e3b\u5bfc\u7ecf\u9a8c\u3002',
            'breakless.title': '\u97f3\u6548\u603b\u76d1<br>\u4e3b\u97f3\u6548\u8bbe\u8ba1\u5e08 / \u97f3\u9891\u7a0b\u5e8f',
            'breakless.desc': '\u539f\u9e70\u89d2\u7f51\u7edc\u3001\u4e0d\u9e23\u79d1\u6280\u97f3\u9891\u603b\u76d1\uff0c\u66fe\u4efbVanguard Sound\u97f3\u9891\u8bbe\u8ba1\u5e08\u3002',
            'breakless.skill.1': '\u97f3\u6548\u5236\u4f5c',
            'breakless.skill.2': '\u65b9\u6848\u8bbe\u8ba1',
            'breakless.skill.3': '\u97f3\u9891\u6574\u5408',
            'breakless.skill.4': '\u97f3\u54cd\u6548\u679c',
            'breakless.works': '<strong>\u4ee3\u8868\u4f5c:</strong>\u62c5\u4efb\u300a\u660e\u65e5\u65b9\u821f\u300b\u9879\u76ee\u97f3\u9891\u603b\u76d1\uff1b\u300a\u68a6\u5e7b\u6a21\u62df\u6218\u300b\u300a\u604b\u4e0e\u5236\u4f5c\u4eba\u300b\u7b49\u4e3b\u97f3\u6548\uff1b\u53c2\u4e0e\u300a\u4f7f\u547d\u53ec\u5524\u624b\u6e38\u300b\u300a\u6218\u53cc\u5e15\u5f25\u4ec0\u300b\u7b49\u97f3\u6548\u5236\u4f5c\u3002',
            'breakless.extra': '\u7cbe\u901a\u5e38\u7528\u5f15\u64ce\u53ca\u5bf9\u5e94\u8bed\u8a00\u7684\u97f3\u9891\u7a0b\u5e8f\u67b6\u6784\u5f00\u53d1\uff0c\u5177\u4e30\u5bcc\u97f3\u9891\u65b9\u6848\u7b56\u5212\u4e0e\u6267\u884c\u7ecf\u9a8c\u3002',
            // Services
            'section.services': '\u670d\u52a1\u9879\u76ee',
            'service.sd.title': '\u97f3\u6548\u5236\u4f5c',
            'service.sd.desc': '\u5c61\u83b7\u6b8a\u8363\u7684 AAA \u7ea7\u97f3\u6548\u4e0e\u81ea\u5b9a\u4e49\u97f3\u9891\u5408\u6210\u3002',
            'service.music.title': '\u539f\u521b\u97f3\u4e50',
            'service.music.desc': '\u7535\u5f71\u7ea7\u914d\u4e50\u3001\u4e92\u52a8\u97f3\u4e50\u7cfb\u7edf\u53ca\u5bcc\u6709\u611f\u67d3\u529b\u7684\u539f\u521b\u4f5c\u54c1\u3002',
            'service.vo.title': '\u914d\u97f3\u5236\u4f5c',
            'service.vo.desc': '\u5168\u7403\u9009\u89d2\u3001\u5f55\u97f3\u6307\u5bfc\u4e0e\u672c\u5730\u5316\uff0c\u4e3a\u6c89\u6d78\u5f0f\u53d9\u4e8b\u91cf\u8eab\u6253\u9020\u3002',
            'service.impl.title': '\u97f3\u9891\u5b9e\u73b0',
            'service.impl.desc': '\u57fa\u4e8e Wwise\u3001FMOD\u3001Unreal \u53ca Unity \u7684\u4e13\u4e1a\u97f3\u9891\u96c6\u6210\u3002',
            'service.prog.title': '\u97f3\u9891\u7a0b\u5e8f',
            'service.prog.desc': '\u81ea\u5b9a\u4e49\u97f3\u9891\u7cfb\u7edf\u3001\u5b9e\u65f6 DSP \u53ca\u5f15\u64ce\u7ea7\u89e3\u51b3\u65b9\u6848\uff0c\u517c\u987e\u6027\u80fd\u4e0e\u521b\u610f\u63a7\u5236\u3002',
            // Clients
            'section.clients': '\u5408\u4f5c\u5ba2\u6237',
            // Portfolio
            'section.videoreel': '\u89c6\u9891\u4f5c\u54c1',
            'section.recentworks': '\u8fd1\u671f\u4f5c\u54c1',
            'tab.credits': '\u4f5c\u54c1',
            'tab.music': '\u97f3\u4e50',
            'tab.video': '\u89c6\u9891',
            'player.select': '\u8bf7\u9009\u62e9\u66f2\u76ee',
            'btn.downloadAll': '\u4e0b\u8f7d\u5168\u90e8',
            'vj.label': '\u89c2\u770b\u6e20\u9053',
            // Blog
            'blog.title.1': '\u77e5\u8bc6',
            'blog.title.2': '\u5e93',
            'blog.subtitle': '\u6765\u81ea Luminium \u97f3\u9891\u56e2\u961f\u7684\u6d1e\u89c1\u3001\u6559\u7a0b\u4e0e\u5e55\u540e\u6545\u4e8b\u3002',
            'blog.soon': '\u5373\u5c06\u63a8\u51fa',
            // Trust / About
            'trust.title': '\u53ef\u9760\u6027\u4e0e\u521b\u9020\u529b',
            'trust.quote': '\u201cLuminium Studio \u662f\u53ef\u9760\u6027\u4e0e\u5353\u8d8a\u54c1\u8d28\u7684\u57fa\u77f3\u3002\u4ed6\u4eec\u5bf9\u9876\u7ea7 AAA \u54c1\u8d28\u7684\u6267\u7740\u8ffd\u6c42\u3001\u5bf9\u53cd\u9988\u7684\u8fc5\u901f\u54cd\u5e94\u4ee5\u53ca\u6df1\u539a\u7684\u4e13\u4e1a\u79ef\u7d2f\uff0c\u4f7f\u5176\u6210\u4e3a\u6e38\u620f\u97f3\u9891\u9886\u57df\u4e0d\u53ef\u6216\u7f3a\u7684\u5408\u4f5c\u4f19\u4f34\u3002\u201d',
            'trust.client': '\u4e1a\u754c\u9886\u5148\u5f00\u53d1\u5546',
            // Lang toggle button label (shows current language)
            'lang.toggle': '\u4e2d\u6587',
        }
    };

    let currentLang = localStorage.getItem('luminium-lang') || 'en';

    function applyLang(lang) {
        currentLang = lang;
        localStorage.setItem('luminium-lang', lang);
        document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
        var t = translations[lang];

        // data-i18n → textContent
        document.querySelectorAll('[data-i18n]').forEach(function (el) {
            var key = el.getAttribute('data-i18n');
            if (t[key] !== undefined) el.textContent = t[key];
        });

        // data-i18n-html → innerHTML
        document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
            var key = el.getAttribute('data-i18n-html');
            if (t[key] !== undefined) el.innerHTML = t[key];
        });

        // Update audio player placeholder (only when no track is loaded)
        var playerTitle = document.getElementById('current-title');
        if (playerTitle) {
            var placeholders = [translations.en['player.select'], translations.zh['player.select']];
            if (placeholders.indexOf(playerTitle.textContent.trim()) !== -1) {
                playerTitle.textContent = t['player.select'];
            }
        }

        // Update all toggle button labels
        document.querySelectorAll('.lang-toggle-btn').forEach(function (btn) {
            btn.textContent = t['lang.toggle'];
        });

        // Notify other scripts that language changed
        document.dispatchEvent(new CustomEvent('langchange', { detail: { lang: lang } }));
    }

    function toggleLang() {
        applyLang(currentLang === 'en' ? 'zh' : 'en');
    }

    document.addEventListener('DOMContentLoaded', function () {
        document.querySelectorAll('.lang-toggle-btn').forEach(function (btn) {
            btn.addEventListener('click', toggleLang);
        });
        applyLang(currentLang);
    });

    window.i18n = { applyLang: applyLang, toggleLang: toggleLang };
})();
