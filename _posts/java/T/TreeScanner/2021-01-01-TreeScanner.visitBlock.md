---
title: TreeScanner.visitBlock()
permalink: /Java/TreeScanner/visitBlock/
date: 2021-01-11
key: Java.T.TreeScanner
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeScanner.metodos valor="visitBlock" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitBlock(BlockTree node, P p)
~~~

## Parámetros
* **BlockTree node**,  {% include w3api/param_description.html metodo=_dato parametro="BlockTree node" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}

## Clase Padre
[TreeScanner](/Java/TreeScanner/)

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
