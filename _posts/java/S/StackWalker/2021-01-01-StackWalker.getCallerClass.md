---
title: StackWalker.getCallerClass()
permalink: Java/StackWalker/getCallerClass
date: 2021-01-11
key: JavaJava.S.StackWalker
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackWalker.metodos valor="getCallerClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Class<?> getCallerClass()
~~~

## Excepciones
[IllegalCallerException](/Java/IllegalCallerException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[StackWalker](/Java/StackWalker/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
