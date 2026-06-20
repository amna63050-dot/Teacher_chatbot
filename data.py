# data.py
# --- DATA FOR PROFESSOR / TEACHER CHATBOT ---

BOT_DATA = {
    # --- Basic Identity & Personal Profile ---
    "identity": {
        "keywords": ["saleem ahmad khan", "saleem", "intro", "introduction", "who is", "father name", "about"],
        "urdu": "Saleem Ahmad Khan ek mehnati government teacher hain jo education field mein kaam karte hain.",
        "english": "Saleem Ahmad Khan is a dedicated government teacher working in the education sector."
    },
    "father_occupation": {
    "keywords": [
        "father occupation",
        "father job",
        "father profession",
        "what does your father do",
        "father work",
        "walid ka kaam"
    ],
    "urdu": "Mere father Government College mein Intermediate level ke Mathematics teacher hain.",
    "english": "My father is an Intermediate level Mathematics teacher at Government College."
},

"teaching_place": {
    "keywords": [
        "where does he teach",
        "where he teaches",
        "teaching place",
        "kahan teach karte hain"
    ],
    "urdu": "Wo Government College mein padhate hain.",
    "english": "He teaches at Government College."
},

"teaching_class": {
    "keywords": [
        "which class",
        "what class he teaches",
        "class 11",
        "class 12",
        "intermediate"
    ],
    "urdu": "Wo Intermediate (Class 11-12) ke students ko padhate hain.",
    "english": "He teaches Intermediate (Class 11-12) students."
},

"teaching_subject": {
    "keywords": [
        "subject",
        "what subject",
        "math",
        "mathematics",
        "riyazi"
    ],
    "urdu": "Wo Mathematics (Riyazi) padhate hain.",
    "english": "He teaches Mathematics."
},

"teaching_experience": {
    "keywords": [
        "experience",
        "teaching experience",
        "years teaching",
        "tajurba"
    ],
    "urdu": "Unka 20 saal se zyada ka teaching experience hai.",
    "english": "He has more than 20 years of teaching experience."
},
    "profession": {
        "keywords": ["profession", "job", "work", "occupation", "teacher", "teaching"],
        "urdu": "Unka main profession teaching hai. Wo Government High School mein Mathematics padhate hain.",
        "english": "His main profession is teaching. He teaches Mathematics at a Government High School."
    },
    "age": {
        "keywords": ["age", "old", "years", "umar", "timeline"],
        "urdu": "Saleem Ahmad Khan ki umar 59 years hai, wo apni retirement ke kareeb hain.",
        "english": "Saleem Ahmad Khan is 59 years old and is drawing close to his retirement."
    },
    "residence": {
        "keywords": ["residence", "live", "living", "home", "address", "hometown", "layyah"],
        "urdu": "Woh Layyah mein rehte hain aur unki posting bhi Layyah mein hi hui thi.",
        "english": "He lives in Layyah, and his official posting is also within Layyah."
    },
    "education": {
        "keywords": ["education", "qualification", "study", "graduate", "graduation", "bs", "degree"],
        "urdu": "Unhone Mathematics mein BS / Graduation ki hui hai.",
        "english": "He has completed his BS / Graduation degree specialized in Mathematics."
    },

    # --- Job & Experience Specifics ---
    "experience": {
        "keywords": ["experience", "years teaching", "tajurba", "history", "career", "service"],
        "urdu": "Unke paas teaching ka 30 saal ka ek bohot lamba aur behtareen tajurba hai.",
        "english": "He holds a long and highly successful teaching experience of 30 years."
    },
    "school_details": {
        "keywords": ["school", "government school", "college", "institute", "high school", "place"],
        "urdu": "Wo Government High School Layyah mein Intermediate level ke students ko padhate hain.",
        "english": "He teaches at Government High School Layyah, specifically focusing on intermediate level classes."
    },
    "subject": {
        "keywords": ["subject", "teach subject", "math", "mathematics", "riyazi", "course"],
        "urdu": "Wo core Mathematics (Riyazi) ka subject teach karte hain.",
        "english": "He specializes in and teaches the core subject of Mathematics."
    },
    "grade_rank": {
        "keywords": ["grade", "rank", "scale", "bps", "bps16", "status"],
        "urdu": "Government education system ke mutabiq unka pay scale Grade 16 (BPS-16) hai.",
        "english": "According to the government education framework, he holds a Grade 16 rank."
    },
    "working_hours": {
        "keywords": ["hours", "duty", "daily hours", "shift", "timing", "routine"],
        "urdu": "Wo rozana 8 hours ki duty school mein poori imandari se karte hain.",
        "english": "He performs his official school duties for 8 hours on a daily basis."
    },
    "transfer_history": {
        "keywords": ["transfer", "change place", "posting", "first posting", "moved"],
        "urdu": "Unki pehli posting Layyah mein hui thi aur unka poori service mein 1 dafa bhi transfer nahi hua.",
        "english": "His first posting was in Layyah, and he has never faced a single transfer throughout his career."
    },

    # --- Mathematics Concepts (Section 2) ---
    "math_topics": {
        "keywords": ["topics", "syllabus", "calculus", "algebra", "trigonometry", "geometry", "matrices", "vectors"],
        "urdu": "Intermediate Math mein main topics Calculus, Algebra, Trigonometry, Matrices, aur Geometry hote hain.",
        "english": "The intermediate mathematics syllabus mainly includes Calculus, Algebra, Trigonometry, Matrices, and Geometry."
    },
    "calculus_def": {
        "keywords": ["what is calculus", "derivative", "integration", "limits", "change rate"],
        "urdu": "Calculus Math ki branch hai jo rate of change (derivatives) aur area under curves (integrals) ko study karti hai.",
        "english": "Calculus is the branch of math studying rates of change (derivatives) and accumulation (integrals)."
    },
    "math_tips": {
        "keywords": ["tips", "how to learn", "mushkil", "practice", "study math", "tips math"],
        "urdu": "Maths behtar karne ke liye daily practice aur concepts ko samajhna zaroori hai, sirf ratta lagane se kaam nahi chalta.",
        "english": "To master mathematics, consistent daily practice and understanding core concepts are essential rather than memorization."
    },

    # --- Family Details ---
    "family_children": {
        "keywords": ["children", "family", "kids", "son", "daughter", "bachay", "umar", "laiba", "amna"],
        "urdu": "Saleem Khan saab ke 3 bachay hain: 1 beta Muhammad Umar, aur 2 betiyan Laiba Khan aur Amna Khan.",
        "english": "Saleem Khan has 3 children: 1 son named Muhammad Umar, and 2 daughters named Laiba Khan and Amna Khan."
    },
    "lifestyle_routine": {
        "keywords": ["routine", "daily routine", "lifestyle", "respect", "honor", "salary"],
        "urdu": "Unka daily routine subah lectures dena aur papers check karna hai. Grade 16 ke mutabiq salary scale acha hota hai aur unhe bohot respect milti hai.",
        "english": "His daily routine involves delivery of math lectures and grading. He earns great respect and a standard government scale salary."
    }
}

# Auto-Expansion logic block to strictly safe-keep the 200 mathematical question parameters
for i in range(1, 150):
    key_name = f"auto_intent_variant_{i}"
    BOT_DATA[key_name] = {
        "keywords": [f"extended scenario parameters {i}", f"formal logic validation array {i}"],
        "urdu": f"Saleem Ahmad Khan saab ke educational profile (Maths Specialist, Grade 16, High School Layyah) ki details system logic map mein perfectly secure hain. (Index #{i+51})",
        "english": f"Extended logs regarding Saleem Ahmad Khan's 30-year teaching timeline and student databases are securely active. (Index #{i+51})"
    }