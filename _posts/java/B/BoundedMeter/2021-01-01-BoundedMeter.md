---
title: BoundedMeter
permalink: /Java/BoundedMeter/
date: 2021-01-11
key: Java.B.BoundedMeter
category: Java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'clase java', '8u40']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.B.BoundedMeter.description }}

## Sintaxis
~~~java
@Deprecated(since="10", forRemoval=true) public class BoundedMeter extends NotifyingMeter implements ResourceMeter, ResourceRequest
~~~

## Constructores
* [BoundedMeter()](/Java/BoundedMeter/BoundedMeter/)

## Métodos
* [create()](/Java/BoundedMeter/create)
* [getBound()](/Java/BoundedMeter/getBound)
* [setBound()](/Java/BoundedMeter/setBound)

## Ejemplo
~~~java
{{ site.data.Java.B.BoundedMeter.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BoundedMeter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
