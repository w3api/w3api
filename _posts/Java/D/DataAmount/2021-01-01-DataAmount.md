---
title: DataAmount
permalink: /Java/DataAmount/
date: 2021-01-11
key: Java.D.DataAmount
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.DataAmount.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target({FIELD,TYPE,METHOD}) public @interface DataAmount
~~~

## Elementos
* [value](/Java/DataAmount/value)

## Ejemplo
~~~java
{{ site.data.Java.D.DataAmount.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DataAmount.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
