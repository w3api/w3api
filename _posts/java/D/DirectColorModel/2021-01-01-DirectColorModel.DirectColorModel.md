---
title: DirectColorModel.DirectColorModel()
permalink: /Java/DirectColorModel/DirectColorModel/
date: 2021-01-11
key: Java.D.DirectColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectColorModel.constructores valor="DirectColorModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DirectColorModel(int bits, int rmask, int gmask, int bmask)
public DirectColorModel(int bits, int rmask, int gmask, int bmask, int amask)
public DirectColorModel(ColorSpace space, int bits, int rmask, int gmask, int bmask, int amask, boolean isAlphaPremultiplied, int transferType)
~~~

## Parámetros
* **int amask**,  {% include w3api/param_description.html metodo=_dato parametro="int amask" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isAlphaPremultiplied" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_dato parametro="int transferType" %}
* **int rmask**,  {% include w3api/param_description.html metodo=_dato parametro="int rmask" %}
* **int bits**,  {% include w3api/param_description.html metodo=_dato parametro="int bits" %}
* **int bmask**,  {% include w3api/param_description.html metodo=_dato parametro="int bmask" %}
* **ColorSpace space**,  {% include w3api/param_description.html metodo=_dato parametro="ColorSpace space" %}
* **int gmask**,  {% include w3api/param_description.html metodo=_dato parametro="int gmask" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DirectColorModel](/Java/DirectColorModel/)

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
