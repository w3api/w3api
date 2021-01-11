---
title: DataBuffer.setElemDouble()
permalink: Java/DataBuffer/setElemDouble
date: 2021-01-11
key: JavaJava.D.DataBuffer
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataBuffer.metodos valor="setElemDouble" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setElemDouble(int i, double val)
public void setElemDouble(int bank, int i, double val)
~~~

## Parámetros
* **int bank**,  {% include w3api/param_description.html metodo=_dato parametro="int bank" %}
* **double val**,  {% include w3api/param_description.html metodo=_dato parametro="double val" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}

## Clase Padre
[DataBuffer](/Java/DataBuffer/)

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
