---
title: ComponentSampleModel.setPixels()
permalink: /Java/ComponentSampleModel/setPixels/
date: 2021-01-11
key: Java.C.ComponentSampleModel
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentSampleModel.metodos valor="setPixels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setPixels(int x, int y, int w, int h, int[] iArray, DataBuffer data)
~~~

## Parámetros
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_dato parametro="DataBuffer data" %}
* **int h**,  {% include w3api/param_description.html metodo=_dato parametro="int h" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **int[] iArray**,  {% include w3api/param_description.html metodo=_dato parametro="int[] iArray" %}
* **int w**,  {% include w3api/param_description.html metodo=_dato parametro="int w" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}

## Clase Padre
[ComponentSampleModel](/Java/ComponentSampleModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
