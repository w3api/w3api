---
title: ExecutionControl.extensionCommand()
permalink: Java/ExecutionControl/extensionCommand
date: 2021-01-04
key: JavaJava.E.ExecutionControl
category: java
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
* **String command**,  {% include w3api/param_description.html metodo=_data parametro="String command" %}
* **Object arg**,  {% include w3api/param_description.html metodo=_data parametro="Object arg" %}

## Excepciones
[ExecutionControl.NotImplementedException](/Java/ExecutionControl.NotImplementedException/), [ExecutionControl.UserException](/Java/ExecutionControl.UserException/), [ExecutionControl.RunException](/Java/ExecutionControl.RunException/), [ExecutionControl.StoppedException](/Java/ExecutionControl.StoppedException/), [ExecutionControl.ResolutionException](/Java/ExecutionControl.ResolutionException/), [ExecutionControl.EngineTerminationException](/Java/ExecutionControl.EngineTerminationException/), [ExecutionControl.InternalException](/Java/ExecutionControl.InternalException/)

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
