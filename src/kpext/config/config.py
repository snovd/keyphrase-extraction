"""config/config

Default corpus configs.

"""
import sys
import inspect
from pathlib import Path

from kpext import kpext_data

ACLRDTEC = "acl-rd-tec-2.0"
SEMEVAL2017 = "semeval2017-task10"

KPEXTDATA_PATH = str(Path(inspect.getfile(kpext_data)).parents[1])

# Check for default paths for corpus
DEFAULT_CORPUS_PATH = "kpext_data/corpus/" + SEMEVAL2017 + "/"
if Path("./" + DEFAULT_CORPUS_PATH).exists():
    CORPUS_PATH = "./" + DEFAULT_CORPUS_PATH
elif Path("~/" + DEFAULT_CORPUS_PATH).exists():
    CORPUS_PATH = "~/" + DEFAULT_CORPUS_PATH
elif Path(KPEXTDATA_PATH + "/" + DEFAULT_CORPUS_PATH).exists():
    CORPUS_PATH = KPEXTDATA_PATH + "/" + DEFAULT_CORPUS_PATH
else:
    print("Warning: SemEval 2017 Task 10 corpus doesn't exists.", file=sys.stderr)
    print("    - Download from here https://scienceie.github.io/resources.html",
          file=sys.stderr)
    print("    - Use one of the following paths.", file=sys.stderr)
    print("        + %s" % (KPEXTDATA_PATH + "/" + DEFAULT_CORPUS_PATH), file=sys.stderr)
    print("        + ./%s" % DEFAULT_CORPUS_PATH, file=sys.stderr)
    print("        + ~/%s" % DEFAULT_CORPUS_PATH, file=sys.stderr)
    print("    - You can use pre-trained models.", file=sys.stderr)
    CORPUS_PATH = DEFAULT_CORPUS_PATH

CORPUS = {
    ACLRDTEC: {
        "_id": "acl-rd-tec-2.0",
        "options": {}
        },
    SEMEVAL2017: {
        "_id": "semeval2017-task10",
        "format": "brat",
        "format-description": "brat standoff format, http://brat.nlplab.org/standoff.html",
        "dataset": {
            "train-labeled": CORPUS_PATH + "/train2/",
            "train-unlabeled": None,
            "dev-labeled": CORPUS_PATH + "/dev/",
            "dev-unlabeled": None,
            "test-unlabeled": CORPUS_PATH + "/scienceie2017_test_unlabelled/",
            "test-labeled": CORPUS_PATH + "/semeval_articles_test/"
            },
        "options": {}
        },
    "options": {}
}
CORPUS_DEFAULT = CORPUS[SEMEVAL2017]
CORPUS_SEMEVAL2017_TASK10 = CORPUS[SEMEVAL2017]
CORPUS_ACL_RD_TEC_2_0 = CORPUS[ACLRDTEC]

# Check for default paths for models
DEFAULT_MODELS_PATH = "kpext_data/models/"
if Path("./" + DEFAULT_MODELS_PATH).exists():
    MODELS_PATH = "./" + DEFAULT_MODELS_PATH
elif Path("~/" + DEFAULT_MODELS_PATH).exists():
    MODELS_PATH = "~/" + DEFAULT_MODELS_PATH
elif Path(KPEXTDATA_PATH + "/" + DEFAULT_MODELS_PATH).exists():
    MODELS_PATH = KPEXTDATA_PATH + "/" + DEFAULT_MODELS_PATH
else:
    print("Warning: Path to save models doesn't exists.", file=sys.stderr)
    print("    - Possible paths are:", file=sys.stderr)
    print("        + %s" % (KPEXTDATA_PATH + "/" + DEFAULT_MODELS_PATH), file=sys.stderr)
    print("        + %s" % ("./" + DEFAULT_MODELS_PATH), file=sys.stderr)
    print("        + %s" % ("~/" + DEFAULT_MODELS_PATH), file=sys.stderr)
    print("    - Default will be %s" % DEFAULT_MODELS_PATH, file=sys.stderr)
    MODELS_PATH = DEFAULT_MODELS_PATH

OUTPUT_PATH = "output/"
