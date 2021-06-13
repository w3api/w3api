---
title: Frequency
permalink: /Java/Frequency/
date: 2021-01-11
key: Java.F.Frequency
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.F.Frequency.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,METHOD}) public @interface Frequency
~~~

## Ejemplo
~~~java
{{ site.data.Java.F.Frequency.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.Frequency.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
