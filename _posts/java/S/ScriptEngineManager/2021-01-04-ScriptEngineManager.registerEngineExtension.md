---
title: ScriptEngineManager.registerEngineExtension()
permalink: Java/ScriptEngineManager/registerEngineExtension
date: 2021-01-04
key: JavaJava.S.ScriptEngineManager
category: java
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
* **ScriptEngineFactory factory**,  {% include w3api/param_description.html metodo=_data parametro="ScriptEngineFactory factory" %}
* **String extension**,  {% include w3api/param_description.html metodo=_data parametro="String extension" %}

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
{%- for _ldc in site.data.Java.S.ScriptEngineManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
