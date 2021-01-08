---
title: NashornScriptEngineFactory.getScriptEngine()
permalink: Java/NashornScriptEngineFactory/getScriptEngine
date: 2021-01-04
key: JavaJava.N.NashornScriptEngineFactory
category: java
tags: ['java se', 'jdk.nashorn.api.scripting', 'jdk.scripting.nashorn', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NashornScriptEngineFactory.metodos valor="getScriptEngine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ScriptEngine getScriptEngine(ClassLoader appLoader)
public ScriptEngine getScriptEngine(String... args)
public ScriptEngine getScriptEngine(String[] args, ClassLoader appLoader)
public ScriptEngine getScriptEngine(String[] args, ClassLoader appLoader, ClassFilter classFilter)
public ScriptEngine getScriptEngine(ClassFilter classFilter)
~~~

## Parámetros
* **String... args**,  {% include w3api/param_description.html metodo=_data parametro="String... args" %}
* **ClassLoader appLoader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader appLoader" %}
* **ClassFilter classFilter**,  {% include w3api/param_description.html metodo=_data parametro="ClassFilter classFilter" %}
* **String[] args**,  {% include w3api/param_description.html metodo=_data parametro="String[] args" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NashornScriptEngineFactory](/Java/NashornScriptEngineFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NashornScriptEngineFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
