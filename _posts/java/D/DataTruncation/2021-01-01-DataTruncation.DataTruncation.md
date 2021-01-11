---
title: DataTruncation.DataTruncation()
permalink: Java/DataTruncation/DataTruncation
date: 2021-01-11
key: JavaJava.D.DataTruncation
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DataTruncation.constructores valor="DataTruncation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DataTruncation(int index, boolean parameter, boolean read, int dataSize, int transferSize)
public DataTruncation(int index, boolean parameter, boolean read, int dataSize, int transferSize, Throwable cause)
~~~

## Parámetros
* **int transferSize**,  {% include w3api/param_description.html metodo=_dato parametro="int transferSize" %}
* **boolean read**,  {% include w3api/param_description.html metodo=_dato parametro="boolean read" %}
* **int dataSize**,  {% include w3api/param_description.html metodo=_dato parametro="int dataSize" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}
* **boolean parameter**,  {% include w3api/param_description.html metodo=_dato parametro="boolean parameter" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Clase Padre
[DataTruncation](/Java/DataTruncation/)

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
