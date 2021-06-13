---
title: DocTreeScanner.visitReturn()
permalink: /Java/DocTreeScanner/visitReturn/
date: 2021-01-11
key: Java.D.DocTreeScanner
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeScanner.metodos valor="visitReturn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitReturn(ReturnTree node, P p)
~~~

## Parámetros
* **ReturnTree node**,  {% include w3api/param_description.html metodo=_dato parametro="ReturnTree node" %}
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
