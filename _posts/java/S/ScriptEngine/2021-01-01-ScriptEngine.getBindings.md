---
title: ScriptEngine.getBindings()
permalink: /Java/ScriptEngine/getBindings/
date: 2021-01-11
key: Java.S.ScriptEngine
category: Java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptEngine.metodos valor="getBindings" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Bindings getBindings(int scope)
~~~

## Parámetros
* **int scope**,  {% include w3api/param_description.html metodo=_dato parametro="int scope" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ScriptEngine](/Java/ScriptEngine/)

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
