---
title: Relational
permalink: /Java/Relational/
date: 2021-01-11
key: Java.R.Relational
category: Java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.Relational.description }}

## Sintaxis
~~~java
@Retention(RUNTIME) @Target(ANNOTATION_TYPE) public @interface Relational
~~~

## Ejemplo
~~~java
{{ site.data.Java.R.Relational.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.Relational.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
