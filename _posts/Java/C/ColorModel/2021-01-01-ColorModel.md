---
title: ColorModel
permalink: /Java/ColorModel/
date: 2021-01-11
key: Java.C.ColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ColorModel.description }}

## Sintaxis
~~~java
public abstract class ColorModel extends Object implements Transparency
~~~

## Constructores
* [ColorModel()](/Java/ColorModel/ColorModel/)

## Campos
* [pixel_bits](/Java/ColorModel/pixel_bits/)
* [transferType](/Java/ColorModel/transferType/)

## Métodos
* [coerceData()](/Java/ColorModel/coerceData/)
* [createCompatibleSampleModel()](/Java/ColorModel/createCompatibleSampleModel/)
* [createCompatibleWritableRaster()](/Java/ColorModel/createCompatibleWritableRaster/)
* [equals()](/Java/ColorModel/equals/)
* [finalize()](/Java/ColorModel/finalize/)
* [getAlpha()](/Java/ColorModel/getAlpha/)
* [getAlphaRaster()](/Java/ColorModel/getAlphaRaster/)
* [getBlue()](/Java/ColorModel/getBlue/)
* [getColorSpace()](/Java/ColorModel/getColorSpace/)
* [getComponents()](/Java/ColorModel/getComponents/)
* [getComponentSize()](/Java/ColorModel/getComponentSize/)
* [getDataElement()](/Java/ColorModel/getDataElement/)
* [getDataElements()](/Java/ColorModel/getDataElements/)
* [getGreen()](/Java/ColorModel/getGreen/)
* [getNormalizedComponents()](/Java/ColorModel/getNormalizedComponents/)
* [getNumColorComponents()](/Java/ColorModel/getNumColorComponents/)
* [getNumComponents()](/Java/ColorModel/getNumComponents/)
* [getPixelSize()](/Java/ColorModel/getPixelSize/)
* [getRed()](/Java/ColorModel/getRed/)
* [getRGB()](/Java/ColorModel/getRGB/)
* [getRGBdefault()](/Java/ColorModel/getRGBdefault/)
* [getTransferType()](/Java/ColorModel/getTransferType/)
* [getTransparency()](/Java/ColorModel/getTransparency/)
* [getUnnormalizedComponents()](/Java/ColorModel/getUnnormalizedComponents/)
* [hasAlpha()](/Java/ColorModel/hasAlpha/)
* [hashCode()](/Java/ColorModel/hashCode/)
* [isAlphaPremultiplied()](/Java/ColorModel/isAlphaPremultiplied/)
* [isCompatibleRaster()](/Java/ColorModel/isCompatibleRaster/)
* [isCompatibleSampleModel()](/Java/ColorModel/isCompatibleSampleModel/)
* [toString()](/Java/ColorModel/toString/)

## Ejemplo
~~~java
{{ site.data.Java.C.ColorModel.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.C.ColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
