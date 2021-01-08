---
title: DirectColorModel.DirectColorModel()
permalink: Java/DirectColorModel/DirectColorModel
date: 2021-01-04
key: JavaJava.D.DirectColorModel
category: java
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
* **ColorSpace space**,  {% include w3api/param_description.html metodo=_data parametro="ColorSpace space" %}
* **int bits**,  {% include w3api/param_description.html metodo=_data parametro="int bits" %}
* **int rmask**,  {% include w3api/param_description.html metodo=_data parametro="int rmask" %}
* **int amask**,  {% include w3api/param_description.html metodo=_data parametro="int amask" %}
* **int gmask**,  {% include w3api/param_description.html metodo=_data parametro="int gmask" %}
* **int bmask**,  {% include w3api/param_description.html metodo=_data parametro="int bmask" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_data parametro="int transferType" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAlphaPremultiplied" %}

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
{%- for _ldc in site.data.Java.D.DirectColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
