---
title: ScriptEngine.setContext()
permalink: Java/ScriptEngine/setContext
date: 2021-01-11
key: JavaJava.S.ScriptEngine
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptEngine.metodos valor="setContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setContext(ScriptContext context)
~~~

## Parámetros
* **ScriptContext context**,  {% include w3api/param_description.html metodo=_dato parametro="ScriptContext context" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
