---
title: DocTreeVisitor.visitLink()
permalink: /Java/DocTreeVisitor/visitLink/
date: 2021-01-11
key: Java.D.DocTreeVisitor
category: Java
tags: ['java se', 'com.sun.source.doctree', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeVisitor.metodos valor="visitLink" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
R visitLink(LinkTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **LinkTree node**,  {% include w3api/param_description.html metodo=_dato parametro="LinkTree node" %}

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
