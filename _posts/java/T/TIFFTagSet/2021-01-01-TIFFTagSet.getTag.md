---
title: TIFFTagSet.getTag()
permalink: Java/TIFFTagSet/getTag
date: 2021-01-11
key: JavaJava.T.TIFFTagSet
category: java
tags: ['java se', 'javax.imageio.plugins.tiff', 'java.desktop', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TIFFTagSet.metodos valor="getTag" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TIFFTag getTag(int tagNumber)
public TIFFTag getTag(String tagName)
~~~

## Parámetros
* **String tagName**,  {% include w3api/param_description.html metodo=_dato parametro="String tagName" %}
* **int tagNumber**,  {% include w3api/param_description.html metodo=_dato parametro="int tagNumber" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TIFFTagSet](/Java/TIFFTagSet/)

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
