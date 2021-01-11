---
title: ScriptEngineManager.registerEngineName()
permalink: Java/ScriptEngineManager/registerEngineName
date: 2021-01-11
key: JavaJava.S.ScriptEngineManager
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptEngineManager.metodos valor="registerEngineName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void registerEngineName(String name, ScriptEngineFactory factory)
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}
* **ScriptEngineFactory factory**,  {% include w3api/param_description.html metodo=_dato parametro="ScriptEngineFactory factory" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ScriptEngineManager](/Java/ScriptEngineManager/)

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
