"""
Setup script for Ascend AI Analyzer
"""
import os
import subprocess
import sys
from pathlib import Path

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing requirements: {e}")
        return False
    return True

def setup_neo4j():
    """Setup Neo4j database"""
    print("🗄️ Setting up Neo4j database...")
    
    # Check if Neo4j is running
    try:
        from neo4j import GraphDatabase
        driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
        with driver.session() as session:
            session.run("RETURN 1")
        driver.close()
        print("✅ Neo4j connection successful")
        return True
    except Exception as e:
        print(f"⚠️ Neo4j not accessible: {e}")
        print("Please ensure Neo4j is running on bolt://localhost:7687")
        print("Default credentials: neo4j/password")
        return False

def create_directories():
    """Create necessary directories"""
    print("📁 Creating directories...")
    directories = ["data", "reports", "static"]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"  • Created {directory}/")
    
    return True

def setup_environment():
    """Setup environment variables"""
    print("🔧 Setting up environment...")
    
    env_content = """# Ascend AI Analyzer Environment Variables
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password
DEBUG=False
"""
    
    with open(".env", "w") as f:
        f.write(env_content)
    
    print("✅ Environment file created (.env)")
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up Ascend AI Analyzer")
    print("=" * 40)
    
    # Create directories
    if not create_directories():
        return 1
    
    # Install requirements
    if not install_requirements():
        return 1
    
    # Setup environment
    if not setup_environment():
        return 1
    
    # Check Neo4j
    neo4j_ok = setup_neo4j()
    
    print("\n" + "=" * 40)
    print("✅ SETUP COMPLETE!")
    print("=" * 40)
    
    if neo4j_ok:
        print("🎉 All components ready!")
        print("\nNext steps:")
        print("1. Run analysis: python analyze_comcast_data.py")
        print("2. Start API server: python app.py")
        print("3. Start dashboard: python dashboard.py")
    else:
        print("⚠️ Setup complete, but Neo4j needs attention")
        print("\nTo complete setup:")
        print("1. Install and start Neo4j")
        print("2. Update .env with correct credentials")
        print("3. Run: python analyze_comcast_data.py")
    
    return 0

if __name__ == "__main__":
    exit(main())
