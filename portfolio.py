import yaml
from classes.portfolio_page import PortfolioPage
from classes.project import Project

def main(portfolio_file='portfolio.yml'):
	details, projects = load_config(portfolio_file)

	portfolio = PortfolioPage(details, projects)
	print(portfolio.html)

# Loads projects from the YAML file
def load_config(file_path):
	f = open(file_path)
	dataMap = yaml.safe_load(f)
	f.close()

	projects = []

	for project in dataMap['Projects']:
		projects.append(Project(**dataMap['Projects'][project]))

	return dataMap['Portfolio'], projects

if __name__ == "__main__":
	main()