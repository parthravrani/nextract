const puppeteer = require('puppeteer');
const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

// Simple HTTP server to serve HTML files
function startServer(port = 8080) {
    return new Promise((resolve) => {
        const server = http.createServer((req, res) => {
            const parsedUrl = new URL(req.url, `http://localhost:${port}`);
            let filePath = '.' + parsedUrl.pathname;
            if (filePath === './') filePath = './pitch-deck.html';
            
            const extname = String(path.extname(filePath)).toLowerCase();
            const mimeTypes = {
                '.html': 'text/html',
                '.js': 'text/javascript',
                '.css': 'text/css',
                '.json': 'application/json',
                '.png': 'image/png',
                '.jpg': 'image/jpg',
                '.gif': 'image/gif',
                '.svg': 'image/svg+xml',
                '.wav': 'audio/wav',
                '.mp4': 'video/mp4',
                '.woff': 'application/font-woff',
                '.ttf': 'application/font-ttf',
                '.eot': 'application/vnd.ms-fontobject',
                '.otf': 'application/font-otf',
                '.wasm': 'application/wasm'
            };

            const contentType = mimeTypes[extname] || 'application/octet-stream';

            fs.readFile(filePath, (error, content) => {
                if (error) {
                    if (error.code === 'ENOENT') {
                        res.writeHead(404);
                        res.end('File not found');
                    } else {
                        res.writeHead(500);
                        res.end('Server error: ' + error.code);
                    }
                } else {
                    res.writeHead(200, { 'Content-Type': contentType });
                    res.end(content, 'utf-8');
                }
            });
        });

        server.listen(port, () => {
            console.log(`Server running on http://localhost:${port}`);
            resolve(server);
        });
    });
}

async function generatePDF(htmlFile, outputFile, port, landscape = true) {
    console.log(`\nGenerating PDF from ${htmlFile}...`);
    
    const browser = await puppeteer.launch({
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    
    const page = await browser.newPage();
    
    // Set viewport based on orientation
    if (landscape) {
        // A4 landscape dimensions
        await page.setViewport({
            width: 1123,
            height: 794,
            deviceScaleFactor: 1
        });
    } else {
        // A4 portrait dimensions
        await page.setViewport({
            width: 794,
            height: 1123,
            deviceScaleFactor: 1
        });
    }
    
    // Load the HTML file via HTTP server
    await page.goto(`http://localhost:${port}/${htmlFile}`, {
        waitUntil: 'networkidle0',
        timeout: 30000
    });
    
    // Wait a bit for any animations or dynamic content
    await new Promise(resolve => setTimeout(resolve, 1500));
    
    // Generate PDF with print-optimized settings
    await page.pdf({
        path: outputFile,
        format: 'A4',
        landscape: landscape,
        printBackground: true,
        margin: {
            top: '0',
            right: '0',
            bottom: '0',
            left: '0'
        },
        preferCSSPageSize: true,
        displayHeaderFooter: false,
        pageRanges: '1-999'
    });
    
    await browser.close();
    console.log(`✓ PDF generated: ${outputFile}`);
}

async function main() {
    const port = 8080;
    let server;
    
    try {
        // Start HTTP server
        server = await startServer(port);
        
        // Wait for server to be ready
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        // Generate pitch deck PDF (landscape)
        await generatePDF('pitch-deck.html', 'Nextract-Pitch-Deck.pdf', port, true);
        
        // Generate social media posts PDF (landscape)
        await generatePDF('social-media-posts.html', 'Nextract-Social-Media-Posts.pdf', port, true);
        
        // Generate salary slip PDF (portrait)
        await generatePDF('salary-slip.html', 'Nextract-Salary-Slip.pdf', port, false);
        
        console.log('\n✅ All PDFs generated successfully!');
        console.log('\nGenerated files:');
        console.log('  - Nextract-Pitch-Deck.pdf');
        console.log('  - Nextract-Social-Media-Posts.pdf');
        console.log('  - Nextract-Salary-Slip.pdf');
        
    } catch (error) {
        console.error('Error generating PDFs:', error);
        process.exit(1);
    } finally {
        if (server) {
            server.close();
        }
    }
}

main();
