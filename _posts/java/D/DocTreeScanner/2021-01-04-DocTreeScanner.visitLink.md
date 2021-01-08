---
title: DocTreeScanner.visitLink()
permalink: Java/DocTreeScanner/visitLink
date: 2021-01-04
key: JavaJava.D.DocTreeScanner
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeScanner.metodos valor="visitLink" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R visitLink(LinkTree node, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **LinkTree node**,  {% include w3api/param_description.html metodo=_data parametro="LinkTree node" %}

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
