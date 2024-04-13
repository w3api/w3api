---
title: ScriptException.ScriptException()
permalink: /Java/ScriptException/ScriptException/
date: 2021-01-11
key: Java.S.ScriptException
category: Java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptException.constructores valor="ScriptException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ScriptException(Exception e)
public ScriptException(String s)
public ScriptException(String message, String fileName, int lineNumber)
public ScriptException(String message, String fileName, int lineNumber, int columnNumber)
~~~

## Parámetros
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **String message**,  {% include w3api/param_description.html metodo=_dato parametro="String message" %}
* **int lineNumber**,  {% include w3api/param_description.html metodo=_dato parametro="int lineNumber" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_dato parametro="String fileName" %}
* **int columnNumber**,  {% include w3api/param_description.html metodo=_dato parametro="int columnNumber" %}
* **Exception e**,  {% include w3api/param_description.html metodo=_dato parametro="Exception e" %}

## Clase Padre
[ScriptException](/Java/ScriptException/)

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
