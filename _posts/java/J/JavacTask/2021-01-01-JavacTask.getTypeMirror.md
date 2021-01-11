---
title: JavacTask.getTypeMirror()
permalink: Java/JavacTask/getTypeMirror
date: 2021-01-11
key: JavaJava.J.JavacTask
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavacTask.metodos valor="getTypeMirror" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract TypeMirror getTypeMirror(Iterable<? extends Tree> path)
~~~

## Parámetros
* **Iterable&lt;? extends Tree&gt; path**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends Tree> path" %}

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
