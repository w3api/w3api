---
title: DocTreeScanner.visitUses()
permalink: Java/DocTreeScanner/visitUses
date: 2021-01-04
key: JavaJava.D.DocTreeScanner
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeScanner.metodos valor="visitUses" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitUses(UsesTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **UsesTree node**,  {% include w3api/param_description.html metodo=_data parametro="UsesTree node" %}

## Clase Padre
[DocTreeScanner](/Java/DocTreeScanner/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocTreeScanner.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
