## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[2] NullType-BlackItalic.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-Black.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-BoldItalic.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-Bold.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-ExtraBoldItalic.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-ExtraBold.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-ExtraLightItalic.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-ExtraLight.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-Italic.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-LightItalic.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-Light.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-MediumItalic.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-Medium.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-Regular.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-SemiBoldItalic.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-SemiBold.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-ThinItalic.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>

<details><summary>[2] NullType-Thin.otf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 💥 **ERROR** <p>Failed with KeyError: 'glyf'</p>
<pre><code>  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;<venv>/lib/python3.13/site-packages/fontbakery/checks/opentype/monospace.py&quot;, line 169, in check_monospace
    num_glyphs = len(ttFont[&quot;glyf&quot;].glyphs)
                     ~~~~~~^^^^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 817, in __getitem__
    table = self._readTable(tag)
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/ttFont.py&quot;, line 825, in _readTable
    data = self.reader[tag]
           ~~~~~~~~~~~^^^^^
  File &quot;<venv>/lib/python3.13/site-packages/fontTools/ttLib/sfnt.py&quot;, line 111, in __getitem__
    entry = self.tables[Tag(tag)]
            ~~~~~~~~~~~^^^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 18 | 0 | 0 | 18 | 821 | 54 | 1171 | 0 | 
| 1% | 0% | 0% | 1% | 39% | 3% | 56% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
