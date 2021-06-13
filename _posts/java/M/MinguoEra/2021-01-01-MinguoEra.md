---
title: MinguoEra
permalink: Java/MinguoEra
date: 2021-01-11
key: JavaJava.M.MinguoEra
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'enumerado java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.M.MinguoEra.description }}

## Sintaxis
~~~java
public enum MinguoEra extends Enum<MinguoEra> implements Era
~~~

## Enumerados
* [BEFORE_ROC](/Java/MinguoEra/BEFORE_ROC)
* [ROC](/Java/MinguoEra/ROC)

## Métodos
* [getDisplayName()](/Java/MinguoEra/getDisplayName)
* [getValue()](/Java/MinguoEra/getValue)
* [of()](/Java/MinguoEra/of)
* [valueOf()](/Java/MinguoEra/valueOf)
* [values()](/Java/MinguoEra/values)

## Ejemplo
~~~java
{{ site.data.Java.M.MinguoEra.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MinguoEra.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
