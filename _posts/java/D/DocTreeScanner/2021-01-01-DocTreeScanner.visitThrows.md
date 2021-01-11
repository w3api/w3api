---
title: DocTreeScanner.visitThrows()
permalink: Java/DocTreeScanner/visitThrows
date: 2021-01-11
key: JavaJava.D.DocTreeScanner
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeScanner.metodos valor="visitThrows" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitThrows(ThrowsTree node, P p)
~~~

## Parámetros
* **ThrowsTree node**,  {% include w3api/param_description.html metodo=_dato parametro="ThrowsTree node" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}

## Clase Padre
[DocTreeScanner](/Java/DocTreeScanner/)

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
