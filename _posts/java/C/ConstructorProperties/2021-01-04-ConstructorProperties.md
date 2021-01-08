---
title: ConstructorProperties
permalink: Java/ConstructorProperties
date: 2021-01-04
key: JavaJava.C.ConstructorProperties
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'anotacion java', 'Java 1.6']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.C.ConstructorProperties.description }}

## Sintaxis
~~~java
@Documented @Target(CONSTRUCTOR) @Retention(RUNTIME) public @interface ConstructorProperties
~~~

## Ejemplo
~~~java
{{ site.data.Java.C.ConstructorProperties.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConstructorProperties.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
