---
title: CompiledScript.eval()
permalink: /Java/CompiledScript/eval/
date: 2021-01-11
key: Java.C.CompiledScript
category: Java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompiledScript.metodos valor="eval" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object eval() throws ScriptException
public Object eval(Bindings bindings) throws ScriptException
public abstract Object eval(ScriptContext context) throws ScriptException
~~~

## Parámetros
* **ScriptContext context**,  {% include w3api/param_description.html metodo=_dato parametro="ScriptContext context" %}
* **Bindings bindings**,  {% include w3api/param_description.html metodo=_dato parametro="Bindings bindings" %}

## Excepciones
[ScriptException](/Java/ScriptException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CompiledScript](/Java/CompiledScript/)

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
