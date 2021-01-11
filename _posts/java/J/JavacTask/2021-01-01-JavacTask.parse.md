---
title: JavacTask.parse()
permalink: Java/JavacTask/parse
date: 2021-01-11
key: JavaJava.J.JavacTask
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavacTask.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Iterable<? extends CompilationUnitTree> parse() throws IOException
~~~

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [IOException](/Java/IOException/)

## Clase Padre
[JavacTask](/Java/JavacTask/)

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