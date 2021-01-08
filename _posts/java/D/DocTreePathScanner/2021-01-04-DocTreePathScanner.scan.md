---
title: DocTreePathScanner.scan()
permalink: Java/DocTreePathScanner/scan
date: 2021-01-04
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
* **P p**,  {% include w3api/param_description.html metodo=_data parametro="P p" %}
* **DocTree tree**,  {% include w3api/param_description.html metodo=_data parametro="DocTree tree" %}
* **DocTreePath path**,  {% include w3api/param_description.html metodo=_data parametro="DocTreePath path" %}

## Clase Padre
[DocTreePathScanner](/Java/DocTreePathScanner/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DocTreePathScanner.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
