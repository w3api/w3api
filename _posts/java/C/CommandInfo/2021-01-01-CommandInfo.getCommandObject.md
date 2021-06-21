---
title: CommandInfo.getCommandObject()
permalink: /Java/CommandInfo/getCommandObject/
date: 2021-01-11
key: Java.C.CommandInfo
category: Java
tags: ['java se', 'javax.activation', 'java.activation', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CommandInfo.metodos valor="getCommandObject" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getCommandObject(DataHandler dh, ClassLoader loader) throws IOException, ClassNotFoundException
~~~

## Parámetros
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}
* **DataHandler dh**,  {% include w3api/param_description.html metodo=_dato parametro="DataHandler dh" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[CommandInfo](/Java/CommandInfo/)

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
