---
title: ScriptEngineManager.getEngineByName()
permalink: Java/ScriptEngineManager/getEngineByName
date: 2021-01-11
key: JavaJava.S.ScriptEngineManager
category: java
tags: ['java se', 'javax.script', 'java.scripting', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ScriptEngineManager.metodos valor="getEngineByName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ScriptEngine getEngineByName(String shortName)
~~~

## Parámetros
* **String shortName**,  {% include w3api/param_description.html metodo=_dato parametro="String shortName" %}

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
