---
title: JPEGImageWriteParam.setEncodeTables()
permalink: Java/JPEGImageWriteParam/setEncodeTables
date: 2021-01-11
key: JavaJava.J.JPEGImageWriteParam
category: java
tags: ['java se', 'javax.imageio.plugins.jpeg', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JPEGImageWriteParam.metodos valor="setEncodeTables" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setEncodeTables(JPEGQTable[] qTables, JPEGHuffmanTable[] DCHuffmanTables, JPEGHuffmanTable[] ACHuffmanTables)
~~~

## Parámetros
* **JPEGHuffmanTable[] DCHuffmanTables**,  {% include w3api/param_description.html metodo=_dato parametro="JPEGHuffmanTable[] DCHuffmanTables" %}
* **JPEGQTable[] qTables**,  {% include w3api/param_description.html metodo=_dato parametro="JPEGQTable[] qTables" %}
* **JPEGHuffmanTable[] ACHuffmanTables**,  {% include w3api/param_description.html metodo=_dato parametro="JPEGHuffmanTable[] ACHuffmanTables" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JPEGImageWriteParam](/Java/JPEGImageWriteParam/)

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
