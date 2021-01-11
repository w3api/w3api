---
title: CommandMap.getCommand()
permalink: Java/CommandMap/getCommand
date: 2021-01-11
key: JavaJava.C.CommandMap
category: java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CommandMap.metodos valor="getCommand" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract CommandInfo getCommand(String mimeType, String cmdName)
public CommandInfo getCommand(String mimeType, String cmdName, DataSource ds)
~~~

## Parámetros
* **String mimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String mimeType" %}
* **DataSource ds**,  {% include w3api/param_description.html metodo=_dato parametro="DataSource ds" %}
* **String cmdName**,  {% include w3api/param_description.html metodo=_dato parametro="String cmdName" %}

## Clase Padre
[CommandMap](/Java/CommandMap/)

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
