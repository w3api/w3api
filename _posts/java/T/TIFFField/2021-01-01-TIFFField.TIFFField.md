---
title: TIFFField.TIFFField()
permalink: Java/TIFFField/TIFFField
date: 2021-01-11
key: JavaJava.T.TIFFField
category: java
tags: ['java se', 'javax.imageio.plugins.tiff', 'java.desktop', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TIFFField.constructores valor="TIFFField" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TIFFField(TIFFTag tag, int type, int count)
public TIFFField(TIFFTag tag, int type, int count, Object data)
public TIFFField(TIFFTag tag, int type, long offset, TIFFDirectory dir)
public TIFFField(TIFFTag tag, long value)
~~~

## Parámetros
* **TIFFTag tag**,  {% include w3api/param_description.html metodo=_dato parametro="TIFFTag tag" %}
* **TIFFDirectory dir**,  {% include w3api/param_description.html metodo=_dato parametro="TIFFDirectory dir" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}
* **long offset**,  {% include w3api/param_description.html metodo=_dato parametro="long offset" %}
* **Object data**,  {% include w3api/param_description.html metodo=_dato parametro="Object data" %}
* **long value**,  {% include w3api/param_description.html metodo=_dato parametro="long value" %}
* **int count**,  {% include w3api/param_description.html metodo=_dato parametro="int count" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TIFFField](/Java/TIFFField/)

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
