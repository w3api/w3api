---
title: PlainView
permalink: /Java/PlainView/
date: 2021-01-11
key: Java.P.PlainView
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'clase java', 'Java 1.0']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.P.PlainView.description }}

## Sintaxis
~~~java
public class PlainView extends View implements TabExpander
~~~

## Constructores
* [PlainView()](/Java/PlainView/PlainView/)

## Campos
* [metrics](/Java/PlainView/metrics)

## Métodos
* [changedUpdate()](/Java/PlainView/changedUpdate)
* [damageLineRange()](/Java/PlainView/damageLineRange)
* [drawLine()](/Java/PlainView/drawLine)
* [drawSelectedText()](/Java/PlainView/drawSelectedText)
* [drawUnselectedText()](/Java/PlainView/drawUnselectedText)
* [getLineBuffer()](/Java/PlainView/getLineBuffer)
* [getPreferredSpan()](/Java/PlainView/getPreferredSpan)
* [getTabSize()](/Java/PlainView/getTabSize)
* [insertUpdate()](/Java/PlainView/insertUpdate)
* [lineToRect()](/Java/PlainView/lineToRect)
* [modelToView()](/Java/PlainView/modelToView)
* [nextTabStop()](/Java/PlainView/nextTabStop)
* [paint()](/Java/PlainView/paint)
* [removeUpdate()](/Java/PlainView/removeUpdate)
* [setSize()](/Java/PlainView/setSize)
* [updateDamage()](/Java/PlainView/updateDamage)
* [updateMetrics()](/Java/PlainView/updateMetrics)
* [viewToModel()](/Java/PlainView/viewToModel)

## Ejemplo
~~~java
{{ site.data.Java.P.PlainView.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Java.P.PlainView.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
