---
title: DocTreePathScanner.scan()
permalink: Java/DocTreePathScanner/scan
date: 2021-01-11
key: JavaJava.D.DocTreePathScanner
category: java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreePathScanner.metodos valor="scan" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R scan(DocTree tree, P p)
public R scan(DocTreePath path, P p)
~~~

## Parámetros
* **DocTreePath path**,  {% include w3api/param_description.html metodo=_dato parametro="DocTreePath path" %}
* **DocTree tree**,  {% include w3api/param_description.html metodo=_dato parametro="DocTree tree" %}
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}

## Clase Padre
[DocTreePathScanner](/Java/DocTreePathScanner/)

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
