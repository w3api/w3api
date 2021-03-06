---
title: ThrottledMeter
permalink: /Java/ThrottledMeter/
date: 2021-01-11
key: Java.T.ThrottledMeter
category: Java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'clase java', 'Java 1.8']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.ThrottledMeter.description }}

## Sintaxis
~~~java
@Deprecated(since="10", forRemoval=true) public class ThrottledMeter extends NotifyingMeter
~~~

## Métodos
* [create()](/Java/ThrottledMeter/create)
* [getCurrentRate()](/Java/ThrottledMeter/getCurrentRate)
* [getRatePerSec()](/Java/ThrottledMeter/getRatePerSec)
* [setRatePerSec()](/Java/ThrottledMeter/setRatePerSec)
* [validate()](/Java/ThrottledMeter/validate)

## Ejemplo
~~~java
{{ site.data.Java.T.ThrottledMeter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThrottledMeter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
