---
title: ConvolveOp
permalink: Java/ConvolveOp
date: 2021-01-11
key: JavaJava.C.ConvolveOp
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConvolveOp.description }}

## Sintaxis
~~~java
public class ConvolveOp extends Object implements BufferedImageOp, RasterOp
~~~

## Constructores
* [ConvolveOp()](/Java/ConvolveOp/ConvolveOp/)

## Campos
* [EDGE_NO_OP](/Java/ConvolveOp/EDGE_NO_OP)
* [EDGE_ZERO_FILL](/Java/ConvolveOp/EDGE_ZERO_FILL)

## Métodos
* [createCompatibleDestImage()](/Java/ConvolveOp/createCompatibleDestImage)
* [createCompatibleDestRaster()](/Java/ConvolveOp/createCompatibleDestRaster)
* [filter()](/Java/ConvolveOp/filter)
* [getBounds2D()](/Java/ConvolveOp/getBounds2D)
* [getEdgeCondition()](/Java/ConvolveOp/getEdgeCondition)
* [getKernel()](/Java/ConvolveOp/getKernel)
* [getPoint2D()](/Java/ConvolveOp/getPoint2D)
* [getRenderingHints()](/Java/ConvolveOp/getRenderingHints)

## Ejemplo
~~~java
{{ site.data.Java.C.ConvolveOp.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConvolveOp.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
