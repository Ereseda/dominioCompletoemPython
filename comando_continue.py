for tech_skills in "Python", "Liderança Técnica", "PHP", "Scrum", "Java", "Agile Management":
    if (tech_skills == "Java" or tech_skills =="Python"):
        print(tech_skills, "Developer")
        continue
    if (tech_skills == "Agile Management"):
        break
    if (tech_skills == "Liderança Técnica"):
        print(tech_skills == "tech lead")
    if (tech_skills == "PHP"):
        print(tech_skills, "Project Manager")
print("RH, favor seguir com os candidatos para a etapa de entrevista técnica")        