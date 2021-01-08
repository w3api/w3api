---
title: ThrottledMeter
permalink: Java/ThrottledMeter
date: 2021-01-04
key: JavaJava.T.ThrottledMeter
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'clase java', '8u40']
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
