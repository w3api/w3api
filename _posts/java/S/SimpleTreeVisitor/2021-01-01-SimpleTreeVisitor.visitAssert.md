---
title: SimpleTreeVisitor.visitAssert()
permalink: Java/SimpleTreeVisitor/visitAssert
date: 2021-01-11
key: JavaJava.S.SimpleTreeVisitor
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleTreeVisitor.metodos valor="visitAssert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitAssert(AssertTree node, P p)
~~~

## Parámetros
* **AssertTree node**,  {% include w3api/param_description.html metodo=_dato parametro="AssertTree node" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}

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