---
title: NashornException.NashornException()
permalink: Java/NashornException/NashornException
date: 2021-01-11
key: JavaJava.N.NashornException
category: java
tags: ['java se', 'jdk.nashorn.api.scripting', 'jdk.scripting.nashorn', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NashornException.constructores valor="NashornException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected NashornException(String msg, String fileName, int line, int column)
protected NashornException(String msg, Throwable cause)
protected NashornException(String msg, Throwable cause, String fileName, int line, int column)
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_dato parametro="int column" %}
* **int line**,  {% include w3api/param_description.html metodo=_dato parametro="int line" %}
* **String msg**,  {% include w3api/param_description.html metodo=_dato parametro="String msg" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_dato parametro="String fileName" %}
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}

## Clase Padre
[NashornException](/Java/NashornException/)

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
