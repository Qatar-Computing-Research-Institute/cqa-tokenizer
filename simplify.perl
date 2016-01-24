#!/usr/bin/perl
#Simple cleaning script: Removes most URLs/TELS, etc.
#Francisco Guzman

while(<>)
{
    s/\<img.*?\>/ \@IMG /gi;
    s/\[img_assist.*?\]/ \@IMG /gi;
    s/\<\/?(br|a|b|i|strong).*?\>/ /g;
    s/\<(h1|p)\>.*?<\/\1\>/ /gi;
    s/(href=")?(http:\/\/|www\.)(\S*)/ \@URL \1/gi;
    s/[a-zA-Z0-9_\.]+(\@|\(at\)|\/\-a\-t\-\/)([a-z]+(\.|\(dot\)))+(com|co|uk|qa)/ \@EMAIL /gi;
    s/ ?[\_\*\=\-\~]{3,} ?/ /g;
    s/(\+?\d{2,3})? *(4|5|3|6)\d{3}[ \-]?\d{3,4}/ \@TEL /g;
    s/"+/" /g;
    s/[^\.]\.{2}[^\.\s]/\./g;
    s/^ *"/ /g;
    s/" *$/ /g;
    s/\,+/,/g;
    s/\?+/\?/g;
    s/\!+/\!/g;
    s/\+\|//g;
    s/\|\+//g;
    s/(\d+)QA?R/\1 QAR/gi;
    s/QA?R(\d+)/QAR \1/gi;
    s/[\.]{3,}/... /g;
    #html
    s/\&amp;/\&/g;
    s/\&#39;/\'/g;
    print;


}
