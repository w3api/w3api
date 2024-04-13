---
title: DocTreeVisitor.visitHidden()
permalink: /Java/DocTreeVisitor/visitHidden/
date: 2021-01-11
key: Java.D.DocTreeVisitor
category: Java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeVisitor.metodos valor="visitHidden" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default R visitHidden(HiddenTree node, P p)
~~~

## Parámetros
* **HiddenTree node**,  {% include w3api/param_description.html metodo=_dato parametro="HiddenTree node" %}
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
