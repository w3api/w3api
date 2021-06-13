---
title: ScriptUtils.makeSynchronizedFunction()
permalink: /Java/ScriptUtils/makeSynchronizedFunction/
date: 2021-01-11
key: Java.S.ScriptUtils
category: Java
tags: ['java se', 'jdk.nashorn.api.scripting', 'jdk.scripting.nashorn', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptUtils.metodos valor="makeSynchronizedFunction" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Object makeSynchronizedFunction(Object func, Object sync)
~~~

## Parámetros
* **Object func**,  {% include w3api/param_description.html metodo=_dato parametro="Object func" %}
* **Object sync**,  {% include w3api/param_description.html metodo=_dato parametro="Object sync" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ScriptUtils](/Java/ScriptUtils/)

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
