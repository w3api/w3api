---
title: SimpleTreeVisitor.visitVariable()
permalink: Java/SimpleTreeVisitor/visitVariable
date: 2021-01-11
key: JavaJava.S.SimpleTreeVisitor
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleTreeVisitor.metodos valor="visitVariable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitVariable(VariableTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **VariableTree node**,  {% include w3api/param_description.html metodo=_dato parametro="VariableTree node" %}

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
