---
title: DocTreeVisitor.visitThrows()
permalink: /Java/DocTreeVisitor/visitThrows/
date: 2021-01-11
key: Java.D.DocTreeVisitor
category: Java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeVisitor.metodos valor="visitThrows" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitThrows(ThrowsTree node, P p)
~~~

## Parámetros
* **ThrowsTree node**,  {% include w3api/param_description.html metodo=_dato parametro="ThrowsTree node" %}
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
