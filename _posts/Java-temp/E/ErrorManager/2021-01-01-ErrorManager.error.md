---
title: ErrorManager.error()
permalink: /Java/ErrorManager/error/
date: 2021-01-11
key: Java.E.ErrorManager
category: Java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ErrorManager.metodos valor="error" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void error(String msg, Exception ex, int code)
~~~

## Parámetros
* **int code**,  {% include w3api/param_description.html metodo=_dato parametro="int code" %}
* **Exception ex**,  {% include w3api/param_description.html metodo=_dato parametro="Exception ex" %}
* **String msg**,  {% include w3api/param_description.html metodo=_dato parametro="String msg" %}

## Clase Padre
[ErrorManager](/Java/ErrorManager/)

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
