---
title: Deprecated
permalink: Java/Deprecated
date: 2021-01-11
key: JavaJava.D.Deprecated
category: java
tags: ['java se', 'java.lang', 'java.base', 'anotacion java', 'Java 1.5']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.D.Deprecated.description }}

## Sintaxis
~~~java
@Documented @Retention(RUNTIME) @Target({CONSTRUCTOR,FIELD,LOCAL_VARIABLE,METHOD,PACKAGE,MODULE,PARAMETER,TYPE}) public @interface Deprecated
~~~

## Elementos
* [forRemoval](/Java/Deprecated/forRemoval)
* [since](/Java/Deprecated/since)

## Ejemplo
~~~java
{{ site.data.Java.D.Deprecated.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.Deprecated.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
