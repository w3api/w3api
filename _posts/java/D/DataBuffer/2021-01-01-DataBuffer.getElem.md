---
title: DataBuffer.getElem()
permalink: /Java/DataBuffer/getElem/
date: 2021-01-11
key: Java.D.DataBuffer
category: Java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataBuffer.metodos valor="getElem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int getElem(int i)
public abstract int getElem(int bank, int i)
~~~

## Parámetros
* **int bank**,  {% include w3api/param_description.html metodo=_dato parametro="int bank" %}
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
