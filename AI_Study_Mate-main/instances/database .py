import sqlite3

from tabulate import tabulate
connect_to = sqlite3.connect('database.db')
cursor = connect_to.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS maths (
         topic_name PRIMARY KEY,
        video_link TEXT NOT NULL
    )
''')


data = [
    ('sets introduction', 'https://youtu.be/7KFUH7uGQZ4?feature=shared'),
    ('empty set, infinite set, singleton sets', 'https://youtu.be/TbQJcw5WHWg?feature=shared'),
    ('introduction to Cartesian Products of Sets relations, introduction functions ','https://youtu.be/wZzzCcIACr4?feature=shared'),
('introduction to angles ,Notational Convention ,Trigonometric Functions Domain and range of trigonometric functions','https://youtu.be/zGFBw_8CCeY?feature=shared'), 
('Complex Numbers, Algebra of Complex Numbers ,The Modulus and the Conjugate of a Complex Number','https://youtu.be/XKWzISrb3X4?feature=shared'), 
('Inequalities, Algebraic Solutions of Linear Inequalities in One Variable and their Graphical Representation','https://youtu.be/XKWzISrb3X4?feature=shared'),
('Inequalities, Algebraic Solutions of Linear Inequalities in One Variable and their Graphical Representation',' https://youtu.be/lnuBo9SINxQ?feature=shared'),
('Permutations and combination, Fundamental Principle of Counting permutations combination','https://youtu.be/N7MNPVB75_s?feature=shared'),  
('Binomial Theorem for Positive Integral Indices, Pascal Triangle, Binomial theorem for any positive integer n','https://youtu.be/uqNF4asObC0?feature=shared'), 
('Sequence, series, geometric progression  ,arithmetic progression  ','https://youtu.be/mTKoHsZSWGk?feature=shared'), 
('Geometric progression relationship between A.M G.M','https://youtu.be/iPeXpsqrXe4?feature=shared'), 
('The slope of line angle between two lines, collinearity of three points , various forms of eqautiion of line point, slope form and two form','https://youtu.be/IXZLiqwNrcM?feature=shared'), 
('The slope of intercept form normal form, general equations of a line distance between two parallel lines','https://youtu.be/P4KTQo4HSCE?feature=shared'), 
('Conic sections, ellipse, parabola,hyperbola , degenerate comix,','https://youtu.be/HO2zAU3Eppo?feature=shared'), 
('Lactus rectum','https://youtu.be/eXqy296wYpM?feature=shared'), 
('Ellipse','https://youtu.be/da99zdE6nJc?feature=shared'), 
('Three-dimensional geometry','https://youtu.be/yPysmMXI_Is?feature=shared'), 
(' Distance between Two Points','https://youtu.be/BXzj9mJvTKQ?feature=shared'), 
(' Intuitive Idea of Derivatives Limits derivatives','https://youtu.be/AXuNOHNRg0o?feature=shared'),     
('Derivatives',' https://youtu.be/N2PpRnFqnqY?feature=shared'), 
('Random experiment, event, Axiomatic Approach to Probability, Probability of an event', 'https://youtu.be/vJy_s-TvUXE?feature=shared'),



    ('Introduction to Computer', "https://youtu.be/qfUZBKDh9BY?si=z8oYXonEDMIRIA0w"),
    # (other data entries here)
    ('Functional components of a computer',"https://youtu.be/dUHHr--WGsc?si=C0FGPq_yrnAsGZOQ"),

('Evolution of the computer',"https://youtu.be/rKjfb9vscVM?si=eH5jpg8g4vQou9iS"),

('Generations of computers',"https://youtu.be/NqgpZ_v4Ne8?si=coXzbdsPVFQ_20pk"),

('Classifications of computer',"https://youtu.be/h7p52L7SQe0?si=EzA2OF05Py1xSFV8"),

('Applications of computers',"https://youtube.com/shorts/zZVguBsaN64?si=DceWj-nljqplI8CU"),

('Introduction to input devices',"https://youtu.be/wUHGN-B1tt0?si=0JPgbUcqU8Q_R8IA"),

('The OMR, OCR, MICR',"https://youtu.be/xnwNPo--kk8?si=nMc2gpAPJyMag1DX"),


('Introduction to output devices',"https://youtu.be/KV_L3a0Cl3U?si=ByJkOXq8nN2_nvPT"),

('Introduction to Memory devices ( Primary Memory and Secondary Memory Cache Memory)',"https://youtu.be/c3m9r62jMS8?si=4KCdgJEAqvCl763r"),


('Data representataion and conversion',"https://youtu.be/G6Lv7REHdOQ?si=7ajpP4Hlrvv0qEiH"),


('Sign and Magnitude representation',"https://youtu.be/zMX2WERv74k?si=1ugNIyE1Awi3B6RX"),


(' Ones and Twos Complement   representation',"https://youtu.be/pXIfEklKsOQ?si=-bfqdM9wdOUGf0iJ"),


 ('Binary Arithmetic:Addition and Subtraction of binary numbers',"https://youtu.be/AE-27BSbkJ4?si=Q4MQV0XnzioUVWWh"),


('Subtraction using 1s complement',"https://youtu.be/lbo-P2WZe9Y?si=rEwG8-9E5YCn_6ss"),
('Subtraction using 2s Complement',"https://youtu.be/zvznt6XYTXY?si=DByYYTtvqckcYBcs"),


('Computer Codes: Introduction to BCD  EBCDIC ASCII and  Excess-3',"https://youtu.be/0UVSPwzGw4U?si=phKogoWO9qTy_FVq"),


('Introduction Types Of Software (Application and System software)',"https://youtu.be/riRKu15_dCE?si=cLNRv1hYeMCWK42v"),


(' Introduction to Operating Systems and their Functions',"https://youtu.be/WJ-UaAaumNA?si=p0Cu95jLyDwr-MLL"),


('Types Of Operating Systems',"https://youtu.be/s-tk8el8JoU?si=UO6_eeTh_y5PiaZ7"),

('Types of software',"https://youtu.be/hD0db1VkVoU?si=7eSDpUed0YcR9yaP"),

('Types of interfaces',"https://youtu.be/qsX32Sh4DEA?si=lEsqLwS75n6XIcOR"),

 
('Steps of  Problem Solving',"https://youtu.be/1VqMViLFbYY?si=OYGnDjcrKAg4Mmum"),

 
('Programming Constructs (Sequence  Selection  and Iteration)',"https://youtu.be/cLRCz7gKsBo?si=4AdUI2dXDTEzGaYd"),

('Types Of Errors',"https://youtu.be/d6CrQBM4kW0?si=cWdUWnsfVDkmcpRz"),

 ('Approaches to Problem-Solving (Top-down Bottom-up  Modular  Structured)',"https://youtu.be/cjgGrlhL30c?si=zt7QWQ-fK9KwKZ4l"),

('Programming techniques',"https://youtu.be/yW90RGeRDOE?si=zscIe2D8yraPJZEu"),

('Basic Concepts of OOP',"https://youtu.be/D6HH9BqR9fQ?si=ACZGVKKcVFykUnUi"),

('Characteristics of OOPS',"https://youtu.be/40SkIa7iog4?si=9Y17ZAcQ2DBzA5p-"),

('Advantages and disadvantages of OOP',"https://youtu.be/6ybYX9Lz4-c?si=BkdFR5ceR30MqFiR"),

('Characteristics of C++',"https://youtu.be/5V9mtMX2Ktc?si=bSnVhRsWPCem4Kac"),

 ('C++ Character Set ',"https://youtu.be/5V9mtMX2Ktc?si=bSnVhRsWPCem4Kac"),

('Types of Operators',"https://youtu.be/V6pufdvxBfE?si=CKlTqGYS99SyRsGK"),

('Type conversion (Implicit and Explicit)',"https://youtu.be/ql2F5Am3_9E?si=Nu-dM7NsLRWm7egh"),

 ('Structure of a C++ program (with example)',"https://youtu.be/uqbLWH7EQUU?si=zMUxyUtHguMjxrch"),

 ('Data types',"https://youtu.be/pi0APsRmEpA?si=_Yf2-JDmMtEIHXnf"),

('Input and Output Input operator">>" and Output operator "<<<"',"https://youtu.be/KbRviay23ho?si=i3RatqXosPq6DfrO"),

('Library functions',"https://youtu.be/rGSuzaT7E1g?si=Eu7EFsU-qB8LbdM2"),

('Types Of Control Statements Selection statements',"https://youtu.be/YiPoFeWrSYY?si=XVfzK3OTASfpdPZc"),

('Iteration statement',"https://youtu.be/PQJqfqxS6cg?si=mUzbWyHwoKpSz5_p"),

('Jump statements (goto, break, continue)',"https://youtu.be/zWodzzfTqTY?si=gV_uQvMZhok_oNQm"),

('Arrays and types',"https://youtu.be/DocpqYMnOXs?si=oevGGTb7Y7lJDRMv"),

('Initialization and declaration of 1-D arrays',"https://youtu.be/VgONsOtEuZw?si=q3OPFwkekxLTlb3D"),

('Initialization and declaration of 2-D arrays',"https://youtu.be/nC2Ygv33Tvg?si=G-VRLXVH6dt8PXLB"),

('Types of  functions',"https://youtu.be/mSLfuypD-AQ?si=_elbxo41GME6Yom6"),
 
('String functions',"https://youtu.be/E7T2cnSjO3M?si=OvOSvNi4QHEqtoUF"),


 ('Returning a value',"https://youtu.be/9sj5TJOtsxo?si=WVVLfWC3T7Jsr5L3"),

('Function prototype',"https://youtu.be/vc9A6HdrTz4?si=mJs1mD6ulGFvtsjn"),

('Types of arguments Scope of variables',"https://youtu.be/elMQ5YtZPxA?si=r4GW9LuzzdCihLom"),

(' Types of Functions',"https://youtu.be/CGRt0T5LOOM?si=_C8HdUvQ4Iaigtgx"),

('Call by value and Call by reference (using reference variables)',"https://youtu.be/HEiPxjVR8CU?si=aDVEuoIjpxyv7ct"),

('Arrays as arguments',"https://youtu.be/gNlmJ2WrZSY?si=MvFNwHK8xIxwwF36"),

('Introduction to Structures',"https://youtu.be/vqtyDXFlS98?si=HI-mI-r01gJkVZqQ"),

('Referencing structure elements',"https://youtu.be/otu7gJVcwDw?si=DDy4KiRp9BowYz-S"),

('Nested structures',"https://youtu.be/cAgj7aVjCp4?si=9Bgh0Bg7P1Bx5lz7"),

('Array of structures',"https://youtu.be/EGeIsvx4Wns?si=cSGDRg2IlW4se_3e"),

('Elementary Concepts of Word Processing',"https://youtu.be/ViYa5Rkbq3s?si=BGFZcoxjcacINOC2"),

('Spreadsheets',"https://youtu.be/pUE1IBfCuN8?si=9LiNrAS3aFyqGvBx"),

('Web designing',"https://youtu.be/ethIpWRsrng?si=PabmnzGdSO_oQbkq"),

('Word Processing',"https://youtu.be/ViYa5Rkbq3s?si=8HY1yDn2zPHq9F1"),

('Web Designing and Introduction to the Internet',"https://youtu.be/gl8w8kWsOno?si=6TeQc7AA7WaH5fvu"),

('Services On the Internet Some Definitions related to the web',"https://youtu.be/qw6zLs1cOEY?si=anBakYsY7xXrHHl"),

('Introduction to HTML',"https://youtu.be/MDLn5-zSQQI?si=5bbDJOCC4QOoxi0X"),

('Basic tags',"https://youtu.be/bUEykHfMMnc?si=yIdw9yof4gxy_6zx"),

('Formatting tags',"https://youtu.be/0sN951icaRE?si=nmmvrieix9bjbD9m"),


('Lists in HTML',"https://youtu.be/HeQvQEiGMKk?si=qQ7gyB94xW_At9Ly"),










('structure of atom','https://youtu.be/TYEYEIuTmGQ?feature=shared'),
  ('Some Basic Concepts of Chemistry','https://youtu.be/W1Olmqd5_FU?feature=share'),
  ('atomic structure','https://youtu.be/4QblYo-XeoY?feature=shared'),
  ('Daltons Atomic Theory','https://youtu.be/GB0LUS3wel8?feature=shared'),
  ('Rutherford alpha particle scattering experiment','https://youtu.be/fLFXDdnJN5U?feature=shared'),
  ('Bohrs model','https://youtu.be/S1LDJUu4nko?feature=share'),
  ('What are Shells Subshells,and Orbitals?','https://youtu.be/Q0UEMXM5MTI?feature=share'),
  ('dual nature of matter and light|de Broglies hypothesis','https://youtu.be/Z_R81QiuAiw?feature=shared'),
  ('Heisenberg uncertainty principle','https://youtu.be/TQKELOE9eY4?feature=shared'),
  ('quantum numbers-strucutre of atom','https://youtu.be/g7QocY5Oy3A?feature=shared'),
('shapes of s| p and d orbitals','https://youtu.be/nNkw_0c8vY0?feature=shared'),
('Aufbau principle','https://youtu.be/JRIxuqd7uts?feature=shared'),
(' Paulis exclusion principle','https://youtu.be/bdfir8uT06Q?feature=shared'),
('Hunds rule','https://youtu.be/bdfir8uT06Q?feature=shared'),
('Complete Electronic Configuration |Aufbau Principle | Hunds Rule |Pauli Exclusion Principle','https://youtu.be/ako0iJrG03Q?feature=shared'),
('stability of half-filled and completely filled orbitals','https://youtu.be/GAK8d8e8DLE?feature=shared'),
('Discovery of Electron','https://youtu.be/XR3LedUjbYg?feature=shared'),
('Discovery of Proton','https://youtu.be/0G_Ja08K3zw?feature=shared'),
('Discovery of Neutron','https://youtu.be/PoHGzh6PPSI?feature=shared'),
('Atomic Number & Mass Number','https://youtu.be/_S7ov25y3_M?feature=shared'),
('Periodic Table','https://youtu.be/ogpWoB4m-Ns?feature=shared'),
('Modern PeriodicTable','https://youtu.be/U8q1JetNu_w?feature=shared'),
('Periodic Trends Atomic Radius| Electronegativity| Ionization Energy','https://youtu.be/7cEtOHLZQ2A?feature=shared'),
 ('Valency,','https://youtu.be/lVSF2lP4oBA?feature=shared'),
 ('CLASSIFICATION OF ELEMENTS & PERIODIC PROPERTIES| Nomenclature of Elements With Z100','https://youtu.be/U9v__bhU0PQ?feature=shared'),
 ('What are Ionic Bonds?','https://youtu.be/zpaHPXVR8WU?feature=shared'),
('What are covalent bonds','https://youtu.be/zpaHPXVR8WU?feature=shared'),
('How to calculate bond order','https://youtu.be/1SZIonu9FsE?feature=shared'),
('Lewis structure','https://youtu.be/cIuXl7o6mAw?feature=shared'),
('Polar Character of Covalent Bond','https://youtu.be/MjKRu8nPWgU?feature=shared'),
('Fajans Rule','https://youtu.be/cpzOMPGCIj4?feature=shared'),
('Valence Bond Theory','https://youtu.be/WZYC5uWcRxs?feature=shared'),
('Geometry of molecules','https://youtu.be/DWS5HlyndAI?feature=shared'),
('VSEPR Theory','https://youtu.be/wj4u5hM6QhI?feature=shared'),
('How to draw an energy level diagram of an atom','https://youtu.be/bLvaqbC3FUQ?feature=shared'),
('Resonance Structures','https://youtu.be/1hxyq3yxVck?feature=shared'),
('Hybridization of Atomic Orbitals | SP, SP2, SP3 Hybridization of Carbon','https://youtu.be/J8GLj_armbA?feature=shared'),
('Pi and Sigma Bonds','https://youtu.be/pG3f_vqvbO8?feature=shared'),
('How to calculate Hybridization','https://youtu.be/iA91SpYZ1vo?feature=shared'),
('Molecular Orbital Theory - Bonding & Antibonding MO - Bond Order','https://youtu.be/6tB6E6R_XpQ?feature=shared'),
('Hydrogen bonding | Intermolecular forces and properties','https://youtu.be/ltxqQbiI6-o?feature=shared'),
('Thermodynamic Processes ','https://youtu.be/3QMfZZs-Vm0?feature=shared'),
('First law of Thermodynamics','https://youtu.be/fdZ2qhfVO30?feature=shared'),
('Endothermic and Exothermic Reactions','https://youtu.be/kCmVpJYR7kQ?feature=shared'),
('Enthalpy and Enthalpy Change','https://youtu.be/JlPFLK3XSQw?feature=shared'),
('Basic Concepts of Thermodynamics','https://youtu.be/cLSYrrnjauo?feature=shared'),
('Thermodynamics: Internal Energy and Degree of freedom','https://youtu.be/rboAF09Va3s?feature=shared'),
('Thermodynamics: Energy|Work and Heat','https://youtu.be/vlzYLk5ll14?feature=shared'),
('Hess Law',',https://youtu.be/TYylc61qdnI?feature=shared'),
('Bond enthalpy and enthalpy of reaction','https://youtu.be/xE1gdQZcR-o?feature=shared'),
('ZEROTH LAW OF THERMODYNAMICS','https://youtu.be/4OSZ3wYo6-Y?feature=shared'),
('Second Law of Thermodynamics','https://youtu.be/WTtxlaeC9PY?feature=shared'),
('Standard Enthalpy of Formation and Combustion','https://youtu.be/7p5XzGu0cy0?feature=shared'),
('Standard enthalpy of atomisation','https://youtu.be/QAmIXGtOzs0?feature=shared'),  
('Enthalpy of sublimation','https://youtu.be/AlamskBXpus?feature=shared'), 
('Enthalpy and phase changes','https://youtu.be/jCKvxH5mXR4?feature=shared'), 
('Enthalpy of Solution| Enthalpy of Hydration| Lattice Energy and Heat of Formation ',',https://youtu.be/fDglQCYTiqc?feature=shared'), 
('Proof: S (or entropy) is a valid state variable','https://youtu.be/sPz5RrFus1Q?feature=shared'), 
('Gibbs free energy and spontaneity ','https://youtu.be/ViAmQivKif0?feature=shared'), 
('What are the conditions for thermodynamic equilibrium?','https://youtu.be/6Ia_N_trkqI?feature=shared'), 
('Chemical Equilibrium | Dynamic Equilibrium','https://youtu.be/fwk3grEcSVs?feature=shared'), 
('The Law of Mass Action','https://youtu.be/2hwfBIelucA?feature=shared'), 
('Le Chateliers Principle','https://youtu.be/bNcTt3l3Q8k?feature=shared'), 
('Arrhenius Concept of Acids and Bases','https://youtu.be/QPdmC3oganw?feature=shared'), 
('pH of Weak Acids and Bases - Percent Ionization - Ka & Kb','https://youtu.be/kJTCuRSeh6g?feature=shared'), 
('Weak acid equilibria','https://youtu.be/nJLNlB-7Rhk?feature=shared'), 
('PH and POH | Ionic Product of Water','https://youtu.be/cXb-8nofWAI?feature=shared'), 
('Degree Of Ionisation | Ostwalds Dilution Law','https://youtu.be/lzHAPPzpmjA?feature=shared'), 
('pKa|Ka,|and Acid Strength','https://youtu.be/IQ6gHQAg_Nk?feature=shared'), 
('Hydrolysis of Salt of Weak Acid and Weak Base','https://youtu.be/tXTwQCfmffU?feature=shared'), 
('HendersonHasselbalch equation','https://youtu.be/7QgtdYiWH50?feature=shared'), 
('Buffer Solutions','https://youtu.be/kBzPTEB21Po?feature=shared'),
 ('The common-ion effect','https://youtu.be/fI3U9T7LigY?feature=shared'), 
('Oxidation and Reduction Reactions',',https://youtu.be/dF5lB7gRtcA?feature=shared'), 
('Balancing Redox Reactions By Ion Electron Method,','https://youtu.be/PRqCI03c5QE?feature=shared'), 
('How To Calculate Oxidation Number or Oxidation State','https://youtu.be/gJWq4cNxnvc?feature=shared'), 
('Balancing redox reactions using oxidation number method','https://youtu.be/Qp1dWUDzzvE?feature=shared'), 
('Basic principles and techniques in organic chemistry','https://www.youtube.com/watch?v=re17uCCIwnI'), 
('Industrial Applications of Organic Chemistry','https://www.youtube.com/watch?v=dtvJ0pmd-LA'), 
('General Characteristics of Organic Compounds','https://www.youtube.com/watch?v=c6RbFgLr6LM'), 
('Purifications of Organic Compounds','https://www.youtube.com/watch?v=SsunOrsbXes'), 
('Definition and Example of Sublimation -Organic Chemistry','https://www.youtube.com/watch?v=6E7ZltIsZ0E'), 
('Method to Determine Melting Point of a Soild - Organic Chemistry','https://www.youtube.com/watch?v=cC09fqxtcsc'), 
('Distillation Definition and Technique - Organic Chemistry','https://www.youtube.com/watch?v=_YyqOof8zIU'), 
('Distillation Under Reduced Pressure Definition, Principle and Advantage - Organic chemistry','https://www.youtube.com/watch?v=RomJB-h7-ck'), 
('Steam Distillation- Technique - Organic Chemistry','https://www.youtube.com/watch?v=vYYMHP83Zbo'), 
('Differential Extraction Method - Organic Chemistry','https://www.youtube.com/watch?v=azSki81HAQ8'), 
('Thin Layer Chromatography  Principle and Technique - Organic Chemistry','https://www.youtube.com/watch?v=vZr3sEmfPsE'), 
('Paper Chromatography  Principle and Technique  - Organic chemistry','https://www.youtube.com/watch?v=6o0yFvDYex4'), 
('Detection of Phosphorus, Metal and Oxygen in Organic Compound','https://www.youtube.com/watch?v=09N29B-Yhd0'), 
('Estimation of Nitrogen in Dumas Method - Basic Principles and Techniques in Organic Chemistry,','https://www.youtube.com/watch?v=ntKAbHOEqP8'), 
('Percentage of Nitrogen in a Compound (Dumas Method) Problems','https://www.youtube.com/watch?v=kpTTIaGNaxs'), 
('Estimation of Nitrogen in Kjeldahls Method','https://www.youtube.com/watch?v=Dd2fSS5sRvs'), 
('Percentage of Nitrogen in a Compound Kjeldahls MethodProblems','https://www.youtube.com/watch?v=NkL7C_DvYY4'), 
('Estimation of Halogen (Carius Method)','https://www.youtube.com/watch?v=_diS1Vkhyxg'), 
('Percentage of Chlorine in a Compound (Carius Method) Problems','https://www.youtube.com/watch?v=QdhN_smxi88'), 
('Methods to Estimate Phosphorus','https://www.youtube.com/watch?v=OHPLpDO3cxg'), 
('Percentage of Phosphorus in a Compound Problem 1-Basic Principles and Techniques inOrganic Chemistry,','https://www.youtube.com/watch?v=G-_Gp1zmemg'), 
('Methods to Estimate Oxygen - Basic Principles and Techniques in Organic Chemistry',',https://www.youtube.com/watch?v=jTAoKdFRl64'), 
('Empirical and Molecular Formula - Basic Principles and Techniques in Organic Chemistry - Chemistry','https://www.youtube.com/watch?v=_8Pn7bZRMvo'), 
('Determination of Molecular Formula of a Compound Problem 1','https://www.youtube.com/watch?v=_CD-mjPbrsc'), 
('Representations of Organic Compound','https://www.youtube.com/watch?v=VL7n2hMqKzs'), 
('Structure Classifications of Organic Compound','https://www.youtube.com/watch?v=IeERQfaDtH4'), 
('Functional Group -Organic chemistry','https://www.youtube.com/watch?v=RBUFpwchTwQ'), 
('Classifications of Organic Compounds Based on Their FunctionalGroup','https://www.youtube.com/watch?v=QCVU2zQ0AKA'), 
('Homologous Series and its Characteristics with Examples','https://www.youtube.com/watch?v=eHqRCSN_1TQ'), 
('Rules for IUPAC Nomenclature of Functional Group','https://www.youtube.com/watch?v=W505wjWM8jo')







]

cursor.executemany('INSERT OR REPLACE INTO maths (topic_name, video_link) VALUES (?, ?)', data)
connect_to.commit()
connect_to.close()






connect_to = sqlite3.connect('database.db')
cursor = connect_to.cursor()

# SELECT all rows from the "maths" table
cursor.execute('SELECT * FROM maths')
data = cursor.fetchall()

# Display the data
for row in data:
    print(f'Topic: {row[0]}')
    print(f'Video Link: {row[1]}')
    print('---')

connect_to.close()






connect_to = sqlite3.connect('database.db')
cursor = connect_to.cursor()

# SELECT all rows from the "maths" table
cursor.execute('SELECT * FROM maths')
data = cursor.fetchall()

# Define headers for the table
headers = ["Topic", "Video Link"]

# Use tabulate to format and print the data
table = tabulate(data, headers, tablefmt="fancy_grid")

print(table)

connect_to.close()



































































































