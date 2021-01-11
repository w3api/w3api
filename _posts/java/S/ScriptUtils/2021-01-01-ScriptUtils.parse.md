---
title: ScriptUtils.parse()
permalink: Java/ScriptUtils/parse
date: 2021-01-11
key: JavaJava.S.ScriptUtils
category: java
tags: ['java se', 'jdk.nashorn.api.scripting', 'jdk.scripting.nashorn', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptUtils.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String parse(String code, String name, boolean includeLoc)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **String code**,  {% include w3api/param_description.html metodo=_dato parametro="String code" %}
* **boolean includeLoc**,  {% include w3api/param_description.html metodo=_dato parametro="boolean includeLoc" %}

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
