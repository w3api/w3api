---
title: ColorConvertOp
permalink: /Java/ColorConvertOp/
date: 2021-01-11
key: Java.C.ColorConvertOp
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ColorConvertOp.description }}

## Sintaxis
~~~java
public class ColorConvertOp extends Object implements BufferedImageOp, RasterOp
~~~

## Constructores
* [ColorConvertOp()](/Java/ColorConvertOp/ColorConvertOp/)

## Métodos
* [createCompatibleDestImage()](/Java/ColorConvertOp/createCompatibleDestImage/)
* [createCompatibleDestRaster()](/Java/ColorConvertOp/createCompatibleDestRaster/)
* [filter()](/Java/ColorConvertOp/filter/)
* [getBounds2D()](/Java/ColorConvertOp/getBounds2D/)
* [getICC_Profiles()](/Java/ColorConvertOp/getICC_Profiles/)
* [getPoint2D()](/Java/ColorConvertOp/getPoint2D/)
* [getRenderingHints()](/Java/ColorConvertOp/getRenderingHints/)

## Ejemplo
~~~java
{{ site.data.Java.C.ColorConvertOp.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ColorConvertOp.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
