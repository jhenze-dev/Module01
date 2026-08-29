import puppeteer from "puppeteer";
import { pathToFileURL } from "url";
import path from "path";

const [, , inputArg, outputArg] = process.argv;

if (!inputArg || !outputArg) {
    console.error(
        "Gebruik: node render_pdf.mjs <input.html> <output.pdf>"
    );
    process.exit(1);
}

const inputPath = path.resolve(inputArg);
const outputPath = path.resolve(outputArg);

const browser = await puppeteer.launch({
    headless: true,
});

try {
    const page = await browser.newPage();

    const inputUrl = pathToFileURL(inputPath).href;

    await page.goto(inputUrl, {
        waitUntil: "networkidle0",
    });

    await page.pdf({
        path: outputPath,
        format: "A4",
        printBackground: true,
    });

} finally {
    await browser.close();
}
