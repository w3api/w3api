---
title: ScriptEngineManager.registerEngineExtension()
permalink: /Java/ScriptEngineManager/registerEngineExtension/
date: 2021-01-11
key: Java.S.ScriptEngineManager
category: Java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptEngineManager.metodos valor="registerEngineExtension" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void registerEngineExtension(String extension, ScriptEngineFactory factory)
~~~

## Parámetros
* **ScriptEngineFactory factory**,  {% include w3api/param_description.html metodo=_dato parametro="ScriptEngineFactory factory" %}
* **String extension**,  {% include w3api/param_description.html metodo=_dato parametro="String extension" %}

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
