---
title: NashornException.NashornException()
permalink: Java/NashornException/NashornException
date: 2021-01-04
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
* **Throwable cause**,  {% include w3api/param_description.html metodo=_data parametro="Throwable cause" %}
* **int line**,  {% include w3api/param_description.html metodo=_data parametro="int line" %}
* **int column**,  {% include w3api/param_description.html metodo=_data parametro="int column" %}
* **String msg**,  {% include w3api/param_description.html metodo=_data parametro="String msg" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_data parametro="String fileName" %}

## Clase Padre
[NashornException](/Java/NashornException/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NashornException.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
