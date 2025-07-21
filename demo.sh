#!/bin/bash

echo "🚀 Starting Seller Risk MLOps Platform Demo"
echo "=========================================="

# Check if we're in the right directory
if [ ! -f "package.json" ]; then
    echo "❌ Error: Please run this script from the seller-risk-mlops directory"
    exit 1
fi

echo "📦 Installing dependencies..."
npm install

echo "🔨 Building the application..."
npm run build

if [ $? -eq 0 ]; then
    echo "✅ Build successful!"
    echo ""
    echo "🌐 Starting the demo server on http://localhost:3000"
    echo ""
    echo "📖 Platform Features:"
    echo "   • Multi-persona dashboards (Data Scientist, MLOps Engineer, Risk Ops, Executive)"
    echo "   • Interactive workflow visualization with 4 deployment flows"
    echo "   • Real-time performance simulation and monitoring"
    echo "   • Feature store integration and model registry"
    echo "   • Natural language strategy input interface"
    echo ""
    echo "🎯 Key Capabilities:"
    echo "   • <50ms inference latency simulation"
    echo "   • 100K+ TPS throughput monitoring"
    echo "   • 89.7% fraud prevention rate tracking"
    echo "   • End-to-end MLOps workflow demonstration"
    echo ""
    echo "Press Ctrl+C to stop the server"
    echo "=========================================="
    
    # Start the server
    npx serve -s build -p 3000
else
    echo "❌ Build failed. Please check for errors and try again."
    exit 1
fi