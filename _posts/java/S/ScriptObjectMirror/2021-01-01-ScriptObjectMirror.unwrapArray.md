---
title: ScriptObjectMirror.unwrapArray()
permalink: Java/ScriptObjectMirror/unwrapArray
date: 2021-01-11
key: JavaJava.S.ScriptObjectMirror
category: java
tags: ['java se', 'jdk.nashorn.api.scripting', 'jdk.scripting.nashorn', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptObjectMirror.metodos valor="unwrapArray" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Object[] unwrapArray(Object[] args, Object homeGlobal)
~~~

## Parámetros
* **Object homeGlobal**,  {% include w3api/param_description.html metodo=_dato parametro="Object homeGlobal" %}
* **Object[] args**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] args" %}

## Clase Padre
[ScriptObjectMirror](/Java/ScriptObjectMirror/)

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
