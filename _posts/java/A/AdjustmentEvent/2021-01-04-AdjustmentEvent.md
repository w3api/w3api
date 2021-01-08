---
title: AdjustmentEvent
permalink: Java/AdjustmentEvent
date: 2021-01-04
key: JavaJava.A.AdjustmentEvent
category: java
tags: ['java se', 'java.awt.event', 'java.desktop', 'clase java', 'Java 1.1']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.A.AdjustmentEvent.description }}

## Sintaxis
~~~java
public class AdjustmentEvent extends AWTEvent
~~~

## Constructores
* [AdjustmentEvent()](/Java/AdjustmentEvent/AdjustmentEvent/)

## Campos
* [ADJUSTMENT_FIRST](/Java/AdjustmentEvent/ADJUSTMENT_FIRST)
* [ADJUSTMENT_LAST](/Java/AdjustmentEvent/ADJUSTMENT_LAST)
* [ADJUSTMENT_VALUE_CHANGED](/Java/AdjustmentEvent/ADJUSTMENT_VALUE_CHANGED)
* [BLOCK_DECREMENT](/Java/AdjustmentEvent/BLOCK_DECREMENT)
* [BLOCK_INCREMENT](/Java/AdjustmentEvent/BLOCK_INCREMENT)
* [TRACK](/Java/AdjustmentEvent/TRACK)
* [UNIT_DECREMENT](/Java/AdjustmentEvent/UNIT_DECREMENT)
* [UNIT_INCREMENT](/Java/AdjustmentEvent/UNIT_INCREMENT)

## Métodos
* [getAdjustable()](/Java/AdjustmentEvent/getAdjustable)
* [getAdjustmentType()](/Java/AdjustmentEvent/getAdjustmentType)
* [getValue()](/Java/AdjustmentEvent/getValue)
* [getValueIsAdjusting()](/Java/AdjustmentEvent/getValueIsAdjusting)

## Ejemplo
~~~java
{{ site.data.Java.A.AdjustmentEvent.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AdjustmentEvent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
