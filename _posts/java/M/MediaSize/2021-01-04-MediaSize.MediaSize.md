---
title: MediaSize.MediaSize()
permalink: Java/MediaSize/MediaSize
date: 2021-01-04
key: JavaJava.M.MediaSize
category: java
tags: ['java se', 'javax.print.attribute.standard', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MediaSize.constructores valor="MediaSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MediaSize(float x, float y, int units)
public MediaSize(float x, float y, int units, MediaSizeName media)
public MediaSize(int x, int y, int units)
public MediaSize(int x, int y, int units, MediaSizeName media)
~~~

## Parámetros
* **float x**,  {% include w3api/param_description.html metodo=_data parametro="float x" %}
* **float y**,  {% include w3api/param_description.html metodo=_data parametro="float y" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **MediaSizeName media**,  {% include w3api/param_description.html metodo=_data parametro="MediaSizeName media" %}
* **int units**,  {% include w3api/param_description.html metodo=_data parametro="int units" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MediaSize](/Java/MediaSize/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MediaSize.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
