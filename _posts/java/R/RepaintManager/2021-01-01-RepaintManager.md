---
title: RepaintManager
permalink: Java/RepaintManager
date: 2021-01-11
key: Java.R.RepaintManager
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'clase java', 'Java 1.2']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.RepaintManager.description }}

## Sintaxis
~~~java
public class RepaintManager extends Object
~~~

## Constructores
* [RepaintManager()](/Java/RepaintManager/RepaintManager/)

## Métodos
* [addDirtyRegion()](/Java/RepaintManager/addDirtyRegion)
* [addInvalidComponent()](/Java/RepaintManager/addInvalidComponent)
* [currentManager()](/Java/RepaintManager/currentManager)
* [getDirtyRegion()](/Java/RepaintManager/getDirtyRegion)
* [getDoubleBufferMaximumSize()](/Java/RepaintManager/getDoubleBufferMaximumSize)
* [getOffscreenBuffer()](/Java/RepaintManager/getOffscreenBuffer)
* [getVolatileOffscreenBuffer()](/Java/RepaintManager/getVolatileOffscreenBuffer)
* [isCompletelyDirty()](/Java/RepaintManager/isCompletelyDirty)
* [isDoubleBufferingEnabled()](/Java/RepaintManager/isDoubleBufferingEnabled)
* [markCompletelyClean()](/Java/RepaintManager/markCompletelyClean)
* [markCompletelyDirty()](/Java/RepaintManager/markCompletelyDirty)
* [paintDirtyRegions()](/Java/RepaintManager/paintDirtyRegions)
* [removeInvalidComponent()](/Java/RepaintManager/removeInvalidComponent)
* [setCurrentManager()](/Java/RepaintManager/setCurrentManager)
* [setDoubleBufferingEnabled()](/Java/RepaintManager/setDoubleBufferingEnabled)
* [setDoubleBufferMaximumSize()](/Java/RepaintManager/setDoubleBufferMaximumSize)
* [toString()](/Java/RepaintManager/toString)
* [validateInvalidComponents()](/Java/RepaintManager/validateInvalidComponents)

## Ejemplo
~~~java
{{ site.data.Java.R.RepaintManager.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RepaintManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
