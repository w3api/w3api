---
title: ScriptEngineFactory.getMethodCallSyntax()
permalink: Java/ScriptEngineFactory/getMethodCallSyntax
date: 2021-01-11
key: JavaJava.S.ScriptEngineFactory
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptEngineFactory.metodos valor="getMethodCallSyntax" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String getMethodCallSyntax(String obj, String m, String... args)
~~~

## Parámetros
* **String... args**,  {% include w3api/param_description.html metodo=_dato parametro="String... args" %}
* **String obj**,  {% include w3api/param_description.html metodo=_dato parametro="String obj" %}
* **String m**,  {% include w3api/param_description.html metodo=_dato parametro="String m" %}

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
