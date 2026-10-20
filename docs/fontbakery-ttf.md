## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[5] NullType-BlackItalic.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: numbersign	Contours detected: 1	Expected: 2

- Glyph name: percent	Contours detected: 1	Expected: 4 or 5

- Glyph name: at	Contours detected: 3	Expected: 2

- Glyph name: dieresis	Contours detected: 1	Expected: 2

- Glyph name: copyright	Contours detected: 4	Expected: 3

- Glyph name: guillemotleft	Contours detected: 1	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: guillemotright	Contours detected: 1	Expected: 2

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- 130 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* dollar (U+0024): L&lt;&lt;382.0,262.0&gt;--&lt;378.0,238.0&gt;&gt; has the same coordinates as a previous segment.

* currency (U+00A4): L&lt;&lt;298.0,238.0&gt;--&lt;330.0,420.0&gt;&gt; has the same coordinates as a previous segment.

* paragraph (U+00B6): L&lt;&lt;259.0,469.0&gt;--&lt;265.0,504.0&gt;&gt; has the same coordinates as a previous segment.

* ae (U+00E6): L&lt;&lt;410.0,420.0&gt;--&lt;393.0,322.0&gt;&gt; has the same coordinates as a previous segment.

* ae (U+00E6): L&lt;&lt;213.0,210.0&gt;--&lt;199.0,133.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



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

<details><summary>[4] NullType-Black.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: numbersign	Contours detected: 1	Expected: 2

- Glyph name: percent	Contours detected: 1	Expected: 4 or 5

- Glyph name: at	Contours detected: 3	Expected: 2

- Glyph name: dieresis	Contours detected: 1	Expected: 2

- Glyph name: copyright	Contours detected: 4	Expected: 3

- Glyph name: guillemotleft	Contours detected: 1	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: guillemotright	Contours detected: 1	Expected: 2

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- 130 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-BoldItalic.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: numbersign	Contours detected: 1	Expected: 2

- Glyph name: percent	Contours detected: 1	Expected: 4 or 5

- Glyph name: at	Contours detected: 3	Expected: 2

- Glyph name: copyright	Contours detected: 4	Expected: 3

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- Glyph name: Atilde	Contours detected: 2	Expected: 3

- Glyph name: Aring	Contours detected: 2	Expected: 3 or 4

- Glyph name: Egrave	Contours detected: 1	Expected: 2

- 82 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-Bold.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: at	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- Glyph name: Atilde	Contours detected: 2	Expected: 3

- Glyph name: Aring	Contours detected: 2	Expected: 3 or 4

- Glyph name: Egrave	Contours detected: 1	Expected: 2

- Glyph name: Eacute	Contours detected: 1	Expected: 2

- 68 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-ExtraBoldItalic.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: numbersign	Contours detected: 1	Expected: 2

- Glyph name: percent	Contours detected: 1	Expected: 4 or 5

- Glyph name: at	Contours detected: 3	Expected: 2

- Glyph name: copyright	Contours detected: 4	Expected: 3

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- Glyph name: Atilde	Contours detected: 2	Expected: 3

- Glyph name: Aring	Contours detected: 2	Expected: 3 or 4

- Glyph name: Egrave	Contours detected: 1	Expected: 2

- 78 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-ExtraBold.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: numbersign	Contours detected: 1	Expected: 2

- Glyph name: percent	Contours detected: 1	Expected: 4 or 5

- Glyph name: at	Contours detected: 3	Expected: 2

- Glyph name: copyright	Contours detected: 4	Expected: 3

- Glyph name: guillemotleft	Contours detected: 1	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: guillemotright	Contours detected: 1	Expected: 2

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- Glyph name: Atilde	Contours detected: 2	Expected: 3

- 90 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-ExtraLightItalic.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: section	Contours detected: 1	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: bullet	Contours detected: 3	Expected: 1

- Glyph name: SF420000	Contours detected: 2	Expected: 3

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF410000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- Glyph name: SF440000	Contours detected: 2	Expected: 4

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- 6 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-ExtraLight.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: section	Contours detected: 1	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: bullet	Contours detected: 3	Expected: 1

- Glyph name: SF420000	Contours detected: 2	Expected: 3

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF410000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- Glyph name: SF440000	Contours detected: 2	Expected: 4

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- 6 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-Italic.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: SF370000	Contours detected: 1	Expected: 2

- Glyph name: SF420000	Contours detected: 2	Expected: 3

- Glyph name: SF200000	Contours detected: 1	Expected: 2

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF470000	Contours detected: 1	Expected: 2

- Glyph name: SF410000	Contours detected: 2	Expected: 3

- Glyph name: SF450000	Contours detected: 1	Expected: 2

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- Glyph name: SF440000	Contours detected: 2	Expected: 4

- 10 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-LightItalic.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: section	Contours detected: 1	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: SF420000	Contours detected: 2	Expected: 3

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF410000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- Glyph name: SF440000	Contours detected: 2	Expected: 4

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- Glyph name: SF410000	Contours detected: 2	Expected: 3

- 4 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-Light.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: section	Contours detected: 1	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: bullet	Contours detected: 3	Expected: 1

- Glyph name: SF420000	Contours detected: 2	Expected: 3

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF410000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- Glyph name: SF440000	Contours detected: 2	Expected: 4

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- 6 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[5] NullType-MediumItalic.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: at	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: Aring	Contours detected: 2	Expected: 3 or 4

- Glyph name: aring	Contours detected: 2	Expected: 4

- Glyph name: SF370000	Contours detected: 1	Expected: 2

- Glyph name: SF420000	Contours detected: 2	Expected: 3

- Glyph name: SF200000	Contours detected: 1	Expected: 2

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF470000	Contours detected: 1	Expected: 2

- 18 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* infinity (U+221E): L&lt;&lt;216.0,343.0&gt;--&lt;233.0,357.0&gt;&gt; has the same coordinates as a previous segment.

* infinity (U+221E): L&lt;&lt;419.0,357.0&gt;--&lt;402.0,343.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



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

<details><summary>[4] NullType-Medium.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: SF370000	Contours detected: 1	Expected: 2

- Glyph name: SF420000	Contours detected: 2	Expected: 3

- Glyph name: SF200000	Contours detected: 1	Expected: 2

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF470000	Contours detected: 1	Expected: 2

- Glyph name: SF410000	Contours detected: 2	Expected: 3

- Glyph name: SF450000	Contours detected: 1	Expected: 2

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- 12 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-Regular.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: SF370000	Contours detected: 1	Expected: 2

- Glyph name: SF420000	Contours detected: 2	Expected: 3

- Glyph name: SF200000	Contours detected: 1	Expected: 2

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF470000	Contours detected: 1	Expected: 2

- Glyph name: SF410000	Contours detected: 2	Expected: 3

- Glyph name: SF450000	Contours detected: 1	Expected: 2

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- Glyph name: SF440000	Contours detected: 2	Expected: 4

- 10 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-SemiBoldItalic.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: at	Contours detected: 3	Expected: 2

- Glyph name: guillemotleft	Contours detected: 1	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: registered	Contours detected: 5	Expected: 3 or 4

- Glyph name: guillemotright	Contours detected: 1	Expected: 2

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- Glyph name: Atilde	Contours detected: 2	Expected: 3

- Glyph name: Aring	Contours detected: 2	Expected: 3 or 4

- 48 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-SemiBold.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: at	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: registered	Contours detected: 6	Expected: 3 or 4

- Glyph name: Agrave	Contours detected: 2	Expected: 3

- Glyph name: Aacute	Contours detected: 2	Expected: 3

- Glyph name: Atilde	Contours detected: 2	Expected: 3

- Glyph name: Aring	Contours detected: 2	Expected: 3 or 4

- Glyph name: Egrave	Contours detected: 1	Expected: 2

- Glyph name: Eacute	Contours detected: 1	Expected: 2

- 44 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-ThinItalic.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: section	Contours detected: 1	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: bullet	Contours detected: 3	Expected: 1

- Glyph name: SF420000	Contours detected: 2	Expected: 3

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF410000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- Glyph name: SF440000	Contours detected: 2	Expected: 4

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- 6 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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

<details><summary>[4] NullType-Thin.ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>


> 
> We need to check names are not already used, and today the best place to check
> that is http://namecheck.fontdata.com
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/494





* 💥 **ERROR** <p>Failed with KeyError: 'data'</p>
<pre><code>  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checkrunner.py&quot;, line 223, in _run_check
    subresults = list(subresults)
  File &quot;/home/r3dg0d/.cache/tripletype-fb/lib/python3.13/site-packages/fontbakery/checks/fontdata_namecheck.py&quot;, line 24, in check_fontdata_namecheck
    if data[&quot;data&quot;][&quot;confidence&quot;][&quot;1.0&quot;] &gt; 0:
       ~~~~^^^^^^^^

</code></pre>
 [code: failed-check]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
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





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: section	Contours detected: 1	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: bullet	Contours detected: 3	Expected: 1

- Glyph name: SF420000	Contours detected: 2	Expected: 3

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF410000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- Glyph name: SF440000	Contours detected: 2	Expected: 4

- Glyph name: SF230000	Contours detected: 2	Expected: 3

- Glyph name: SF400000	Contours detected: 2	Expected: 3

- 6 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: contour-count]



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
| 18 | 0 | 0 | 56 | 677 | 54 | 1277 | 0 | 
| 1% | 0% | 0% | 3% | 33% | 3% | 61% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
