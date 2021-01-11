---
title: Threshold
permalink: Java/Threshold
date: 2021-01-11
key: JavaJava.T.Threshold
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.T.Threshold.description }}

## Sintaxis
~~~java
@Target(TYPE) @Inherited @Retention(RUNTIME) public @interface Threshold
~~~

## Elementos
* [value](/Java/Threshold/value)

## Ejemplo
~~~java
{{ site.data.Java.T.Threshold.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.Threshold.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
