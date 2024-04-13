---
title: Timestamp
permalink: /Java/Timestamp-jdk-jfr/
date: 2021-01-11
key: Java.T.Timestamp-jdk-jfr
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.Timestamp-jdk-jfr.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,TYPE,METHOD}) public @interface Timestamp
~~~

## Elementos
* [value](/Java/Timestamp-jdk-jfr/value)

## Ejemplo
~~~java
{{ site.data.Java.T.Timestamp-jdk-jfr.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.Timestamp-jdk-jfr.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
