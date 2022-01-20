const text = document.querySelectorAll('h1, h2, h3, h4, h5, p, li, td, caption, span, a')

// place words you want to blacklist in the conditions , and replace the worlds in the .replace section ! example as follows:
// tested on this site (or just search up dr. oz): https://www.google.com/search?gs_ssp=eJzj4tTP1TdIMs8uKDdg9GJNKVLIrwIAMcMFWQ&q=dr+oz&rlz=1C1CHBF_enCA926CA926&oq=dr+oz&aqs=chrome.1.69i57j46i433i512j46i131i433i512j0i131i433j0i131i433i512j0i512l4j0i131i433i512.9099j0j7&sourceid=chrome&ie=UTF-8
for (let i = 0; i < text.length; i++) {
    if (text[i].innerHTML.includes('Mehmet Oz')) {
        text[i].innerHTML = text[i].innerHTML.replace('Mehmet Oz', 'Dr. Phil :)')
    } else if (text[i].innerHTML.includes('Doctor Oz')) {
        text[i].innerHTML = text[i].innerHTML.replace('Doctor Oz', 'Dr. Phil :)')
    } else if (text[i].innerHTML.includes('Dr.Oz')) {
        text[i].innerHTML = text[i].innerHTML.replace('Dr. Oz', 'Dr. Phil :)')
    } else if (text[i].innerHTML.includes('Mehmet Cengiz Öz')) {
        text[i].innerHTML = text[i].innerHTML.replace('Mehmet Cengiz Öz', 'Phil McGraw :)')
    }
}