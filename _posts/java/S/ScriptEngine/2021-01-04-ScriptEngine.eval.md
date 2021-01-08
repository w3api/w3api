---
title: ScriptEngine.eval()
permalink: Java/ScriptEngine/eval
date: 2021-01-04
key: JavaJava.S.ScriptEngine
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptEngine.metodos valor="eval" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object eval(Reader reader) throws ScriptException
Object eval(Reader reader, Bindings n) throws ScriptException
Object eval(Reader reader, ScriptContext context) throws ScriptException
Object eval(String script) throws ScriptException
Object eval(String script, Bindings n) throws ScriptException
Object eval(String script, ScriptContext context) throws ScriptException
~~~

## Parámetros
* **String script**,  {% include w3api/param_description.html metodo=_data parametro="String script" %}
* **ScriptContext context**,  {% include w3api/param_description.html metodo=_data parametro="ScriptContext context" %}
* **Bindings n**,  {% include w3api/param_description.html metodo=_data parametro="Bindings n" %}
* **Reader reader**,  {% include w3api/param_description.html metodo=_data parametro="Reader reader" %}

## Excepciones
[ScriptException](/Java/ScriptException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ScriptEngine](/Java/ScriptEngine/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.ScriptEngine.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
