---
title: Retention
permalink: Java/Retention
date: 2021-01-11
key: Java.R.Retention
category: java
tags: ['java se', 'java.lang.annotation', 'java.base', 'anotacion java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.Retention.description }}

## Sintaxis
~~~java
@Documented @Retention(RUNTIME) @Target(ANNOTATION_TYPE) public @interface Retention
~~~

## Ejemplo
~~~java
{{ site.data.Java.R.Retention.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.Retention.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
