---
title: ResourceAccuracy
permalink: Java/ResourceAccuracy
date: 2021-01-11
key: JavaJava.R.ResourceAccuracy
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'enumerado java', '8u40']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.ResourceAccuracy.description }}

## Sintaxis
~~~java
@Deprecated(since="10", forRemoval=true) public enum ResourceAccuracy extends Enum<ResourceAccuracy>
~~~

## Enumerados
* [HIGH](/Java/ResourceAccuracy/HIGH)
* [HIGHEST](/Java/ResourceAccuracy/HIGHEST)
* [LOW](/Java/ResourceAccuracy/LOW)
* [MEDIUM](/Java/ResourceAccuracy/MEDIUM)

## Métodos
* [improve()](/Java/ResourceAccuracy/improve)
* [valueOf()](/Java/ResourceAccuracy/valueOf)
* [values()](/Java/ResourceAccuracy/values)

## Ejemplo
~~~java
{{ site.data.Java.R.ResourceAccuracy.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResourceAccuracy.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
