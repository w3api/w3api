---
title: SafeVarargs
permalink: /Java/SafeVarargs/
date: 2021-01-11
key: Java.S.SafeVarargs
category: Java
tags: ['java se', 'java.lang', 'java.base', 'anotacion java', 'Java 1.7']
sidebar: 
  nav: java
---

## Descripción
{{site.data.Java.S.SafeVarargs.description }}

## Sintaxis
~~~java
@Documented @Retention(RUNTIME) @Target({CONSTRUCTOR,METHOD}) public @interface SafeVarargs
~~~

## Ejemplo
~~~java
{{ site.data.Java.S.SafeVarargs.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.SafeVarargs.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
