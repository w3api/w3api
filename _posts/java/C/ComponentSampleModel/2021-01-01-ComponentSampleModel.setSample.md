---
title: ComponentSampleModel.setSample()
permalink: Java/ComponentSampleModel/setSample
date: 2021-01-11
key: JavaJava.C.ComponentSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentSampleModel.metodos valor="setSample" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSample(int x, int y, int b, double s, DataBuffer data)
public void setSample(int x, int y, int b, float s, DataBuffer data)
public void setSample(int x, int y, int b, int s, DataBuffer data)
~~~

## Parámetros
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_dato parametro="DataBuffer data" %}
* **double s**,  {% include w3api/param_description.html metodo=_dato parametro="double s" %}
* **int s**,  {% include w3api/param_description.html metodo=_dato parametro="int s" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}
* **float s**,  {% include w3api/param_description.html metodo=_dato parametro="float s" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int b**,  {% include w3api/param_description.html metodo=_dato parametro="int b" %}

## Clase Padre
[ComponentSampleModel](/Java/ComponentSampleModel/)

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
