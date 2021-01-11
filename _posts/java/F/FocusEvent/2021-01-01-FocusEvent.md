---
title: FocusEvent
permalink: Java/FocusEvent
date: 2021-01-11
key: JavaJava.F.FocusEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.FocusEvent.description }}

## Sintaxis
~~~java
public class FocusEvent extends ComponentEvent
~~~

## Constructores
* [FocusEvent()](/Java/FocusEvent/FocusEvent/)

## Campos
* [FOCUS_FIRST](/Java/FocusEvent/FOCUS_FIRST)
* [FOCUS_GAINED](/Java/FocusEvent/FOCUS_GAINED)
* [FOCUS_LAST](/Java/FocusEvent/FOCUS_LAST)
* [FOCUS_LOST](/Java/FocusEvent/FOCUS_LOST)

## Métodos
* [getCause()](/Java/FocusEvent/getCause)
* [getOppositeComponent()](/Java/FocusEvent/getOppositeComponent)
* [isTemporary()](/Java/FocusEvent/isTemporary)
* [paramString()](/Java/FocusEvent/paramString)

## Ejemplo
~~~java
{{ site.data.Java.F.FocusEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FocusEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
