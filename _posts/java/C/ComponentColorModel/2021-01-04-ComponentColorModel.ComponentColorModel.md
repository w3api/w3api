---
title: ComponentColorModel.ComponentColorModel()
permalink: Java/ComponentColorModel/ComponentColorModel
date: 2021-01-04
key: JavaJava.C.ComponentColorModel
category: java
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
* **int transparency**,  {% include w3api/param_description.html metodo=_data parametro="int transparency" %}
* **boolean hasAlpha**,  {% include w3api/param_description.html metodo=_data parametro="boolean hasAlpha" %}
* **int[] bits**,  {% include w3api/param_description.html metodo=_data parametro="int[] bits" %}
* **int transferType**,  {% include w3api/param_description.html metodo=_data parametro="int transferType" %}
* **boolean isAlphaPremultiplied**,  {% include w3api/param_description.html metodo=_data parametro="boolean isAlphaPremultiplied" %}
* **ColorSpace colorSpace**,  {% include w3api/param_description.html metodo=_data parametro="ColorSpace colorSpace" %}

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
{%- for _ldc in site.data.Java.C.ComponentColorModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
