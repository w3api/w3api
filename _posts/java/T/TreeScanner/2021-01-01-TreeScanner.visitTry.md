---
title: TreeScanner.visitTry()
permalink: /Java/TreeScanner/visitTry/
date: 2021-01-11
key: Java.T.TreeScanner
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeScanner.metodos valor="visitTry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitTry(TryTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **TryTree node**,  {% include w3api/param_description.html metodo=_dato parametro="TryTree node" %}

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
