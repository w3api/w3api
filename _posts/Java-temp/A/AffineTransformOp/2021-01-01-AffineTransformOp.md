---
title: AffineTransformOp
permalink: /Java/AffineTransformOp/
date: 2021-01-11
key: Java.A.AffineTransformOp
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AffineTransformOp.description }}

## Sintaxis
~~~java
public class AffineTransformOp extends Object implements BufferedImageOp, RasterOp
~~~

## Constructores
* [AffineTransformOp()](/Java/AffineTransformOp/AffineTransformOp/)

## Campos
* [TYPE_BICUBIC](/Java/AffineTransformOp/TYPE_BICUBIC)
* [TYPE_BILINEAR](/Java/AffineTransformOp/TYPE_BILINEAR)
* [TYPE_NEAREST_NEIGHBOR](/Java/AffineTransformOp/TYPE_NEAREST_NEIGHBOR)

## Métodos
* [createCompatibleDestImage()](/Java/AffineTransformOp/createCompatibleDestImage)
* [createCompatibleDestRaster()](/Java/AffineTransformOp/createCompatibleDestRaster)
* [filter()](/Java/AffineTransformOp/filter)
* [getBounds2D()](/Java/AffineTransformOp/getBounds2D)
* [getInterpolationType()](/Java/AffineTransformOp/getInterpolationType)
* [getPoint2D()](/Java/AffineTransformOp/getPoint2D)
* [getRenderingHints()](/Java/AffineTransformOp/getRenderingHints)
* [getTransform()](/Java/AffineTransformOp/getTransform)

## Ejemplo
~~~java
{{ site.data.Java.A.AffineTransformOp.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AffineTransformOp.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
