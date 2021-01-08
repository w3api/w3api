---
title: SuppressWarnings
permalink: Java/SuppressWarnings
date: 2021-01-04
key: JavaJava.S.SuppressWarnings
category: java
tags: ['java se', 'java.lang', 'java.base', 'anotacion java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SuppressWarnings.description }}

## Sintaxis
~~~java
@Target({TYPE,FIELD,METHOD,PARAMETER,CONSTRUCTOR,LOCAL_VARIABLE,MODULE}) @Retention(SOURCE) public @interface SuppressWarnings
~~~

## Ejemplo
~~~java
{{ site.data.Java.S.SuppressWarnings.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SuppressWarnings.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
