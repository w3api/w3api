---
title: DocSourcePositions.getStartPosition()
permalink: Java/DocSourcePositions/getStartPosition
date: 2021-01-04
key: JavaJava.D.DocSourcePositions
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocSourcePositions.metodos valor="getStartPosition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long getStartPosition(CompilationUnitTree file, DocCommentTree comment, DocTree tree)
~~~

## Parámetros
* **DocTree tree**,  {% include w3api/param_description.html metodo=_data parametro="DocTree tree" %}
* **CompilationUnitTree file**,  {% include w3api/param_description.html metodo=_data parametro="CompilationUnitTree file" %}
* **DocCommentTree comment**,  {% include w3api/param_description.html metodo=_data parametro="DocCommentTree comment" %}

## Clase Padre
[DocSourcePositions](/Java/DocSourcePositions/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocSourcePositions.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
