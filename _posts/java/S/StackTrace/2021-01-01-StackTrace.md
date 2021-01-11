---
title: StackTrace
permalink: Java/StackTrace
date: 2021-01-11
key: JavaJava.S.StackTrace
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.StackTrace.description }}

## Sintaxis
~~~java
@Target(TYPE) @Inherited @Retention(RUNTIME) public @interface StackTrace
~~~

## Elementos
* [value](/Java/StackTrace/value)

## Ejemplo
~~~java
{{ site.data.Java.S.StackTrace.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StackTrace.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
