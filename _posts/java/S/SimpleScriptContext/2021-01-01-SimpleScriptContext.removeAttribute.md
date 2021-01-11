---
title: SimpleScriptContext.removeAttribute()
permalink: Java/SimpleScriptContext/removeAttribute
date: 2021-01-11
key: JavaJava.S.SimpleScriptContext
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SimpleScriptContext.metodos valor="removeAttribute" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object removeAttribute(String name, int scope)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **int scope**,  {% include w3api/param_description.html metodo=_dato parametro="int scope" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SimpleScriptContext](/Java/SimpleScriptContext/)

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
