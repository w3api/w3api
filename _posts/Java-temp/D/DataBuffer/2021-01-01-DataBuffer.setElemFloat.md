---
title: DataBuffer.setElemFloat()
permalink: /Java/DataBuffer/setElemFloat/
date: 2021-01-11
key: Java.D.DataBuffer
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataBuffer.metodos valor="setElemFloat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setElemFloat(int i, float val)
public void setElemFloat(int bank, int i, float val)
~~~

## Parámetros
* **int bank**,  {% include w3api/param_description.html metodo=_dato parametro="int bank" %}
* **float val**,  {% include w3api/param_description.html metodo=_dato parametro="float val" %}
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
