---
title: Documented
permalink: Java/Documented
date: 2021-01-04
key: JavaJava.D.Documented
category: java
tags: ['java se', 'java.lang.annotation', 'java.base', 'anotacion java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.Documented.description }}

## Sintaxis
~~~java
@Documented @Retention(RUNTIME) @Target(ANNOTATION_TYPE) public @interface Documented
~~~

## Ejemplo
~~~java
{{ site.data.Java.D.Documented.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.Documented.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
