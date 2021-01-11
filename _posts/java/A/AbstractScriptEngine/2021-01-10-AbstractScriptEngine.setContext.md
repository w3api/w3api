---
title: AbstractScriptEngine.setContext()
permalink: Java/AbstractScriptEngine/setContext
date: 2021-01-10
key: JavaJava.A.AbstractScriptEngine
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractScriptEngine.metodos valor="setContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setContext(ScriptContext ctxt)
~~~

## Parámetros
* **ScriptContext ctxt**,  {% include w3api/param_description.html metodo=_dato parametro="ScriptContext ctxt" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
