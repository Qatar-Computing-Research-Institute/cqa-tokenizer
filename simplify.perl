#!/usr/bin/perl
#Simple cleaning script: Removes most URLs/TELS, etc.
#Francisco Guzman

while(<>)
{
    s/\<img.*?\>/ \@IMG /g;
    s/\<\/?(br|a|b|i|strong).*?\>/ /g;
    s/\<(h1|p)\>.*?<\/\1\>/ /g;
    s/(href=")?(http:\/\/|www\.)(\S*)/ \@URL \1/g;
    s/[a-zA-Z0-9_\.]+(\@|\(at\)|\/\-a\-t\-\/)([a-z]+(\.|\(dot\)))+(com|co|uk|qa)/ \@EMAIL /g;
    s/ ?[\_\*\=\-]{3,} ?/ /g;
    s/(\+?\d{2,3})?\s*(4|5|3|6)\d{3}[ \-]?\d{3,4}/ \@TEL /g;
    s/"+/" /g;
    s/[^\.]\.{2}[^\.]/\./g;
    s/^ *"/ /g;
    s/" *$/ /g;
    s/\,+/,/g;
    s/\?+/\?/g;
    s/\!+/\!/g;
    s/[\.]{3,}/... /g;
    print;


}
