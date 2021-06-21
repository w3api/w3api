---
title: CommandMap.getPreferredCommands()
permalink: /Java/CommandMap/getPreferredCommands/
date: 2021-01-11
key: Java.C.CommandMap
category: Java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CommandMap.metodos valor="getPreferredCommands" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract CommandInfo[] getPreferredCommands(String mimeType)
public CommandInfo[] getPreferredCommands(String mimeType, DataSource ds)
~~~

## Parámetros
* **String mimeType**,  {% include w3api/param_description.html metodo=_dato parametro="String mimeType" %}
* **DataSource ds**,  {% include w3api/param_description.html metodo=_dato parametro="DataSource ds" %}

## Clase Padre
[CommandMap](/Java/CommandMap/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
