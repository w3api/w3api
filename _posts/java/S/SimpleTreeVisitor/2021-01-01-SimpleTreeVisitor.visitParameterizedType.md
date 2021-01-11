---
title: SimpleTreeVisitor.visitParameterizedType()
permalink: Java/SimpleTreeVisitor/visitParameterizedType
date: 2021-01-11
key: JavaJava.S.SimpleTreeVisitor
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleTreeVisitor.metodos valor="visitParameterizedType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitParameterizedType(ParameterizedTypeTree node, P p)
~~~

## Parámetros
* **ParameterizedTypeTree node**,  {% include w3api/param_description.html metodo=_dato parametro="ParameterizedTypeTree node" %}
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