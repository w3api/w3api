---
title: ScriptEngineFactory.getProgram()
permalink: /Java/ScriptEngineFactory/getProgram/
date: 2021-01-11
key: Java.S.ScriptEngineFactory
category: Java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptEngineFactory.metodos valor="getProgram" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getProgram(String... statements)
~~~

## Parámetros
* **String... statements**,  {% include w3api/param_description.html metodo=_dato parametro="String... statements" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ScriptEngineFactory](/Java/ScriptEngineFactory/)

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
