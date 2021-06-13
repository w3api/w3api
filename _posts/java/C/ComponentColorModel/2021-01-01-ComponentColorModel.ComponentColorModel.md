---
title: ComponentColorModel.ComponentColorModel()
permalink: /Java/ComponentColorModel/ComponentColorModel/
date: 2021-01-11
key: Java.C.ComponentColorModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentColorModel.constructores valor="ComponentColorModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ComponentColorModel(ColorSpace colorSpace, boolean hasAlpha, boolean isAlphaPremultiplied, int transparency, int transferType)
public ComponentColorModel(ColorSpace colorSpace, int[] bits, boolean hasAlpha, boolean isAlphaPremultiplied, int transparency, int transferType)
~~~

## Parámetros
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_dato parametro="boolean isAlphaPremultiplied" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_dato parametro="int transferType" %}
* **ColorSpace colorSpace**,  {% include w3api/param_description.html metodo=_dato parametro="ColorSpace colorSpace" %}
* **boolean hasAlpha**,  {% include w3api/param_description.html metodo=_dato parametro="boolean hasAlpha" %}
* **int transparency**,  {% include w3api/param_description.html metodo=_dato parametro="int transparency" %}
* **int[] bits**,  {% include w3api/param_description.html metodo=_dato parametro="int[] bits" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ComponentColorModel](/Java/ComponentColorModel/)

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
