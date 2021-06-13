---
title: ScriptContext.setAttribute()
permalink: /Java/ScriptContext/setAttribute/
date: 2021-01-11
key: Java.S.ScriptContext
category: Java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptContext.metodos valor="setAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setAttribute(String name, Object value, int scope)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **Object value**,  {% include w3api/param_description.html metodo=_dato parametro="Object value" %}
* **int scope**,  {% include w3api/param_description.html metodo=_dato parametro="int scope" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ScriptContext](/Java/ScriptContext/)

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
