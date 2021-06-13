---
title: Inherited
permalink: /Java/Inherited/
date: 2021-01-11
key: Java.I.Inherited
category: Java
tags: ['java se', 'java.lang.annotation', 'java.base', 'anotacion java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.I.Inherited.description }}

## Sintaxis
~~~java
@Documented @Retention(RUNTIME) @Target(ANNOTATION_TYPE) public @interface Inherited
~~~

## Ejemplo
~~~java
{{ site.data.Java.I.Inherited.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.Inherited.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
