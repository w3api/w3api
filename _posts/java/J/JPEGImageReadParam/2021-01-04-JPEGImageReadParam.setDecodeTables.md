---
title: JPEGImageReadParam.setDecodeTables()
permalink: Java/JPEGImageReadParam/setDecodeTables
date: 2021-01-04
key: JavaJava.J.JPEGImageReadParam
category: java
tags: ['java se', 'javax.imageio.plugins.jpeg', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JPEGImageReadParam.metodos valor="setDecodeTables" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setDecodeTables(JPEGQTable[] qTables, JPEGHuffmanTable[] DCHuffmanTables, JPEGHuffmanTable[] ACHuffmanTables)
~~~

## Parámetros
* **JPEGQTable[] qTables**,  {% include w3api/param_description.html metodo=_data parametro="JPEGQTable[] qTables" %}
* **JPEGHuffmanTable[] ACHuffmanTables**,  {% include w3api/param_description.html metodo=_data parametro="JPEGHuffmanTable[] ACHuffmanTables" %}
* **JPEGHuffmanTable[] DCHuffmanTables**,  {% include w3api/param_description.html metodo=_data parametro="JPEGHuffmanTable[] DCHuffmanTables" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JPEGImageReadParam](/Java/JPEGImageReadParam/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JPEGImageReadParam.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
