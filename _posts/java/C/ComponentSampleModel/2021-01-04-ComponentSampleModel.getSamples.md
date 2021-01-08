---
title: ComponentSampleModel.getSamples()
permalink: Java/ComponentSampleModel/getSamples
date: 2021-01-04
key: JavaJava.C.ComponentSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentSampleModel.metodos valor="getSamples" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int[] getSamples(int x, int y, int w, int h, int b, int[] iArray, DataBuffer data)
~~~

## Parámetros
* **int[] iArray**,  {% include w3api/param_description.html metodo=_data parametro="int[] iArray" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_data parametro="DataBuffer data" %}
* **int w**,  {% include w3api/param_description.html metodo=_data parametro="int w" %}
* **int h**,  {% include w3api/param_description.html metodo=_data parametro="int h" %}
* **int b**,  {% include w3api/param_description.html metodo=_data parametro="int b" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[ComponentSampleModel](/Java/ComponentSampleModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ComponentSampleModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
