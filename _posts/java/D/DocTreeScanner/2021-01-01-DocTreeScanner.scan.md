---
title: DocTreeScanner.scan()
permalink: /Java/DocTreeScanner/scan/
date: 2021-01-11
key: Java.D.DocTreeScanner
category: Java
tags: ['java se', 'com.sun.source.util', 'jdk.compiler', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DocTreeScanner.metodos valor="scan" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public R scan(DocTree node, P p)
public R scan(Iterable<? extends DocTree> nodes, P p)
~~~

## Parámetros
* **P p**,  {% include w3api/param_description.html metodo=_dato parametro="P p" %}
* **DocTree node**,  {% include w3api/param_description.html metodo=_dato parametro="DocTree node" %}
* **Iterable&lt;? extends DocTree&gt; nodes**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends DocTree> nodes" %}

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
