---
title: DocTreeVisitor.visitProvides()
permalink: Java/DocTreeVisitor/visitProvides
date: 2021-01-11
key: JavaJava.D.DocTreeVisitor
category: java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeVisitor.metodos valor="visitProvides" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default R visitProvides(ProvidesTree node, P p)
~~~

## Parámetros
* **ProvidesTree node**,  {% include w3api/param_description.html metodo=_dato parametro="ProvidesTree node" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}

## Clase Padre
[DocTreeVisitor](/Java/DocTreeVisitor/)

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