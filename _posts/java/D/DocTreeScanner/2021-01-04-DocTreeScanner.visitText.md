---
title: DocTreeScanner.visitText()
permalink: Java/DocTreeScanner/visitText
date: 2021-01-04
key: JavaJava.D.DocTreeScanner
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeScanner.metodos valor="visitText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitText(TextTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **TextTree node**,  {% include w3api/param_description.html metodo=_data parametro="TextTree node" %}

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
