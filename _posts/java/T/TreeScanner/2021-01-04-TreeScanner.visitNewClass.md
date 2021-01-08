---
title: TreeScanner.visitNewClass()
permalink: Java/TreeScanner/visitNewClass
date: 2021-01-04
key: JavaJava.T.TreeScanner
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TreeScanner.metodos valor="visitNewClass" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitNewClass(NewClassTree node, P p)
~~~

## Parámetros
* **NewClassTree node**,  {% include w3api/param_description.html metodo=_data parametro="NewClassTree node" %}
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}

## Clase Padre
[TreeScanner](/Java/TreeScanner/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TreeScanner.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
