---
title: ExecutionControl.varValue()
permalink: Java/ExecutionControl/varValue
date: 2021-01-04
key: JavaJava.E.ExecutionControl
category: java
tags: ['java se', 'jdk.jshell.spi', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutionControl.metodos valor="varValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
String varValue(String className, String varName) throws ExecutionControl.RunException, ExecutionControl.EngineTerminationException, ExecutionControl.InternalException
~~~

## Parámetros
* **String varName**,  {% include w3api/param_description.html metodo=_data parametro="String varName" %}
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}

## Excepciones
[ExecutionControl.UserException](/Java/ExecutionControl.UserException/), [ExecutionControl.RunException](/Java/ExecutionControl.RunException/), [ExecutionControl.StoppedException](/Java/ExecutionControl.StoppedException/), [ExecutionControl.ResolutionException](/Java/ExecutionControl.ResolutionException/), [ExecutionControl.EngineTerminationException](/Java/ExecutionControl.EngineTerminationException/), [ExecutionControl.InternalException](/Java/ExecutionControl.InternalException/)

## Clase Padre
[ExecutionControl](/Java/ExecutionControl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.E.ExecutionControl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
