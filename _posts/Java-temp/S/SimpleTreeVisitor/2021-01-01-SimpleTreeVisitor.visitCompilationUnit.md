---
title: SimpleTreeVisitor.visitCompilationUnit()
permalink: /Java/SimpleTreeVisitor/visitCompilationUnit/
date: 2021-01-11
key: Java.S.SimpleTreeVisitor
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleTreeVisitor.metodos valor="visitCompilationUnit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitCompilationUnit(CompilationUnitTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **CompilationUnitTree node**,  {% include w3api/param_description.html metodo=_dato parametro="CompilationUnitTree node" %}

## Clase Padre
[SimpleTreeVisitor](/Java/SimpleTreeVisitor/)

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
