---
title: TreeScanner.visitInstanceOf()
permalink: /Java/TreeScanner/visitInstanceOf/
date: 2021-01-11
key: Java.T.TreeScanner
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeScanner.metodos valor="visitInstanceOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitInstanceOf(InstanceOfTree node, P p)
~~~

## Parámetros
* **InstanceOfTree node**,  {% include w3api/param_description.html metodo=_dato parametro="InstanceOfTree node" %}
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
