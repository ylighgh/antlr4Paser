lexer grammar MemInfoLexer;

fragment UA: 'A';
fragment UB: 'B';
fragment UC: 'C';
fragment UD: 'D';
fragment UE: 'E';
fragment UF: 'F';
fragment UG: 'G';
fragment UH: 'H';
fragment UI: 'I';
fragment UJ: 'J';
fragment UK: 'K';
fragment UL: 'L';
fragment UM: 'M';
fragment UN: 'N';
fragment UO: 'O';
fragment UP: 'P';
fragment UQ: 'Q';
fragment UR: 'R';
fragment US: 'S';
fragment UT: 'T';
fragment UU: 'U';
fragment UV: 'V';
fragment UW: 'W';
fragment UX: 'X';
fragment UY: 'Y';
fragment UZ: 'Z';

fragment LA: 'a';
fragment LB: 'b';
fragment LC: 'c';
fragment LD: 'd';
fragment LE: 'e';
fragment LF: 'f';
fragment LG: 'g';
fragment LH: 'h';
fragment LI: 'i';
fragment LJ: 'j';
fragment LK: 'k';
fragment LL: 'l';
fragment LM: 'm';
fragment LN: 'n';
fragment LO: 'o';
fragment LP: 'p';
fragment LQ: 'q';
fragment LR: 'r';
fragment LS: 's';
fragment LT: 't';
fragment LU: 'u';
fragment LV: 'v';
fragment LW: 'w';
fragment LX: 'x';
fragment LY: 'y';
fragment LZ: 'z';

fragment ZERO: '0';
fragment ONE: '1';
fragment TWO: '2';
fragment THREE: '3';
fragment FOUR: '4';
fragment FIVE: '5';
fragment SIX: '6';
fragment SEVEN: '7';
fragment EGHIT: '8';
fragment NINE: '9';

fragment DIGIT: [0-9];
fragment SPACE : ' ';
fragment UPPER_ALPHABET : [A-Z];
fragment LOWER_ALPHABET : [a-z];

SPACE_SYMBOL : SPACE;
EQUALS_SYMBOL : '=';
HYPHEN_SYMBOL : '-';
PLUS_SYMBOL : '+';
TILDE_SYMBOL : '~';
UNDERSCORE_SYMBOL : '_';
OPENING_BRACKET_SYMBOL : '[';
CLOSING_BRACKET_SYMBOL : ']';
OPEN_ANGLED_BRACKET_SYMBOL : '<';
CLOSE_ANGLED_BRACKET_SYMBOL: '>';
COLON_SYMBOL : ':';
SEMICOLON_SYMBOL : ';';
DOT_SYMBOL : '.';
WS :  ('\t' | '\r\n') -> skip;
ASTERISK_SYMBOL : '*';
NUMBER_SIGN_SYMBOL : '#';
SLASH_SYMBOL : '/';
COMMA_SYMBOL : ',';
DOUBLE_QUOTES_SYMBOL: '"';
OPENING_PARENTHESIS_SYMBOL : '(';
CLOSING_PARENTHESIS_SYMBOL : ')';

SINGLE_DIGIT: DIGIT; // 单个数字
UPPER_ALPHABET_SYMBOL: UPPER_ALPHABET;  // 大写字母
LOWER_ALPHABET_SYMBOL: LOWER_ALPHABET;  // 小写字母

// 一月 "Jan"
JAN_MONTH_PHRASE: UJ LA LN;
// 二月 "Feb"
FEB_MONTH_PHRASE: UF LE LB;
// 三月 "Mar"
MAR_MONTH_PHRASE: UM LA LR;
// 四月 "Apr"
APR_MONTH_PHRASE: UA LP LR;
// 五月 "May"
MAY_MONTH_PHRASE: UM LA LY;
// 六月 "Jun"
JUN_MONTH_PHRASE: UJ LU LN;
// 七月 "Jul"
JUL_MONTH_PHRASE: UJ LU LL;
// 八月 "Aug"
AUG_MONTH_PHRASE: UA LU LG;
// 九月 "Sep"
SEP_MONTH_PHRASE: US LE LP;
// 十月 "Oct"
OCT_MONTH_PHRASE: UO LC LT;
// 十一月 "Nov"
NOV_MONTH_PHRASE: UN LO LV;
// 十二月 "Dec"
DEC_MONTH_PHRASE: UD LE LC;

// "GET"
GET_HTTP_METHOD_PHRASE: UG UE UT;
// "POST"
POST_HTTP_METHOD_PHRASE: UP UO US UT;
// "PUT"
PUT_HTTP_METHOD_PHRASE: UP UU UT;
// "DELETE"
DELETE_HTTP_METHOD_PHRASE: UD UE UL UE UT UE;
// "CONNECT"
CONNECT_HTTP_METHOD_PHRASE: UC UO UN UN UE UC UT;
// "OPTIONS"
OPTIONS_HTTP_METHOD_PHRASE: UO UP UT UI UO UN US;
// "TRACE"
TRACE_HTTP_METHOD_PHRASE: UT UR UA UC UE;
// "PATCH"
PATCH_HTTP_METHOD_PHRASE: UP UA UT UC UH;

// "HTTP/1.0"
HTTP_VERSION_1_0_PHRASE: UH UT UT UP SLASH_SYMBOL ONE DOT_SYMBOL ZERO;
// "HTTP/1.1"
HTTP_VERSION_1_1_PHRASE: UH UT UT UP SLASH_SYMBOL ONE DOT_SYMBOL ONE;
// "HTTP/2.0"
HTTP_VERSION_2_0_PHRASE: UH UT UT UP SLASH_SYMBOL TWO DOT_SYMBOL ZERO;

// "http://"
SCHEME_HTTP_PHRASE: LH LT LT LP COLON_SYMBOL SLASH_SYMBOL SLASH_SYMBOL;

// "https://"
SCHEME_HTTPS_PHRASE: LH LT LT LP LS COLON_SYMBOL SLASH_SYMBOL SLASH_SYMBOL;

// nginx $upstream_cache_status - "MISS"
MISS_UCS_PHRASE: UM UI US US;

// nginx $upstream_cache_status - "BYPASS"
BYPASS_UCS_PHRASE: UB UY UP UA US US;

// nginx $upstream_cache_status - "EXPIRED"
EXPIRED_UCS_PHRASE: UE UX UP UI UR UE UD;

// nginx $upstream_cache_status - "STALE"
STALE_UCS_PHRASE: US UT UA UL UE;

// nginx $upstream_cache_status - "UPDATING"
UPDATING_UCS_PHRASE: UU UP UD UA UT UI UN UG;

// nginx $upstream_cache_status - "REVALIDATED"
REVALIDATED_UCS_PHRASE: UE UE UV UA UL UI UD UA UT UE UD;

// nginx $upstream_cache_status - "HIT"
HIT_UCS_PHRASE: UH UI UT;

// "<190>"
PRIORITY_LOCAL7_INFO_PHRASE: ONE NINE ZERO;

// "<187>"
PRIORITY_LOCAL7_ERROR_PHRASE: ONE EGHIT SEVEN;

//内存可用"MemAvailable"
MEM_AVAILABLE : UM LE LM UA LV LA LI LL LA LB LL LE;

//内存总共大小"MemTotal"
MEM_TOTAL : UM LE LM UT LO LT LA LL;

//unitRule kB
BYTE_UNIT : LK UB;