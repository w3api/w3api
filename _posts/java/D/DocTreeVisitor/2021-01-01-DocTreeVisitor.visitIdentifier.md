---
title: DocTreeVisitor.visitIdentifier()
permalink: /Java/DocTreeVisitor/visitIdentifier/
date: 2021-01-11
key: Java.D.DocTreeVisitor
category: Java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeVisitor.metodos valor="visitIdentifier" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitIdentifier(IdentifierTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **IdentifierTree node**,  {% include w3api/param_description.html metodo=_dato parametro="IdentifierTree node" %}

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
