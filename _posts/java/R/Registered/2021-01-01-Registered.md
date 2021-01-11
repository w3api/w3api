---
title: Registered
permalink: Java/Registered
date: 2021-01-11
key: JavaJava.R.Registered
category: java
tags: ['java se', 'jdk.jfr', 'jdk.jfr', 'anotacion java', 'Java 9']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.R.Registered.description }}

## Sintaxis
~~~java
@Target(TYPE) @Inherited @Retention(RUNTIME) public @interface Registered
~~~

## Elementos
* [value](/Java/Registered/value)

## Ejemplo
~~~java
{{ site.data.Java.R.Registered.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.Registered.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
