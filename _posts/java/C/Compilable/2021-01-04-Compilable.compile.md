---
title: Compilable.compile()
permalink: Java/Compilable/compile
date: 2021-01-04
key: JavaJava.C.Compilable
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Compilable.metodos valor="compile" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
CompiledScript compile(Reader script) throws ScriptException
CompiledScript compile(String script) throws ScriptException
~~~

## Parámetros
* **String script**,  {% include w3api/param_description.html metodo=_data parametro="String script" %}
* **Reader script**,  {% include w3api/param_description.html metodo=_data parametro="Reader script" %}

## Excepciones
[ScriptException](/Java/ScriptException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Compilable](/Java/Compilable/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Compilable.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
