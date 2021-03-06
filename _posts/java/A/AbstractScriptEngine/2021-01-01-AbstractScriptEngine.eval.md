---
title: AbstractScriptEngine.eval()
permalink: /Java/AbstractScriptEngine/eval/
date: 2021-01-11
key: Java.A.AbstractScriptEngine
category: Java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractScriptEngine.metodos valor="eval" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object eval(Reader reader) throws ScriptException
public Object eval(Reader reader, Bindings bindings) throws ScriptException
public Object eval(String script) throws ScriptException
public Object eval(String script, Bindings bindings) throws ScriptException
~~~

## Parámetros
* **Reader reader**,  {% include w3api/param_description.html metodo=_dato parametro="Reader reader" %}
* **String script**,  {% include w3api/param_description.html metodo=_dato parametro="String script" %}
* **Bindings bindings**,  {% include w3api/param_description.html metodo=_dato parametro="Bindings bindings" %}

## Excepciones
[ScriptException](/Java/ScriptException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractScriptEngine](/Java/AbstractScriptEngine/)

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
