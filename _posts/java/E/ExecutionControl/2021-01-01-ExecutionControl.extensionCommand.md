---
title: ExecutionControl.extensionCommand()
permalink: /Java/ExecutionControl/extensionCommand/
date: 2021-01-11
key: Java.E.ExecutionControl
category: Java
tags: ['java se', 'jdk.jshell.spi', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutionControl.metodos valor="extensionCommand" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object extensionCommand(String command, Object arg) throws ExecutionControl.RunException, ExecutionControl.EngineTerminationException, ExecutionControl.InternalException
~~~

## Parámetros
* **String command**,  {% include w3api/param_description.html metodo=_dato parametro="String command" %}
* **Object arg**,  {% include w3api/param_description.html metodo=_dato parametro="Object arg" %}

## Excepciones
[ExecutionControl.NotImplementedException](/Java/ExecutionControl.NotImplementedException/), [ExecutionControl.EngineTerminationException](/Java/ExecutionControl.EngineTerminationException/), [ExecutionControl.UserException](/Java/ExecutionControl.UserException/), [ExecutionControl.ResolutionException](/Java/ExecutionControl.ResolutionException/), [ExecutionControl.InternalException](/Java/ExecutionControl.InternalException/), [ExecutionControl.RunException](/Java/ExecutionControl.RunException/), [ExecutionControl.StoppedException](/Java/ExecutionControl.StoppedException/)

## Clase Padre
[ExecutionControl](/Java/ExecutionControl/)

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
